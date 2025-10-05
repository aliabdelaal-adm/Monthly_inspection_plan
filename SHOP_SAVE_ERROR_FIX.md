# إصلاح خطأ حفظ المحلات - Shop Save Error Fix

## المشكلة الأصلية / Original Problem

عند حفظ المحلات الجديدة أو حفظ التعديلات في قائمة المحلات الخاضعة للرقابة والتفتيش، تظهر رسالة:
```
❌ فشل في حفظ البيانات
```

**Translation:** When saving new shops or saving edits in the list of shops under control and inspection, a "Failed to save data" error message appears.

---

## السبب الجذري / Root Cause

التوكن (GitHub Personal Access Token) المُستخدم في الكود قد يكون:
1. ❌ منتهي الصلاحية (Expired)
2. ❌ غير صالح (Invalid)
3. ❌ ليس لديه الصلاحيات المطلوبة (Missing required permissions)

**السبب:** عند محاولة حفظ البيانات إلى GitHub، يفشل الطلب بسبب رفض الخادم للتوكن (403 Forbidden أو 401 Unauthorized).

---

## الحل المنفذ / Solution Implemented

### 1. تحسين رسائل الخطأ / Enhanced Error Messages

**قبل (Before):**
```
❌ فشل في حفظ البيانات!
الخطأ: فشل الحفظ: 403
يرجى المحاولة مرة أخرى أو التحقق من التوكن
```

**بعد (After):**
```
❌ فشل في حفظ البيانات!

فشل الحفظ: 403 - Bad credentials

🔑 التوكن غير صالح أو منتهي الصلاحية.

للحل:
1. اضغط على أيقونة الإعدادات ⚙️
2. أدخل توكن GitHub جديد
3. احفظ وحاول مرة أخرى

💡 يرجى المحاولة مرة أخرى

[🔑 تحديث التوكن الآن]  ← زر قابل للنقر
```

### 2. التحقق من التوكن عند تسجيل الدخول / Token Validation on Login

عند تسجيل الدخول كمطور، يتم الآن:
1. ✅ التحقق تلقائياً من صلاحية التوكن
2. ⚠️ عرض تحذير إذا كان التوكن غير صالح
3. 📝 إرشاد المستخدم لكيفية تحديث التوكن

**مثال التحذير:**
```
⚠️ تحذير: التوكن الحالي غير صالح أو منتهي الصلاحية!

🔑 لحفظ البيانات على GitHub، ستحتاج إلى:
1. الذهاب إلى صفحة الإعدادات (أيقونة الإعدادات)
2. إدخال توكن GitHub جديد
3. حفظ التوكن

💡 يمكنك الاستمرار في استخدام التطبيق، لكن لن تتمكن من حفظ التغييرات على GitHub حتى تحديث التوكن.
```

### 3. زر تحديث التوكن السريع / Quick Token Update Button

في رسائل الخطأ، يظهر الآن زر:
```html
<button onclick="showTokenPopup()">🔑 تحديث التوكن الآن</button>
```

عند الضغط عليه، يفتح نافذة إدخال التوكن مباشرة.

---

## التغييرات التقنية / Technical Changes

### الملفات المعدلة / Modified Files
- `index.html` (3 functions enhanced)

### الدوال المحسّنة / Enhanced Functions

#### 1. `saveShopsToGitHub()` (السطر ~10809)
```javascript
// إضافة معالجة أخطاء مفصلة
if (!getResponse.ok) {
    let errorMsg = `فشل في قراءة plan-data.json: ${getResponse.status}`;
    try {
        const errorData = await getResponse.json();
        if (errorData.message) {
            errorMsg += ` - ${errorData.message}`;
        }
    } catch (e) { }
    
    if (getResponse.status === 401 || getResponse.status === 403) {
        errorMsg += '\n\n🔑 التوكن غير صالح...';
    }
    throw new Error(errorMsg);
}
```

