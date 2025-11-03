# Complete Google Maps API Setup Guide
# دليل إعداد Google Maps API الشامل

## 🚨 URGENT: Required for Google Maps Functionality
## 🚨 عاجل: مطلوب لتشغيل خرائط جوجل

This guide provides **step-by-step instructions** to get Google Maps working in your application.
يوفر هذا الدليل **تعليمات مفصلة خطوة بخطوة** لتشغيل خرائط جوجل في تطبيقك.

---

## ⚡ Quick Start (3 Steps)

### Step 1: Get Your API Key / احصل على مفتاح API

1. Go to: **https://console.cloud.google.com/**
2. Create a new project (or select existing)
3. Enable these APIs:
   - Maps JavaScript API
   - Places API
   - Geocoding API
4. Go to "Credentials" → Create API Key
5. **IMPORTANT**: Set up billing (Google requires it, but gives you **$200 free per month**)

### Step 2: Configure Your API Key / قم بتكوين مفتاح API

**Option A: Using Local Configuration (Recommended - More Secure)**

1. Copy the example file:
   ```bash
   cp google-maps-config.local.js.example google-maps-config.local.js
   ```

2. Edit `google-maps-config.local.js`:
   ```javascript
   const GOOGLE_MAPS_API_KEY = 'YOUR_ACTUAL_API_KEY_HERE';  // Replace with your real key
   ```

