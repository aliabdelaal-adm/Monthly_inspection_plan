# دليل أدوات إدخال البيانات المحسّنة - Enhanced Data Entry Tools Guide

## 🌟 نظرة عامة - Overview

تم تطوير مجموعة من الأدوات الذكية والسريعة لإدخال وتحديث خطط التفتيش مباشرة من لوحة المطور دون الحاجة لرفع ملفات إلى المستودع.

A set of smart and fast tools have been developed to enter and update inspection plans directly from the developer panel without needing to upload files to the repository.

---

## 🔐 الوصول - Access

### المتطلبات - Requirements
1. تسجيل الدخول كمطور - Login as Developer
2. كلمة السر: `ali@1940`
3. الأدوات تظهر تلقائياً بعد تسجيل الدخول

### How to Access
1. From main page, select "المطور" from login dropdown
2. Enter password: `ali@1940`
3. Click "دخول المطور"
4. Enhanced tools appear automatically

---

## ⚡ الأدوات المتاحة - Available Tools

### 1. 📋 استيراد جماعي - Bulk Import

**الغرض - Purpose:**
استيراد عدة خطط تفتيش دفعة واحدة بدلاً من إدخالها واحدة تلو الأخرى.

Import multiple inspection plans at once instead of entering them one by one.

#### الصيغ المدعومة - Supported Formats

##### أ. صيغة JSON - JSON Format

```json
[
  {
    "inspector": "د. علي عبدالعال",
    "day": "2025-10-01",
    "shift": "صباحية",
    "area": "سوق الميناء",
    "shops": ["محل بيت الطيور", "محل الميناء للطيور", "محل السحر للطيور"]
  },
  {
    "inspector": "د. آمنه بن صرم",
    "day": "2025-10-01",
    "shift": "مسائية",
    "area": "الحصن",
    "shops": ["محل فورس أند فيذرس", "محل أكوا ريست هب"]
  }
]
```

##### ب. صيغة CSV - CSV Format

```csv
inspector,day,shift,area,shops
د. علي عبدالعال,2025-10-01,صباحية,سوق الميناء,"محل بيت الطيور|محل الميناء للطيور"
د. آمنه بن صرم,2025-10-01,مسائية,الحصن,"محل فورس أند فيذرس|محل أكوا ريست هب"
```

**ملاحظة**: في صيغة CSV، المحلات تفصل بـ `|` داخل الحقل.

**Note**: In CSV format, shops are separated by `|` within the field.

#### خطوات الاستخدام - Usage Steps

1. انقر على زر "📋 استيراد جماعي (Bulk Import)"
2. اختر الصيغة المطلوبة (JSON أو CSV)
3. الصق البيانات في المربع النصي
4. (اختياري) انقر "🔍 التحقق فقط" للتحقق من صحة البيانات
5. انقر "✅ معالجة واستيراد" لإضافة الخطط
6. سيتم عرض رسالة تأكيد بعدد الخطط المضافة

**Steps:**
1. Click "📋 استيراد جماعي (Bulk Import)"
2. Choose format (JSON or CSV)
3. Paste data in text area
4. (Optional) Click "🔍 التحقق فقط" to validate
5. Click "✅ معالجة واستيراد" to import
6. Confirmation message shows number of plans added

#### المميزات - Features

- ✅ التحقق التلقائي من صحة البيانات
- ✅ إنشاء تلقائي للمفتشين الجدد
- ✅ التحقق من وجود المناطق قبل الإضافة
- ✅ رسائل خطأ مفصلة عند وجود مشاكل
- ✅ إمكانية إضافة عشرات الخطط في ثوانٍ

**Features:**
- ✅ Automatic data validation
- ✅ Auto-creates new inspectors
- ✅ Validates areas exist
- ✅ Detailed error messages
- ✅ Add dozens of plans in seconds

---

### 2. 📑 نسخ خطة موجودة - Clone Existing Plan

**الغرض - Purpose:**
نسخ خطة تفتيش موجودة إلى تواريخ متعددة بسرعة.

Copy an existing inspection plan to multiple dates quickly.

#### خطوات الاستخدام - Usage Steps

1. انقر على زر "📑 نسخ خطة موجودة"
2. اختر المفتش من القائمة
3. اختر التاريخ الأصلي
4. أدخل التواريخ المستهدفة (مفصولة بفواصل)
   - مثال: `2025-10-05, 2025-10-12, 2025-10-19`
