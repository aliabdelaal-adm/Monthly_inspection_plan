/**
 * Google Maps API Loader
 * محمل Google Maps API
 * 
 * This module handles loading of Google Maps API with proper error handling
 * تتعامل هذه الوحدة مع تحميل Google Maps API مع معالجة الأخطاء المناسبة
 * 
 * Version: 3.0 - Fresh Implementation
 * Last Updated: 2025-11-13
 */

class GoogleMapsLoader {
    constructor(config) {
        this.config = config || window.GOOGLE_MAPS_CONFIG;
        this.isLoaded = false;
        this.isLoading = false;
        this.loadAttempts = 0;
        this.callbacks = {
            onLoad: [],
            onError: [],
            onRetry: []
        };
    }
    
    /**
     * Check if Google Maps is already loaded
     * التحقق من تحميل خرائط جوجل
     */
    isGoogleMapsAvailable() {
        return typeof google !== 'undefined' && 
               typeof google.maps !== 'undefined' &&
               typeof google.maps.Map !== 'undefined';
    }
    
    /**
     * Initialize and load Google Maps API
     * تهيئة وتحميل Google Maps API
     */
    async init() {
        console.log('🚀 Initializing Google Maps Loader...');
        console.log('🚀 تهيئة محمل خرائط جوجل...');
        
        // Check if already loaded
        if (this.isGoogleMapsAvailable()) {
            console.log('✅ Google Maps is already available');
            this.isLoaded = true;
            this._triggerCallbacks('onLoad');
            return Promise.resolve();
        }
        
        // Start loading
        return this.load();
    }
    
    /**
     * Load Google Maps API
     * تحميل Google Maps API
     */
    async load() {
        if (this.isLoading) {
            console.warn('⚠️ Google Maps is already loading...');
            return new Promise((resolve, reject) => {
                this.on('onLoad', resolve);
                this.on('onError', reject);
            });
        }
        
        this.isLoading = true;
        this.loadAttempts++;
        
        console.log(`🔄 Loading Google Maps API (attempt ${this.loadAttempts}/${this.config.loading.maxRetryAttempts})...`);
        
        return new Promise((resolve, reject) => {
            // Validate API key
            if (!this._validateApiKey()) {
                const error = new Error('Invalid or missing API key');
                this._handleError(error, reject);
                return;
            }
            
            // Create script element
            const script = document.createElement('script');
            script.src = this._buildApiUrl();
            script.async = true;
            script.defer = true;
            
            // Set up timeout
            const timeout = setTimeout(() => {
                this.isLoading = false;
                const error = new Error('Script loading timeout');
                this._handleError(error, reject);
            }, this.config.loading.scriptTimeout);
            
            // Global callback function
            window.initGoogleMapsCallback = () => {
                clearTimeout(timeout);
                this.isLoading = false;
                
                if (this.isGoogleMapsAvailable()) {
                    console.log('✅ Google Maps API loaded successfully!');
                    console.log('✅ تم تحميل Google Maps API بنجاح!');
                    this.isLoaded = true;
                    this.loadAttempts = 0;
                    this._triggerCallbacks('onLoad');
                    resolve();
                } else {
                    const error = new Error('Google Maps objects not available after loading');
                    this._handleError(error, reject);
                }
            };
            
            // Error handler
            script.onerror = () => {
                clearTimeout(timeout);
                this.isLoading = false;
                const error = new Error('Script failed to load');
                this._handleError(error, reject);
            };
            
            // Authentication error handler
            window.gm_authFailure = () => {
                clearTimeout(timeout);
                this.isLoading = false;
                const error = new Error('Google Maps authentication failed');
                this._handleError(error, reject);
            };
            
            // Append script
            document.head.appendChild(script);
        });
    }
    
    /**
     * Validate API key
     * التحقق من مفتاح API
     */
    _validateApiKey() {
        const apiKey = this.config.apiKey;
        
        if (!apiKey || apiKey === 'YOUR_API_KEY_HERE') {
            console.error('❌ Google Maps API key is not configured!');
            console.error('❌ لم يتم تكوين مفتاح Google Maps API!');
            console.error('');
            console.error('Please update google-maps-config.local.js with your API key');
            console.error('الرجاء تحديث google-maps-config.local.js بمفتاح API الخاص بك');
            return false;
        }
        
        // Check if key looks valid
        if (!apiKey.startsWith('AIza')) {
            console.error('❌ API key format appears invalid!');
            console.error('❌ تنسيق مفتاح API يبدو غير صالح!');
            return false;
        }
        
        console.log('✅ API key format looks valid');
        return true;
    }
    
    /**
     * Build API URL
     * بناء رابط API
     */
    _buildApiUrl() {
        const params = new URLSearchParams({
            key: this.config.apiKey,
            libraries: this.config.libraries.join(','),
            language: this.config.language,
            region: this.config.region,
            callback: 'initGoogleMapsCallback',
            v: 'weekly'
        });
        
        return `https://maps.googleapis.com/maps/api/js?${params.toString()}`;
    }
    
    /**
     * Handle errors
     * معالجة الأخطاء
     */
    _handleError(error, reject) {
        console.error('❌ Google Maps loading error:', error.message);
        
        // Check if we should retry
        if (this.loadAttempts < this.config.loading.maxRetryAttempts) {
            console.log(`🔄 Will retry in ${this.config.loading.retryDelay}ms...`);
            
            this._triggerCallbacks('onRetry', { 
                attempt: this.loadAttempts, 
                error 
            });
            
            setTimeout(() => {
                this.isLoading = false;
                this.load().then(resolve => resolve).catch(reject);
            }, this.config.loading.retryDelay);
        } else {
            console.error('❌ Maximum retry attempts reached');
            this._triggerCallbacks('onError', error);
            if (reject) reject(error);
        }
    }
    
    /**
     * Add event listener
     * إضافة مستمع للأحداث
     */
    on(event, callback) {
        if (this.callbacks[event]) {
            this.callbacks[event].push(callback);
        }
    }
    
    /**
     * Trigger callbacks
     * تشغيل callbacks
     */
    _triggerCallbacks(event, data) {
        if (this.callbacks[event]) {
            this.callbacks[event].forEach(callback => {
                try {
                    callback(data);
                } catch (error) {
                    console.error(`Error in ${event} callback:`, error);
                }
            });
        }
    }
    
    /**
     * Get loading status
     * الحصول على حالة التحميل
     */
    getStatus() {
        if (this.isLoaded) return 'loaded';
        if (this.isLoading) return 'loading';
        if (this.loadAttempts > 0) return 'error';
        return 'idle';
    }
}

// Create global instance
// إنشاء نسخة عامة
if (typeof window !== 'undefined') {
    console.log('🔧 Creating Google Maps Loader instance...');
    
    // Wait for config to be available
    if (window.GOOGLE_MAPS_CONFIG) {
        window.googleMapsLoader = new GoogleMapsLoader(window.GOOGLE_MAPS_CONFIG);
        console.log('✅ Google Maps Loader created successfully');
    } else {
        console.warn('⚠️ GOOGLE_MAPS_CONFIG not found, loader will be created when config is available');
        // Try again after a short delay
        setTimeout(() => {
            if (window.GOOGLE_MAPS_CONFIG && !window.googleMapsLoader) {
                window.googleMapsLoader = new GoogleMapsLoader(window.GOOGLE_MAPS_CONFIG);
                console.log('✅ Google Maps Loader created successfully (delayed)');
            }
        }, 100);
    }
}

// Export for module systems
// التصدير لأنظمة الوحدات
if (typeof module !== 'undefined' && module.exports) {
    module.exports = GoogleMapsLoader;
}
