/**
 * Google Maps API Configuration
 * تكوين Google Maps API
 * 
 * IMPORTANT: This file contains the Google Maps API configuration.
 * For production, you should:
 * 1. Get a valid API key from Google Cloud Console: https://console.cloud.google.com/
 * 2. Enable the following APIs:
 *    - Maps JavaScript API
 *    - Places API
 *    - Geocoding API
 * 3. Set up billing (Google Maps requires billing to be enabled)
 * 4. Restrict the API key to your domain for security
 * 
 * ملاحظة هامة: هذا الملف يحتوي على إعدادات Google Maps API
 * للاستخدام الفعلي، يجب عليك:
 * 1. الحصول على مفتاح API صالح من Google Cloud Console
 * 2. تفعيل الخدمات التالية:
 *    - Maps JavaScript API
 *    - Places API
 *    - Geocoding API
 * 3. إعداد الفوترة (Google Maps يتطلب تفعيل الفوترة)
 * 4. تقييد مفتاح API لنطاقك لضمان الأمان
 */

// Placeholder value for API key validation
// قيمة نائبة للتحقق من صحة مفتاح API
const API_KEY_PLACEHOLDER = 'REPLACE_WITH_YOUR_GOOGLE_MAPS_API_KEY';

// Known invalid/old API keys that should not be used
// مفاتيح API قديمة/غير صالحة يجب عدم استخدامها
const INVALID_API_KEYS = [
    'AIzaSyBIu6hLqc2mW6WYKTf1JCMSjKCkN1E-xVU', // Old/invalid key
    'YOUR_ACTUAL_API_KEY_HERE',
    'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD', // Placeholder that needs to be replaced
    'REPLACE_WITH_YOUR_GOOGLE_MAPS_API_KEY'
];

// Try to load API key from local configuration (gitignored for security)
// محاولة تحميل مفتاح API من الإعدادات المحلية (مضاف لـ gitignore للأمان)
let API_KEY = API_KEY_PLACEHOLDER;
if (typeof window !== 'undefined' && window.GOOGLE_MAPS_API_KEY) {
    // Validate that the loaded key is not empty, placeholder, or known invalid key
    if (window.GOOGLE_MAPS_API_KEY && 
        window.GOOGLE_MAPS_API_KEY !== API_KEY_PLACEHOLDER && 
        window.GOOGLE_MAPS_API_KEY.trim() !== '' &&
        !INVALID_API_KEYS.includes(window.GOOGLE_MAPS_API_KEY)) {
        API_KEY = window.GOOGLE_MAPS_API_KEY;
        console.log('✅ Google Maps API key loaded from local configuration');
        console.log('✅ تم تحميل مفتاح Google Maps API من الإعدادات المحلية');
    } else if (INVALID_API_KEYS.includes(window.GOOGLE_MAPS_API_KEY)) {
        console.error('❌ The API key in google-maps-config.local.js is invalid or outdated!');
        console.error('❌ مفتاح API في google-maps-config.local.js غير صالح أو قديم!');
        console.error('⚠️ Please update it with your NEW API key from Google Cloud Console');
        console.error('⚠️ الرجاء تحديثه بمفتاح API الجديد من Google Cloud Console');
    } else {
        console.warn('⚠️ Local config found but API key is invalid or placeholder');
        console.warn('⚠️ تم العثور على إعدادات محلية لكن مفتاح API غير صالح أو قيمة افتراضية');
    }
}