5. انقر "✅ نسخ الخطة"

**Steps:**
1. Click "📑 نسخ خطة موجودة"
2. Select inspector from dropdown
3. Select source date
4. Enter target dates (comma-separated)
   - Example: `2025-10-05, 2025-10-12, 2025-10-19`
5. Click "✅ نسخ الخطة"

#### مثال عملي - Practical Example

**السيناريو:** لديك خطة تفتيش للدكتور علي عبدالعال في 2025-10-01 وتريد نسخها لـ 4 تواريخ أخرى

**Scenario:** You have an inspection plan for Dr. Ali Abdelaal on 2025-10-01 and want to copy it to 4 other dates

```
المفتش: د. علي عبدالعال
التاريخ الأصلي: 2025-10-01
التواريخ المستهدفة: 2025-10-08, 2025-10-15, 2025-10-22, 2025-10-29
```

النتيجة: سيتم إنشاء 4 خطط جديدة بنفس المناوبة والمنطقة والمحلات

**Result:** 4 new plans will be created with same shift, area, and shops

---

### 3. 🔄 عمليات دفعية - Batch Operations

**الغرض - Purpose:**
تنفيذ عمليات على مجموعة من الخطط في نطاق زمني محدد.

Execute operations on multiple plans within a specific date range.

#### العمليات المتاحة - Available Operations

##### أ. حذف الخطط - Delete Plans

حذف جميع خطط التفتيش في نطاق زمني محدد.

Delete all inspection plans in a specific date range.

**مثال:** حذف جميع الخطط من 2025-10-15 إلى 2025-10-20

**Example:** Delete all plans from 2025-10-15 to 2025-10-20

##### ب. تغيير المناوبة - Change Shift

تغيير المناوبة لجميع الخطط في نطاق زمني.

Change shift for all plans in a date range.

**مثال:** تغيير جميع المناوبات من صباحية إلى مسائية للأسبوع الثاني من الشهر

**Example:** Change all morning shifts to evening for the second week

##### ج. تبديل المفتش - Swap Inspector

استبدال مفتش بآخر في جميع الخطط لنطاق زمني محدد.

Replace one inspector with another for all plans in a date range.

**مثال:** استبدال د. علي عبدالعال بـ د. محمد سعيد لفترة إجازة

**Example:** Replace Dr. Ali Abdelaal with Dr. Mohamed Said during vacation period

##### د. إضافة محلات - Add Shops

إضافة محلات جديدة لجميع الخطط في نطاق زمني.

Add new shops to all plans in a date range.

**مثال:** إضافة 3 محلات جديدة لجميع خطط شهر أكتوبر

**Example:** Add 3 new shops to all plans in October

#### خطوات الاستخدام - Usage Steps

1. انقر على زر "🔄 عمليات دفعية"
2. حدد النطاق الزمني (من تاريخ - إلى تاريخ)
3. اختر العملية المطلوبة
4. املأ الحقول الإضافية حسب العملية المختارة
5. انقر "✅ تنفيذ العملية"
6. قد يظهر تأكيد للعمليات الحساسة (مثل الحذف)

**Steps:**
1. Click "🔄 عمليات دفعية"
2. Select date range (from date - to date)
3. Choose operation
4. Fill additional fields based on operation
5. Click "✅ تنفيذ العملية"
6. Confirmation may appear for sensitive operations (like delete)

---

### 4. 💾 حفظ مباشر إلى GitHub - Direct GitHub Save

**الغرض - Purpose:**
حفظ التغييرات مباشرة إلى ملف plan-data.json في GitHub دون تحميل الملف يدوياً.

Save changes directly to plan-data.json in GitHub without manually downloading the file.

#### المتطلبات - Requirements

- توكن GitHub صحيح ومحفوظ
- صلاحيات الكتابة على المستودع

**Requirements:**
- Valid GitHub token saved
- Write permissions on repository

#### خطوات الاستخدام - Usage Steps

1. أدخل أو عدّل الخطط كالمعتاد
2. انقر على زر "💾 حفظ مباشر إلى GitHub"
3. أكد الحفظ
4. انتظر رسالة التأكيد (عادة 2-5 ثواني)
5. تم! البيانات محفوظة في GitHub مباشرة

