# دليل إعداد Google Maps API للمطورين
## Setup Guide for Google Maps API - Smart Planner

---

## 🎯 الهدف - Objective

إصلاح مشكلة عدم تحميل الخريطة في Smart Planner حتى يستطيع المطور إضافة تفتيش من الخريطة مباشرة.

**EN:** Fix the map loading issue in Smart Planner so developers can add inspections directly from the map.

---

## 📋 معلومات المشروع - Project Information

- **اسم المشروع / Project Name:** `monthly-insection-plan`
- **معرف المشروع / Project ID:** `monthly-insection-plan`
- **البريد الإلكتروني للخدمة:** `monthly-inspection-plan@monthly-insection-plan.iam.gserviceaccount.com`

**⚠️ ملاحظة:** هناك خطأ إملائي في اسم المشروع الأصلي ("insection" بدلاً من "inspection"). هذا الخطأ موجود في Google Cloud نفسه ولا يمكن تغييره، لكنه لا يؤثر على عمل الخرائط.

**Note:** There's a typo in the original project name ("insection" instead of "inspection"). This exists in Google Cloud and cannot be changed, but it doesn't affect maps functionality.

---

## ⚠️ ملاحظة هامة جداً - IMPORTANT NOTE

**بيانات حساب الخدمة (Service Account) التي قدمتها لا يمكن استخدامها مباشرة للخرائط!**

**EN:** The service account credentials you provided CANNOT be used directly for browser-based maps!

### لماذا؟ - Why?

- **حساب الخدمة (Service Account):** يُستخدم للمصادقة من جانب الخادم (Server-side)
- **مفتاح API للمتصفح (Browser API Key):** مطلوب لـ Google Maps JavaScript API في المتصفح

**EN:**
- **Service Account:** Used for server-side authentication
- **Browser API Key:** Required for Google Maps JavaScript API in browser

---

## 🚀 الحل - Solution

نحتاج إلى **إنشاء مفتاح API للمتصفح** من نفس مشروع Google Cloud الخاص بك.

**EN:** We need to **create a browser API key** from your Google Cloud project.

---

## 📝 الخطوات التفصيلية - Detailed Steps

### الخطوة 1️⃣: فتح Google Cloud Console

