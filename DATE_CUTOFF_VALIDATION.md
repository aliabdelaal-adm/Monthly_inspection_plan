# التحقق من التكرارات بناءً على التاريخ
# Date-Based Duplicate Validation

## 📅 نظرة عامة / Overview

### بالعربية
تم تطبيق قاعدة جديدة للتحقق من تكرار المحلات بدءاً من **7 أكتوبر 2024**. هذه القاعدة تمنع تعيين نفس المحل لأكثر من مفتش في نفس اليوم، وذلك للتواريخ من 7 أكتوبر 2024 فصاعداً.

### In English
A new validation rule has been implemented starting from **October 7, 2024**. This rule prevents assigning the same shop to multiple inspectors on the same day, for all dates from October 7, 2024 onwards.

---

## 🎯 الهدف / Purpose

### بالعربية
- **منع التعارض**: تجنب إرسال أكثر من مفتش لنفس المحل في نفس اليوم
- **تحسين الكفاءة**: ضمان التوزيع الأمثل للمفتشين على المحلات
- **التوافق العكسي**: السماح بالبيانات التاريخية قبل 7 أكتوبر 2024 دون تأثير

### In English
- **Prevent Conflicts**: Avoid sending multiple inspectors to the same shop on the same day
- **Improve Efficiency**: Ensure optimal distribution of inspectors across shops
- **Backward Compatibility**: Allow historical data before October 7, 2024 without impact

---

## 📋 القواعد / Rules

### ✅ الحالات المسموحة / Allowed Cases

1. **تفتيشات قبل 7 أكتوبر 2024**
   - أي تفتيش قبل هذا التاريخ لا يخضع للقاعدة
   - Any inspection before this date is not subject to the rule

2. **نفس المحل في أيام مختلفة**
   - يمكن للمفتش أ أن يزور محل X في يوم 10 أكتوبر
   - ويمكن للمفتش ب أن يزور نفس المحل X في يوم 11 أكتوبر
   - Inspector A can visit shop X on October 10
   - Inspector B can visit the same shop X on October 11

3. **محلات مختلفة لنفس المفتش**
   - يمكن للمفتش الواحد زيارة عدة محلات في نفس اليوم
   - One inspector can visit multiple shops on the same day

### ❌ الحالات الممنوعة / Blocked Cases

1. **نفس المحل لعدة مفتشين في نفس اليوم (بدءاً من 7 أكتوبر 2024)**
   - المفتش أ: محل X - يوم 15 أكتوبر 2024 - صباحي ❌
   - المفتش ب: محل X - يوم 15 أكتوبر 2024 - مسائي ❌
   
   - Inspector A: Shop X - October 15, 2024 - Morning ❌
   - Inspector B: Shop X - October 15, 2024 - Evening ❌

2. **التكرار يُمنع بغض النظر عن الفترة**
   - حتى لو كانت الفترات مختلفة (صباحي/مسائي)
   - التحقق يتم على مستوى اليوم الواحد
   - Even if shifts are different (morning/evening)
   - Validation is at the day level

---

## 💻 التنفيذ التقني / Technical Implementation

### تعديلات دالة `validateShopDuplicates`

```javascript
function validateShopDuplicates(inspectionDataToValidate, daysToCheck = null) {
    const dayShopInspectors = {};
    const duplicates = [];
    
    // Date cutoff: Only apply validation from October 7, 2024 onwards
    // بداية تطبيق القاعدة: من 7 أكتوبر 2024 فصاعداً
    const VALIDATION_START_DATE = new Date('2024-10-07');
    
    for (const entry of inspectionDataToValidate) {
        const day = entry.day;
        const inspector = entry.inspector;
        const shops = entry.shops || [];
        
        if (!day || !inspector || shops.length === 0) {
            continue;
        }
        
        // If daysToCheck is specified, only process entries for those days
        if (daysToCheck !== null && !daysToCheck.includes(day)) {
            continue;
        }
        
        // Skip validation for dates before October 7, 2024
        // تخطي التحقق للتواريخ قبل 7 أكتوبر 2024
        const entryDate = new Date(day);
        if (entryDate < VALIDATION_START_DATE) {
            continue;
        }
        
        // ... rest of validation logic
    }
    
    // ... find duplicates
}
```

### رسالة الخطأ المحدثة / Updated Error Message

```javascript
function showDuplicateShopsError(duplicates) {
    let errorMessage = '❌ خطأ: تم اكتشاف تكرار محلات لعدة مفتشين في نفس اليوم!\n';
    errorMessage += '❌ Error: Duplicate shop assignments detected!\n\n';
    errorMessage += '📅 القاعدة: لا يُسمح بتكرار نفس المحل لأكثر من مفتش في نفس اليوم (بدءاً من 7 أكتوبر 2024)\n';
    errorMessage += '📅 Policy: Same shop cannot be assigned to multiple inspectors on the same day (starting from October 7, 2024)\n\n';
    
    // ... rest of error message
}
```

---

## 🧪 الاختبارات / Tests

### نتائج الاختبارات / Test Results

