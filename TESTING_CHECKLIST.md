# قائمة اختبار رفع الملفات - File Upload Testing Checklist

## الهدف - Objective
التأكد من أن جميع أزرار رفع الملفات تعمل بشكل صحيح وتقوم برفع الملفات فعلياً إلى GitHub.
Ensure all file upload buttons work correctly and actually upload files to GitHub.

---

## المتطلبات الأساسية - Prerequisites

- [x] ✅ Git repository cloned locally
- [x] ✅ Developer token configured in localStorage
- [ ] 🔐 Developer password entered to enable upload functionality
- [ ] 🌐 Internet connection for GitHub API access

---

## اختبارات جدول المناوبات - Shifts Schedule Tests

### الموقع - Location
```
الصفحة الرئيسية → إدارة خدمات النظام → جدول المناوبات
Main Page → System Services Management → Shifts Schedule
```

### خطوات الاختبار - Test Steps

1. **فتح القسم**
   - [ ] افتح قسم "جدول المناوبات"
   - [ ] تحقق من ظهور زر "📁 رفع ملف"

2. **اختيار ملف**
   - [ ] انقر على زر "رفع ملف"
   - [ ] اختر ملف Excel للمناوبات
   - [ ] تحقق من أن حجم الملف < 25 MB

3. **عملية الرفع**
   - [ ] يجب أن تظهر رسالة تحميل متحركة (⏳)
   - [ ] تحتوي الرسالة على اسم الملف
   - [ ] الرسالة مركزية في الشاشة

4. **التحقق من النجاح**
   - [ ] يجب أن تظهر رسالة: "✅ تم رفع ملف جدول المناوبات بنجاح!"
   - [ ] يذكر اسم الملف في الرسالة
   - [ ] يذكر أن الملف "متاح للجميع في مكتبة الملفات"

5. **التحقق من الرفع الفعلي**
   - [ ] افتح مجلد `files/schedules/` في GitHub
   - [ ] الملف موجود في المجلد
   - [ ] افتح `files.json`
   - [ ] سجل الملف موجود مع جميع البيانات الوصفية

6. **الوصول العام**
   - [ ] افتح قسم "مكتبة الملفات العامة"
   - [ ] ابحث عن الملف في قسم "الجداول"
   - [ ] يمكن تحميل الملف
   - [ ] يمكن معاينة الملف (إذا كان PDF)

### النتيجة المتوقعة - Expected Result
```
✅ SUCCESS: File uploaded to GitHub
✅ SUCCESS: File registered in files.json
✅ SUCCESS: File visible in public library
✅ SUCCESS: File can be downloaded by all users
```

---

## اختبارات تتبع الإجازات - Vacation Tracking Tests

### الموقع - Location
```
الصفحة الرئيسية → إدارة خدمات النظام → تتبع الإجازات
Main Page → System Services Management → Vacation Tracking
```

### خطوات الاختبار - Test Steps

1. **فتح القسم**
   - [ ] افتح قسم "تتبع الإجازات"
   - [ ] تحقق من ظهور زر رفع الملف

2. **اختيار ملف**
   - [ ] اختر ملف Excel أو PDF
   - [ ] تحقق من الحجم المناسب

3. **عملية الرفع**
   - [ ] تظهر رسالة التحميل
   - [ ] تحتوي على اسم الملف

4. **التحقق من النجاح**
   - [ ] رسالة النجاح تظهر
   - [ ] تذكر "ملف الإجازات"
   - [ ] تؤكد التوفر للجميع

5. **التحقق من الرفع الفعلي**
   - [ ] الملف في `files/schedules/`
   - [ ] السجل في `files.json`
   - [ ] Category = "schedules"

6. **الوصول العام**
   - [ ] متاح في مكتبة الملفات
   - [ ] يمكن التحميل والمعاينة

### النتيجة المتوقعة - Expected Result
```
✅ SUCCESS: Vacation file uploaded correctly
✅ SUCCESS: File accessible to all users
✅ SUCCESS: Local processing also works
```

---

## اختبارات قائمة المحلات - Shops List Tests

### الموقع - Location
```
الصفحة الرئيسية → إدارة خدمات النظام → قائمة المحلات
Main Page → System Services Management → Shops List
```

### خطوات الاختبار - Test Steps

1. **فتح القسم**
   - [ ] افتح قسم "قائمة المحلات"
   - [ ] تحقق من وجود زر "📁 رفع ملف المحلات"

2. **اختيار ملف**
   - [ ] اختر ملف CSV أو Excel بقائمة المحلات
   - [ ] تحقق من الحجم

3. **عملية الرفع**
   - [ ] رسالة التحميل تظهر في `shopsUpdateStatus`
   - [ ] النص: "جاري معالجة الملف..."

4. **التحقق من النجاح**
   - [ ] رسالة خضراء تظهر
   - [ ] "✅ تم رفع ملف المحلات بنجاح!"
   - [ ] تختفي بعد 5 ثواني

5. **التحقق من الرفع الفعلي**
   - [ ] الملف في `files/documents/`
   - [ ] السجل في `files.json`
   - [ ] Category = "documents"

6. **الوصول العام**
   - [ ] متاح في قسم "الوثائق"
   - [ ] قابل للتحميل

