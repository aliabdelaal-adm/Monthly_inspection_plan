# دليل استكشاف أخطاء خرائط جوجل
# Google Maps Troubleshooting Guide

## المشكلة / Problem

عند محاولة استخدام خرائط جوجل في التطبيق، قد تظهر رسالة خطأ:
```
❌ Google Maps loading error: Google Maps blocked by browser/extension (ERR_BLOCKED_BY_CLIENT)
```

When trying to use Google Maps in the application, you may see an error message:
```
❌ Google Maps loading error: Google Maps blocked by browser/extension (ERR_BLOCKED_BY_CLIENT)
```

---

## الأسباب المحتملة / Possible Causes

### 🔒 1. مانع الإعلانات / Ad Blocker
معظم إضافات مانع الإعلانات تحجب طلبات Google Maps API تلقائياً لأنها تعتبرها إعلانات أو تتبع.

Most ad blocker extensions automatically block Google Maps API requests because they consider them as ads or tracking.

**الحلول الشائعة / Common ad blockers:**
- uBlock Origin
- AdBlock
- AdBlock Plus
- Ghostery
- Privacy Badger

### 🛡️ 2. إضافات الخصوصية / Privacy Extensions
إضافات الخصوصية قد تحجب الاتصال بخوادم Google.

Privacy extensions may block connections to Google servers.

**أمثلة / Examples:**
- Privacy Badger
- Disconnect
- HTTPS Everywhere (في بعض الحالات / in some cases)
- NoScript

### ⚙️ 3. إعدادات المتصفح / Browser Settings
بعض المتصفحات لديها إعدادات خصوصية وأمان صارمة.

Some browsers have strict privacy and security settings.

**المتصفحات المتأثرة / Affected browsers:**
- Brave Browser (يحجب افتراضياً / blocks by default)
- Firefox (مع إعدادات خصوصية محسّنة / with enhanced privacy settings)
- Safari (مع منع التتبع / with tracking prevention)

### 🌐 4. جدار حماية الشبكة / Network Firewall
جدار حماية الشبكة أو الشركة قد يحجب الوصول إلى Google APIs.

Network or corporate firewall may block access to Google APIs.

---

## الحلول / Solutions

### ✅ الحل 1: تعطيل مانع الإعلانات / Disable Ad Blocker

#### لـ uBlock Origin:
1. انقر على أيقونة uBlock في شريط الأدوات
   Click on uBlock icon in toolbar
2. انقر على زر الطاقة الكبير لتعطيله لهذا الموقع
   Click the big power button to disable it for this site
3. أعد تحميل الصفحة
   Reload the page

#### لـ AdBlock/AdBlock Plus:
1. انقر على أيقونة AdBlock
   Click on AdBlock icon
2. اختر "لا تشغل على صفحات هذا النطاق"
   Select "Don't run on pages on this domain"
3. أعد تحميل الصفحة
   Reload the page

### ✅ الحل 2: إضافة استثناء / Add Exception

إذا كنت لا تريد تعطيل مانع الإعلانات بالكامل:

If you don't want to disable the ad blocker completely:

1. افتح إعدادات الإضافة
   Open extension settings
2. ابحث عن قسم "القائمة البيضاء" أو "المواقع المسموح بها"
   Look for "Whitelist" or "Allowed sites" section
3. أضف هذه النطاقات:
   Add these domains:
   ```
   maps.googleapis.com
   maps.google.com
   *.googleapis.com
   ```

### ✅ الحل 3: إعدادات المتصفح / Browser Settings

#### Brave Browser:
1. انقر على أيقونة الأسد بجانب شريط العنوان
   Click on the lion icon next to the address bar
2. عطّل "Block scripts" لهذا الموقع
   Disable "Block scripts" for this site
3. عطّل "Block all cookies" لهذا الموقع
   Disable "Block all cookies" for this site

#### Firefox:
1. اذهب إلى الإعدادات → الخصوصية والأمان
   Go to Settings → Privacy & Security
2. في قسم "الحماية المحسّنة من التتبع":
   In "Enhanced Tracking Protection" section:
   - اختر "مخصص"
   - Select "Custom"
   - أضف استثناء لهذا الموقع
   - Add exception for this site

#### Safari:
1. Safari → التفضيلات → الخصوصية
   Safari → Preferences → Privacy
2. قم بإلغاء تحديد "منع التتبع عبر المواقع"
   Uncheck "Prevent cross-site tracking"
3. أعد تحميل الصفحة
   Reload the page

### ✅ الحل 4: وضع التصفح الخاص / Private Browsing

جرّب فتح الموقع في وضع التصفح الخاص أو وضع التخفي:

Try opening the site in private/incognito mode:

- **Chrome/Edge**: Ctrl+Shift+N
- **Firefox**: Ctrl+Shift+P
- **Safari**: Cmd+Shift+N

