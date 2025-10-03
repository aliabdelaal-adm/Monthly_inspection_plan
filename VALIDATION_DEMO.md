# Duplicate Shop Validation - Demo Scenarios
# سيناريوهات توضيحية للتحقق من تكرار المحلات

## Demo Scenario 1: Adding Valid Entry / السيناريو 1: إضافة إدخال صحيح

### Setup / الإعداد
Existing data in the system:
```
Inspector: د. علي عبدالعال
Date: 2025-01-15
Shops: محل السمك, محل اللحوم
```

### Action / الإجراء
Developer tries to add:
```
Inspector: د. آمنه بن صرم
Date: 2025-01-15
Shops: محل الدجاج, محل الخضار
```

### Expected Result / النتيجة المتوقعة
✅ **SUCCESS** - Entry saved successfully
- No duplicate shops
- Each shop assigned to only one inspector on this day

---

## Demo Scenario 2: Detecting Duplicate / السيناريو 2: اكتشاف التكرار

### Setup / الإعداد
Existing data in the system:
```
Inspector: د. علي عبدالعال
Date: 2025-01-15
Shops: محل بيت الطيور, محل اللحوم
```

### Action / الإجراء
Developer tries to add:
```
Inspector: د. آمنه بن صرم
Date: 2025-01-15
Shops: محل بيت الطيور, محل الخضار
```

### Expected Result / النتيجة المتوقعة
❌ **ERROR DETECTED** - Entry blocked with error message:

```
❌ خطأ: تم اكتشاف تكرار محلات لعدة مفتشين في نفس اليوم!
❌ Error: Duplicate shop assignments detected!

🔔 عدد التكرارات / Number of duplicates: 1

📋 تفاصيل التكرارات / Duplicate Details:
═══════════════════════════════════════════════════

1. 📅 التاريخ / Date: ١٥ يناير ٢٠٢٥ (2025-01-15)
   🏪 المحل / Shop: محل بيت الطيور
   👥 المفتشين / Inspectors (2):
      - د. علي عبدالعال
      - د. آمنه بن صرم

═══════════════════════════════════════════════════
⚠️  توصيات / Recommendations:
   1. يرجى مراجعة الخطة وتعديل توزيع المحلات
   1. Please review the plan and modify shop assignments
   2. تأكد من أن كل محل مخصص لمفتش واحد فقط في اليوم الواحد
   2. Ensure each shop is assigned to only one inspector per day
   3. يمكن تخصيص نفس المحل لمفتشين مختلفين في أيام مختلفة
   3. The same shop can be assigned to different inspectors on different days
```

### What Happens / ما يحدث
- Error dialog appears / يظهر مربع حوار الخطأ
- Entry is NOT saved / لا يتم حفظ الإدخال
- Developer can modify and try again / يمكن للمطور التعديل والمحاولة مرة أخرى

---

## Demo Scenario 3: Same Shop, Different Days (Valid) / السيناريو 3: نفس المحل، أيام مختلفة (صحيح)

### Setup / الإعداد
Existing data in the system:
```
Inspector: د. علي عبدالعال
Date: 2025-01-15
Shops: محل بيت الطيور
```

### Action / الإجراء
Developer tries to add:
```
Inspector: د. آمنه بن صرم
Date: 2025-01-16  ← Different date!
Shops: محل بيت الطيور
```

### Expected Result / النتيجة المتوقعة
✅ **SUCCESS** - Entry saved successfully
- Same shop on different days is allowed
- يُسمح بنفس المحل في أيام مختلفة

---

## Demo Scenario 4: Multiple Duplicates / السيناريو 4: تكرارات متعددة

### Setup / الإعداد
Existing data in the system:
```
Inspector: د. علي عبدالعال
Date: 2025-01-15
Shops: محل السمك, محل اللحوم

Inspector: د. آمنه بن صرم
Date: 2025-01-15
Shops: محل الدجاج
```

### Action / الإجراء
Developer tries to add:
```
Inspector: د. محمد أحمد
Date: 2025-01-15
Shops: محل السمك, محل الدجاج
```

### Expected Result / النتيجة المتوقعة
❌ **ERROR DETECTED** - Entry blocked with error message showing **2 duplicates**:

```
❌ خطأ: تم اكتشاف تكرار محلات لعدة مفتشين في نفس اليوم!
❌ Error: Duplicate shop assignments detected!

🔔 عدد التكرارات / Number of duplicates: 2

📋 تفاصيل التكرارات / Duplicate Details:
═══════════════════════════════════════════════════

1. 📅 التاريخ / Date: ١٥ يناير ٢٠٢٥ (2025-01-15)
   🏪 المحل / Shop: محل السمك
   👥 المفتشين / Inspectors (2):
      - د. علي عبدالعال
      - د. محمد أحمد

2. 📅 التاريخ / Date: ١٥ يناير ٢٠٢٥ (2025-01-15)
   🏪 المحل / Shop: محل الدجاج
   👥 المفتشين / Inspectors (2):
      - د. آمنه بن صرم
      - د. محمد أحمد

═══════════════════════════════════════════════════
```

---

## Demo Scenario 5: Smart Rotation Validation / السيناريو 5: التحقق من التوزيع الذكي

