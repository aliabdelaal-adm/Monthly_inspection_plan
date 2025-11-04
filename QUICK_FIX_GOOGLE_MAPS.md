# 🚀 Quick Fix - Google Maps Not Loading
# الحل السريع - خرائط جوجل لا تعمل

## ⚡ 3-Minute Fix / الحل في 3 دقائق

### Problem / المشكلة
You activated Google Cloud APIs but maps still don't load.
قمت بتفعيل Google Cloud APIs لكن الخرائط ما زالت لا تعمل.

### Why? / لماذا؟
Your new API key isn't in the configuration file yet.
مفتاح API الجديد ليس في ملف الإعدادات بعد.

---

## 🔧 Fix in 3 Steps / الحل في 3 خطوات

### Step 1: Get Your API Key / الخطوة 1: احصل على مفتاح API

1. Open: https://console.cloud.google.com/
2. Select project: **Monthly_inspection_plan**
3. Go to: **APIs & Services** → **Credentials**
4. **COPY** your API key (starts with `AIza...`)

### Step 2: Update Config File / الخطوة 2: حدّث ملف الإعدادات

1. Open file: **`google-maps-config.local.js`**
2. Find **line 68**:
   ```javascript
   const GOOGLE_MAPS_API_KEY = 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD';
   ```
3. **Replace** with your actual key:
   ```javascript
   const GOOGLE_MAPS_API_KEY = 'AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX';
   ```
4. **Also update line 73** with the same key:
   ```javascript
   window.GOOGLE_MAPS_API_KEY = 'AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX';
   ```
5. **SAVE** the file

### Step 3: Test / الخطوة 3: اختبر

1. Hard refresh: **`Ctrl + Shift + R`** (Windows) or **`Cmd + Shift + R`** (Mac)
2. Open: **`google-maps-setup-validator.html`** in browser
3. Should see ✅ green checks

---

## ✅ Checklist Before Testing / قائمة التحقق قبل الاختبار

Make sure in Google Cloud Console:
تأكد في Google Cloud Console:

- [ ] **Billing** is linked (required!) / الفوترة مربوطة (مطلوب!)
- [ ] **Maps JavaScript API** is enabled / مفعّل
- [ ] **Places API** is enabled / مفعّل  
- [ ] **Geocoding API** is enabled / مفعّل

💡 **Tip:** For testing, set API key restrictions to **"None"**
💡 **نصيحة:** للاختبار، ضع قيود مفتاح API على **"بدون"**

---

## 🆘 Still Not Working? / ما زالت لا تعمل؟

### Common Mistakes / الأخطاء الشائعة

❌ **Editing wrong file**
   - Edit: `google-maps-config.local.js` ✅
   - NOT: `google-maps-config.js` ❌

❌ **Forgot to update BOTH lines**
   - Must update lines 68 AND 73

❌ **Didn't save the file**
   - Press Ctrl+S to save!

❌ **Didn't hard refresh**
   - Must use Ctrl+Shift+R, not just F5

❌ **Billing not enabled**
   - This is the #1 cause of auth failures
   - Go to Billing → Link account

---

## 📋 Complete Guide / الدليل الكامل

For detailed instructions, see:
للتعليمات التفصيلية، راجع:

- **`GOOGLE_MAPS_SETUP_FIX_GUIDE.md`** - Complete step-by-step guide
- **`google-maps-setup-validator.html`** - Interactive testing tool

---

## 🎉 Success = / النجاح =

- ✅ Validation page shows green checks
- ✅ Test map appears on validation page  
- ✅ No errors in browser console (F12)
- ✅ Smart planner can show maps

---

**That's it! / هذا كل شيء!** 🚀

If you still have issues after following these steps, open the browser console (F12) and check what error message appears. The error will tell you exactly what's wrong.

إذا ما زلت تواجه مشاكل بعد اتباع هذه الخطوات، افتح كونسول المتصفح (F12) وتحقق من رسالة الخطأ التي تظهر. الخطأ سيخبرك بالضبط ما المشكلة.