معظم الإضافات لا تعمل في هذا الوضع افتراضياً.

Most extensions don't work in this mode by default.

### ✅ الحل 5: تحقق من وحدة التحكم / Check Console

1. افتح أدوات المطور (F12)
   Open Developer Tools (F12)
2. اذهب إلى تبويب "Console"
   Go to "Console" tab
3. ابحث عن رسائل خطأ تحتوي على:
   Look for error messages containing:
   ```
   ERR_BLOCKED_BY_CLIENT
   blocked by extension
   Failed to load resource
   ```
4. اقرأ الرسالة بعناية لتحديد السبب الدقيق
   Read the message carefully to identify the exact cause

---

## التحقق من نجاح الحل / Verify Solution

بعد تطبيق أي من الحلول أعلاه، افتح وحدة التحكم (F12) وابحث عن:

After applying any solution above, open Console (F12) and look for:

```
✅ Google Maps API loaded successfully!
✅ تم تحميل Google Maps API بنجاح!
```

إذا رأيت هذه الرسالة، فقد تم حل المشكلة!

If you see this message, the problem is solved!

---

## حلول بديلة / Alternative Solutions

إذا لم تنجح جميع الحلول أعلاه، يمكنك:

If none of the solutions above work, you can:

### 1. استخدام الروابط المباشرة / Use Direct Links
التطبيق يحتوي على روابط مباشرة لخرائط جوجل لكل محل. انقر على أيقونة 📍 بجانب اسم المحل.

The app contains direct links to Google Maps for each shop. Click on the 📍 icon next to the shop name.

### 2. استخدام متصفح مختلف / Use Different Browser
جرّب متصفح آخر لا يحتوي على إضافات حظر.

Try another browser without blocking extensions.

### 3. تعطيل جميع الإضافات مؤقتاً / Disable All Extensions Temporarily
```
Chrome/Edge: chrome://extensions
Firefox: about:addons
```
عطّل جميع الإضافات ثم أعد تحميل الصفحة.

Disable all extensions then reload the page.

---

## معلومات تقنية للمطورين / Technical Information for Developers

### ملفات الإعداد / Configuration Files

```
google-maps-config.js       - الإعدادات الأساسية / Main configuration
google-maps-config.local.js - مفتاح API (مُتجاهل في git) / API key (gitignored)
google-maps-loader.js       - محمل الخرائط / Maps loader
google-maps-init-checker.js - فحص التهيئة / Initialization checker
```

### التحقق من التحميل / Check Loading

في وحدة التحكم:

In Console:

```javascript
// Check if config is loaded
console.log(window.GOOGLE_MAPS_CONFIG);

// Check if loader is ready
console.log(window.googleMapsLoader);

// Check loading status
console.log(window.googleMapsLoader.getStatus());

// Manual init if needed
window.googleMapsLoader.init();
```

### إعادة محاولة التحميل / Retry Loading

```javascript
// Retry loading manually
window.googleMapsLoader.load()
  .then(() => console.log('✅ Loaded!'))
  .catch(err => console.error('❌ Failed:', err));
```

---

## الأسئلة الشائعة / FAQ

### س: هل أحتاج إلى تعطيل مانع الإعلانات بشكل دائم؟
**ج:** لا، يمكنك إضافة استثناء لهذا الموقع فقط.

### Q: Do I need to disable ad blocker permanently?
**A:** No, you can add an exception for this site only.

---

### س: هل هذا آمن؟
**ج:** نعم، التطبيق يستخدم Google Maps API الرسمي فقط لعرض المواقع. لا يوجد تتبع أو إعلانات.

### Q: Is this safe?
**A:** Yes, the app uses official Google Maps API only to display locations. No tracking or ads.

---

### س: لماذا لا تعمل الخرائط في شبكة الشركة؟
**ج:** قد يكون جدار حماية الشركة يحجب الوصول إلى Google APIs. اتصل بقسم IT.

### Q: Why don't maps work on corporate network?
**A:** Corporate firewall may be blocking access to Google APIs. Contact IT department.

---

## الدعم / Support

إذا استمرت المشكلة بعد تجربة جميع الحلول:

If the problem persists after trying all solutions:

1. افتح issue جديدة في GitHub مع:
   Open a new GitHub issue with:
   - نوع المتصفح والإصدار / Browser type and version
   - الإضافات المثبتة / Installed extensions
   - رسالة الخطأ الكاملة من Console / Full error message from Console
   - لقطة شاشة / Screenshot

2. أو استخدم الروابط المباشرة كحل بديل
   Or use direct links as alternative solution

---

## آخر تحديث / Last Updated
2025-11-14

## الإصدار / Version
3.0 - Enhanced Error Handling
