# دليل اختبار إصلاح تعديل المحل
# Shop Edit Fix Testing Guide

## نظرة عامة / Overview

تم إصلاح مشكلتين رئيسيتين في ملف `smart-planner.html`:

Two major issues have been fixed in `smart-planner.html`:

### المشكلة 1 / Issue 1
**الوصف:** عند تعديل محل، كانت تظهر فقط اسم المحل باللغة العربية، بينما باقي التفاصيل (الترخيص، العنوان، الهاتف، إلخ) لا تظهر.

**Description:** When editing a shop, only the Arabic name was displayed, while other details (license, address, phone, etc.) were not shown.

**السبب:** كانت نافذة التعديل تفتح قبل اكتمال تحميل البيانات من `shops_details.json`.

**Root Cause:** The edit modal was opening before data from `shops_details.json` finished loading.

**الحل:** 
- تحويل دالة `openEditShopModal` إلى `async function`
- إظهار رسالة "⏳ جاري تحميل تفاصيل المحل..." أثناء التحميل
- انتظار اكتمال تحميل جميع البيانات قبل السماح بالتعديل
- إظهار رسالة نجاح عند اكتمال التحميل

**Solution:**
- Converted `openEditShopModal` to an `async function`
- Display "⏳ Loading shop details..." message during loading
- Wait for all data to load before allowing edits
- Show success message when loading is complete

### المشكلة 2 / Issue 2
**الوصف:** عند حفظ التعديلات، كان يتم إنشاء محل جديد بدلاً من تحديث المحل الموجود، مما يؤدي إلى تكرار اسم المحل في القائمة.

**Description:** When saving edits, a new shop was created instead of updating the existing one, leading to duplicate shop names in the list.

**السبب:** عدم معالجة الحالة التي يكون فيها `shopId` فارغًا بشكل صحيح.

**Root Cause:** Improper handling of cases where `shopId` is empty.

**الحل:**
- تحسين منطق البحث عن المحل الموجود بالاسم
- إضافة معالجة أخطاء أفضل
- رسائل واضحة تفرق بين "تحديث" و "إضافة" محل

**Solution:**
- Improved logic for finding existing shops by name
- Added better error handling
- Clear messages differentiating between "update" and "add" operations

---

## سيناريوهات الاختبار / Test Scenarios

### السيناريو 1: تعديل محل موجود في plan-data.json و shops_details.json
**Scenario 1: Edit a shop existing in both plan-data.json and shops_details.json**

**الخطوات / Steps:**
1. افتح `smart-planner.html`
2. انتقل إلى تبويب "المحلات"
3. اختر محل موجود (مثل: "جرين لندز")
4. انقر على زر "✏️ تعديل"
5. انتظر رسالة "جاري تحميل تفاصيل المحل..."
6. تحقق من ظهور جميع البيانات:
   - ✅ الاسم بالعربية
   - ✅ الاسم بالإنجليزية
   - ✅ رقم الترخيص
   - ✅ العنوان
   - ✅ رقم الهاتف
   - ✅ البريد الإلكتروني
   - ✅ رابط خرائط جوجل
   - ✅ طبيعة النشاط
   - ✅ رمز ADM
   - ✅ المنطقة
7. عدل أي حقل (مثل: رقم الهاتف)
8. انقر "💾 حفظ فوراً"
9. تحقق من ظهور رسالة "✅ تم تحديث بيانات المحل بنجاح"
10. تأكد من عدم تكرار المحل في القائمة

**النتيجة المتوقعة / Expected Result:**
- جميع الحقول تظهر بشكل صحيح
- التعديلات تُحفظ بنجاح
- لا يوجد تكرار للمحل
- رسالة نجاح واضحة تشير إلى "تحديث" وليس "إضافة"

---

### السيناريو 2: تعديل محل موجود فقط في shops_details.json
**Scenario 2: Edit a shop existing only in shops_details.json**

**الخطوات / Steps:**
1. افتح `smart-planner.html`
2. انتقل إلى تبويب "المحلات"
3. انقر على "📋 عرض قائمة المحلات الكاملة"
4. اختر محل موجود في shops_details.json لكن ليس في plan-data.json
5. انقر على "✏️ تعديل"
6. تحقق من ظهور جميع البيانات من shops_details.json
7. عدل المنطقة أو أي حقل آخر
8. احفظ التعديلات
9. تحقق من الرسالة المناسبة

**النتيجة المتوقعة / Expected Result:**
- البيانات تُحمل بنجاح من shops_details.json
- عند الحفظ لأول مرة، يظهر "تم إضافة المحل بنجاح"
- عند التعديل مرة أخرى، يظهر "تم تحديث بيانات المحل بنجاح"
- لا يتم إنشاء محل مكرر

---

### السيناريو 3: محاولة تعديل محل غير موجود
**Scenario 3: Attempt to edit a non-existent shop**

**الخطوات / Steps:**
1. افتح `smart-planner.html`
2. في console المتصفح، نفذ: `openEditShopModal('محل غير موجود')`
3. تحقق من السلوك