| الاختبار / Test | الوصف / Description | النتيجة / Result |
|-----------------|---------------------|-----------------|
| Test 1 | تكرار قبل 7 أكتوبر 2024 | ✅ مسموح / Allowed |
| Test 2 | تكرار في 7 أكتوبر 2024 | ❌ ممنوع / Blocked |
| Test 3 | تكرار بعد 7 أكتوبر 2024 | ❌ ممنوع / Blocked |
| Test 4 | لا تكرار بعد 7 أكتوبر 2024 | ✅ مسموح / Allowed |
| Test 5 | نفس المحل في أيام مختلفة | ✅ مسموح / Allowed |
| Test 6 | تكرارات متعددة في يوم واحد | ❌ ممنوع / Blocked |
| Test 7 | تواريخ مختلطة | ✅ التحقق من التواريخ بعد القاطع فقط |

---

## 📊 أمثلة عملية / Practical Examples

### مثال 1: سيناريو مسموح / Example 1: Allowed Scenario

```json
[
    {
        "inspector": "د. علي",
        "day": "2024-10-05",
        "shift": "صباحي",
        "shops": ["محل A"]
    },
    {
        "inspector": "د. آمنه",
        "day": "2024-10-05",
        "shift": "مسائي",
        "shops": ["محل A"]
    }
]
```
**النتيجة / Result**: ✅ **مسموح** - التاريخ قبل 7 أكتوبر 2024

---

### مثال 2: سيناريو ممنوع / Example 2: Blocked Scenario

```json
[
    {
        "inspector": "د. علي",
        "day": "2025-09-26",
        "shift": "صباحي",
        "shops": ["محل B"]
    },
    {
        "inspector": "د. آمنه",
        "day": "2025-09-26",
        "shift": "مسائي",
        "shops": ["محل B"]
    }
]
```
**النتيجة / Result**: ❌ **ممنوع** - نفس المحل لمفتشين مختلفين في نفس اليوم

**رسالة الخطأ / Error Message**:
```
❌ خطأ: تم اكتشاف تكرار محلات لعدة مفتشين في نفس اليوم!
❌ Error: Duplicate shop assignments detected!

📅 القاعدة: لا يُسمح بتكرار نفس المحل لأكثر من مفتش في نفس اليوم (بدءاً من 7 أكتوبر 2024)
📅 Policy: Same shop cannot be assigned to multiple inspectors on the same day (starting from October 7, 2024)

🔔 عدد التكرارات / Number of duplicates: 1

📋 تفاصيل التكرارات / Duplicate Details:
═══════════════════════════════════════════════════

1. 📅 التاريخ / Date: ٢٦ سبتمبر ٢٠٢٥ (2025-09-26)
   🏪 المحل / Shop: محل B
   👥 المفتشين / Inspectors (2):
      - د. علي
      - د. آمنه
```

---

### مثال 3: سيناريو مسموح - أيام مختلفة / Example 3: Allowed - Different Days

```json
[
    {
        "inspector": "د. علي",
        "day": "2025-09-26",
        "shift": "صباحي",
        "shops": ["محل C"]
    },
    {
        "inspector": "د. آمنه",
        "day": "2025-09-27",
        "shift": "مسائي",
        "shops": ["محل C"]
    }
]
```
**النتيجة / Result**: ✅ **مسموح** - نفس المحل في أيام مختلفة

---

## 🔧 استكشاف الأخطاء / Troubleshooting

### المشكلة: رفض بيانات تاريخية
**الحل**: تأكد من أن التاريخ قبل 7 أكتوبر 2024. البيانات التاريخية قبل هذا التاريخ لا تخضع للقاعدة.

### Problem: Historical data rejected
**Solution**: Ensure the date is before October 7, 2024. Historical data before this date is not subject to the rule.

---

### المشكلة: عدم ظهور رسالة خطأ للتكرارات
**الحل**: تحقق من:
1. التاريخ >= 7 أكتوبر 2024
2. نفس المحل مخصص لأكثر من مفتش
3. في نفس اليوم

### Problem: No error message for duplicates
**Solution**: Check:
1. Date >= October 7, 2024
2. Same shop assigned to multiple inspectors
3. On the same day

---

## 📝 ملاحظات مهمة / Important Notes

### بالعربية
1. **تاريخ البداية**: القاعدة تطبق فقط على التواريخ من 7 أكتوبر 2024 فصاعداً
2. **التوافق العكسي**: البيانات التاريخية قبل 7 أكتوبر 2024 محفوظة ولا تتأثر
3. **الفترات**: القاعدة تطبق بغض النظر عن الفترة (صباحي/مسائي)
4. **الأيام المختلفة**: يمكن تخصيص نفس المحل لمفتشين مختلفين في أيام مختلفة

### In English
1. **Start Date**: Rule applies only to dates from October 7, 2024 onwards
2. **Backward Compatibility**: Historical data before October 7, 2024 is preserved and unaffected
3. **Shifts**: Rule applies regardless of shift (morning/evening)
4. **Different Days**: Same shop can be assigned to different inspectors on different days

---

## 🔄 تحديثات مستقبلية / Future Updates

### إمكانيات التحسين / Potential Improvements
- إضافة إمكانية تعديل تاريخ البداية من واجهة المستخدم
- إضافة تقارير تحليلية عن التكرارات
- إرسال تنبيهات تلقائية عند محاولة إضافة تكرار

- Add ability to modify start date from UI
- Add analytical reports about duplicates
- Send automatic alerts when attempting to add duplicates

---

## 📞 الدعم / Support

للمزيد من المعلومات أو الإبلاغ عن مشاكل، يرجى فتح issue في المستودع.

For more information or to report issues, please open an issue in the repository.

---

**تاريخ الإضافة / Date Added**: يناير 2025 / January 2025
**الإصدار / Version**: 1.0
**الحالة / Status**: ✅ نشط / Active
