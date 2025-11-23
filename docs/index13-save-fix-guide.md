# دليل استخدام صفحة التفتيش الجماعي - index13.html
# Group Inspection Report Save Fix - User Guide

## نظرة عامة | Overview

تم إصلاح مشكلة الحفظ في صفحة التفتيش الجماعي (index13.html) وإضافة عدة طرق بديلة لضمان حفظ التقارير بنجاح.

The save button issue in the group inspection page (index13.html) has been fixed with multiple fallback methods to ensure reports are always saved successfully.

---

## طرق الحفظ المتاحة | Available Save Methods

### 1. الحفظ المباشر في GitHub | Direct GitHub Save
**الطريقة الأساسية | Primary Method**

- يتم حفظ التقرير مباشرة في مستودع GitHub
- يظهر فوراً في صفحة التقارير
- يتطلب تكوين رمز الوصول الشخصي (GitHub Token)

### 2. عبر GitHub Actions | Via GitHub Actions
**الطريقة الثانوية | Secondary Method**

- يتم إرسال التقرير إلى GitHub Actions للحفظ
- الحفظ يتم من جانب الخادم بشكل آمن
- يظهر التقرير خلال دقائق

### 3. عبر GitHub Issues | Via GitHub Issues
**الطريقة البديلة | Tertiary Method**

- يتم إنشاء Issue في GitHub يحتوي على بيانات التقرير
- يمكن معالجته يدوياً لاحقاً
- يعمل حتى مع الصلاحيات المحدودة

### 4. تنزيل الملف | Download File
**الطريقة اليدوية | Manual Method**

- تنزيل التقرير كملف JSON
- يمكن رفعه يدوياً إلى GitHub
- يعمل بدون اتصال إنترنت

### 5. الحفظ المحلي | Local Storage
**النسخة الاحتياطية التلقائية | Automatic Backup**

- يتم حفظ نسخة احتياطية تلقائياً في المتصفح
- لا يتطلب أي إعدادات
- لا تضيع البيانات أبداً

---

## تكوين رمز GitHub | GitHub Token Configuration

### خطوات التكوين | Setup Steps

1. **افتح لوحة المطور** - اضغط `Ctrl+Shift+D`
2. **افتح إعدادات GitHub** - اضغط على زر "إعدادات GitHub"
3. **أدخل رمز الوصول** - يجب أن يكون للرمز صلاحية `repo` كاملة
4. **احفظ واختبر** - سيتم اختبار الاتصال فوراً

### إنشاء رمز وصول جديد | Creating a New Token

1. GitHub.com → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. اختر صلاحية `repo`
4. انسخ الرمز فوراً

---

## حل المشاكل | Troubleshooting

### لم يتم تكوين رمز وصول GitHub
- افتح لوحة المطور (Ctrl+Shift+D)
- كوّن رمز الوصول في إعدادات GitHub
- أو استخدم زر "تنزيل التقرير كملف احتياطي"

### فشل جميع طرق الحفظ
1. تحقق من الاتصال بالإنترنت
2. تحقق من صلاحية رمز GitHub
3. استخدم زر التنزيل كحل بديل

---

**الإصدار | Version: 2.1.0**
**تاريخ التحديث | Updated: 2025-11-23**
