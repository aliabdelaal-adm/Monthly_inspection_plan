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
        const invalidKeys = window.INVALID_API_KEYS || ['YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD'];
        
        if (!apiKey || apiKey === placeholder || invalidKeys.includes(apiKey)) {
            console.error('❌ Google Maps API key is not configured or is invalid!');
            console.error('❌ لم يتم تكوين مفتاح Google Maps API أو أنه غير صالح!');
            
            // Check which specific issue
            if (apiKey === 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD') {
                console.error('');
                console.error('⚠️  You need to REPLACE the placeholder in google-maps-config.local.js');
                console.error('⚠️  تحتاج إلى استبدال القيمة الافتراضية في google-maps-config.local.js');
                console.error('');
                console.error('Current value: YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD');
                console.error('القيمة الحالية: YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD');
                console.error('');
                console.error('You need a REAL API key from Google Cloud Console!');
                console.error('تحتاج إلى مفتاح API حقيقي من Google Cloud Console!');
            } else if (invalidKeys.includes(apiKey)) {
                console.error('');
                console.error('⚠️  The API key you\'re using is OLD or INVALID!');
                console.error('⚠️  مفتاح API الذي تستخدمه قديم أو غير صالح!');
                console.error('');
                console.error('You mentioned you created a NEW project in Google Cloud.');
                console.error('ذكرت أنك أنشأت مشروعاً جديداً في Google Cloud.');
                console.error('');
                console.error('Please update google-maps-config.local.js with your NEW API key!');
                console.error('الرجاء تحديث google-maps-config.local.js بمفتاح API الجديد!');
            }
            
            this.showApiKeyInstructions();
            return false;
        }
        
        // Additional validation: Check if key looks like a valid Google API key
        if (!apiKey.startsWith('AIza')) {
            console.error('❌ API key format appears invalid!');
            console.error('❌ تنسيق مفتاح API يبدو غير صالح!');
            console.error('Google Maps API keys should start with "AIza"');
            console.error('مفاتيح Google Maps API يجب أن تبدأ بـ "AIza"');
            this.showApiKeyInstructions();
            return false;
        }
        
        console.log('✅ API key format looks valid');
        console.log('✅ تنسيق مفتاح API يبدو صالحاً');
        return true;
    }
    
    /**
     * Show API key setup instructions
     * عرض تعليمات إعداد مفتاح API
     */
    showApiKeyInstructions() {
        const instructions = `
╔════════════════════════════════════════════════════════════════╗
║  🔑 Google Maps API Key Setup - Complete Guide                ║
║  🔑 دليل إعداد مفتاح Google Maps API - الدليل الكامل        ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  You mentioned you activated a NEW project in Google Cloud.   ║
║  ذكرت أنك قمت بتفعيل مشروع جديد في Google Cloud.            ║
║                                                                ║
║  Now you need to UPDATE the configuration file with your      ║
║  NEW API key!                                                  ║
║  الآن تحتاج إلى تحديث ملف الإعدادات بمفتاح API الجديد!       ║
║                                                                ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  📋 QUICK STEPS / الخطوات السريعة:                            ║
║                                                                ║
║  1️⃣  Get your API key from Google Cloud Console:              ║
║     احصل على مفتاح API من Google Cloud Console:              ║
║                                                                ║
║     a) Go to: https://console.cloud.google.com/               ║
║        اذهب إلى: https://console.cloud.google.com/           ║
║                                                                ║
║     b) Select "Monthly_inspection_plan" project               ║
║        اختر مشروع "Monthly_inspection_plan"                  ║
║                                                                ║
║     c) Go to: APIs & Services → Credentials                   ║
║        اذهب إلى: واجهات برمجة التطبيقات والخدمات            ║
║        → بيانات الاعتماد                                      ║
║                                                                ║
║     d) You should see your API key there (or create new one)  ║
║        يجب أن ترى مفتاح API هناك (أو أنشئ واحداً جديداً)    ║
║                                                                ║
║     e) COPY the API key (looks like: AIzaSyXXXXX...)          ║
║        انسخ مفتاح API (يبدو كالتالي: AIzaSyXXXXX...)         ║
║                                                                ║
║  2️⃣  Verify these 3 APIs are ENABLED:                          ║
║     تأكد من تفعيل هذه الخدمات الثلاث:                        ║
║                                                                ║
║     ✓ Maps JavaScript API                                     ║
║     ✓ Places API                                              ║
║     ✓ Geocoding API                                           ║
║                                                                ║
║     (Go to: APIs & Services → Library to enable them)         ║
║     (اذهب إلى: واجهات برمجة التطبيقات والخدمات → المكتبة)   ║
║                                                                ║
║  3️⃣  Verify BILLING is enabled:                                ║
║     تأكد من تفعيل الفوترة:                                   ║
║                                                                ║
║     Go to: Billing section                                    ║
║     اذهب إلى: قسم الفوترة                                    ║
║                                                                ║
║     Make sure billing account is linked                       ║
║     تأكد من ربط حساب الفوترة                                 ║
║                                                                ║
║     💡 Don't worry! Google gives $200 free credit per month   ║
║     💡 لا تقلق! جوجل تمنح رصيد مجاني 200 دولار شهرياً        ║
║                                                                ║
║  4️⃣  Update the configuration file:                            ║
║     حدّث ملف الإعدادات:                                      ║
║                                                                ║
║     a) Open file: google-maps-config.local.js                 ║
║        افتح ملف: google-maps-config.local.js                 ║
║                                                                ║
║     b) Find line ~68:                                         ║
║        ابحث عن السطر ~68:                                    ║
║        const GOOGLE_MAPS_API_KEY = 'YOUR_NEW_API_KEY...';     ║
║                                                                ║
║     c) REPLACE 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD'           ║
║        with your ACTUAL API key                               ║
║        استبدل 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD'           ║
║        بمفتاح API الفعلي الخاص بك                            ║
║                                                                ║
║     d) Also update line ~73:                                  ║
║        وأيضاً حدّث السطر ~73:                                ║
║        window.GOOGLE_MAPS_API_KEY = 'YOUR_NEW_API_KEY...';    ║
║                                                                ║
║     e) SAVE the file                                          ║
║        احفظ الملف                                             ║
║                                                                ║
║  5️⃣  Refresh the page with HARD reload:                        ║
║     حدّث الصفحة بإعادة تحميل كاملة:                          ║
║                                                                ║
║     Windows/Linux: Ctrl + Shift + R  or  Ctrl + F5            ║
║     Mac: Cmd + Shift + R                                      ║
║                                                                ║
║  6️⃣  Optional - Restrict API key (for security):               ║
║     اختياري - قيّد مفتاح API (للأمان):                       ║
║                                                                ║
║     Current domain: ${typeof window !== 'undefined' ? window.location.hostname : 'N/A'}                               ║
║     النطاق الحالي: ${typeof window !== 'undefined' ? window.location.hostname : 'N/A'}                               ║
║                                                                ║
║     In Google Cloud Console → Credentials:                    ║
║     - Click on your API key                                   ║
║     - Set "Application restrictions" to "HTTP referrers"      ║
║     - Add: ${typeof window !== 'undefined' ? window.location.hostname : 'your-domain.com'}/*                                    ║
║     - Click Save                                              ║
║                                                                ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  ⚠️  COMMON ISSUES / المشاكل الشائعة:                         ║
║                                                                ║
║  ❌ "This page can't load Google Maps correctly"              ║
║     → Billing not enabled or API key invalid                  ║
║     → الفوترة غير مفعلة أو مفتاح API غير صالح                ║
║                                                                ║
║  ❌ "RefererNotAllowedMapError"                               ║
║     → Domain restrictions are too strict                      ║
║     → قيود النطاق صارمة جداً                                 ║
║     → Solution: Remove restrictions temporarily               ║
║     → الحل: أزل القيود مؤقتاً                                ║
║                                                                ║
║  ❌ API key looks like: 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD'  ║
║     → You forgot to replace the placeholder!                  ║
║     → نسيت استبدال القيمة الافتراضية!                        ║
║     → Get your REAL key from Google Cloud Console             ║
║     → احصل على مفتاحك الحقيقي من Google Cloud Console        ║
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
