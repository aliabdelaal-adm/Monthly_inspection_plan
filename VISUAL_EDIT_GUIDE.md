# 📝 Visual Guide - Exactly What to Edit
# الدليل المرئي - بالضبط ما يجب تعديله

---

## 🎯 File to Edit / الملف المطلوب تعديله

**File Name:** `google-maps-config.local.js`
**اسم الملف:** `google-maps-config.local.js`

---

## 📍 Line 68 - First Edit / السطر 68 - التعديل الأول

### BEFORE / قبل:
```javascript
const GOOGLE_MAPS_API_KEY = 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD';
```

### AFTER / بعد:
```javascript
const GOOGLE_MAPS_API_KEY = 'AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX';
                            ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
                            Put your ACTUAL API key here
                            ضع مفتاح API الفعلي هنا
```

---

## 📍 Line 73 - Second Edit / السطر 73 - التعديل الثاني

### BEFORE / قبل:
```javascript
if (typeof window !== 'undefined') {
    window.GOOGLE_MAPS_API_KEY = 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD';
}
```

### AFTER / بعد:
```javascript
if (typeof window !== 'undefined') {
    window.GOOGLE_MAPS_API_KEY = 'AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX';
                                  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
                                  SAME API key as line 68
                                  نفس مفتاح API في السطر 68
}
```

---

## ✅ Complete Example / مثال كامل

Here's how the file should look AFTER editing:
هكذا يجب أن يبدو الملف بعد التعديل:

```javascript
// ... (other comments above)

// Set your NEW Google Maps API key here / ضع مفتاح Google Maps API الجديد هنا
// Replace 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD' with your actual key
// استبدل 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD' بمفتاحك الفعلي
const GOOGLE_MAPS_API_KEY = 'AIzaSyDXvBkE9J-qMnlnZVwbJRQFG5Gp9RkTyAm';
                            ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
                            This is an EXAMPLE - use YOUR key!
                            هذا مثال - استخدم مفتاحك الخاص!

// Export the API key / تصدير مفتاح API
// IMPORTANT: Update this line with the same key as above
// مهم: حدّث هذا السطر بنفس المفتاح أعلاه
if (typeof window !== 'undefined') {
    window.GOOGLE_MAPS_API_KEY = 'AIzaSyDXvBkE9J-qMnlnZVwbJRQFG5Gp9RkTyAm';
                                  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
                                  SAME key as above!
                                  نفس المفتاح أعلاه!
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { GOOGLE_MAPS_API_KEY };
}
```

---

## 🔑 Where to Get Your API Key / من أين تحصل على مفتاح API

### Step 1 / الخطوة 1:
Go to / اذهب إلى:
```
https://console.cloud.google.com/
```

### Step 2 / الخطوة 2:
Select your project:
```
Monthly_inspection_plan
```

### Step 3 / الخطوة 3:
Navigate to / انتقل إلى:
```
APIs & Services → Credentials
```

### Step 4 / الخطوة 4:
Look for your API key in the list. It will look like:
ابحث عن مفتاح API في القائمة. سيبدو كالتالي:
```
AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX
```

### Step 5 / الخطوة 5:
**COPY** the entire key (click the copy button or select all)
**انسخ** المفتاح بالكامل (انقر على زر النسخ أو اختر الكل)

---

## ⚠️ Common Mistakes / الأخطاء الشائعة

### ❌ Mistake 1: Editing wrong file
Editing: `google-maps-config.js` ← WRONG!
Should edit: `google-maps-config.local.js` ← CORRECT! ✅

### ❌ Mistake 2: Only updating one line
You must update BOTH:
- Line 68 ✅
- Line 73 ✅

### ❌ Mistake 3: Leaving the placeholder
```javascript
const GOOGLE_MAPS_API_KEY = 'YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD'; // ❌ WRONG!
const GOOGLE_MAPS_API_KEY = 'AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX';  // ✅ CORRECT!
```

### ❌ Mistake 4: Adding spaces
```javascript
const GOOGLE_MAPS_API_KEY = ' AIzaSyXXXXXXX '; // ❌ Has spaces!
const GOOGLE_MAPS_API_KEY = 'AIzaSyXXXXXXX';   // ✅ No spaces!
```

### ❌ Mistake 5: Not saving
Remember to press **Ctrl+S** (or **Cmd+S** on Mac) to save!
تذكر أن تضغط **Ctrl+S** (أو **Cmd+S** على Mac) للحفظ!

---

## 🎯 Checklist / قائمة التحقق

Before testing, make sure:
قبل الاختبار، تأكد من:

- [ ] Edited the correct file: `google-maps-config.local.js`
- [ ] Updated line 68 with your API key
- [ ] Updated line 73 with the SAME API key
- [ ] No spaces before or after the key
- [ ] Key starts with `AIza`
- [ ] Saved the file (Ctrl+S)
- [ ] Hard refreshed browser (Ctrl+Shift+R)

---

## 🧪 How to Test / كيفية الاختبار

After editing and saving:

1. **Hard refresh** your browser:
   ```
   Ctrl + Shift + R  (Windows/Linux)
   Cmd + Shift + R   (Mac)
   ```

2. **Open** in browser:
   ```
   google-maps-setup-validator.html
   ```

3. **Look for**:
   - ✅ Green checkmarks = Success! / نجاح!
   - ❌ Red X marks = Fix the issue shown / أصلح المشكلة المعروضة

4. **If successful**, open:
   ```
   smart-planner.html
   ```
   And try adding a location - map should load!

---

## 📱 Quick Copy-Paste Template / قالب النسخ السريع

Use this template:
استخدم هذا القالب:

1. Copy your API key from Google Cloud Console
2. Replace `PASTE_YOUR_KEY_HERE` in both places below:

```javascript
const GOOGLE_MAPS_API_KEY = 'PASTE_YOUR_KEY_HERE';

// ... some code ...

if (typeof window !== 'undefined') {
    window.GOOGLE_MAPS_API_KEY = 'PASTE_YOUR_KEY_HERE';
}
```

---

## 🎉 That's It! / هذا كل شيء!

Just edit those 2 lines and you're done!
فقط عدّل هذين السطرين وانتهيت!

**Line 68:** Your API key
**Line 73:** Same API key

**Save** → **Refresh** → **Test** → **Success!** ✅

---

## 🆘 Need More Help? / تحتاج المزيد من المساعدة؟

See these guides:
راجع هذه الأدلة:

- `QUICK_FIX_GOOGLE_MAPS.md` - Quick 3-minute guide
- `GOOGLE_MAPS_SETUP_FIX_GUIDE.md` - Detailed guide with troubleshooting
- `README_SOLUTION_COMPLETE.md` - Complete solution overview

Or run the validator:
أو شغّل أداة التحقق:
```
google-maps-setup-validator.html
```

It will show you exactly what's wrong!
ستعرض لك بالضبط ما المشكلة!
