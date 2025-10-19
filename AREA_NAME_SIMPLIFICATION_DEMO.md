# تبسيط أسماء المناطق - Area Name Simplification

## نظرة عامة | Overview

تم تحديث السكريبت `merge_new_pet_shop_licenses.py` لتبسيط أسماء المناطق عند الدمج من ملف "رخص المحلات الجديدة.xlsx".

The script `merge_new_pet_shop_licenses.py` has been updated to simplify area names when merging from "رخص المحلات الجديدة.xlsx".

## المشكلة | The Problem

ملف الرخص الجديدة يحتوي على عناوين تفصيلية تشمل:
- اسم المنطقة
- اسم الشارع
- إحداثيات المبنى
- تفاصيل إضافية

The new licenses file contains detailed addresses including:
- Area name
- Street name
- Building coordinates
- Additional details

### مثال للعنوان التفصيلي | Detailed Address Example
```
شمال الوثبة, شمال الوثبة 59, ق 10 - مستودع 31, وحدة, دائرة بلدية ابوظبي و اخرين
```

## الحل | The Solution

السكريبت الآن يستخرج **اسم المنطقة فقط** ويتجاهل التفاصيل الأخرى.

The script now extracts **only the area name** and ignores other details.

### طريقة الاستخراج | Extraction Method

1. إذا كان العنوان يحتوي على فاصلة (,)، يؤخذ الجزء الأول
2. إذا لم يكن هناك فاصلة ولكن يوجد شرطة (-)، يؤخذ الجزء الأول
3. تنظيف المسافات الزائدة

1. If address contains comma (,), take the first part
2. If no comma but contains dash (-), take the first part
3. Clean up extra whitespace

## أمثلة قبل وبعد | Before & After Examples

### مثال 1 | Example 1
**قبل (Before):**
```
شمال الوثبة, شمال الوثبة 59, ق 10 - مستودع 31, وحدة, دائرة بلدية ابوظبي و اخرين
```
**بعد (After):**
```
شمال الوثبة
```

### مثال 2 | Example 2
**قبل (Before):**
```
المصفح, م 43, 0 : ~, مبنى, السيد غانم حبروت سيف و اخرين
```
**بعد (After):**
```
المصفح
```

### مثال 3 | Example 3
**قبل (Before):**
```
مصفح جنوب, ايكاد 3, 0 : ~, مبنى, السيد سمو الشيخ محمد بن خليفة بن زايد و اخرين
```
**بعد (After):**
```
مصفح جنوب
```

### مثال 4 | Example 4
**قبل (Before):**
```
أبو ظبي - شارع الميناء - بناية دائرة بلدية أبوظبي
```
**بعد (After):**
```
أبو ظبي
```

### مثال 5 | Example 5
**قبل (Before):**
```
الوثبة, مسلخ الوثبة - زريبة 39, بناية / بلدية أبوظبي
```
**بعد (After):**
```
الوثبة
```

### مثال 6 | Example 6
**قبل (Before):**
```
مدينة خليفة, مدينة خليفة أ - شارع 12 - مبنى 45
```
**بعد (After):**
```
مدينة خليفة
```

## المناطق الشائعة | Common Areas

الأسماء المبسطة تتطابق مع أسماء المناطق المعروفة:

Simplified names match known area names:

- **الوثبة جنوب** (Al Wathba South)
- **المصفح** (Musaffah)
- **الشهامة** (Al Shahama)
- **مدينة خليفة** (Khalifa City)
- **الدانة** (Al Dana)
- **الحصن** (Al Hisn)
- **أبو ظبي** (Abu Dhabi)
- **جزيرة أبوظبي** (Abu Dhabi Island)
- **ميناء زايد** (Zayed Port)
- **مدينة الرياض** (Riyadh City)

## التأثير | Impact

### في ملف pet-shops.xlsx
عمود العنوان (Q) الآن يحتوي على أسماء مناطق مبسطة فقط

Column Q (ADDRESS) now contains only simplified area names

### في ملف shops_details.json
حقل `address` الآن يحتوي على اسم المنطقة المبسط فقط

Field `address` now contains only the simplified area name

## الاختبارات | Tests

تم إنشاء اختبارات شاملة للتحقق من صحة التبسيط:

Comprehensive tests have been created to verify the simplification:

### 1. test_area_name_extraction.py
اختبار وظيفة استخراج اسم المنطقة

Tests the area name extraction function

### 2. test_merge_area_simplification.py
اختبار تكاملي لعملية الدمج الكاملة

Integration test for the complete merge process

### نتائج الاختبارات | Test Results
```
✅ 16/16 unit tests passed
✅ 18/18 integration tests passed
```

## استخدام السكريبت | Script Usage

```bash
python3 merge_new_pet_shop_licenses.py
```

السكريبت الآن يقوم تلقائياً بتبسيط أسماء المناطق عند الدمج.

The script now automatically simplifies area names during merge.

## الفوائد | Benefits

✅ **وضوح أكبر** - أسماء المناطق أقصر وأوضح
✅ **توحيد البيانات** - تطابق مع أسماء المناطق في الملف القديم
✅ **سهولة الاستخدام** - لا حاجة للتمرير لقراءة العنوان الكامل
✅ **تنظيم أفضل** - البيانات منظمة ومرتبة

✅ **Better clarity** - Area names are shorter and clearer
✅ **Data consistency** - Matches area names in old file
✅ **Easier to use** - No need to scroll to read full address
✅ **Better organization** - Data is organized and tidy

## الملفات المعدلة | Modified Files

1. **merge_new_pet_shop_licenses.py** - إضافة دالة `extract_area_name()`
2. **test_area_name_extraction.py** - اختبارات الوحدة
3. **test_merge_area_simplification.py** - اختبارات التكامل

1. **merge_new_pet_shop_licenses.py** - Added `extract_area_name()` function
2. **test_area_name_extraction.py** - Unit tests
3. **test_merge_area_simplification.py** - Integration tests

---

**تاريخ التحديث | Update Date:** 2025-10-19  
**المطور | Developer:** د. علي عبدالعال - Ali Abdelaal
