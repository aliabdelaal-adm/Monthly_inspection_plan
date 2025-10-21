# تقرير إزالة المحلات المكررة
# Duplicate Shops Removal Report

## نظرة عامة | Overview

تم تنفيذ عملية شاملة لإزالة ودمج المحلات المكررة في نظام خطة التفتيش الشهرية.
A comprehensive duplicate shops removal and merging operation was performed on the monthly inspection plan system.

## المشكلة | Problem

كانت المشكلة تتمثل في:
The problem consisted of:

1. **محلات بنفس الاسم تماماً** - Exact duplicate shop names
2. **محلات تختلف فقط بوجود/عدم وجود كلمة "محل"** - Shops differing only by "محل" prefix
3. **محلات بنفس رقم الرخصة** - Shops with same license number
4. **محلات بنفس الاسم الإنجليزي** - Shops with same English name

## الحل | Solution

تم إنشاء برنامج نصي شامل (`remove_duplicate_shops.py`) يقوم بـ:
A comprehensive script was created (`remove_duplicate_shops.py`) that:

### 1. تحديد المحلات المكررة | Identify Duplicates
- البحث عن محلات تختلف فقط بوجود كلمة "محل"
- Search for shops differing only by "محل" prefix
- البحث عن محلات بنفس رقم الرخصة
- Search for shops with same license number
- البحث عن محلات بنفس الاسم الإنجليزي
- Search for shops with same English name

### 2. اختيار النسخة الأفضل | Select Best Version
يتم اختيار المحل الذي يحتوي على معلومات أكثر اكتمالاً:
The shop with more complete information is selected:
- الاسم الإنجليزي | English name (+10 points)
- رقم الرخصة | License number (+10 points)
- الموقع على الخريطة | Map location (+5 points)
- العنوان | Address (+3 points)
- معلومات الاتصال | Contact info (+2 points)
- تفضيل الاسم بدون "محل" | Prefer name without "محل" (+1 point)

### 3. الدمج والتحديث | Merge and Update
- حذف المحلات المكررة من `shops_details.json`
- Delete duplicate shops from `shops_details.json`
- تحديث جميع المراجع في `plan-data.json`
- Update all references in `plan-data.json`
- إزالة التكرارات التي قد تنشأ من عملية الدمج
- Remove duplicates that may arise from merging

## النتائج | Results

### المحلات المحذوفة من shops_details.json | Shops Removed from shops_details.json

1. **مركز الاحياء المائية 2**
   - السبب | Reason: نفس رقم الرخصة | Same license (CN-1020637)
   - تم الاحتفاظ بـ | Kept: مركز الاحياء المائية 1

2. **كوارييام وورد**
   - السبب | Reason: نفس رقم الرخصة | Same license (CN-4745331)
   - تم الاحتفاظ بـ | Kept: عالم الأحياء المائية

3. **بديز لإيواء الحيوانات و تربيتها**
   - السبب | Reason: نفس رقم الرخصة | Same license (CN-4525643)
   - تم الاحتفاظ بـ | Kept: اف ثري لتجارة اغذية الطيور و مستلزمات الطيور

4. **ذا بيت شوب ش.ذ.م.م - فرع  ابوظبي 2**
   - السبب | Reason: نفس الاسم الإنجليزي | Same English name
   - تم الاحتفاظ بـ | Kept: ذا بيت شوب ش.ذ.م.م - فرع  ابوظبي 1

### الدمج في plan-data.json | Merging in plan-data.json

تم دمج المحلات التي تختلف فقط بكلمة "محل":
Shops differing only by "محل" prefix were merged:

1. **محل المشرف لتجارة الأسماك** → **المشرف لتجارة الأسماك**
   - عدد المراجع المحدثة | References updated: 3

2. **محل مركز الأحياء المائية** → **مركز الأحياء المائية**
   - عدد المراجع المحدثة | References updated: 4

### الإحصائيات | Statistics

- **المحلات قبل** | Shops before: 510
- **المحلات بعد** | Shops after: 506
- **المحلات المحذوفة** | Shops removed: 4
- **المراجع المحدثة** | References updated: 7

## التحقق | Verification

تم إنشاء مجموعة اختبارات شاملة للتحقق من:
A comprehensive test suite was created to verify:

✅ عدم وجود تكرارات لكلمة "محل" | No "محل" prefix duplicates
✅ عدم وجود تكرارات في أرقام الرخص | No license duplicates
✅ عدم وجود تكرارات في الأسماء الإنجليزية | No English name duplicates
✅ حذف المحلات المكررة المحددة | Specific duplicates removed
✅ الاحتفاظ بالمحلات الصحيحة | Correct shops kept
✅ تحديث المراجع بشكل صحيح | References properly updated
✅ سلامة البيانات | Data integrity maintained

## الملفات المعدلة | Modified Files

1. **shops_details.json** - تم حذف 4 محلات مكررة | 4 duplicate shops removed
2. **plan-data.json** - تم تحديث 7 مراجع | 7 references updated
3. **remove_duplicate_shops.py** - برنامج نصي جديد | New script
4. **test_remove_duplicates.py** - اختبارات الوحدة | Unit tests
5. **test_duplicate_removal_results.py** - اختبارات التحقق | Verification tests

## كيفية الاستخدام | How to Use

لإزالة المحلات المكررة مرة أخرى في المستقبل:
To remove duplicate shops again in the future:

```bash
python3 remove_duplicate_shops.py
```

للتحقق من النتائج:
To verify results:

```bash
python3 test_duplicate_removal_results.py
```

## الخلاصة | Conclusion

تم بنجاح إزالة جميع المحلات المكررة ودمج المحلات التي تختلف فقط بوجود كلمة "محل". تم الاحتفاظ دائماً بالمحل الذي يحتوي على معلومات أكثر اكتمالاً (الموقع على الخريطة، رقم الرخصة، الاسم بالإنجليزية).

All duplicate shops were successfully removed and shops differing only by the word "محل" were merged. The shop with more complete information (map location, license number, English name) was always kept.

---

**تاريخ التنفيذ | Implementation Date:** 2025-10-21
**الحالة | Status:** ✅ مكتمل | Completed