**النتيجة المتوقعة / Expected Result:**
- تظهر رسالة تحذير تشير إلى عدم العثور على المحل
- لا يحدث أخطاء في console

---

## فحص الكود / Code Inspection

### التغييرات الرئيسية / Key Changes

#### في `openEditShopModal`:
```javascript
// OLD: function openEditShopModal(shopIdOrName)
// NEW: async function openEditShopModal(shopIdOrName)

// NEW: Clear fields first
document.getElementById('shopModalNameEn').value = '';
// ... (all optional fields cleared)

// NEW: Show modal with loading message
document.getElementById('shopModal').style.display = 'block';
showMessage('shopModalStatus', 'info', '⏳ جاري تحميل تفاصيل المحل...');

// NEW: Use await instead of .then()
const response = await fetch('shops_details.json?' + new Date().getTime());
const shopsDetails = await response.json();

// NEW: Show success message after loading
showMessage('shopModalStatus', 'success', '✅ تم تحميل جميع تفاصيل المحل بنجاح');
```

#### في `saveShop`:
```javascript
// NEW: Better error handling
if (shopIndex !== -1) {
    // Update logic
    isUpdate = true;
} else {
    // NEW: Error handling for missing shop
    console.error('Shop ID provided but not found:', shopId);
    showMessage('shopModalStatus', 'error', '❌ خطأ: لم يتم العثور على المحل في البيانات');
    return;
}

// NEW: Store new shop ID
planData.shops.push(newShop);
shopId = newShop.id; // Store for reference

// NEW: Differentiated success messages
const successMessage = isUpdate 
    ? '✅ تم تحديث بيانات المحل بنجاح - جميع التفاصيل محفوظة' 
    : '✅ تم إضافة المحل بنجاح - المحل ظاهر الآن في القائمة';
```

---

## قائمة التحقق النهائية / Final Checklist

قبل إغلاق هذا التذكرة، تأكد من:

Before closing this ticket, verify:

- [ ] جميع حقول المحل تظهر بشكل صحيح عند التعديل
- [ ] All shop fields display correctly when editing
- [ ] رسالة "جاري التحميل" تظهر أثناء تحميل البيانات
- [ ] "Loading" message appears during data load
- [ ] رسالة نجاح تظهر بعد اكتمال التحميل
- [ ] Success message appears after loading completes
- [ ] التعديلات تُحفظ بنجاح دون تكرار المحل
- [ ] Edits save successfully without duplicating the shop
- [ ] رسائل مختلفة تظهر للتحديث مقابل الإضافة
- [ ] Different messages for update vs. add operations
- [ ] لا توجد أخطاء في console المتصفح
- [ ] No errors in browser console
- [ ] البيانات تُحفظ في كل من plan-data.json و shops_details.json
- [ ] Data saves to both plan-data.json and shops_details.json

---

## ملاحظات للمطورين / Developer Notes

### البيانات المصدر / Data Sources
- `plan-data.json`: يحتوي على 135 محل مع معلومات أساسية (id, name, area, areaId)
- `shops_details.json`: يحتوي على 291 محل مع تفاصيل كاملة (nameEn, licenseNo, address, contact, email, locationMap, activity, admCode)

### التدفق المنطقي / Logic Flow
1. عند النقر على "تعديل محل"، تبحث الدالة أولاً في `planData.shops`
2. إذا لم يُعثر على المحل، تُنشئ كائن مؤقت
3. تُحمل البيانات الإضافية من `shops_details.json` بشكل متزامن
4. عند الحفظ، تتحقق من وجود المحل بالاسم لمنع التكرار
5. تُحدث البيانات في كلا الملفين

### المناطق الحساسة / Critical Areas
- ⚠️ **لا توليد تلقائي لروابط خرائط جوجل** - يجب إدخالها يدوياً
- ⚠️ **معالجة async/await** - تأكد من انتظار جميع العمليات
- ⚠️ **منع التكرار** - الفحص بالاسم والID

---

## الأسئلة الشائعة / FAQ

**س: لماذا تظهر رسالة "جاري التحميل" حتى للمحلات الموجودة في plan-data.json؟**

ج: لأن التفاصيل الإضافية (مثل رقم الترخيص، العنوان، إلخ) موجودة فقط في shops_details.json ويجب تحميلها.

**Q: Why does the "Loading" message appear even for shops in plan-data.json?**

A: Because additional details (like license number, address, etc.) are stored only in shops_details.json and must be loaded.

---

**س: ماذا يحدث إذا كان المحل موجود في shops_details.json فقط؟**

ج: عند التعديل الأول، يُضاف المحل إلى plan-data.json. التعديلات اللاحقة ستقوم بالتحديث بدلاً من الإضافة.

**Q: What happens if a shop exists only in shops_details.json?**

A: On first edit, it's added to plan-data.json. Subsequent edits will update instead of adding.

---

## التاريخ / History

- **2025-01-24**: إصلاح مشكلة تعديل المحل - عرض جميع البيانات ومنع التكرار
- **2025-01-24**: Fixed shop edit issue - display all data and prevent duplication