3. Save the file (it's automatically gitignored for security)

**Option B: Direct Configuration (Quick but Less Secure)**

1. Edit `google-maps-config.js`
2. Find line 33: `apiKey: API_KEY_PLACEHOLDER,`
3. Replace with: `apiKey: 'YOUR_ACTUAL_API_KEY_HERE',`

### Step 3: Test It / اختبره

1. Open `smart-planner.html` in your browser
2. Look for: "✅ خرائط جوجل جاهزة" (Google Maps Ready)
3. Click "إضافة تفتيش من الخريطة" (Add Inspection from Map)
4. The map should load successfully! 🎉

---

## 📋 Detailed Instructions / التعليمات المفصلة

### Part 1: Creating a Google Cloud Project
### الجزء 1: إنشاء مشروع Google Cloud

#### English:
1. **Visit Google Cloud Console**
   - Go to: https://console.cloud.google.com/
   - Sign in with your Google account

2. **Create a New Project**
   - Click the project dropdown at the top
   - Click "New Project"
   - Enter project name: "Monthly Inspection Plan" (or any name you prefer)
   - Click "Create"
   - Wait 10-30 seconds for project creation

3. **Select Your Project**
   - Make sure your new project is selected in the dropdown

#### العربية:
1. **زيارة وحدة التحكم في Google Cloud**
   - اذهب إلى: https://console.cloud.google.com/
   - سجل الدخول بحساب جوجل الخاص بك

2. **إنشاء مشروع جديد**
   - انقر على القائمة المنسدلة للمشروع في الأعلى
   - انقر على "مشروع جديد"
   - أدخل اسم المشروع: "خطة التفتيش الشهرية" (أو أي اسم تفضله)
   - انقر على "إنشاء"
   - انتظر 10-30 ثانية لإنشاء المشروع

3. **اختر مشروعك**
   - تأكد من أن مشروعك الجديد محدد في القائمة المنسدلة

---

### Part 2: Enable Required APIs
### الجزء 2: تفعيل الخدمات المطلوبة

#### English:
1. **Navigate to API Library**
   - In the left sidebar, click "APIs & Services"
   - Click "Library"

2. **Enable Maps JavaScript API**
   - In the search box, type "Maps JavaScript API"
   - Click on "Maps JavaScript API"
   - Click the "Enable" button
   - Wait for it to activate (takes a few seconds)

3. **Enable Places API**
   - Click "APIs & Services" → "Library" again
   - Search for "Places API"
   - Click on it and click "Enable"

4. **Enable Geocoding API**
   - Return to the Library
   - Search for "Geocoding API"
   - Click on it and click "Enable"

#### العربية:
1. **الانتقال إلى مكتبة API**
   - في الشريط الجانبي الأيسر، انقر على "واجهات برمجة التطبيقات والخدمات"
   - انقر على "المكتبة"

2. **تفعيل Maps JavaScript API**
   - في مربع البحث، اكتب "Maps JavaScript API"
   - انقر على "Maps JavaScript API"
   - انقر على زر "تفعيل"
   - انتظر التفعيل (يستغرق بضع ثوانٍ)

3. **تفعيل Places API**
   - انقر على "واجهات برمجة التطبيقات والخدمات" → "المكتبة" مرة أخرى
   - ابحث عن "Places API"
   - انقر عليه وانقر "تفعيل"

4. **تفعيل Geocoding API**
   - ارجع إلى المكتبة
   - ابحث عن "Geocoding API"
   - انقر عليه وانقر "تفعيل"

---

### Part 3: Set Up Billing (Required)
### الجزء 3: إعداد الفوترة (مطلوب)

#### English:

**Don't worry!** Google provides **$200 free credit every month**. You won't be charged unless you exceed this limit (which is very unlikely for normal use).

1. **Access Billing**
   - Click "Billing" in the left sidebar
   - Click "Link a billing account"

2. **Create Billing Account**
   - Click "Create billing account"
   - Enter your billing information
   - Add a valid credit/debit card
   - Click "Start my free trial" or "Submit"

3. **Link to Your Project**
   - Make sure your project is linked to the billing account
   - You should see "Billing enabled" status

4. **Set Up Budget Alerts (Optional but Recommended)**
   - Go to "Budgets & alerts"
   - Create a budget alert at $50, $100, $150
   - You'll be notified before exceeding free tier

#### العربية:

**لا تقلق!** توفر جوجل **رصيد مجاني بقيمة 200 دولار كل شهر**. لن يتم فرض رسوم عليك إلا إذا تجاوزت هذا الحد (وهو أمر غير محتمل للاستخدام العادي).

1. **الوصول إلى الفوترة**
   - انقر على "الفوترة" في الشريط الجانبي الأيسر
   - انقر على "ربط حساب فوترة"

2. **إنشاء حساب فوترة**
   - انقر على "إنشاء حساب فوترة"
   - أدخل معلومات الفوترة الخاصة بك
   - أضف بطاقة ائتمان/خصم صالحة
   - انقر على "ابدأ تجربتي المجانية" أو "إرسال"

3. **الربط بمشروعك**
   - تأكد من ربط مشروعك بحساب الفوترة
   - يجب أن ترى حالة "الفوترة مفعلة"

4. **إعداد تنبيهات الميزانية (اختياري لكن موصى به)**
   - اذهب إلى "الميزانيات والتنبيهات"
   - أنشئ تنبيه ميزانية عند 50 دولار، 100 دولار، 150 دولار
   - ستتلقى إشعاراً قبل تجاوز المستوى المجاني

---

### Part 4: Create and Configure API Key
### الجزء 4: إنشاء وتكوين مفتاح API

#### English:

1. **Create API Key**
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials"
   - Select "API Key"
   - Your API key will be generated (looks like: `AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q`)
   - **IMPORTANT**: Copy this key immediately!

2. **Restrict API Key (Security)**
   - Click on the API key you just created
   - Under "Application restrictions":
     - Select "HTTP referrers (websites)"
     - Click "Add an item"
     - Add your domains:
       - For local testing: `http://localhost/*`
       - For GitHub Pages: `https://your-username.github.io/*`
       - For production: `https://yourdomain.com/*`
   
3. **Restrict APIs**
   - Under "API restrictions":
     - Select "Restrict key"
     - Check these APIs:
       ✅ Maps JavaScript API
       ✅ Places API
       ✅ Geocoding API
     - Click "Save"

4. **Name Your Key (Optional)**
   - Give it a descriptive name like: "Monthly Inspection Plan - Production"

#### العربية:

1. **إنشاء مفتاح API**
   - اذهب إلى "واجهات برمجة التطبيقات والخدمات" → "بيانات الاعتماد"
   - انقر على "إنشاء بيانات اعتماد"
   - اختر "مفتاح API"
   - سيتم إنشاء مفتاح API الخاص بك (يبدو كالتالي: `AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q`)
   - **مهم**: انسخ هذا المفتاح فوراً!

2. **تقييد مفتاح API (الأمان)**
   - انقر على مفتاح API الذي أنشأته للتو
   - تحت "قيود التطبيق":
     - اختر "مراجع HTTP (مواقع الويب)"
     - انقر على "إضافة عنصر"
     - أضف نطاقاتك:
       - للاختبار المحلي: `http://localhost/*`
       - لـ GitHub Pages: `https://your-username.github.io/*`
       - للإنتاج: `https://yourdomain.com/*`
   
3. **تقييد الخدمات**
   - تحت "قيود API":
     - اختر "تقييد المفتاح"
     - ضع علامة على هذه الخدمات:
       ✅ Maps JavaScript API
       ✅ Places API
       ✅ Geocoding API
     - انقر على "حفظ"

4. **تسمية مفتاحك (اختياري)**
   - أعطه اسماً وصفياً مثل: "خطة التفتيش الشهرية - الإنتاج"

---

### Part 5: Configure Your Application
### الجزء 5: تكوين تطبيقك

#### Method A: Local Configuration (Recommended - Secure)
#### الطريقة أ: الإعدادات المحلية (موصى بها - آمنة)

**English:**

1. **Copy the example file**:
   ```bash
   cp google-maps-config.local.js.example google-maps-config.local.js
   ```

2. **Edit the local config**:
   - Open `google-maps-config.local.js` in a text editor
   - Find: `const GOOGLE_MAPS_API_KEY = 'YOUR_ACTUAL_API_KEY_HERE';`
   - Replace `YOUR_ACTUAL_API_KEY_HERE` with your actual API key
   - Example: `const GOOGLE_MAPS_API_KEY = 'AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q';`

3. **Save the file**
   - The file is automatically gitignored
   - Your API key won't be committed to the repository
   - ✅ More secure!

**العربية:**

1. **انسخ ملف المثال**:
   ```bash
   cp google-maps-config.local.js.example google-maps-config.local.js
   ```

2. **حرر الإعدادات المحلية**:
   - افتح `google-maps-config.local.js` في محرر نصوص
   - ابحث عن: `const GOOGLE_MAPS_API_KEY = 'YOUR_ACTUAL_API_KEY_HERE';`
   - استبدل `YOUR_ACTUAL_API_KEY_HERE` بمفتاح API الفعلي الخاص بك
   - مثال: `const GOOGLE_MAPS_API_KEY = 'AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q';`

3. **احفظ الملف**
   - الملف مضاف تلقائياً لـ gitignore
   - لن يتم إضافة مفتاح API الخاص بك إلى المستودع
   - ✅ أكثر أماناً!

---

#### Method B: Direct Configuration (Quick)
#### الطريقة ب: الإعدادات المباشرة (سريعة)

**English:**

1. **Edit google-maps-config.js**:
   - Open `google-maps-config.js`
   - Find line ~33: `apiKey: API_KEY_PLACEHOLDER,`
   - Replace with: `apiKey: 'YOUR_ACTUAL_API_KEY_HERE',`
   - Example: `apiKey: 'AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q',`

2. **Save the file**

⚠️ **Warning**: If you commit this file to a public repository, your API key will be visible to everyone. Use Method A for better security.

**العربية:**

1. **حرر google-maps-config.js**:
   - افتح `google-maps-config.js`
   - ابحث عن السطر ~33: `apiKey: API_KEY_PLACEHOLDER,`
   - استبدل بـ: `apiKey: 'YOUR_ACTUAL_API_KEY_HERE',`
   - مثال: `apiKey: 'AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q',`

2. **احفظ الملف**

⚠️ **تحذير**: إذا أضفت هذا الملف إلى مستودع عام، سيكون مفتاح API الخاص بك مرئياً للجميع. استخدم الطريقة أ لأمان أفضل.

---

### Part 6: Test Your Setup
### الجزء 6: اختبار إعداداتك

#### English:

1. **Open the application**:
   - Open `smart-planner.html` in your browser
   - Or use a local server:
     ```bash
     python -m http.server 8000
     # Then open: http://localhost:8000/smart-planner.html
     ```

2. **Check for success indicators**:
   - Look for console message: `✅ Google Maps API loaded successfully!`
   - Look for status indicator: `✅ خرائط جوجل جاهزة`
   - No error messages in the browser console (F12)

3. **Test map functionality**:
   - Click the button: "إضافة تفتيش من الخريطة" (Add Inspection from Map)
   - A map should appear
   - You should be able to:
     - Zoom in/out
     - Pan around
     - Search for locations
     - Click on the map

4. **Success! 🎉**
   - If the map loads and works, you're all set!

#### العربية:

1. **افتح التطبيق**:
   - افتح `smart-planner.html` في متصفحك
   - أو استخدم خادم محلي:
     ```bash
     python -m http.server 8000
     # ثم افتح: http://localhost:8000/smart-planner.html
     ```

2. **تحقق من مؤشرات النجاح**:
   - ابحث عن رسالة في وحدة التحكم: `✅ Google Maps API loaded successfully!`
   - ابحث عن مؤشر الحالة: `✅ خرائط جوجل جاهزة`
   - لا توجد رسائل خطأ في وحدة تحكم المتصفح (F12)

3. **اختبر وظائف الخريطة**:
   - انقر على الزر: "إضافة تفتيش من الخريطة"
   - يجب أن تظهر الخريطة
   - يجب أن تكون قادراً على:
     - التكبير/التصغير
     - التحرك حول الخريطة
     - البحث عن المواقع
     - النقر على الخريطة

4. **نجاح! 🎉**
   - إذا تحمّلت الخريطة وتعمل، فأنت جاهز تماماً!

---

## 🐛 Troubleshooting / استكشاف الأخطاء

### Problem: "This page can't load Google Maps correctly"

**Possible causes:**
- ❌ Billing not enabled
- ❌ Invalid API key
- ❌ Required APIs not enabled

**Solutions:**
1. Check billing is enabled in Google Cloud Console
2. Verify your API key is correct (no extra spaces)
3. Make sure all 3 APIs are enabled (Maps JavaScript, Places, Geocoding)

---

### Problem: "RefererNotAllowedMapError"

**Cause:** Your website domain is not in the allowed list

**Solution:**
1. Go to Google Cloud Console → Credentials
2. Edit your API key
3. Add your domain to HTTP referrers:
   - `http://localhost/*` for local testing
   - `https://yourdomain.com/*` for production
4. Save and wait 5 minutes for changes to propagate

---

### Problem: Map shows but has a gray overlay with "For development purposes only"

**Cause:** Billing is not enabled

**Solution:**
1. Enable billing in Google Cloud Console
2. Add a payment method
3. Wait a few minutes for activation

---

### Problem: Console shows "Google Maps API error: ApiNotActivatedMapError"

**Cause:** One or more required APIs are not enabled

**Solution:**
Enable all three required APIs:
1. Maps JavaScript API
2. Places API
3. Geocoding API

---

## 💰 Pricing Information / معلومات التسعير

### English:

**Free Tier:**
- Google provides **$200 free credit every month**
- This covers approximately:
  - 28,000 map loads
  - 100,000 static map loads  
  - 40,000 geocoding requests
  - 40,000 places searches

**For typical use:**
- A small to medium inspection app will stay well within free limits
- You'd need thousands of daily active users to exceed free tier

**Cost monitoring:**
- Set up billing alerts at $50, $100, $150
- Monitor usage in Google Cloud Console
- You can set daily quotas to prevent overuse

### العربية:

**المستوى المجاني:**
- توفر جوجل **رصيد مجاني بقيمة 200 دولار شهرياً**
- يغطي هذا تقريباً:
  - 28,000 تحميل للخريطة
  - 100,000 تحميل لخريطة ثابتة
  - 40,000 طلب تحويل جغرافي
  - 40,000 بحث عن الأماكن

**للاستخدام النموذجي:**
- تطبيق تفتيش صغير إلى متوسط سيبقى ضمن الحدود المجانية
- ستحتاج لآلاف المستخدمين النشطين يومياً لتجاوز المستوى المجاني

**مراقبة التكاليف:**
- أعد تنبيهات الفوترة عند 50، 100، 150 دولار
- راقب الاستخدام في Google Cloud Console
- يمكنك تعيين حصص يومية لمنع الإفراط في الاستخدام

---

## 🔒 Security Best Practices / أفضل ممارسات الأمان

### English:

1. **Use Local Configuration**
   - Keep API keys in `google-maps-config.local.js` (gitignored)
   - Never commit API keys to public repositories

2. **Restrict Your API Key**
   - Always use HTTP referrer restrictions
   - Only allow your actual domains
   - Don't use wildcards like `*` (allows anyone to use your key)

3. **Restrict APIs**
   - Only enable the APIs you actually use
   - Disable unused APIs to reduce attack surface

4. **Monitor Usage**
   - Set up billing alerts
   - Check usage reports weekly
   - Investigate any unusual spikes

5. **Rotate Keys Periodically**
   - Change API keys every 3-6 months
   - Use separate keys for development and production

6. **Use Quotas**
   - Set daily quotas to prevent abuse
   - Example: 1000 requests per day for small apps

### العربية:

1. **استخدم الإعدادات المحلية**
   - احفظ مفاتيح API في `google-maps-config.local.js` (مضاف لـ gitignore)
   - لا تلتزم بمفاتيح API في المستودعات العامة أبداً

2. **قيّد مفتاح API الخاص بك**
   - استخدم دائماً قيود مراجع HTTP
   - اسمح فقط لنطاقاتك الفعلية
   - لا تستخدم أحرف البدل مثل `*` (يسمح لأي شخص باستخدام مفتاحك)

3. **قيّد الخدمات**
   - فعّل فقط الخدمات التي تستخدمها فعلياً
   - عطّل الخدمات غير المستخدمة لتقليل نقاط الضعف

4. **راقب الاستخدام**
   - أعد تنبيهات الفوترة
   - تحقق من تقارير الاستخدام أسبوعياً
   - ابحث عن أي ارتفاعات غير عادية

5. **قم بتدوير المفاتيح بشكل دوري**
   - غيّر مفاتيح API كل 3-6 أشهر
   - استخدم مفاتيح منفصلة للتطوير والإنتاج

6. **استخدم الحصص**
   - عيّن حصص يومية لمنع سوء الاستخدام
   - مثال: 1000 طلب يومياً للتطبيقات الصغيرة

---

## 📞 Support / الدعم

### Need Help? / تحتاج مساعدة؟

**English:**

1. **Check browser console** (Press F12)
   - Look for error messages
   - Red errors indicate problems

2. **Review this guide**
   - Make sure you completed all steps
   - Double-check your API key

3. **Google Maps Documentation**
   - https://developers.google.com/maps/documentation

4. **Google Cloud Support**
   - https://cloud.google.com/support

5. **Common Issues**
   - Most problems are due to billing not enabled
   - Or incorrect API key restrictions

**العربية:**

1. **تحقق من وحدة تحكم المتصفح** (اضغط F12)
   - ابحث عن رسائل الخطأ
   - الأخطاء الحمراء تشير إلى مشاكل

2. **راجع هذا الدليل**
   - تأكد من إكمال جميع الخطوات
   - تحقق مرة أخرى من مفتاح API الخاص بك

3. **وثائق خرائط جوجل**
   - https://developers.google.com/maps/documentation

4. **دعم Google Cloud**
   - https://cloud.google.com/support

5. **المشاكل الشائعة**
   - معظم المشاكل تحدث بسبب عدم تفعيل الفوترة
   - أو قيود مفتاح API غير صحيحة

---

## ✅ Checklist / قائمة التحقق

Use this checklist to ensure you've completed all steps:

- [ ] Created Google Cloud project
- [ ] Enabled Maps JavaScript API
- [ ] Enabled Places API
- [ ] Enabled Geocoding API
- [ ] Set up billing with credit card
- [ ] Created API key
- [ ] Restricted API key to my domain
- [ ] Restricted API key to required APIs only
- [ ] Configured API key in application (Method A or B)
- [ ] Tested map loading in browser
- [ ] Verified no errors in console
- [ ] Set up billing alerts (recommended)
- [ ] Documented API key location for future reference

---

## 📚 Additional Resources / موارد إضافية

- [Google Maps Platform Documentation](https://developers.google.com/maps/documentation)
- [Google Cloud Console](https://console.cloud.google.com/)
- [API Key Best Practices](https://developers.google.com/maps/api-key-best-practices)
- [Pricing Calculator](https://cloud.google.com/maps-platform/pricing)
- [Billing Documentation](https://cloud.google.com/billing/docs)

---

**Document Version:** 1.0.0  
**Last Updated:** November 3, 2025  
**Status:** ✅ Complete and Ready to Use

---

## 🎯 Summary / الملخص

**English:**
This is everything you need to get Google Maps working in your application. The process takes about 15-30 minutes for first-time setup. After configuration, maps will load automatically every time. If you encounter issues, refer to the Troubleshooting section or check the browser console for specific error messages.

**العربية:**
هذا كل ما تحتاجه لتشغيل خرائط جوجل في تطبيقك. تستغرق العملية حوالي 15-30 دقيقة للإعداد الأول. بعد التكوين، ستحمّل الخرائط تلقائياً في كل مرة. إذا واجهت مشاكل، راجع قسم استكشاف الأخطاء أو تحقق من وحدة تحكم المتصفح لرسائل خطأ محددة.
