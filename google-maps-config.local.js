/**
 * Local Google Maps API Configuration
 * تكوين Google Maps API المحلي
 * 
 * ═══════════════════════════════════════════════════════════════════════════
 *  🔑 IMPORTANT: UPDATE THIS FILE WITH YOUR NEW GOOGLE MAPS API KEY!
 *  🔑 مهم جداً: حدّث هذا الملف بمفتاح Google Maps API الجديد الخاص بك!
 * ═══════════════════════════════════════════════════════════════════════════
 * 
 * STEP-BY-STEP INSTRUCTIONS / التعليمات خطوة بخطوة:
 * 
 * ENGLISH:
 * --------
 * 1. Go to Google Cloud Console: https://console.cloud.google.com/
 * 2. Select your "Monthly_inspection_plan" project (or create new one)
 * 3. Verify these 3 APIs are ENABLED (very important!):
 *    ✓ Maps JavaScript API
 *    ✓ Places API
 *    ✓ Geocoding API
 *    (Go to "APIs & Services" > "Library" to enable them)
 * 
 * 4. Verify BILLING is enabled:
 *    - Go to "Billing" section
 *    - Link a billing account (Google provides $200 free credit/month)
 *    - You won't be charged unless you exceed the free tier
 * 
 * 5. Get your API Key:
 *    - Go to "APIs & Services" > "Credentials"
 *    - Click "Create Credentials" > "API key"
 *    - COPY the new API key (looks like: AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX)
 * 
 * 6. Paste your NEW API key in BOTH places below (lines 68 and 73)
 * 
 * 7. SAVE this file
 * 
 * 8. Refresh the page with hard reload:
 *    - Windows/Linux: Ctrl + Shift + R  or  Ctrl + F5
 *    - Mac: Cmd + Shift + R
 * 
 * 9. OPTIONAL: Restrict API key to your domain for security
 *    (But for testing, you can leave it unrestricted)
 * 
 * 
 * العربية:
 * -------
 * ١. اذهب إلى Google Cloud Console: https://console.cloud.google.com/
 * ٢. اختر مشروع "Monthly_inspection_plan" (أو أنشئ مشروعاً جديداً)
 * ٣. تأكد من تفعيل هذه الخدمات الثلاث (مهم جداً!):
 *    ✓ Maps JavaScript API
 *    ✓ Places API
 *    ✓ Geocoding API
 *    (اذهب إلى "واجهات برمجة التطبيقات والخدمات" > "المكتبة" لتفعيلها)
 * 
 * ٤. تأكد من تفعيل الفوترة:
 *    - اذهب إلى قسم "الفوترة"
 *    - اربط حساب فوترة (جوجل توفر رصيد مجاني 200 دولار شهرياً)
 *    - لن يتم فرض رسوم عليك إلا إذا تجاوزت المستوى المجاني
 * 
 * ٥. احصل على مفتاح API:
 *    - اذهب إلى "واجهات برمجة التطبيقات والخدمات" > "بيانات الاعتماد"
 *    - انقر "إنشاء بيانات اعتماد" > "مفتاح API"
 *    - انسخ مفتاح API الجديد (يبدو كالتالي: AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX)
 * 
 * ٦. الصق مفتاح API الجديد في الموضعين أدناه (السطرين 68 و 73)
 * 
 * ٧. احفظ هذا الملف
 * 
 * ٨. حدّث الصفحة بإعادة تحميل كاملة:
 *    - Windows/Linux: Ctrl + Shift + R  أو  Ctrl + F5
 *    - Mac: Cmd + Shift + R
 * 
 * ٩. اختياري: قيّد مفتاح API لنطاقك للأمان
 *    (لكن للاختبار، يمكنك تركه بدون قيود)
 * 
 * ═══════════════════════════════════════════════════════════════════════════
 */

// Set your NEW Google Maps API key here / ضع مفتاح Google Maps API الجديد هنا
// Replace 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD' with your actual key
// استبدل 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD' بمفتاحك الفعلي
const GOOGLE_MAPS_API_KEY = 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD';

// Export the API key / تصدير مفتاح API
// IMPORTANT: Update this line with the same key as above
// مهم: حدّث هذا السطر بنفس المفتاح أعلاه
if (typeof window !== 'undefined') {
    window.GOOGLE_MAPS_API_KEY = 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD';
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { GOOGLE_MAPS_API_KEY };
}
