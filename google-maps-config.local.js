/**
 * Local Google Maps API Configuration Example
 * مثال على تكوين Google Maps API المحلي
 * 
 * INSTRUCTIONS / التعليمات:
 * 1. Copy this file and rename it to: google-maps-config.local.js
 *    انسخ هذا الملف وأعد تسميته إلى: google-maps-config.local.js
 * 
 * 2. Replace 'YOUR_ACTUAL_API_KEY_HERE' with your real Google Maps API key
 *    استبدل 'YOUR_ACTUAL_API_KEY_HERE' بمفتاح Google Maps API الحقيقي الخاص بك
 * 
 * 3. The .local.js file is gitignored for security
 *    ملف .local.js مضاف لـ gitignore للأمان
 * 
 * HOW TO GET AN API KEY / كيفية الحصول على مفتاح API:
 * 1. Go to: https://console.cloud.google.com/
 *    اذهب إلى: https://console.cloud.google.com/
 * 
 * 2. Create a new project or select existing one
 *    أنشئ مشروعاً جديداً أو اختر مشروعاً موجوداً
 * 
 * 3. Enable these APIs:
 *    فعّل هذه الخدمات:
 *    - Maps JavaScript API
 *    - Places API  
 *    - Geocoding API
 * 
 * 4. Go to "Credentials" and create an API key
 *    اذهب إلى "بيانات الاعتماد" وأنشئ مفتاح API
 * 
 * 5. IMPORTANT: Set up billing (Google requires it, but provides $200 free monthly credit)
 *    مهم: أعد الفوترة (جوجل تتطلبها، لكن توفر رصيد مجاني 200 دولار شهرياً)
 * 
 * 6. Restrict your API key to your domain for security
 *    قيّد مفتاح API الخاص بك لنطاقك للأمان
 */

// Set your actual Google Maps API key here
// ضع مفتاح Google Maps API الفعلي هنا
const GOOGLE_MAPS_API_KEY = 'AIzaSyBIu6hLqc2mW6WYKTf1JCMSjKCkN1E-xVU';

// Export the API key
// تصدير مفتاح API
if (typeof window !== 'undefined') {
    window.GOOGLE_MAPS_API_KEY = 'AIzaSyBIu6hLqc2mW6WYKTf1JCMSjKCkN1E-xVU';
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { GOOGLE_MAPS_API_KEY };
}