### النتيجة المتوقعة - Expected Result
```
✅ SUCCESS: Shops file uploaded to documents folder
✅ SUCCESS: File publicly accessible
✅ SUCCESS: Shops data processed locally
```

---

## اختبارات الأخطاء - Error Handling Tests

### 1. اختبار بدون صلاحيات
- [ ] افتح الموقع بدون تسجيل دخول مطور
- [ ] حاول رفع ملف
- [ ] النتيجة المتوقعة: "❌ عذراً، رفع الملفات متاح للمطور فقط"

### 2. اختبار ملف كبير
- [ ] اختر ملف أكبر من 25 MB
- [ ] النتيجة المتوقعة: "❌ حجم الملف كبير جداً!"

### 3. اختبار بدون توكن
- [ ] احذف التوكن من localStorage
- [ ] حاول الرفع
- [ ] النتيجة المتوقعة: "❌ يجب تسجيل الدخول كمطور أولاً"

### 4. اختبار فشل الشبكة
- [ ] افصل الإنترنت
- [ ] حاول رفع ملف
- [ ] النتيجة المتوقعة: "⚠️ فشل رفع الملف" + تفاصيل الخطأ

---

## اختبارات التكامل - Integration Tests

### 1. الرفع المتعدد
- [ ] ارفع ملف لكل قسم من الأقسام الثلاثة
- [ ] تحقق من أن جميع الملفات في المجلدات الصحيحة
- [ ] تحقق من أن `files.json` يحتوي على 3 سجلات جديدة

### 2. أنواع الملفات المختلفة
- [ ] ارفع JSON file
- [ ] ارفع Excel file (.xlsx)
- [ ] ارفع PDF file
- [ ] ارفع CSV file
- [ ] تحقق من أن جميعها تُرفع بنجاح

### 3. أسماء الملفات بالعربية
- [ ] ارفع ملف باسم عربي: "جدول_المناوبات_يناير.xlsx"
- [ ] تحقق من الرفع الصحيح
- [ ] تحقق من التحميل بدون مشاكل

### 4. الملفات الموجودة
- [ ] حاول رفع ملف بنفس اسم ملف موجود
- [ ] تحقق من رسالة الخطأ أو الاستبدال

---

## قائمة التحقق النهائية - Final Checklist

### الوظائف الأساسية
- [ ] ✅ رفع ملفات جدول المناوبات يعمل
- [ ] ✅ رفع ملفات تتبع الإجازات يعمل
- [ ] ✅ رفع ملفات قائمة المحلات يعمل

### الأمان
- [ ] ✅ فقط المطور يمكنه الرفع
- [ ] ✅ التوكن مطلوب
- [ ] ✅ رسائل خطأ واضحة للمستخدمين غير المصرح لهم

### التغذية الراجعة
- [ ] ✅ رسالة تحميل تظهر أثناء الرفع
- [ ] ✅ رسائل نجاح واضحة
- [ ] ✅ رسائل خطأ مفصلة

### الوصول العام
- [ ] ✅ الملفات تظهر في مكتبة الملفات العامة
- [ ] ✅ يمكن لجميع المستخدمين التحميل
- [ ] ✅ المعاينة تعمل للملفات المدعومة

### التوثيق
- [ ] ✅ FILE_UPLOAD_GUIDE.md موجود وكامل
- [ ] ✅ TESTING_CHECKLIST.md موجود وكامل
- [ ] ✅ README updated (إذا لزم الأمر)

---

## ملاحظات الاختبار - Testing Notes

### تاريخ الاختبار - Test Date
```
Date: _______________
Tester: _______________
Environment: _______________
```

### النتائج - Results
```
Total Tests: _____
Passed: _____
Failed: _____
Skipped: _____
```

### المشاكل المكتشفة - Issues Found
```
1. ________________________________
2. ________________________________
3. ________________________________
```

### التوصيات - Recommendations
```
1. ________________________________
2. ________________________________
3. ________________________________
```

---

## التوقيع - Sign Off

```
✅ All tests passed successfully
✅ Feature is ready for production
✅ Documentation is complete

Approved by: _______________
Date: _______________
```

---

## المرجع السريع - Quick Reference

### أوامر Git للتحقق
```bash
# التحقق من الملفات المرفوعة
git log --all --full-history -- "files/*"

# عرض محتوى files.json
cat files.json | jq .

# عرض الملفات في مجلد schedules
ls -la files/schedules/

# عرض الملفات في مجلد documents
ls -la files/documents/
```

### عناوين URL للاختبار
```
Main Page: http://localhost:8088/index.html
Admin Page: http://localhost:8088/admin.html
GitHub Repo: https://github.com/aliabdelaal-adm/Monthly_inspection_plan
```

---

## الخلاصة - Summary

هذه القائمة تضمن أن جميع ميزات رفع الملفات تعمل بشكل صحيح وأن الملفات:
1. ✅ تُرفع فعلياً إلى GitHub
2. ✅ تُسجل في files.json
3. ✅ تظهر في مكتبة الملفات العامة
4. ✅ يمكن الوصول إليها من قبل جميع المستخدمين

This checklist ensures all file upload features work correctly and files are:
1. ✅ Actually uploaded to GitHub
2. ✅ Registered in files.json
3. ✅ Visible in public files library
4. ✅ Accessible by all users
