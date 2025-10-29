# تحديث نظام مواقع المحلات على خرائط جوجل
# Google Maps Location System Update

## التحديث - Update

تم تعطيل السكريبتات التي كانت تولد روابط خرائط جوجل تلقائياً من بيانات المحلات. الآن النظام يعتمد **فقط** على روابط خرائط جوجل اليدوية المُضافة مباشرة لكل محل.

The scripts that automatically generated Google Maps links from shop data have been disabled. The system now relies **only** on manual Google Maps links added directly for each shop.

---

## السكريبتات المُعطلة - Disabled Scripts

### 1. `generate_google_maps_links.py` ❌
- **الحالة السابقة**: كان يولد روابط خرائط جوجل تلقائياً بناءً على اسم المحل والعنوان
- **Previous State**: Auto-generated Google Maps links based on shop name and address
- **الحالة الحالية**: مُعطل - يعرض رسالة خطأ عند التشغيل
- **Current State**: Disabled - shows error message when executed

### 2. `standardize_google_maps_links.py` ❌
- **الحالة السابقة**: كان يوحد صيغة روابط خرائط جوجل ويولد روابط جديدة عند الحاجة
- **Previous State**: Standardized Google Maps link format and generated new links when needed
- **الحالة الحالة**: مُعطل - يعرض رسالة خطأ عند التشغيل
- **Current State**: Disabled - shows error message when executed

---

## الطريقة الصحيحة لإضافة مواقع المحلات
## Correct Method to Add Shop Locations

### الخطوات - Steps:

#### 1. افتح خرائط جوجل - Open Google Maps
```
https://maps.google.com
```

#### 2. ابحث عن المحل - Search for the Shop
- استخدم اسم المحل والعنوان الكامل
- Use shop name and full address

#### 3. احصل على رابط الموقع - Get Location Link
**الطريقة الأولى - Method 1: Share Link**
1. اضغط على "مشاركة" أو "Share"
2. اختر "نسخ الرابط" أو "Copy link"
3. استخدم الرابط المنسوخ

**الطريقة الثانية - Method 2: Direct Link**
1. انقر على موقع المحل على الخريطة
2. انسخ الرابط من شريط العنوان
3. الرابط سيكون بصيغة: `https://www.google.com/maps/...`

#### 4. أضف الرابط في النظام - Add Link to System
افتح ملف `shops_details.json` وأضف الرابط في حقل `locationMap`:

Open `shops_details.json` file and add the link in the `locationMap` field:

```json
{
  "اسم المحل": {
    "nameAr": "اسم المحل بالعربي",
    "nameEn": "Shop Name in English",
    "locationMap": "https://www.google.com/maps/place/...",
    "address": "العنوان",
    ...
  }
}
```

---

## أمثلة على صيغ الروابط المقبولة
## Examples of Acceptable Link Formats

### ✅ روابط صحيحة - Valid Links:

```
https://www.google.com/maps/place/Shop+Name/@24.5100,54.3787,17z/...
https://maps.google.com/?q=24.5100,54.3787
https://goo.gl/maps/abcd1234
https://www.google.com/maps/@24.5100632,54.3787346,15z
```

### ❌ روابط غير صحيحة - Invalid Links:

```
(empty string)
"TBD"
"Not available"
"قريباً"
```

---

## التحقق من الروابط - Verify Links

### في Smart Planner - In Smart Planner:
1. افتح `smart-planner.html`
2. اذهب إلى قسم "إدارة المحلات"
3. انقر على أيقونة 🗺️ بجانب اسم المحل
4. تأكد من فتح الموقع الصحيح

### برمجياً - Programmatically:

```python
import json

# تحميل بيانات المحلات
with open('shops_details.json', 'r', encoding='utf-8') as f:
    shops = json.load(f)

# فحص المحلات بدون روابط
missing_links = []
for shop_name, details in shops.items():
    if not details.get('locationMap') or details['locationMap'] == '':
        missing_links.append(shop_name)

print(f"عدد المحلات بدون روابط: {len(missing_links)}")
for shop in missing_links:
    print(f"  - {shop}")
```

---

## الأسئلة الشائعة - FAQ

### س: لماذا تم تعطيل السكريبتات؟
**ج:** لضمان دقة مواقع المحلات. الروابط المولدة تلقائياً قد تكون غير دقيقة، بينما الروابط اليدوية من خرائط جوجل تكون دقيقة 100%.

### Q: Why were the scripts disabled?
**A:** To ensure accuracy of shop locations. Auto-generated links may be inaccurate, while manual Google Maps links are 100% accurate.

---

### س: ماذا لو كان لدي عدد كبير من المحلات؟
**ج:** يمكنك:
1. إضافة الروابط تدريجياً
2. استخدام Google Maps API (يتطلب مفتاح API)
3. الاستعانة بفريق لإدخال البيانات

### Q: What if I have many shops?
**A:** You can:
1. Add links gradually
2. Use Google Maps API (requires API key)
3. Get help from data entry team

---

### س: هل يمكن استخدام إحداثيات GPS مباشرة؟
**ج:** نعم! يمكنك استخدام روابط بصيغة:
```
https://maps.google.com/?q=24.5100,54.3787
```
حيث `24.5100` هي خط العرض و `54.3787` هي خط الطول.

### Q: Can I use GPS coordinates directly?
**A:** Yes! You can use links in format:
```
https://maps.google.com/?q=24.5100,54.3787
```
Where `24.5100` is latitude and `54.3787` is longitude.

---

## ملاحظات مهمة - Important Notes

⚠️ **تحذيرات - Warnings:**
- لا تستخدم السكريبتات المُعطلة
- Don't use the disabled scripts
- تأكد من اختبار كل رابط قبل إضافته
- Test each link before adding it
- احتفظ بنسخة احتياطية من `shops_details.json` قبل التعديل
- Keep a backup of `shops_details.json` before editing

✅ **أفضل الممارسات - Best Practices:**
- استخدم روابط Google Maps الرسمية فقط
- Use official Google Maps links only
- تحقق من دقة الموقع على الخريطة
- Verify location accuracy on the map
- أضف ملاحظات توضيحية للمحلات الصعبة
- Add notes for difficult-to-find shops

---

## الملفات ذات الصلة - Related Files

- ✅ `shops_details.json` - ملف بيانات المحلات الرئيسي (Main shops data file)
- ❌ `generate_google_maps_links.py` - مُعطل (Disabled)
- ❌ `standardize_google_maps_links.py` - مُعطل (Disabled)
- 📖 `GOOGLE_MAPS_IMPLEMENTATION.md` - التوثيق القديم (Old documentation)
- 📖 `GOOGLE_MAPS_MANUAL_LINKS_ONLY.md` - هذا الملف (This file)

---

## تاريخ التحديث - Update History

**تاريخ - Date:** 2025-10-29
**السبب - Reason:** تحسين دقة مواقع المحلات بالاعتماد على روابط يدوية فقط
**Reason:** Improve shop location accuracy by relying on manual links only

---

## الدعم - Support

للمساعدة أو الأسئلة، يرجى مراجعة هذا الملف أو التواصل مع مطور النظام.

For help or questions, please refer to this file or contact the system developer.