**Steps:**
1. Add or edit plans as usual
2. Click "💾 حفظ مباشر إلى GitHub"
3. Confirm save
4. Wait for confirmation (usually 2-5 seconds)
5. Done! Data saved directly to GitHub

#### إعداد التوكن - Token Setup

إذا لم يكن لديك توكن محفوظ:

If you don't have a token saved:

1. انقر "🔑 تحديث التوكن" في قسم إدارة وضع الصيانة
2. أدخل توكن GitHub الخاص بك
3. انقر "حفظ"

**Steps:**
1. Click "🔑 تحديث التوكن" in maintenance section
2. Enter your GitHub token
3. Click "حفظ"

---

## 📊 أمثلة عملية - Practical Examples

### مثال 1: إضافة خطة شهرية كاملة

**السيناريو:** إضافة 30 خطة تفتيش لشهر نوفمبر دفعة واحدة

**Scenario:** Add 30 inspection plans for November at once

1. جهز ملف JSON أو CSV بجميع الخطط
2. استخدم "📋 استيراد جماعي"
3. الصق البيانات
4. انقر "✅ معالجة واستيراد"
5. سيتم إضافة جميع الـ 30 خطة في أقل من 5 ثواني!

**Time saved:** Instead of 30 minutes, only 1 minute!

---

### مثال 2: نسخ نمط أسبوعي

**السيناريو:** لديك نمط تفتيش أسبوعي وتريد تكراره لمدة شهر

**Scenario:** You have a weekly inspection pattern to repeat for a month

1. استخدم "📑 نسخ خطة موجودة"
2. اختر الخطة الأولى
3. أدخل 4 تواريخ (كل أسبوع)
4. كرر لكل مفتش
5. انتهى في دقائق معدودة!

**Time saved:** Instead of 2 hours, only 10 minutes!

---

### مثال 3: إجازة مفتش

**السيناريو:** مفتش في إجازة لمدة أسبوع، تريد استبداله

**Scenario:** Inspector on vacation for a week, need replacement

1. استخدم "🔄 عمليات دفعية"
2. حدد أسبوع الإجازة
3. اختر "تبديل المفتش"
4. اختر المفتش الأصلي والبديل
5. انقر "تنفيذ"

**Time saved:** Instead of 30 minutes, only 2 minutes!

---

## ⚠️ نصائح وتحذيرات - Tips & Warnings

### ✅ نصائح للاستخدام الأمثل - Best Practices

1. **استخدم التحقق أولاً**: دائماً اضغط "التحقق فقط" قبل الاستيراد النهائي
2. **احفظ نسخة احتياطية**: استخدم "تصدير البيانات إلى ملف JSON" قبل العمليات الكبيرة
3. **ابدأ بالتجربة**: جرب على بيانات قليلة أولاً
4. **استخدم الأنماط**: احفظ أنماط JSON/CSV المتكررة في ملفات نصية

**Tips:**
1. **Validate first**: Always click "التحقق فقط" before final import
2. **Backup**: Use "تصدير البيانات إلى ملف JSON" before large operations
3. **Start small**: Test with small data first
4. **Use patterns**: Save recurring JSON/CSV patterns in text files

### ⚠️ تحذيرات - Warnings

1. **عملية الحذف نهائية**: لا يمكن التراجع عن الحذف الدفعي
2. **التأكد من المناطق**: تأكد أن المناطق موجودة قبل الاستيراد
3. **تجنب التكرارات**: النظام يمنع تعيين نفس المحل لمفتشين في نفس اليوم
4. **حفظ GitHub**: تأكد من صلاحية التوكن قبل الحفظ المباشر

**Warnings:**
1. **Delete is permanent**: Cannot undo batch delete
2. **Verify areas**: Make sure areas exist before import
3. **Avoid duplicates**: System prevents assigning same shop to multiple inspectors on same day
4. **GitHub save**: Verify token validity before direct save

---

## 🐛 حل المشاكل - Troubleshooting

### مشكلة: فشل الاستيراد - Import Failed

**السبب المحتمل:** خطأ في صيغة البيانات

**Possible Cause:** Error in data format

**الحل:**
1. تحقق من صيغة JSON/CSV
2. تأكد من وجود جميع الحقول المطلوبة
3. استخدم "التحقق فقط" لمعرفة الخطأ تحديداً

**Solution:**
1. Check JSON/CSV format
2. Ensure all required fields exist
3. Use "التحقق فقط" to see specific error

---

