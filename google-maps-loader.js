/**
 * Advanced Google Maps API Loader
 * محمل متقدم لـ Google Maps API
 * 
 * This module provides intelligent loading and error handling for Google Maps API
 * هذه الوحدة توفر تحميل ذكي ومعالجة أخطاء لـ Google Maps API
 */

class GoogleMapsLoader {
    constructor(config) {
        this.config = config || window.GOOGLE_MAPS_CONFIG;
        this.isLoaded = false;
        this.isLoading = false;
        this.loadAttempts = 0;
        this.listeners = {
            onLoad: [],
            onError: [],
            onRetry: []
        };
        
        // Bind methods
        this.init = this.init.bind(this);
        this.load = this.load.bind(this);
        this.retry = this.retry.bind(this);
    }
    
    /**
     * Initialize the loader
     * تهيئة المحمل
     */
    init() {
        console.log('🚀 Initializing Google Maps Loader...');
        console.log('🚀 تهيئة محمل خرائط جوجل...');
        
        // Check if already loaded
        if (this.isGoogleMapsAvailable()) {
            console.log('✅ Google Maps is already available');
            this.isLoaded = true;
            this.notifyListeners('onLoad');
            return Promise.resolve();
        }
        
        // Start loading
        return this.load();
    }
    
    /**
     * Check if Google Maps is available
     * التحقق من توفر Google Maps
     */
    isGoogleMapsAvailable() {
        return typeof google !== 'undefined' && 
               typeof google.maps !== 'undefined' &&
               typeof google.maps.Map !== 'undefined';
    }
    
