# إصلاح سريع: خرائط جوجل لا تعمل
# Quick Fix: Google Maps Not Working

## المشكلة / Problem
❌ خرائط جوجل محجوبة / Google Maps is blocked

## الحل السريع (30 ثانية) / Quick Fix (30 seconds)

### الخطوة 1: تحديد السبب / Step 1: Identify Cause
افتح أدوات المطور (اضغط **F12**)

Open Developer Tools (press **F12**)

### الخطوة 2: انظر إلى Console / Step 2: Look at Console
ابحث عن / Look for:
```
❌ Google Maps blocked by browser/extension (ERR_BLOCKED_BY_CLIENT)
```

### الخطوة 3: الحل حسب السبب / Step 3: Fix Based on Cause

#### ✅ إذا كان لديك مانع إعلانات / If you have ad blocker:
1. انقر على أيقونة مانع الإعلانات في شريط الأدوات
   Click on ad blocker icon in toolbar
2. اختر "تعطيل لهذا الموقع" أو "إيقاف على هذه الصفحة"
   Choose "Disable for this site" or "Pause on this page"
3. أعد تحميل الصفحة (**F5** أو **Ctrl+R**)
   Reload page (**F5** or **Ctrl+R**)

#### ✅ إذا كنت تستخدم Brave Browser:
1. انقر على أيقونة الأسد 🦁 بجانب شريط العنوان
   Click on lion icon 🦁 next to address bar
2. عطّل "Block scripts"
   Disable "Block scripts"  
3. أعد تحميل الصفحة
   Reload page

#### ✅ إذا كنت تستخدم Firefox مع إعدادات خصوصية صارمة:
1. اذهب إلى الإعدادات → الخصوصية والأمان
   Go to Settings → Privacy & Security
2. في "الحماية المحسّنة من التتبع"، اختر "مخصص"
   In "Enhanced Tracking Protection", choose "Custom"
3. أضف استثناء لهذا الموقع
   Add exception for this site

### الخطوة 4: التحقق / Step 4: Verify
ابحث في Console عن / Look in Console for:
```
✅ Google Maps API loaded successfully!
✅ تم تحميل Google Maps API بنجاح!
```

---

## حل بديل فوري / Instant Alternative
💡 **استخدم الروابط المباشرة / Use Direct Links**

بدلاً من انتظار تحميل الخرائط، انقر على أيقونة 📍 بجانب اسم المحل لفتح خرائط جوجل مباشرة في تبويب جديد.

Instead of waiting for maps to load, click on the 📍 icon next to the shop name to open Google Maps directly in a new tab.

---

## الأسباب الشائعة / Common Causes

| السبب / Cause | الحل / Solution | الوقت / Time |
|---------------|-----------------|--------------|
| مانع الإعلانات / Ad Blocker | تعطيله للموقع / Disable for site | 10 ثانية / 10 sec |
| Brave Browser | تعطيل Block Scripts | 10 ثانية / 10 sec |
| Privacy Extension | إضافة استثناء / Add exception | 30 ثانية / 30 sec |
| جدار حماية الشركة / Corporate Firewall | اتصل بقسم IT / Contact IT | - |

---

## الأدوات الموصى بها / Recommended Tools

### 1. uBlock Origin ⭐
**الإعداد المثالي / Ideal Setup:**
```
1. انقر على الأيقونة → Click on icon
2. انقر على زر الطاقة (سيتحول إلى رمادي) → Click power button (turns gray)
3. أعد تحميل → Reload
```

### 2. AdBlock Plus
**الإعداد المثالي / Ideal Setup:**
```
1. انقر على الأيقونة → Click on icon
2. "Don't run on pages on this domain"
3. أعد تحميل → Reload
```

---

## التحقق المتقدم / Advanced Verification

### تحقق من تحميل الملفات / Check Files Loaded
في Console:
```javascript
// ✅ Should return object
console.log(window.GOOGLE_MAPS_CONFIG);

// ✅ Should return object
console.log(window.googleMapsLoader);

// ✅ Should return 'loaded' or 'loading'
console.log(window.googleMapsLoader.getStatus());
```

### إعادة المحاولة يدوياً / Manual Retry
```javascript
// إذا فشل التحميل، جرّب / If loading failed, try:
window.googleMapsLoader.load()
  .then(() => alert('✅ تم التحميل! / Loaded!'))
  .catch(err => alert('❌ فشل: / Failed: ' + err.message));
```

---

## مزيد من المساعدة / More Help

📚 **دليل شامل / Complete Guide:**
[GOOGLE_MAPS_TROUBLESHOOTING_GUIDE_AR.md](./GOOGLE_MAPS_TROUBLESHOOTING_GUIDE_AR.md)

🐛 **الإبلاغ عن مشكلة / Report Issue:**
[GitHub Issues](https://github.com/aliabdelaal-adm/Monthly_inspection_plan/issues)

---

## نصائح إضافية / Additional Tips

### 💡 نصيحة 1: وضع التصفح الخاص / Private Browsing
جرّب فتح الموقع في وضع التصفح الخاص (Ctrl+Shift+N). معظم الإضافات لا تعمل في هذا الوضع.

Try opening the site in private browsing mode (Ctrl+Shift+N). Most extensions don't work in this mode.

### 💡 نصيحة 2: متصفح بديل / Alternative Browser
إذا لم ينجح شيء، جرّب متصفح آخر بدون إضافات.

If nothing works, try another browser without extensions.

### 💡 نصيحة 3: تحديث المتصفح / Update Browser
تأكد من أنك تستخدم أحدث إصدار من المتصفح.

Make sure you're using the latest browser version.

---

## الأسئلة الشائعة / FAQ

**س: هل يجب إيقاف مانع الإعلانات نهائياً؟**
ج: لا، فقط لهذا الموقع.

**Q: Do I need to disable ad blocker permanently?**
A: No, only for this site.

---

**س: هل هذا آمن؟**
ج: نعم، نستخدم Google Maps API الرسمي فقط.

**Q: Is this safe?**
A: Yes, we use only official Google Maps API.

---

**س: ماذا لو لم تنجح أي من الحلول؟**
ج: استخدم الروابط المباشرة 📍 أو اتصل بقسم IT.

**Q: What if none of the solutions work?**
A: Use direct links 📍 or contact IT department.

---

آخر تحديث / Last Updated: 2025-11-14
الإصدار / Version: 3.0 - Quick Fix Guide
