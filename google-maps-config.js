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

// Try to load API key from local configuration (gitignored for security)
// محاولة تحميل مفتاح API من الإعدادات المحلية (مضاف لـ gitignore للأمان)
let API_KEY = API_KEY_PLACEHOLDER;
if (typeof window !== 'undefined' && window.GOOGLE_MAPS_API_KEY) {
    // Validate that the loaded key is not empty or the placeholder
    if (window.GOOGLE_MAPS_API_KEY && 
        window.GOOGLE_MAPS_API_KEY !== API_KEY_PLACEHOLDER && 
        window.GOOGLE_MAPS_API_KEY.trim() !== '') {
        API_KEY = window.GOOGLE_MAPS_API_KEY;
        console.log('✅ Google Maps API key loaded from local configuration');
        console.log('✅ تم تحميل مفتاح Google Maps API من الإعدادات المحلية');
    } else {
        console.warn('⚠️ Local config found but API key is invalid or placeholder');
        console.warn('⚠️ تم العثور على إعدادات محلية لكن مفتاح API غير صالح أو قيمة افتراضية');
    }
}

const GOOGLE_MAPS_CONFIG = {
    // API Key - Replace with your valid Google Maps API key
    // مفتاح API - استبدله بمفتاح Google Maps API الصالح الخاص بك
    apiKey: 'AIzaSyBIu6hLqc2mW6WYKTf1JCMSjKCkN1E-xVU',
    
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
    
    if (!apiKey || apiKey === API_KEY_PLACEHOLDER) {
        console.error('❌ Google Maps API key is not configured!');
        console.error('❌ لم يتم تكوين مفتاح Google Maps API!');
        console.info('📝 Please follow these steps:');
        console.info('📝 الرجاء اتباع هذه الخطوات:');
        console.info('1. Go to: https://console.cloud.google.com/');
        console.info('2. Create a project or select an existing one');
        console.info('3. Enable Maps JavaScript API, Places API, and Geocoding API');
        console.info('4. Create an API key');
        console.info('5. Set up billing (required by Google)');
        console.info('6. Update the apiKey in google-maps-config.js');
        console.info('7. Restrict the API key to your domain');
        return false;
    }
    
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

// Export configuration
// تصدير الإعدادات
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        GOOGLE_MAPS_CONFIG,
        API_KEY_PLACEHOLDER,
        validateGoogleMapsApiKey,
        buildGoogleMapsApiUrl
    };
}