1. اذهب إلى: [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. قم بتسجيل الدخول بنفس الحساب الذي أنشأت به المشروع
3. من القائمة العلوية، اختر المشروع: **`monthly-insection-plan`**

**EN:**
1. Go to: [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. Sign in with the same account you created the project with
3. From the top menu, select project: **`monthly-insection-plan`**

---

### الخطوة 2️⃣: تفعيل الخدمات المطلوبة - Enable Required APIs

يجب تفعيل 3 خدمات مهمة:

1. في القائمة الجانبية، اذهب إلى: **APIs & Services** → **Library**
2. ابحث وفعّل كل خدمة من التالي:

   #### أ) Maps JavaScript API
   - ابحث عن: "Maps JavaScript API"
   - انقر على النتيجة
   - اضغط **Enable** (إذا لم تكن مفعلة)

   #### ب) Places API
   - ابحث عن: "Places API"
   - انقر على النتيجة
   - اضغط **Enable**

   #### ج) Geocoding API
   - ابحث عن: "Geocoding API"
   - انقر على النتيجة
   - اضغط **Enable**

**رابط مباشر:** [https://console.cloud.google.com/apis/library](https://console.cloud.google.com/apis/library)

**EN:** Enable these 3 APIs:
- Maps JavaScript API
- Places API
- Geocoding API

---

### الخطوة 3️⃣: تفعيل الفوترة - Enable Billing

⚠️ **مهم جداً:** Google Maps يتطلب تفعيل الفوترة

**لكن لا تقلق!** 💚

- Google تمنحك **200 دولار رصيد مجاني كل شهر**
- الاستخدام العادي لن يتجاوز المجاني
- لن يتم فرض رسوم إلا إذا تجاوزت الحد المجاني

#### الخطوات:

1. في القائمة الجانبية، اذهب إلى: **Billing**
2. إذا لم يكن لديك حساب فوترة:
   - انقر **Link a Billing Account**
   - انقر **Create Billing Account**
   - أدخل معلومات بطاقة الائتمان (للتحقق فقط)
   - اقبل الشروط
3. اربط حساب الفوترة بالمشروع

**رابط مباشر:** [https://console.cloud.google.com/billing](https://console.cloud.google.com/billing)

**EN:** 
- Billing is required but Google provides **$200 free credit monthly**
- Normal usage won't exceed the free tier
- Link a billing account to your project

---

### الخطوة 4️⃣: إنشاء مفتاح API - Create API Key

1. في القائمة الجانبية، اذهب إلى: **APIs & Services** → **Credentials**
2. في الأعلى، انقر على: **+ Create Credentials**
3. اختر: **API key**
4. سيظهر مفتاح API الجديد في نافذة منبثقة
5. **انسخ المفتاح** (يبدأ بـ `AIzaSy...`)
6. يمكنك الضغط على **Restrict Key** لتقييد الاستخدام (اختياري للآن)

**رابط مباشر:** [https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials)

**EN:**
1. Go to: APIs & Services → Credentials
2. Click: + Create Credentials
3. Select: API key
4. Copy the new API key (starts with `AIzaSy...`)

---

### الخطوة 5️⃣: تحديث ملف الإعدادات - Update Configuration File

الآن لديك مفتاح API، نحتاج لوضعه في المشروع.

#### طريقة 1: استخدام أداة الإعداد (موصى بها) ✅

1. افتح الملف: **`setup-google-maps-api.html`** في المتصفح
2. اتبع الخطوات في الصفحة
3. الصق مفتاح API في الحقل
4. انقر "التحقق وإنشاء ملف الإعدادات"
5. حمّل الملف أو انسخ الكود
6. استبدل محتوى `google-maps-config.local.js` بالكود الجديد

#### طريقة 2: التحديث اليدوي

1. افتح الملف: **`google-maps-config.local.js`**
2. ابحث عن السطر رقم 81 تقريباً:
   ```javascript
   const GOOGLE_MAPS_API_KEY = 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD';
   ```
3. استبدل `'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD'` بمفتاح API الخاص بك
4. ابحث عن السطر رقم 87 تقريباً:
   ```javascript
   window.GOOGLE_MAPS_API_KEY = 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD';
   ```
5. استبدل `'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD'` بنفس المفتاح
6. **احفظ الملف**

**مثال:**
```javascript
// قبل - Before
const GOOGLE_MAPS_API_KEY = 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD';

// بعد - After
const GOOGLE_MAPS_API_KEY = 'AIzaSyBIu6hLqc2mW6WYKTf1JCMSjKCkN1E-xVU';
```

---

### الخطوة 6️⃣: اختبار الإعداد - Test the Setup

1. احفظ جميع التغييرات
2. افتح **`smart-planner.html`** في المتصفح
3. اضغط على **Ctrl + Shift + R** (Windows/Linux) أو **Cmd + Shift + R** (Mac) لإعادة تحميل كاملة
4. افتح أدوات المطور (F12)
5. تحقق من رسائل Console:
   - يجب أن ترى: ✅ "Google Maps API loaded successfully"
   - يجب ألا ترى أخطاء حمراء عن Google Maps

6. جرب فتح خريطة في Smart Planner:
   - انقر على زر إضافة تفتيش
   - يجب أن تظهر الخريطة بدون أخطاء

**EN:**
1. Save all changes
2. Open `smart-planner.html` in browser
3. Hard reload: Ctrl+Shift+R (Win/Linux) or Cmd+Shift+R (Mac)
4. Check console for: ✅ "Google Maps API loaded successfully"
5. Try opening map in Smart Planner

---

## 🔒 اختياري: تقييد مفتاح API (للأمان) - Optional: Restrict API Key

بعد التأكد من عمل الخريطة، يُنصح بتقييد المفتاح:

1. في Google Cloud Console → Credentials
2. انقر على مفتاح API الذي أنشأته
3. في قسم **"Application restrictions"**:
   - اختر: **HTTP referrers (web sites)**
   - أضف النطاق الخاص بك:
     - للتطوير المحلي: `localhost/*`
     - للموقع المباشر: `your-domain.com/*`
4. في قسم **"API restrictions"**:
   - اختر: **Restrict key**
   - فعّل فقط:
     - Maps JavaScript API
     - Places API
     - Geocoding API
5. اضغط **Save**

**EN:**
- Go to Credentials → Click on your API key
- Set "Application restrictions" to "HTTP referrers"
- Add your domain: `your-domain.com/*`
- Set "API restrictions" to the 3 required APIs
- Save

---

## ❓ حل المشاكل الشائعة - Troubleshooting

### مشكلة 1: "This page can't load Google Maps correctly"

**السبب:** الفوترة غير مفعلة أو مفتاح API غير صالح

**الحل:**
1. تأكد من تفعيل الفوترة في Google Cloud
2. تأكد من نسخ مفتاح API بشكل صحيح
3. تأكد من تفعيل الخدمات الثلاث المطلوبة

---

### مشكلة 2: "RefererNotAllowedMapError"

**السبب:** قيود النطاق صارمة جداً

**الحل:**
1. اذهب إلى Credentials في Google Cloud
2. انقر على مفتاح API
3. في "Application restrictions":
   - اختر "None" مؤقتاً للاختبار
   - أو أضف النطاق الصحيح
4. احفظ وحدّث الصفحة

---

### مشكلة 3: الخريطة لا تظهر ولا توجد أخطاء

**الحل:**
1. افتح أدوات المطور (F12)
2. اذهب إلى تبويب Console
3. ابحث عن رسائل Google Maps
4. تأكد من وجود: `✅ Google Maps API loaded successfully`
5. إذا لم تجد الرسالة، تأكد من:
   - حفظ ملف `google-maps-config.local.js`
   - إعادة تحميل الصفحة بـ Ctrl+Shift+R

---

### مشكلة 4: "API key not valid"

**السبب:** مفتاح API غير صحيح أو له قيود

**الحل:**
1. تأكد من نسخ المفتاح كاملاً
2. تأكد من عدم وجود مسافات في البداية أو النهاية
3. تأكد من أن المفتاح يبدأ بـ `AIza`
4. جرب إنشاء مفتاح جديد

---

## 📞 الدعم - Support

إذا واجهت مشاكل:

1. **تحقق من Console في المتصفح** (F12 → Console)
2. **انسخ رسالة الخطأ بالكامل**
3. **تأكد من إتمام جميع الخطوات**
4. **جرب الملف:** `setup-google-maps-api.html` للمساعدة

---

## ✅ قائمة التحقق النهائية - Final Checklist

قبل الإبلاغ عن مشكلة، تأكد من:

- [ ] فتحت Google Cloud Console واخترت المشروع الصحيح
- [ ] فعّلت Maps JavaScript API
- [ ] فعّلت Places API
- [ ] فعّلت Geocoding API
- [ ] فعّلت الفوترة وربطت حساب فوترة
- [ ] أنشأت مفتاح API جديد ونسخته
- [ ] حدّثت ملف `google-maps-config.local.js` بالمفتاح الجديد
- [ ] حفظت الملف
- [ ] أعدت تحميل الصفحة بـ Ctrl+Shift+R
- [ ] فتحت Console وتحققت من الرسائل

---

## 🎉 نجح الإعداد! - Setup Successful!

عندما ترى هذه الرسائل في Console:

```
✅ Google Maps API key loaded from local configuration
✅ تم تحميل مفتاح Google Maps API من الإعدادات المحلية
✅ API Key validation passed
✅ تم التحقق من صحة مفتاح API بنجاح
✅ Google Maps API loaded successfully!
✅ تم تحميل Google Maps API بنجاح!
```

**تهانينا! 🎊** الآن يمكنك:
- استخدام الخرائط في Smart Planner
- إضافة تفتيشات مباشرة من الخريطة
- عرض مواقع المحلات على الخريطة

---

## 📚 مصادر إضافية - Additional Resources

- [Google Maps JavaScript API Documentation](https://developers.google.com/maps/documentation/javascript)
- [Google Cloud Console](https://console.cloud.google.com/)
- [Google Maps Pricing](https://mapsplatform.google.com/pricing/)
- [API Key Best Practices](https://developers.google.com/maps/api-security-best-practices)

---

**آخر تحديث:** 2025-11-05
**الإصدار:** 1.0
