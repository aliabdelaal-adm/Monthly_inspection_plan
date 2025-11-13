/**
 * Local Google Maps API Key Configuration
 * ملف إعداد مفتاح Google Maps API المحلي
 * 
 * This file overrides the API key from google-maps-config.js
 * يقوم هذا الملف باستبدال مفتاح API من google-maps-config.js
 * 
 * IMPORTANT: This file should be loaded BEFORE google-maps-config.js
 * مهم: يجب تحميل هذا الملف قبل google-maps-config.js
 * 
 * Version: 3.0 - Fresh Implementation
 * Last Updated: 2025-11-13
 */

// Set the Google Maps API Key
// تعيين مفتاح Google Maps API
const GOOGLE_MAPS_API_KEY = 'AIzaSyBIu6hLqc2mW6WYKTf1JCMSjKCkN1E-xVU';

// Export to window object
// تصدير إلى كائن النافذة
if (typeof window !== 'undefined') {
    window.GOOGLE_MAPS_API_KEY = GOOGLE_MAPS_API_KEY;
    console.log('✅ Google Maps API Key configured');
    console.log('✅ تم تكوين مفتاح Google Maps API');
}

// Export for Node.js if needed
// تصدير لـ Node.js إذا لزم الأمر
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { GOOGLE_MAPS_API_KEY };
}
