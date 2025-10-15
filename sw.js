// Service Worker for Monthly Inspection Plan PWA
// Version 1.0.0

const CACHE_NAME = 'monthly-inspection-v1.0.0';
const RUNTIME_CACHE = 'runtime-cache-v1';

// Files to cache immediately on install
const STATIC_CACHE_URLS = [
  './',
  './index.html',
  './admin.html',
  './admin-dashboard.html',
  './plan-data.json',
  './shops_details.json',
  './files.json',
  './maintenance-status.json',
  './manifest.json',
  './icon-192x192.png',
  './icon-512x512.png'
];

// Install event - cache static assets
self.addEventListener('install', (event) => {
  console.log('Service Worker: Installing...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Service Worker: Caching static assets');
        // Try to cache all URLs, but don't fail if some are missing
        return Promise.allSettled(
          STATIC_CACHE_URLS.map(url => 
            cache.add(url).catch(err => {
              console.warn(`Failed to cache ${url}:`, err);
              return null;
            })
          )
        );
      })
      .then(() => {
        console.log('Service Worker: Installation complete');
        return self.skipWaiting();
      })
      .catch((error) => {
        console.error('Service Worker: Installation failed', error);
      })
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
  console.log('Service Worker: Activating...');
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME && cacheName !== RUNTIME_CACHE) {
            console.log('Service Worker: Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => {
      console.log('Service Worker: Activation complete');
      return self.clients.claim();
    })
  );
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  // Skip cross-origin requests
  if (url.origin !== location.origin) {
    return;
  }

  // Skip GitHub API requests (need fresh data)
  if (url.pathname.includes('/api/')) {
    return;
  }

  event.respondWith(
    caches.match(request)
      .then((cachedResponse) => {
        if (cachedResponse) {
          console.log('Service Worker: Serving from cache:', request.url);
          // Return cached response and update cache in background
          event.waitUntil(updateCache(request));
          return cachedResponse;
        }

        console.log('Service Worker: Fetching from network:', request.url);
        return fetch(request)
          .then((response) => {
            // Don't cache if not successful
            if (!response || response.status !== 200 || response.type === 'error') {
              return response;
            }

            // Clone the response
            const responseToCache = response.clone();

            // Cache the fetched response for runtime
            caches.open(RUNTIME_CACHE)
              .then((cache) => {
                cache.put(request, responseToCache);
              });

            return response;
          })
          .catch((error) => {
            console.error('Service Worker: Fetch failed:', error);
            
            // Return a custom offline page if available
            return caches.match('./index.html');
          });
      })
  );
});

// Function to update cache in background
async function updateCache(request) {
  try {
    const cache = await caches.open(RUNTIME_CACHE);
    const response = await fetch(request);
    if (response && response.status === 200) {
      await cache.put(request, response);
    }
  } catch (error) {
    console.log('Service Worker: Background update failed:', error);
  }
}

// Handle messages from the main app
self.addEventListener('message', (event) => {
  console.log('Service Worker: Received message:', event.data);
  
  if (event.data.action === 'skipWaiting') {
    self.skipWaiting();
  }
  
  if (event.data.action === 'clearCache') {
    event.waitUntil(
      caches.keys().then((cacheNames) => {
        return Promise.all(
          cacheNames.map((cacheName) => caches.delete(cacheName))
        );
      }).then(() => {
        event.ports[0].postMessage({ success: true });
      })
    );
  }
});

// Background sync for data updates (if supported)
if ('sync' in self.registration) {
  self.addEventListener('sync', (event) => {
    console.log('Service Worker: Background sync:', event.tag);
    
    if (event.tag === 'sync-data') {
      event.waitUntil(
        Promise.all([
          fetch('./plan-data.json').then(r => r.json()),
          fetch('./shops_details.json').then(r => r.json()),
          fetch('./files.json').then(r => r.json())
        ]).then(([planData, shopsData, filesData]) => {
          console.log('Service Worker: Data synced successfully');
        }).catch((error) => {
          console.error('Service Worker: Sync failed:', error);
        })
      );
    }
  });
}

// Periodic background sync (if supported)
if ('periodicSync' in self.registration) {
  self.addEventListener('periodicsync', (event) => {
    console.log('Service Worker: Periodic sync:', event.tag);
    
    if (event.tag === 'update-data') {
      event.waitUntil(updateCache(new Request('./plan-data.json')));
    }
  });
}

console.log('Service Worker: Script loaded');