### Setup / الإعداد
Existing data in the system:
```
Inspector: د. علي عبدالعال
Date: 2025-01-15
Shops: محل الخضار
```

### Action / الإجراء
Developer generates a smart rotation plan that includes:
```
Inspector: د. آمنه بن صرم
Date: 2025-01-15
Shops: محل الخضار, محل الفواكه
```

### Expected Result / النتيجة المتوقعة
❌ **ERROR DETECTED** - Plan NOT applied, with two error messages:

First message (detailed duplicates):
```
[Same format as above showing محل الخضار conflict]
```

Second message:
```
❌ لا يمكن تطبيق الخطة بسبب وجود تكرارات!
يرجى مراجعة الخطة أو حذف البيانات المتعارضة.
```

### What Happens / ما يحدث
- Generated plan is NOT applied / لا يتم تطبيق الخطة المولدة
- Existing data remains unchanged / تبقى البيانات الموجودة دون تغيير
- Developer can review and fix conflicts / يمكن للمطور مراجعة وإصلاح التعارضات

---

## How to Test These Scenarios / كيفية اختبار هذه السيناريوهات

### Method 1: Interactive Test Page / الطريقة 1: صفحة الاختبار التفاعلية
1. Open `test_frontend_validation.html` in a browser
2. Click on each test button
3. Observe the results

### Method 2: Main Application / الطريقة 2: التطبيق الرئيسي
1. Open `index.html` in a browser
2. Log in as developer
3. Try to add entries as described in scenarios above
4. Observe validation messages

### Method 3: Automated Tests / الطريقة 3: الاختبارات التلقائية
```bash
# JavaScript tests
node test_validation.js

# Python tests (backend)
python3 test_duplicate_validation.py
```

---

## User Experience Flow / تدفق تجربة المستخدم

```
Developer Action → Validation Check → Result
   إجراء المطور ← فحص التحقق ← النتيجة

┌─────────────────┐
│ Developer adds  │
│ or edits entry  │
│ المطور يضيف أو │
│ يحرر إدخال     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ System creates  │
│ temp copy and   │
│ validates       │
│ النظام ينشئ    │
│ نسخة مؤقتة     │
│ ويتحقق         │
└────────┬────────┘
         │
         ▼
    ┌───┴───┐
    │ Valid?│
    │صحيح؟ │
    └───┬───┘
        │
   ┌────┴────┐
   │         │
   ▼         ▼
┌──────┐  ┌──────┐
│ YES  │  │  NO  │
│ نعم  │  │  لا  │
└───┬──┘  └──┬───┘
    │         │
    ▼         ▼
┌──────┐  ┌──────┐
│ Save │  │Error │
│ Data │  │ Msg  │
│حفظ   │  │رسالة │
│البيان│  │ خطأ  │
│ ات   │  │      │
└──────┘  └──────┘
```

---

## Benefits / الفوائد

✅ **Immediate Feedback** - Developer knows instantly if there's a problem
✅ **تغذية راجعة فورية** - يعرف المطور فوراً إذا كانت هناك مشكلة

✅ **Detailed Information** - Shows exactly which shops and inspectors conflict
✅ **معلومات مفصلة** - يعرض بالضبط أي المحلات والمفتشين تتعارض

✅ **Data Integrity** - Prevents invalid data from being saved
✅ **سلامة البيانات** - يمنع حفظ البيانات غير الصحيحة

✅ **User Friendly** - Clear bilingual messages guide the developer
✅ **سهل الاستخدام** - رسائل واضحة بلغتين توجه المطور

✅ **Consistent** - Same validation logic as backend Python scripts
✅ **متسق** - نفس منطق التحقق مثل سكريبتات Python الخلفية

---

## Common Questions / أسئلة شائعة

### Q: Can the same shop be assigned to different inspectors on different days?
### س: هل يمكن تعيين نفس المحل لمفتشين مختلفين في أيام مختلفة؟

**A: YES** - This is allowed and valid. The validation only checks for duplicates **on the same day**.

**ج: نعم** - هذا مسموح وصحيح. يتحقق النظام فقط من التكرارات **في نفس اليوم**.

### Q: What if I need to override the validation?
### س: ماذا لو احتجت إلى تجاوز التحقق؟

**A:** The validation cannot be overridden in the UI for data integrity. If you need to make an exception, you would need to modify the data directly in `plan-data.json` file and ensure you understand the implications.

**ج:** لا يمكن تجاوز التحقق في واجهة المستخدم للحفاظ على سلامة البيانات. إذا كنت بحاجة إلى استثناء، ستحتاج إلى تعديل البيانات مباشرة في ملف `plan-data.json` والتأكد من فهم التداعيات.

### Q: Does this affect existing data?
### س: هل يؤثر هذا على البيانات الموجودة؟

**A: NO** - Validation only occurs when **adding or editing** entries. Existing data is not automatically checked or modified. You can run `python3 validate_plan.py` to check existing data for duplicates.

**ج: لا** - يحدث التحقق فقط عند **إضافة أو تحرير** الإدخالات. لا يتم فحص أو تعديل البيانات الموجودة تلقائياً. يمكنك تشغيل `python3 validate_plan.py` للتحقق من البيانات الموجودة.
