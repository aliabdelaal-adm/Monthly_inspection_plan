# Google Maps API Setup Guide
# دليل إعداد Google Maps API

## 🎯 Overview / نظرة عامة

This guide will help you set up Google Maps API for the Smart Planner application.
سيساعدك هذا الدليل في إعداد Google Maps API لتطبيق المخطط الذكي.

---

## 📋 Prerequisites / المتطلبات

- A Google account / حساب جوجل
- A credit/debit card for billing (required by Google, even for free tier) / بطاقة ائتمان/خصم للفوترة (مطلوبة من جوجل حتى للمستوى المجاني)
- Access to Google Cloud Console / الوصول إلى Google Cloud Console

---

## 🚀 Step-by-Step Setup / الإعداد خطوة بخطوة

### Step 1: Create a Google Cloud Project
### الخطوة 1: إنشاء مشروع Google Cloud

**English:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with your Google account
3. Click on the project dropdown at the top
4. Click "New Project"
5. Enter a project name (e.g., "Monthly Inspection Plan")
6. Click "Create"
7. Wait for the project to be created (this may take a few seconds)

**العربية:**
1. اذهب إلى [Google Cloud Console](https://console.cloud.google.com/)
2. سجل الدخول بحساب جوجل الخاص بك
3. انقر على القائمة المنسدلة للمشروع في الأعلى
4. انقر على "مشروع جديد"
5. أدخل اسم المشروع (مثال: "خطة التفتيش الشهرية")
6. انقر على "إنشاء"
7. انتظر حتى يتم إنشاء المشروع (قد يستغرق بضع ثوانٍ)

---

### Step 2: Enable Required APIs
### الخطوة 2: تفعيل الخدمات المطلوبة

**English:**
1. In your project, go to "APIs & Services" > "Library"
2. Search for and enable the following APIs:
   - **Maps JavaScript API** (required for map display)
   - **Places API** (required for location search)
   - **Geocoding API** (required for address conversion)
3. For each API:
   - Click on the API name
   - Click "Enable"
   - Wait for activation

**العربية:**
1. في مشروعك، اذهب إلى "واجهات برمجة التطبيقات والخدمات" > "المكتبة"
2. ابحث وفعّل الخدمات التالية:
   - **Maps JavaScript API** (مطلوب لعرض الخريطة)
   - **Places API** (مطلوب للبحث عن الأماكن)
   - **Geocoding API** (مطلوب لتحويل العناوين)
3. لكل واجهة برمجة تطبيقات:
   - انقر على اسم الخدمة
   - انقر على "تفعيل"
   - انتظر التفعيل

---

### Step 3: Set Up Billing
### الخطوة 3: إعداد الفوترة

**English:**
1. Go to "Billing" in the left sidebar
2. Click "Link a billing account"
3. Create a new billing account or link an existing one
4. Enter your credit/debit card information
5. Complete the billing setup

**Important Notes:**
- Google Maps API requires billing to be enabled
- Google provides $200 free credits per month
- You won't be charged unless you exceed the free tier
- You can set up billing alerts to avoid unexpected charges

**العربية:**
1. اذهب إلى "الفوترة" في الشريط الجانبي الأيسر
2. انقر على "ربط حساب فوترة"
3. أنشئ حساب فوترة جديد أو اربط حساباً موجوداً
4. أدخل معلومات بطاقة الائتمان/الخصم الخاصة بك
5. أكمل إعداد الفوترة

**ملاحظات مهمة:**
- Google Maps API يتطلب تفعيل الفوترة
- توفر جوجل رصيد مجاني بقيمة 200 دولار شهرياً
- لن يتم فرض رسوم عليك إلا إذا تجاوزت المستوى المجاني
- يمكنك إعداد تنبيهات الفوترة لتجنب الرسوم غير المتوقعة

---

### Step 4: Create API Key
### الخطوة 4: إنشاء مفتاح API

**English:**
1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "API Key"
3. Your API key will be created and displayed
4. **IMPORTANT:** Copy this key immediately - you'll need it later
5. Click "Restrict Key" (recommended for security)

**العربية:**
1. اذهب إلى "واجهات برمجة التطبيقات والخدمات" > "بيانات الاعتماد"
2. انقر على "إنشاء بيانات اعتماد" > "مفتاح API"
3. سيتم إنشاء مفتاح API وعرضه
4. **مهم:** انسخ هذا المفتاح فوراً - ستحتاجه لاحقاً
5. انقر على "تقييد المفتاح" (موصى به للأمان)

---

### Step 5: Restrict API Key (Security)
### الخطوة 5: تقييد مفتاح API (الأمان)

**English:**
1. In the API key settings, under "Application restrictions":
   - Select "HTTP referrers (websites)"
   
2. Add your website URLs:
   - For local development: `http://localhost/*`
   - For GitHub Pages: `https://<your-username>.github.io/*`
   - For custom domain: `https://yourdomain.com/*`
   
3. Under "API restrictions":
   - Select "Restrict key"
   - Choose:
     - Maps JavaScript API
     - Places API
     - Geocoding API
     
4. Click "Save"

**العربية:**
1. في إعدادات مفتاح API، تحت "قيود التطبيق":
   - اختر "مراجع HTTP (مواقع الويب)"
   
2. أضف عناوين URL لموقعك:
   - للتطوير المحلي: `http://localhost/*`
   - لـ GitHub Pages: `https://<اسم-المستخدم>.github.io/*`
   - للنطاق المخصص: `https://yourdomain.com/*`
   
3. تحت "قيود API":
   - اختر "تقييد المفتاح"
   - اختر:
     - Maps JavaScript API
     - Places API
     - Geocoding API
     
4. انقر على "حفظ"

---

### Step 6: Configure the Application
### الخطوة 6: تكوين التطبيق

**English:**
1. Open the file `google-maps-config.js` in your project
2. Find the line: `apiKey: 'YOUR_GOOGLE_MAPS_API_KEY_HERE',`
3. Replace `YOUR_GOOGLE_MAPS_API_KEY_HERE` with your actual API key
4. Save the file

**Example:**
```javascript
const GOOGLE_MAPS_CONFIG = {
    apiKey: 'AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q',  // Your actual key
    libraries: ['places', 'geometry'],
    language: 'ar',
    // ... rest of config
};
```

**العربية:**
1. افتح ملف `google-maps-config.js` في مشروعك
2. ابحث عن السطر: `apiKey: 'YOUR_GOOGLE_MAPS_API_KEY_HERE',`
3. استبدل `YOUR_GOOGLE_MAPS_API_KEY_HERE` بمفتاح API الفعلي الخاص بك
4. احفظ الملف

**مثال:**
```javascript
const GOOGLE_MAPS_CONFIG = {
    apiKey: 'AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q',  // مفتاحك الفعلي
    libraries: ['places', 'geometry'],
    language: 'ar',
    // ... بقية الإعدادات
};
```

---

### Step 7: Test the Integration
### الخطوة 7: اختبار التكامل

**English:**
1. Open `smart-planner.html` in your browser
2. Wait for the page to load completely
3. Look for the status indicator that should show: "✅ خرائط جوجل جاهزة"
4. Click "إضافة تفتيش من الخريطة" button
5. The map should load and display

**If the map doesn't load:**
- Check the browser console (F12) for errors
- Verify your API key is correct
- Ensure billing is enabled
- Check that all required APIs are enabled
- Verify your domain is in the allowed referrers

**العربية:**
1. افتح `smart-planner.html` في متصفحك
2. انتظر حتى يتم تحميل الصفحة بالكامل
3. ابحث عن مؤشر الحالة الذي يجب أن يظهر: "✅ خرائط جوجل جاهزة"
4. انقر على زر "إضافة تفتيش من الخريطة"
5. يجب أن تحمّل الخريطة وتظهر

**إذا لم تحمّل الخريطة:**
- تحقق من وحدة تحكم المتصفح (F12) بحثاً عن الأخطاء
- تأكد من صحة مفتاح API الخاص بك
- تأكد من تفعيل الفوترة
- تحقق من تفعيل جميع الخدمات المطلوبة
- تأكد من أن نطاقك موجود في المراجع المسموح بها

---

## 💰 Pricing Information / معلومات التسعير

**English:**
- Google provides **$200 free credit per month**
- This covers approximately:
  - 28,000 map loads
  - 100,000 static map loads
  - 40,000 geocoding requests
- For most small to medium applications, you won't exceed the free tier
- You can set up billing alerts in Google Cloud Console

**العربية:**
- توفر جوجل **رصيد مجاني بقيمة 200 دولار شهرياً**
- يغطي هذا تقريباً:
  - 28,000 تحميل للخريطة
  - 100,000 تحميل لخريطة ثابتة
  - 40,000 طلب تحويل جغرافي
- بالنسبة لمعظم التطبيقات الصغيرة إلى المتوسطة، لن تتجاوز المستوى المجاني
- يمكنك إعداد تنبيهات الفوترة في Google Cloud Console

For detailed pricing: https://cloud.google.com/maps-platform/pricing

---

## 🔒 Security Best Practices / أفضل ممارسات الأمان

**English:**
1. **Always restrict your API key** - Never use unrestricted keys
2. **Use HTTP referrer restrictions** - Limit to your domain only
3. **Enable only required APIs** - Don't enable APIs you don't use
4. **Monitor usage** - Set up billing alerts
5. **Rotate keys periodically** - Change keys every few months
6. **Never commit keys to public repositories** - Use environment variables
7. **Use separate keys** - Different keys for dev/staging/production

**العربية:**
1. **قيّد مفتاح API دائماً** - لا تستخدم مفاتيح غير مقيدة أبداً
2. **استخدم قيود مراجع HTTP** - حدد نطاقك فقط
3. **فعّل الخدمات المطلوبة فقط** - لا تفعّل خدمات لا تستخدمها
4. **راقب الاستخدام** - أعد تنبيهات الفوترة
5. **قم بتدوير المفاتيح بشكل دوري** - غيّر المفاتيح كل بضعة أشهر
6. **لا تلتزم بالمفاتيح في المستودعات العامة** - استخدم متغيرات البيئة
7. **استخدم مفاتيح منفصلة** - مفاتيح مختلفة للتطوير/التجهيز/الإنتاج

---

## 🐛 Troubleshooting / استكشاف الأخطاء

### Error: "This page can't load Google Maps correctly"
### خطأ: "لا يمكن لهذه الصفحة تحميل خرائط جوجل بشكل صحيح"

**Possible causes / الأسباب المحتملة:**
- Billing not enabled / الفوترة غير مفعلة
- Invalid API key / مفتاح API غير صالح
- Required APIs not enabled / الخدمات المطلوبة غير مفعلة
- Domain restrictions / قيود النطاق

**Solutions / الحلول:**
1. Enable billing in Google Cloud Console
2. Verify API key is correct
3. Enable all required APIs (Maps JavaScript, Places, Geocoding)
4. Check domain restrictions in API key settings

---

### Error: "RefererNotAllowedMapError"
### خطأ: "RefererNotAllowedMapError"

**Cause / السبب:**
Your domain is not in the allowed referrers list
نطاقك غير موجود في قائمة المراجع المسموح بها

**Solution / الحل:**
1. Go to API key settings
2. Add your domain to HTTP referrers
3. Don't forget the `/*` wildcard

---

### Error: "ApiNotActivatedMapError"
### خطأ: "ApiNotActivatedMapError"

**Cause / السبب:**
One or more required APIs are not enabled
واحدة أو أكثر من الخدمات المطلوبة غير مفعلة

**Solution / الحل:**
1. Go to "APIs & Services" > "Library"
2. Enable Maps JavaScript API
3. Enable Places API
4. Enable Geocoding API

---

## 📞 Support / الدعم

**English:**
If you encounter issues:
1. Check the browser console (F12) for detailed error messages
2. Review this guide and ensure all steps are completed
3. Check Google's official documentation: https://developers.google.com/maps
4. Contact the application developer with:
   - Error messages from console
   - Screenshots of the issue
   - Steps to reproduce

**العربية:**
إذا واجهت مشاكل:
1. تحقق من وحدة تحكم المتصفح (F12) لرسائل الخطأ التفصيلية
2. راجع هذا الدليل وتأكد من إكمال جميع الخطوات
3. راجع وثائق جوجل الرسمية: https://developers.google.com/maps
4. تواصل مع مطور التطبيق مع:
   - رسائل الخطأ من وحدة التحكم
   - لقطات الشاشة للمشكلة
   - خطوات إعادة إنتاج المشكلة

---

## 📚 Additional Resources / موارد إضافية

- [Google Maps Platform Documentation](https://developers.google.com/maps/documentation)
- [Google Cloud Console](https://console.cloud.google.com/)
- [API Key Best Practices](https://developers.google.com/maps/api-key-best-practices)
- [Pricing Calculator](https://cloud.google.com/maps-platform/pricing)

---

**Last Updated:** November 3, 2025
**Version:** 1.0.0
