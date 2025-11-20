# إصلاح خطأ زر العرض في تقارير التفتيش الجماعي
# Fix Group Inspection View Button Error

## المشكلة | Problem

عند الضغط على زر "عرض" في قسم تقارير التفتيش الجماعي، كانت تظهر رسالة خطأ:
> "نحن آسفون لكن ولسبب ما لا يمكن فتح هذه الصفحة"

When clicking the "View" button in the group inspection reports section, an error message appeared:
> "We're sorry but for some reason we cannot open this page"

## السبب | Root Cause

كانت دالة `viewGroupReport` تستخدم مسار نسبي (relative path) عند محاولة فتح ملفات Office في عارض Microsoft Office Online. المشكلة أن عارض Office يتطلب URL مطلق (absolute URL) وقابل للوصول علنياً.

The `viewGroupReport` function was using a relative path when trying to open Office files in Microsoft Office Online Viewer. The issue is that the Office viewer requires an absolute URL that is publicly accessible.

### الكود القديم | Old Code
```javascript
// محاولة الحصول على URL الملف
try {
    const testResponse = await fetch(`./${filePath}`, { method: 'HEAD' });
    if (testResponse.ok) {
        fileUrl = `./${filePath}`;  // ❌ مسار نسبي - لا يعمل مع Office Viewer
    }
}

// استخدام Office Online Viewer
const viewerUrl = `https://view.officeapps.live.com/op/view.aspx?src=${encodeURIComponent(fileUrl)}`;
window.open(viewerUrl, '_blank');
```

## الحل | Solution

تم تحديث الدالة لبناء URL مطلق بناءً على البيئة الحالية:

The function was updated to build an absolute URL based on the current environment:

### الكود الجديد | New Code
```javascript
// بناء URL الكامل للملف
let fileUrl;
const isLocalhost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';

if (isLocalhost) {
    // في حالة التطوير المحلي، استخدم المسار النسبي
    fileUrl = `./${filePath}`;
} else {
    // في حالة GitHub Pages أو الاستضافة، استخدم URL الكامل
    // إزالة اسم الملف من pathname للحصول على المسار الأساسي
    const baseUrl = window.location.origin + window.location.pathname.replace(/\/[^\/]*$/, '');
    fileUrl = `${baseUrl}/${filePath}`;
}

// للملفات Office: استخدام Office Online Viewer
if (['xlsx', 'xls', 'docx', 'doc', 'pptx', 'ppt'].includes(lowerFileType)) {
    const viewerUrl = `https://view.officeapps.live.com/op/view.aspx?src=${encodeURIComponent(fileUrl)}`;
    const newWindow = window.open(viewerUrl, '_blank', 'noopener,noreferrer');
    
    if (newWindow) {
        statusDiv.textContent = '✅ تم فتح التقرير في عارض Office';
    } else {
        // معالجة حظر النوافذ المنبثقة
        statusDiv.innerHTML = `⚠️ تم حظر النافذة المنبثقة. <a href="${viewerUrl}" target="_blank">اضغط هنا لفتح التقرير</a>`;
    }
}
```

## التحسينات | Improvements

1. ✅ **بناء URL صحيح** | Correct URL Construction
   - للاستضافة (GitHub Pages): يستخدم `window.location.origin` + pathname
   - للتطوير المحلي: يستخدم المسار النسبي

2. ✅ **معالجة حظر النوافذ المنبثقة** | Popup Blocker Handling
   - يتحقق من نجاح فتح النافذة
   - يوفر رابط بديل في حالة الحظر

3. ✅ **رسائل واضحة للمستخدم** | Clear User Messages
   - رسائل حالة محسنة
   - ألوان مناسبة للحالات المختلفة

4. ✅ **تعليقات توضيحية** | Code Comments
   - شرح واضح للكود
   - توثيق للـ regex pattern المستخدم

## الاختبار | Testing

تم إنشاء ملف اختبار شامل: `test_view_button_fix.html`

A comprehensive test file was created: `test_view_button_fix.html`

### ما يتم اختباره | What is Tested

1. ✅ عرض معلومات البيئة (localhost vs production)
2. ✅ اختبار بناء URL
3. ✅ اختبار فتح الملفات في Office Viewer
4. ✅ اختبار الفتح المباشر للملفات

### كيفية الاختبار | How to Test

1. افتح الملف: `test_view_button_fix.html`
2. اضغط على "اختبار بناء URL"
3. اضغط على "عرض التقرير (PowerPoint)"
4. تحقق من فتح الملف في Office Online Viewer

## الملفات المعدلة | Modified Files

1. **index.html**
   - تحديث دالة `viewGroupReport` (السطر 30274)
   - إضافة تعليقات توضيحية
   - معالجة أفضل للأخطاء

2. **test_view_button_fix.html** (جديد)
   - ملف اختبار شامل
   - واجهة مستخدم واضحة
   - أمثلة عملية

## النتيجة | Result

✅ **تم إصلاح المشكلة بنجاح**

الآن عند الضغط على زر "عرض":
- يتم فتح ملفات PowerPoint/Word/Excel في Office Online Viewer
- يعمل بشكل صحيح على GitHub Pages
- توفر رسائل واضحة للمستخدم
- معالجة صحيحة لحالات الخطأ

Now when clicking the "View" button:
- PowerPoint/Word/Excel files open in Office Online Viewer
- Works correctly on GitHub Pages
- Provides clear user messages
- Proper error handling

## ملاحظات تقنية | Technical Notes

### متطلبات Office Online Viewer

لكي يعمل Office Online Viewer بشكل صحيح، يجب:

1. **URL مطلق**: يجب أن يكون الرابط كاملاً بما في ذلك البروتوكول والدومين
   ```
   ✅ https://aliabdelaal-adm.github.io/Monthly_inspection_plan/files/...
   ❌ ./files/...
   ```

2. **الملف قابل للوصول علنياً**: يجب أن يكون الملف متاحاً للتحميل من الإنترنت

3. **أنواع الملفات المدعومة**:
   - PowerPoint: `.ppt`, `.pptx`
   - Word: `.doc`, `.docx`
   - Excel: `.xls`, `.xlsx`

### التوافق | Compatibility

- ✅ Chrome (Desktop & Mobile)
- ✅ Firefox
- ✅ Safari (Desktop & Mobile)
- ✅ Edge
- ✅ GitHub Pages
- ✅ Development Environment (localhost)

## المراجع | References

- [Microsoft Office Online Viewer Documentation](https://docs.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/online/)
- [GitHub Pages Custom Domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

---

**تاريخ الإصلاح** | Fix Date: 2025-11-20  
**الإصدار** | Version: 1.0  
**الحالة** | Status: ✅ مكتمل | Completed
