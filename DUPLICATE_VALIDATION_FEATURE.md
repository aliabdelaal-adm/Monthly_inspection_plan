# Duplicate Shop Validation Feature

## Overview / نظرة عامة

This feature automatically validates inspection plans to ensure that no shop is assigned to multiple inspectors on the same day. When duplicates are detected, the system rejects the plan and provides detailed error messages to help developers correct the issue.

هذه الميزة تتحقق تلقائياً من خطط التفتيش للتأكد من عدم تعيين نفس المحل لعدة مفتشين في نفس اليوم. عند اكتشاف تكرارات، يرفض النظام الخطة ويوفر رسائل خطأ مفصلة لمساعدة المطورين على تصحيح المشكلة.

## Problem Statement / المشكلة

Previously, there was no automatic validation to prevent assigning the same shop to multiple inspectors on the same day. This could lead to conflicts and inefficiencies in the inspection process.

سابقاً، لم يكن هناك تحقق تلقائي لمنع تعيين نفس المحل لعدة مفتشين في نفس اليوم. هذا قد يؤدي إلى تعارضات وعدم كفاءة في عملية التفتيش.

## Solution / الحل

A validation function has been added to the `merge_plan_data.py` script that:

تم إضافة دالة تحقق إلى سكريبت `merge_plan_data.py` التي:

1. **Checks for duplicates** / **تتحقق من التكرارات**: Scans all inspection data to find shops assigned to multiple inspectors on the same day
2. **Rejects invalid plans** / **ترفض الخطط غير الصحيحة**: Prevents merging data that contains duplicate shop assignments
3. **Provides detailed feedback** / **توفر تعليقات مفصلة**: Shows which shops are duplicated, on which dates, and which inspectors are involved
4. **Allows valid assignments** / **تسمح بالتعيينات الصحيحة**: Permits the same shop to be assigned to different inspectors on different days

## Features / المميزات

### 1. Automatic Validation / التحقق التلقائي

The validation runs automatically during the merge process before any data is saved.

يتم التحقق تلقائياً أثناء عملية الدمج قبل حفظ أي بيانات.

### 2. Bilingual Error Messages / رسائل خطأ ثنائية اللغة

All error messages are displayed in both Arabic and English for clarity.

جميع رسائل الخطأ معروضة بالعربية والإنجليزية للوضوح.

### 3. Detailed Duplicate Reports / تقارير مفصلة عن التكرارات

When duplicates are found, the system shows:
- Date of the conflict / تاريخ التعارض
- Shop name / اسم المحل
- List of all inspectors assigned to that shop / قائمة بجميع المفتشين المعينين لذلك المحل

## Usage / الاستخدام

### Using the Merge Script / استخدام سكريبت الدمج

```bash
python3 merge_plan_data.py
```

The merge script now automatically validates data. If duplicates are detected, you'll see:

سكريبت الدمج الآن يتحقق من البيانات تلقائياً. إذا تم اكتشاف تكرارات، سترى:

```
❌ خطأ: تم اكتشاف تكرار محلات لعدة مفتشين في نفس اليوم!
❌ Error: Duplicate shop assignments detected!

🔔 تفاصيل التكرارات / Duplicate Details:
================================================================================

📅 التاريخ / Date: 2025-09-26
🏪 المحل / Shop: محل بيت الطيور
👥 المفتشين / Inspectors:
   - د. آمنه بن صرم
   - د. علي عبدالعال

⚠️  يرجى تصحيح الخطة واختيار محلات مختلفة للمفتشين في نفس اليوم
⚠️  Please correct the plan and choose different shops for inspectors on the same day
❌ الدمج ملغى / Merge cancelled
```

### Using the Standalone Validation Tool / استخدام أداة التحقق المستقلة

To check the current `plan-data.json` for duplicates without merging:

للتحقق من `plan-data.json` الحالي عن التكرارات دون الدمج:

```bash
python3 validate_plan.py
```

This will scan the existing data and report any duplicates found.

هذا سيفحص البيانات الموجودة ويبلغ عن أي تكرارات موجودة.

## Technical Details / التفاصيل التقنية

### Validation Function / دالة التحقق

```python
def validate_shop_duplicates(inspection_data):
    """Validate that no shop is assigned to multiple inspectors on the same day."""
    # Returns: (is_valid, duplicate_info_list)
```

The function:
1. Groups all shop assignments by date
2. For each date, tracks which inspectors are assigned to each shop
3. Identifies shops assigned to more than one inspector on the same day
4. Returns validation status and detailed duplicate information

### Integration in Merge Script / التكامل في سكريبت الدمج

The validation is integrated into the merge workflow:

```python
# After merging data
merged_data['inspectionData'] = merged_inspections

# Validate before saving
is_valid, duplicates = validate_shop_duplicates(merged_data['inspectionData'])

if not is_valid:
    # Display errors and cancel merge
    return False

# Continue with save if valid
```

## Test Files / ملفات الاختبار

### test_duplicate_validation.py

Comprehensive unit tests for the validation function:
- Test with no duplicates (should pass)
- Test with duplicates on same day (should fail)
- Test with same shop on different days (should pass)
- Test with multiple duplicates (should fail)

### test_merge_with_duplicates.py

Tests the integration of validation with the merge function.

### validate_plan.py

Standalone tool to check existing plan data for duplicates.

## Running Tests / تشغيل الاختبارات

```bash
# Run validation function tests
python3 test_duplicate_validation.py

# Run merge integration tests
python3 test_merge_with_duplicates.py

# Check current plan data
python3 validate_plan.py
```

## Important Notes / ملاحظات مهمة

1. **Same shop, different days is allowed** / **نفس المحل، أيام مختلفة مسموح**
   - A shop can be assigned to different inspectors on different days
   - المحل يمكن تعيينه لمفتشين مختلفين في أيام مختلفة

2. **Same inspector, same day, different shifts** / **نفس المفتش، نفس اليوم، فترات مختلفة**
   - The validation checks by day, not by shift
   - If two inspectors have the same shop on the same day (even different shifts), it's flagged
   - التحقق يتم حسب اليوم، وليس حسب الفترة
   - إذا كان لدى مفتشين نفس المحل في نفس اليوم (حتى في فترات مختلفة)، يتم الإبلاغ عنه

3. **Validation runs before saving** / **التحقق يتم قبل الحفظ**
   - No data is saved if validation fails
   - The original files remain unchanged
   - لا يتم حفظ أي بيانات إذا فشل التحقق
   - الملفات الأصلية تبقى دون تغيير

## Benefits / الفوائد

1. **Prevents conflicts** / **يمنع التعارضات**: Ensures efficient inspection scheduling
2. **Early error detection** / **كشف مبكر للأخطاء**: Catches issues before they affect operations
3. **Clear feedback** / **تعليقات واضحة**: Helps developers quickly identify and fix problems
4. **Data integrity** / **سلامة البيانات**: Maintains high-quality inspection plans
5. **Bilingual support** / **دعم ثنائي اللغة**: Accessible to Arabic and English speakers

## Future Enhancements / التحسينات المستقبلية

Possible improvements:
- Web interface for validation
- Automatic suggestion of alternative shops
- Validation API endpoint
- Integration with notification system

تحسينات محتملة:
- واجهة ويب للتحقق
- اقتراح تلقائي لمحلات بديلة
- نقطة نهاية API للتحقق
- التكامل مع نظام الإشعارات