const GOOGLE_MAPS_CONFIG = {
    // API Key - Replace with your valid Google Maps API key
    // مفتاح API - استبدله بمفتاح Google Maps API الصالح الخاص بك
    // 
    // ⚠️ IMPORTANT: Update google-maps-config.local.js with your NEW API key!
    // ⚠️ مهم: حدّث ملف google-maps-config.local.js بمفتاح API الجديد الخاص بك!
    apiKey: API_KEY_PLACEHOLDER,
    
    // API Libraries to load
    // مكتبات API المطلوب تحميلها
    libraries: ['places', 'geometry'],
    
    // Language
    // اللغة
    language: 'ar',
    
    // Region
    // المنطقة
    region: 'AE',
    
    // Map Configuration
    // إعدادات الخريطة
    mapConfig: {
        // Default center (Abu Dhabi)
        // المركز الافتراضي (أبو ظبي)
        defaultCenter: { 
            lat: 24.4539, 
            lng: 54.3773 
        },
        
        // Default zoom level
        // مستوى التكبير الافتراضي
        defaultZoom: 12,
        
        // Maximum zoom level
        // مستوى التكبير الأقصى
        maxZoom: 18,
        
        // Minimum zoom level
        // مستوى التكبير الأدنى
        minZoom: 10,
        
        // Map type control
        // عنصر التحكم في نوع الخريطة
        mapTypeControl: true,
        
        // Street view control
        // عنصر التحكم في عرض الشارع
        streetViewControl: true,
        
        // Zoom control
        // عنصر التحكم في التكبير
        zoomControl: true,
        
        // Fullscreen control
        // عنصر التحكم في وضع ملء الشاشة
        fullscreenControl: true,
        
        // Gesture handling
        // معالجة الإيماءات
        gestureHandling: 'greedy',
        
        // Map styles (optional - for custom map appearance)
        // أنماط الخريطة (اختياري - لمظهر مخصص للخريطة)
        styles: []
    },
    
    // Feature Configuration
    // إعدادات الميزات
    features: {
        // Nearby shops radius in meters
        // نطاق المحلات القريبة بالأمتار
        nearbyRadius: 2000,
        
        // Geocoding batch size
        // حجم دفعة التحويل الجغرافي
        geocodingBatchSize: 10,
        
        // Geocoding delay in milliseconds
        // تأخير التحويل الجغرافي بالميلي ثانية
        geocodingDelay: 100,
        
        // Area overlap offset
        // إزاحة تداخل المنطقة
        areaOverlapOffset: 0.005
    },
    
    // Loading Configuration
    // إعدادات التحميل
    loading: {
        // Maximum number of retry attempts
        // الحد الأقصى لعدد محاولات إعادة المحاولة
        maxRetryAttempts: 5,
        
        // Delay between retry attempts in milliseconds
        // التأخير بين محاولات إعادة المحاولة بالميلي ثانية
        retryDelay: 2000,
        
        // Initial check delay in milliseconds
        // تأخير الفحص الأولي بالميلي ثانية
        initialCheckDelay: 1000,
        
        // Final check delay in milliseconds
        // تأخير الفحص النهائي بالميلي ثانية
        finalCheckDelay: 3000,
        
        // Timeout for script loading in milliseconds
        // مهلة تحميل السكريبت بالميلي ثانية
        scriptTimeout: 10000
    },
    
    // Error Messages
    // رسائل الخطأ
    messages: {
        ar: {
            loading: 'جاري تحميل خرائط جوجل...',
            ready: 'خرائط جوجل جاهزة',
            error: 'فشل تحميل خرائط جوجل',
            retrying: 'إعادة المحاولة...',
            noApiKey: 'لم يتم تعيين مفتاح API',
            invalidApiKey: 'مفتاح API غير صالح',
            quotaExceeded: 'تم تجاوز الحد المسموح',
            networkError: 'خطأ في الاتصال بالإنترنت',
            authError: 'خطأ في المصادقة',
            unknownError: 'خطأ غير معروف'
        },
        en: {
            loading: 'Loading Google Maps...',
            ready: 'Google Maps Ready',
            error: 'Failed to load Google Maps',
            retrying: 'Retrying...',
            noApiKey: 'No API key set',
            invalidApiKey: 'Invalid API key',
            quotaExceeded: 'Quota exceeded',
            networkError: 'Network connection error',
            authError: 'Authentication error',
            unknownError: 'Unknown error'
        }
    }
};