### مشكلة: منطقة غير موجودة - Area Not Found

**السبب:** المنطقة المدخلة غير مسجلة في النظام

**Cause:** Area entered is not registered in system

**الحل:**
1. اذهب إلى "إدارة المناطق"
2. أضف المنطقة أولاً
3. ثم أعد محاولة الاستيراد

**Solution:**
1. Go to "إدارة المناطق"
2. Add the area first
3. Retry import

---

### مشكلة: فشل الحفظ إلى GitHub - GitHub Save Failed

**السبب المحتمل:** توكن منتهي الصلاحية أو غير صحيح

**Possible Cause:** Expired or invalid token

**الحل:**
1. انقر "🔑 تحديث التوكن"
2. أدخل توكن GitHub جديد
3. أعد محاولة الحفظ

**Solution:**
1. Click "🔑 تحديث التوكن"
2. Enter new GitHub token
3. Retry save

---

## 📈 قياس الأداء - Performance Metrics

### مقارنة الأداء - Performance Comparison

| العملية / Operation | الطريقة القديمة / Old Method | الطريقة الجديدة / New Method | توفير الوقت / Time Saved |
|---------------------|----------------------------|----------------------------|------------------------|
| إضافة 10 خطط / Add 10 plans | 15 دقيقة / 15 min | 1 دقيقة / 1 min | 93% |
| نسخ خطة لـ 5 أيام / Clone to 5 days | 10 دقائق / 10 min | 30 ثانية / 30 sec | 95% |
| تبديل مفتش لأسبوع / Swap inspector for week | 25 دقيقة / 25 min | 2 دقيقة / 2 min | 92% |
| حفظ البيانات / Save data | 5 دقائق / 5 min | 10 ثواني / 10 sec | 97% |

---

## 🎓 تمارين عملية - Practice Exercises

### تمرين 1: استيراد جماعي - Bulk Import Exercise

**الهدف:** إضافة 5 خطط تفتيش دفعة واحدة

**Goal:** Add 5 inspection plans at once

**البيانات:**
```json
[
  {"inspector": "د. علي عبدالعال", "day": "2025-11-01", "shift": "صباحية", "area": "سوق الميناء", "shops": ["محل 1", "محل 2"]},
  {"inspector": "د. آمنه بن صرم", "day": "2025-11-01", "shift": "صباحية", "area": "الحصن", "shops": ["محل 3", "محل 4"]},
  {"inspector": "د. آيه سلامة", "day": "2025-11-01", "shift": "صباحية", "area": "مدينة خليفة", "shops": ["محل 5", "محل 6"]},
  {"inspector": "د. حسينة العامري", "day": "2025-11-01", "shift": "مسائية", "area": "سوق التراث", "shops": ["محل 7"]},
  {"inspector": "د. حصة العلي", "day": "2025-11-01", "shift": "مسائية", "area": "المصفح", "shops": ["محل 8", "محل 9"]}
]
```

**الخطوات:**
1. افتح "استيراد جماعي"
2. الصق البيانات أعلاه
3. اضغط "معالجة واستيراد"
4. تحقق من الجدول

---

### تمرين 2: نسخ وتعديل - Clone and Modify Exercise

**الهدف:** نسخ خطة أسبوعية لمدة شهر

**Goal:** Clone a weekly plan for a month

**الخطوات:**
1. اختر أي خطة موجودة
2. استخدم "نسخ خطة موجودة"
3. أدخل 4 تواريخ (كل 7 أيام)
4. تحقق من النتيجة

---

## 📞 الدعم - Support

للمساعدة أو الاستفسارات:

For help or inquiries:

**المطور:** د. علي عبدالعال  
**Developer:** Dr. Ali Abdelaal

---

## 🔄 التحديثات المستقبلية - Future Updates

### قيد التطوير - In Development

- [ ] قوالب خطط التفتيش - Inspection plan templates
- [ ] اختصارات لوحة المفاتيح - Keyboard shortcuts
- [ ] التراجع والإعادة - Undo/Redo functionality
- [ ] استيراد من Excel مباشرة - Direct Excel import
- [ ] عرض تقويمي للخطط - Calendar view for plans
- [ ] إشعارات التعديلات - Edit notifications

---

## 📄 الترخيص - License

© 2025 المطور د. علي عبدالعال - Developed by Dr. Ali Abdelaal

جميع الحقوق محفوظة - All Rights Reserved