#### 2. `saveDataToGitHub()` (السطر ~5437)
```javascript
// تخزين الخطأ في متغير عام
window.lastSaveError = errorMsg;

// إضافة Authorization header للطلب
const getResponse = await fetch('...', {
    headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
    }
});
```

#### 3. `document.getElementById("devLoginBtn").onclick` (السطر ~4465)
```javascript
// إضافة التحقق من التوكن
const testResponse = await fetch('https://api.github.com/repos/...', {
    headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
    }
});

if (!testResponse.ok && (testResponse.status === 401 || testResponse.status === 403)) {
    alert('⚠️ تحذير: التوكن الحالي غير صالح...');
}
```

---

## كيفية الحصول على توكن جديد / How to Get a New Token

### الخطوات / Steps:

1. **اذهب إلى GitHub Settings**
   ```
   https://github.com/settings/tokens
   ```

2. **انقر على "Generate new token (classic)"**

3. **اختر الصلاحيات التالية / Select these scopes:**
   - ✅ `repo` (Full control of private repositories)
     - ✅ `repo:status`
     - ✅ `repo_deployment`
     - ✅ `public_repo`
     - ✅ `repo:invite`

4. **انقر "Generate token"**

5. **انسخ التوكن مباشرة** (لن تتمكن من رؤيته مرة أخرى!)

6. **في التطبيق:**
   - اضغط على ⚙️ (أيقونة الإعدادات)
   - ألصق التوكن
   - احفظ

---

## الاختبار / Testing

### سيناريو 1: توكن غير صالح
```
✅ النتيجة: رسالة خطأ واضحة مع إرشادات
✅ النتيجة: زر "تحديث التوكن الآن" يظهر
✅ النتيجة: الضغط على الزر يفتح نافذة التوكن
```

### سيناريو 2: توكن صالح
```
✅ النتيجة: الحفظ يتم بنجاح
✅ النتيجة: رسالة نجاح تظهر
```

### سيناريو 3: تسجيل دخول مع توكن منتهي
```
✅ النتيجة: تحذير يظهر عند تسجيل الدخول
✅ النتيجة: إرشادات واضحة للحل
```

---

## الفوائد / Benefits

### للمستخدم / For Users:
1. ✅ **رسائل خطأ واضحة** - يعرف بالضبط ما المشكلة
2. ✅ **حل سريع** - زر مباشر لتحديث التوكن
3. ✅ **إرشادات خطوة بخطوة** - كيفية الحصول على توكن جديد

### للمطور / For Developers:
1. ✅ **تشخيص أفضل** - معلومات تفصيلية عن الخطأ
2. ✅ **تقليل الدعم** - المستخدمون يمكنهم حل المشكلة بأنفسهم
3. ✅ **كود أنظف** - معالجة أخطاء موحدة

---

## ملاحظات مهمة / Important Notes

### ⚠️ أمان التوكن / Token Security
- 🔐 لا تشارك التوكن مع أحد
- 🔐 لا ترفعه إلى GitHub في الكود
- 🔐 استخدم `localStorage` للتخزين المحلي فقط
- 🔐 قم بتغييره بشكل دوري

### 🔄 صلاحية التوكن / Token Expiration
- GitHub tokens can expire based on your settings
- يُفضّل إنشاء tokens بدون تاريخ انتهاء للاستخدام الشخصي
- أو تفعيل التجديد التلقائي

### 📝 التوثيق / Documentation
- هذا الإصلاح موثق بالكامل
- الكود يحتوي على تعليقات توضيحية
- رسائل الخطأ باللغة العربية للوضوح

---

## المراجع / References

- [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [GitHub API Error Codes](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#client-errors)

---

**تاريخ الإصلاح / Fix Date:** 2025-01-XX  
**الحالة / Status:** ✅ مكتمل ومختبر / Completed and tested  
**المطور / Developer:** GitHub Copilot Agent
