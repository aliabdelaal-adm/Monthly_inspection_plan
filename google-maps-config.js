/**
 * Google Maps API Configuration for Monthly Inspection Plan
 * إعدادات Google Maps API لخطة التفتيش الشهرية
 * 
 * This file contains the complete configuration for Google Maps integration
 * يحتوي هذا الملف على الإعداد الكامل لتكامل خرائط جوجل
 * 
 * Version: 3.0 - Fresh Implementation
 * Last Updated: 2025-11-13
 */

// Google Maps API Configuration
// إعدادات Google Maps API
window.GOOGLE_MAPS_CONFIG = {
    // API Key (will be overridden by google-maps-config.local.js if exists)
    // مفتاح API (سيتم استبداله بواسطة google-maps-config.local.js إذا كان موجوداً)
    apiKey: window.GOOGLE_MAPS_API_KEY || 'YOUR_API_KEY_HERE',
    
    // Map Configuration
    // إعدادات الخريطة
    mapConfig: {
        // Default center: Abu Dhabi, UAE
        // المركز الافتراضي: أبوظبي، الإمارات
        defaultCenter: { lat: 24.4539, lng: 54.3773 },
        
        // Zoom levels
        // مستويات التكبير
        defaultZoom: 12,
        minZoom: 10,
        maxZoom: 18,
        
        // Map styles
        // أنماط الخريطة
        styles: [
            {
                featureType: "poi.business",
                elementType: "labels",
                stylers: [{ visibility: "on" }]
            }
        ]
    },
    
    // Libraries to load
    // المكتبات المطلوب تحميلها
    libraries: ['places', 'geocoding'],
    
    // Language and region
    // اللغة والمنطقة
    language: 'ar',
    region: 'AE',
    
    // Feature Configuration
    // إعدادات الميزات
    features: {
        // Auto-geocoding settings
        // إعدادات التحديد التلقائي للموقع
        enableAutoGeocoding: true,
        geocodingBatchSize: 10,
        geocodingDelay: 100,
        
        // Nearby shops selection radius (in meters)
        // نطاق اختيار المحلات القريبة (بالأمتار)
        nearbyRadius: 2000,
        
        // Area overlap offset to avoid marker clustering
        // إزاحة تداخل المناطق لتجنب تجمع العلامات
        areaOverlapOffset: 0.005,
        
        // Marker colors by priority
        // ألوان العلامات حسب الأولوية
        markerColors: {
            'very-high': '#8b0000',  // Dark red
            'high': '#dc3545',       // Red
            'medium': '#ffc107',     // Yellow
            'normal': '#667eea',     // Blue
            'selected': '#28a745',   // Green
            'unavailable': '#999999' // Gray
        }
    },
    
    // Loading Configuration
    // إعدادات التحميل
    loading: {
        maxRetryAttempts: 3,
        retryDelay: 2000,
        scriptTimeout: 15000
    },
    
    // Messages
    // الرسائل
    messages: {
        ar: {
            loading: 'جاري تحميل خرائط جوجل...',
            ready: 'خرائط جوجل جاهزة',
            error: 'فشل تحميل الخرائط'
        },
        en: {
            loading: 'Loading Google Maps...',
            ready: 'Google Maps Ready',
            error: 'Failed to load Google Maps'
        }
    }
};

console.log('✅ Google Maps Configuration loaded successfully');
console.log('✅ تم تحميل إعدادات خرائط جوجل بنجاح');
