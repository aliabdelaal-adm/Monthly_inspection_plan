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
            script.onerror = (event) => {
                clearTimeout(timeout);
                this.isLoading = false;
                
                // Detect if blocked by browser/extension (ERR_BLOCKED_BY_CLIENT)
                // Use proper URL validation to prevent URL substring bypass
                let isBlocked = !navigator.onLine;
                if (event.target && event.target.src) {
                    try {
                        const url = new URL(event.target.src);
                        // Check if hostname ends with googleapis.com (proper domain validation)
                        isBlocked = isBlocked || url.hostname.endsWith('.googleapis.com') || url.hostname === 'googleapis.com';
                    } catch (e) {
                        // Invalid URL, treat as blocked
                        isBlocked = true;
                    }
                }
                
                let errorMsg = 'Script failed to load';
                if (isBlocked) {
                    errorMsg = 'Google Maps blocked by browser/extension (ERR_BLOCKED_BY_CLIENT)';
                    console.error('❌ Google Maps is being blocked!');
                    console.error('❌ خرائط جوجل محجوبة!');
                    console.error('');
                    console.error('Possible causes / الأسباب المحتملة:');
                    console.error('1. Ad blocker extension / إضافة مانع الإعلانات');
                    console.error('2. Privacy/security extension / إضافة الخصوصية/الأمان');
                    console.error('3. Browser security settings / إعدادات أمان المتصفح');
                    console.error('4. Network firewall / جدار حماية الشبكة');
                    console.error('');
                    console.error('Solution / الحل:');
                    console.error('- Disable ad blocker temporarily / عطّل مانع الإعلانات مؤقتاً');
                    console.error('- Allow maps.googleapis.com / اسمح بـ maps.googleapis.com');
                    console.error('- Check browser extensions / افحص إضافات المتصفح');
                }
                
                const error = new Error(errorMsg);
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
        console.error('❌ خطأ في تحميل خرائط جوجل:', error.message);
        
        // Check if it's a blocking error
        const isBlockingError = error.message.includes('blocked') || 
                               error.message.includes('ERR_BLOCKED_BY_CLIENT');
        
        // Don't retry if blocked by browser
        if (isBlockingError) {
            console.error('');
            console.error('⛔ Google Maps is blocked by your browser or extension');
            console.error('⛔ خرائط جوجل محجوبة بواسطة المتصفح أو إضافة');
            console.error('');
            console.error('📋 To fix this issue / لإصلاح هذه المشكلة:');
            console.error('');
            console.error('English:');
            console.error('1. Disable your ad blocker for this site');
            console.error('2. Whitelist maps.googleapis.com in your privacy extensions');
            console.error('3. Check browser security settings');
            console.error('4. Reload the page after making changes');
            console.error('');
            console.error('العربية:');
            console.error('1. عطّل مانع الإعلانات لهذا الموقع');
            console.error('2. أضف maps.googleapis.com إلى القائمة المسموحة في إضافات الخصوصية');
            console.error('3. افحص إعدادات أمان المتصفح');
            console.error('4. أعد تحميل الصفحة بعد إجراء التغييرات');
            console.error('');
            
            this._triggerCallbacks('onError', error);
            if (reject) reject(error);
            return;
        }
        
 copilot/fix-google-maps-config-load
        // Check if we should retry for non-blocking errors

        // Check if error is due to ad blocker / content blocker
        if (error.message.includes('Script failed to load')) {
            console.warn('⚠️ Google Maps script blocked - This may be due to:');
            console.warn('   1. Ad blocker or content blocker extension');
            console.warn('   2. Browser privacy settings');
            console.warn('   3. Network firewall restrictions');
            console.warn('');
            console.warn('💡 Solution: The app will use direct Google Maps links instead');
            console.warn('   All shops have working Google Maps links that will open in a new tab');
            console.warn('');
            console.warn('⚠️ الخرائط محجوبة - قد يكون السبب:');
            console.warn('   1. إضافة حجب الإعلانات أو المحتوى');
            console.warn('   2. إعدادات الخصوصية في المتصفح');
            console.warn('   3. قيود جدار الحماية');
            console.warn('');
            console.warn('💡 الحل: سيستخدم التطبيق روابط خرائط جوجل المباشرة');
            console.warn('   جميع المحلات لديها روابط خرائط جوجل تعمل وتفتح في نافذة جديدة');
        }
        
        // Check if we should retry
 main
        if (this.loadAttempts < this.config.loading.maxRetryAttempts) {
            console.log(`🔄 Will retry in ${this.config.loading.retryDelay}ms...`);
            console.log(`🔄 سيتم إعادة المحاولة خلال ${this.config.loading.retryDelay}ms...`);
            
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
 copilot/fix-google-maps-config-load
            console.error('❌ تم الوصول إلى الحد الأقصى لمحاولات إعادة المحاولة');

            console.error('');
            console.error('✅ Don\'t worry! All shops have direct Google Maps links');
            console.error('✅ لا تقلق! جميع المحلات لديها روابط خرائط جوجل مباشرة');
 main
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
