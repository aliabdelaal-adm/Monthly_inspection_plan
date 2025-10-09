# مرجع سريع - وضع الصيانة المجدول
# Quick Reference - Scheduled Maintenance Mode

## ⚡ الأساسيات | Basics

### متى يعمل؟ | When does it work?
```
⏰ كل يوم من الساعة 9 مساءً (21:00) حتى 11 مساءً (23:00)
⏰ Every day from 9 PM (21:00) to 11 PM (23:00)
```

### من يراه؟ | Who sees it?
```
✅ جميع المفتشين | All inspectors
❌ المطور (معفى) | Developer (exempted)
```

### ماذا يحدث؟ | What happens?
```
1️⃣ رسالة صيانة تظهر تلقائياً
   Maintenance message appears automatically

2️⃣ موسيقى هادئة تبدأ
   Calm music starts playing

3️⃣ تفاصيل واضحة عن وقت الصيانة
   Clear details about maintenance time
```

---

## 🔧 الملفات المعدلة | Modified Files

### `index.html`
```javascript
// الوظائف المضافة | Added functions:
- isScheduledMaintenanceTime()      // فحص الوقت | Check time
- checkScheduledMaintenance()       // تطبيق الصيانة | Apply maintenance  
- startScheduledMaintenanceChecker() // بدء الفاحص | Start checker

// الاستدعاء | Call:
- في DOMContentLoaded | In DOMContentLoaded
- السطر | Line: ~6505
```

---

## 🧪 الاختبار | Testing

### ملف الاختبار | Test File
```
test_scheduled_maintenance.html
```

### كيفية الاختبار | How to Test
```bash
# 1. افتح الملف في المتصفح
open test_scheduled_maintenance.html

# 2. استخدم محاكي الوقت لاختبار أوقات مختلفة
# Use time simulator to test different times

# 3. جرب السيناريوهات الأربعة
# Try the four scenarios
```

---

## 🎯 السيناريوهات | Scenarios

### ✅ السيناريو 1: وقت الصيانة
```
الوقت | Time: 9:00 PM
المستخدم | User: مفتش | Inspector
النتيجة | Result: رسالة الصيانة تظهر | Maintenance shows
```

### ✅ السيناريو 2: خارج الوقت
```
الوقت | Time: 8:00 PM
المستخدم | User: مفتش | Inspector
النتيجة | Result: لا شيء | Nothing
```

### ✅ السيناريو 3: المطور
```
الوقت | Time: 9:00 PM
المستخدم | User: مطور | Developer
النتيجة | Result: لا شيء (معفى) | Nothing (exempted)
```

### ✅ السيناريو 4: نهاية الصيانة
```
الوقت | Time: 11:00 PM
المستخدم | User: مفتش | Inspector
النتيجة | Result: إخفاء تلقائي | Auto hide
```

---

## 📝 التخصيص | Customization

### تغيير أوقات الصيانة | Change Maintenance Times

في `index.html`، ابحث عن:
In `index.html`, find:

```javascript
function isScheduledMaintenanceTime() {
    const now = new Date();
    const currentHour = now.getHours();
    
    // غيّر هذه الأرقام | Change these numbers
    const isMaintenanceTime = currentHour >= 21 && currentHour < 23;
    //                                      ^^              ^^
    //                                    START           END
    
    return isMaintenanceTime;
}
```

### أمثلة | Examples:

```javascript
// من 10 مساءً إلى 12 صباحاً | From 10 PM to 12 AM
currentHour >= 22 && currentHour < 24

// من 8 مساءً إلى 10 مساءً | From 8 PM to 10 PM
currentHour >= 20 && currentHour < 22

// من 1 صباحاً إلى 3 صباحاً | From 1 AM to 3 AM
currentHour >= 1 && currentHour < 3
```

---

## 🔍 استكشاف الأخطاء | Troubleshooting

### المشكلة: الصيانة لا تظهر
**Problem: Maintenance not showing**

```javascript
// تحقق من | Check:
1. الوقت الحالي بين 9م - 11م؟
   Current time between 9PM - 11PM?
   
2. المستخدم مفتش (وليس مطور)؟
   User is inspector (not developer)?
   
3. افتح Console وابحث عن رسائل الخطأ
   Open Console and look for error messages
```

### المشكلة: الموسيقى لا تعمل
**Problem: Music not playing**

```javascript
// تحقق من | Check:
1. ملف الموسيقى موجود: whatsapp Audio.mp3
   Music file exists: whatsapp Audio.mp3
   
2. المتصفح يسمح بتشغيل الصوت التلقائي
   Browser allows autoplay
   
3. اضغط في أي مكان على الصفحة (بعض المتصفحات تتطلب تفاعل)
   Click anywhere on page (some browsers require interaction)
```

### المشكلة: المطور يرى الصيانة
**Problem: Developer sees maintenance**

```javascript
// تحقق من | Check:
1. isDev = true?
   console.log(isDev);
   
2. تسجيل الدخول كمطور صحيح؟
   Developer login correct?
   
3. localStorage.getItem('isDevLoggedIn') === 'true'?
```

---

## 📊 رسائل Console | Console Messages

### رسائل عادية | Normal Messages

```javascript
✅ "Developer logged in - skipping scheduled maintenance check"
   // المطور مسجل دخول - تخطي فحص الصيانة

⏰ "Scheduled maintenance time detected: 21:30"
   // تم اكتشاف وقت الصيانة المجدول

🔧 "Activating scheduled maintenance mode..."
   // تفعيل وضع الصيانة المجدول

✅ "Scheduled maintenance period ended - hiding maintenance mode"
   // انتهى وقت الصيانة المجدول - إخفاء وضع الصيانة
```

---

## 📚 الوثائق الكاملة | Full Documentation

للحصول على معلومات مفصلة، راجع:
For detailed information, see:

1. **`SCHEDULED_MAINTENANCE_FEATURE.md`**
   - توثيق شامل للميزة
   - Complete feature documentation

2. **`SCHEDULED_MAINTENANCE_IMPLEMENTATION_SUMMARY.md`**
   - ملخص التنفيذ ونتائج الاختبار
   - Implementation summary and test results

3. **`test_scheduled_maintenance.html`**
   - صفحة اختبار تفاعلية
   - Interactive test page

---

## ✅ قائمة التحقق | Checklist

```
☑️ النظام يعمل تلقائياً من 9م - 11م
   System works automatically 9PM - 11PM

☑️ المفتشون يرون رسالة الصيانة
   Inspectors see maintenance message

☑️ المطور معفى من رسالة الصيانة
   Developer exempted from maintenance

☑️ الموسيقى تعمل تلقائياً
   Music plays automatically

☑️ الإخفاء التلقائي عند انتهاء الوقت
   Auto hide when time ends

☑️ تم الاختبار في جميع السيناريوهات
   Tested in all scenarios

☑️ موثق بالكامل
   Fully documented
```

---

**آخر تحديث | Last Updated:** 2024  
**الحالة | Status:** ✅ نشط | Active  
**الدعم | Support:** انظر الوثائق الكاملة | See full documentation