    /**
     * Load Google Maps API
     * تحميل Google Maps API
     */
    load() {
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
            // Validate API key first
            if (!this.validateApiKey()) {
                const error = new Error('Invalid or missing API key');
                this.handleError(error, reject, resolve);
                return;
            }
            
            // Create script element
            const script = document.createElement('script');
            script.src = this.buildApiUrl();
            script.async = true;
            script.defer = true;
            
            // Set up timeout
            const timeout = setTimeout(() => {
                this.isLoading = false;
                const error = new Error('Script loading timeout');
                this.handleError(error, reject, resolve);
            }, this.config.loading.scriptTimeout);
            
            // Success handler
            window.initMap = () => {
                clearTimeout(timeout);
                this.isLoading = false;
                
                if (this.isGoogleMapsAvailable()) {
                    console.log('✅ Google Maps API loaded successfully!');
                    console.log('✅ تم تحميل Google Maps API بنجاح!');
                    this.isLoaded = true;
                    this.loadAttempts = 0;
                    this.notifyListeners('onLoad');
                    resolve();
                } else {
                    const error = new Error('Google Maps objects not available after loading');
                    this.handleError(error, reject, resolve);
                }
            };
            
            // Error handler
            script.onerror = (event) => {
                clearTimeout(timeout);
                this.isLoading = false;
                const error = new Error('Script failed to load');
                this.handleError(error, reject, resolve);
            };
            
            // Authentication error handler
            window.gm_authFailure = () => {
                clearTimeout(timeout);
                this.isLoading = false;
                const error = new Error('Google Maps authentication failed - check API key and billing');
                this.handleError(error, reject, resolve);
            };
            
            // Append script to document
            document.head.appendChild(script);
            
            // Also listen for load event
            this.on('onLoad', resolve);
            this.on('onError', reject);
        });
    }
    
    /**
     * Validate API key
     * التحقق من صحة مفتاح API
     */
    validateApiKey() {
        const apiKey = this.config.apiKey;
        const placeholder = window.API_KEY_PLACEHOLDER || 'REPLACE_WITH_YOUR_GOOGLE_MAPS_API_KEY';
        
        if (!apiKey || apiKey === placeholder) {
            console.error('❌ Google Maps API key is not configured!');
            console.error('❌ لم يتم تكوين مفتاح Google Maps API!');
            this.showApiKeyInstructions();
            return false;
        }
        
        return true;
    }
    
    /**
     * Show API key setup instructions
     * عرض تعليمات إعداد مفتاح API
     */
    showApiKeyInstructions() {
        const instructions = `
╔════════════════════════════════════════════════════════════════╗
║  Google Maps API Key Setup Instructions                       ║
║  تعليمات إعداد مفتاح Google Maps API                         ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  English:                                                      ║
║  1. Go to: https://console.cloud.google.com/                  ║
║  2. Create a new project or select an existing one            ║
║  3. Enable these APIs:                                        ║
║     • Maps JavaScript API                                     ║
║     • Places API                                              ║
║     • Geocoding API                                           ║
║  4. Go to "Credentials" and create an API key                 ║
║  5. Set up billing (Google Maps requires billing)             ║
║  6. Restrict your API key:                                    ║
║     • HTTP referrers (websites)                               ║
║     • Add your domain                                         ║
║  7. Copy the API key                                          ║
║  8. Update google-maps-config.js:                             ║
║     apiKey: 'YOUR_ACTUAL_API_KEY_HERE'                        ║
║                                                                ║
║  العربية:                                                     ║
║  ١. اذهب إلى: https://console.cloud.google.com/              ║
║  ٢. أنشئ مشروع جديد أو اختر مشروعاً موجوداً                  ║
║  ٣. فعّل هذه الخدمات:                                        ║
║     • Maps JavaScript API                                     ║
║     • Places API                                              ║
║     • Geocoding API                                           ║
║  ٤. اذهب إلى "بيانات الاعتماد" وأنشئ مفتاح API               ║
║  ٥. أعد إعداد الفوترة (خرائط جوجل تتطلب تفعيل الفوترة)       ║
║  ٦. قيّد مفتاح API الخاص بك:                                 ║
║     • HTTP referrers (المواقع الإلكترونية)                   ║
║     • أضف نطاقك                                              ║
║  ٧. انسخ مفتاح API                                           ║
║  ٨. حدّث google-maps-config.js:                              ║
║     apiKey: 'مفتاح_API_الفعلي_الخاص_بك'                      ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
        `;
        
        console.info(instructions);
    }
    
    /**
     * Build API URL
     * بناء رابط API
     */
    buildApiUrl() {
        const params = new URLSearchParams({
            key: this.config.apiKey,
            libraries: this.config.libraries.join(','),
            language: this.config.language,
            region: this.config.region,
            callback: 'initMap',
            v: '3.55' // Use stable version for production reliability
        });
        
        return `https://maps.googleapis.com/maps/api/js?${params.toString()}`;
    }
    
    /**
     * Handle errors
     * معالجة الأخطاء
     */
    handleError(error, reject, resolve) {
        console.error('❌ Google Maps loading error:', error);
        console.error('❌ خطأ في تحميل خرائط جوجل:', error.message);
        
        // Check if we should retry
        if (this.loadAttempts < this.config.loading.maxRetryAttempts) {
            console.log(`🔄 Will retry in ${this.config.loading.retryDelay}ms...`);
            console.log(`🔄 سيتم إعادة المحاولة بعد ${this.config.loading.retryDelay} ميلي ثانية...`);
            
            this.notifyListeners('onRetry', { attempt: this.loadAttempts, error });
            
            setTimeout(() => {
                this.retry()
                    .then(() => {
                        if (resolve) resolve();
                    })
                    .catch((retryError) => {
                        if (reject) reject(retryError);
                    });
            }, this.config.loading.retryDelay);
        } else {
            console.error('❌ Maximum retry attempts reached');
            console.error('❌ تم الوصول إلى الحد الأقصى لمحاولات إعادة المحاولة');
            this.notifyListeners('onError', error);
            if (reject) reject(error);
        }
    }
    
    /**
     * Retry loading
     * إعادة محاولة التحميل
     */
    retry() {
        console.log('🔄 Retrying Google Maps API loading...');
        this.isLoading = false;
        return this.load();
    }
    
    /**
     * Add event listener
     * إضافة مستمع للأحداث
     */
    on(event, callback) {
        if (this.listeners[event]) {
            this.listeners[event].push(callback);
        }
    }
    
    /**
     * Remove event listener
     * إزالة مستمع الأحداث
     */
    off(event, callback) {
        if (this.listeners[event]) {
            const index = this.listeners[event].indexOf(callback);
            if (index > -1) {
                this.listeners[event].splice(index, 1);
            }
        }
    }
    
    /**
     * Notify listeners
     * إخطار المستمعين
     */
    notifyListeners(event, data) {
        if (this.listeners[event]) {
            this.listeners[event].forEach(callback => {
                try {
                    callback(data);
                } catch (error) {
                    console.error(`Error in ${event} listener:`, error);
                }
            });
        }
    }
    
    /**
     * Get status
     * الحصول على الحالة
     */
    getStatus() {
        if (this.isLoaded) {
            return 'loaded';
        } else if (this.isLoading) {
            return 'loading';
        } else if (this.loadAttempts > 0) {
            return 'error';
        } else {
            return 'idle';
        }
    }
    
    /**
     * Get status message
     * الحصول على رسالة الحالة
     */
    getStatusMessage(language = 'ar') {
        const status = this.getStatus();
        const messages = this.config.messages[language];
        
        switch (status) {
            case 'loaded':
                return messages.ready;
            case 'loading':
                return messages.loading;
            case 'error':
                return messages.error;
            default:
                return '';
        }
    }
}

// Create global instance
// إنشاء نسخة عامة
if (typeof window !== 'undefined' && window.GOOGLE_MAPS_CONFIG) {
    window.googleMapsLoader = new GoogleMapsLoader(window.GOOGLE_MAPS_CONFIG);
}

// Export for module systems
// التصدير لأنظمة الوحدات
if (typeof module !== 'undefined' && module.exports) {
    module.exports = GoogleMapsLoader;
}