// Validate API Key
// التحقق من صحة مفتاح API
function validateGoogleMapsApiKey() {
    const apiKey = GOOGLE_MAPS_CONFIG.apiKey;
    
    if (!apiKey || apiKey === API_KEY_PLACEHOLDER || INVALID_API_KEYS.includes(apiKey)) {
        console.error('❌ Google Maps API key is not configured or is invalid!');
        console.error('❌ لم يتم تكوين مفتاح Google Maps API أو أنه غير صالح!');
        console.error('');
        console.error('═════════════════════════════════════════════════════════════');
        console.error('  CRITICAL: You need to configure your NEW Google Maps API Key');
        console.error('  هام: تحتاج إلى تكوين مفتاح Google Maps API الجديد الخاص بك');
        console.error('═════════════════════════════════════════════════════════════');
        console.error('');
        console.info('📝 Please follow these steps / الرجاء اتباع هذه الخطوات:');
        console.info('');
        console.info('STEP 1 / الخطوة 1:');
        console.info('  Go to: https://console.cloud.google.com/');
        console.info('  اذهب إلى: https://console.cloud.google.com/');
        console.info('');
        console.info('STEP 2 / الخطوة 2:');
        console.info('  Create a NEW project or select your existing Monthly_inspection_plan project');
        console.info('  أنشئ مشروعاً جديداً أو اختر مشروع Monthly_inspection_plan الموجود');
        console.info('');
        console.info('STEP 3 / الخطوة 3:');
        console.info('  Enable these 3 APIs (if not already enabled):');
        console.info('  فعّل هذه الخدمات الثلاث (إذا لم تكن مفعلة):');
        console.info('  ✓ Maps JavaScript API');
        console.info('  ✓ Places API');
        console.info('  ✓ Geocoding API');
        console.info('');
        console.info('STEP 4 / الخطوة 4:');
        console.info('  Go to "Credentials" → "Create Credentials" → "API key"');
        console.info('  اذهب إلى "بيانات الاعتماد" → "إنشاء بيانات اعتماد" → "مفتاح API"');
        console.info('  COPY the new API key that looks like: AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX');
        console.info('  انسخ مفتاح API الجديد الذي يبدو كالتالي: AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX');
        console.info('');
        console.info('STEP 5 / الخطوة 5:');
        console.info('  IMPORTANT: Set up billing (Google requires it, provides $200 free/month)');
        console.info('  مهم: أعد الفوترة (جوجل تتطلبها، توفر 200 دولار مجاناً شهرياً)');
        console.info('');
        console.info('STEP 6 / الخطوة 6:');
        console.info('  Open file: google-maps-config.local.js');
        console.info('  افتح ملف: google-maps-config.local.js');
        console.info('  Replace BOTH occurrences of the old API key with your NEW key:');
        console.info('  استبدل كلا الموضعين لمفتاح API القديم بالمفتاح الجديد:');
        console.info('    Line 40: const GOOGLE_MAPS_API_KEY = \'YOUR_NEW_KEY\';');
        console.info('    Line 45: window.GOOGLE_MAPS_API_KEY = \'YOUR_NEW_KEY\';');
        console.info('');
        console.info('STEP 7 / الخطوة 7:');
        console.info('  Save the file and refresh the page (Ctrl+F5 or Cmd+Shift+R)');
        console.info('  احفظ الملف وحدّث الصفحة (Ctrl+F5 أو Cmd+Shift+R)');
        console.info('');
        console.info('OPTIONAL / اختياري:');
        console.info('  Restrict the API key to your domain for security');
        console.info('  قيّد مفتاح API لنطاقك للأمان');
        console.info('  Current domain: ' + (typeof window !== 'undefined' ? window.location.hostname : 'N/A'));
        console.info('  النطاق الحالي: ' + (typeof window !== 'undefined' ? window.location.hostname : 'N/A'));
        console.info('');
        console.error('═════════════════════════════════════════════════════════════');
        return false;
    }
    
    console.log('✅ API Key validation passed');
    console.log('✅ تم التحقق من صحة مفتاح API بنجاح');
    return true;
}

// Build Google Maps API URL
// بناء رابط Google Maps API
function buildGoogleMapsApiUrl() {
    if (!validateGoogleMapsApiKey()) {
        return null;
    }
    
    const params = new URLSearchParams({
        key: GOOGLE_MAPS_CONFIG.apiKey,
        libraries: GOOGLE_MAPS_CONFIG.libraries.join(','),
        language: GOOGLE_MAPS_CONFIG.language,
        region: GOOGLE_MAPS_CONFIG.region,
        callback: 'initMap'
    });
    
    return `https://maps.googleapis.com/maps/api/js?${params.toString()}`;
}

// Export configuration for browser
// تصدير الإعدادات للمتصفح
if (typeof window !== 'undefined') {
    window.GOOGLE_MAPS_CONFIG = GOOGLE_MAPS_CONFIG;
    window.API_KEY_PLACEHOLDER = API_KEY_PLACEHOLDER;
    window.INVALID_API_KEYS = INVALID_API_KEYS;
    window.validateGoogleMapsApiKey = validateGoogleMapsApiKey;
    window.buildGoogleMapsApiUrl = buildGoogleMapsApiUrl;
}

// Export configuration for Node.js
// تصدير الإعدادات لـ Node.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        GOOGLE_MAPS_CONFIG,
        API_KEY_PLACEHOLDER,
        validateGoogleMapsApiKey,
        buildGoogleMapsApiUrl
    };
}
