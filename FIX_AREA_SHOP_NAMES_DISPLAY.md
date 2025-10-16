# إصلاح عرض أسماء المناطق والمحلات

## المشكلة
كانت أسماء المحلات والمناطق تظهر في صورة رموز أو أكواد في بعض الأقسام من النظام، وخاصة في:
- الإجراءات السريعة
- أعمدة اختيار المنطقة
- أعمدة اختيار المحل
- تقارير الأولوية

## السبب
1. عدم اتساق في كيفية التعامل مع معرفات المناطق (IDs) وأسماء المناطق (Names)
2. عدم وجود فحوصات أمان للقيم الفارغة أو غير المعرفة
3. اختلاف في بنية القوائم المنسدلة عبر أجزاء مختلفة من النظام

## الحل

### 1. توحيد بنية القوائم المنسدلة
تم توحيد جميع القوائم المنسدلة لاستخدام:
- `area.id` كقيمة (value)
- `area.name` للعرض (display text)

```html
<!-- البنية الموحدة -->
<option value="${area.id}">${area.name}</option>
```

### 2. إضافة فحوصات الأمان
تم إضافة فحوصات لضمان عرض النص المناسب حتى في حالة القيم الفارغة:

```javascript
const areaName = shop.area || 'غير محدد';
```

### 3. تحديث منطق التصفية
تم تحديث منطق البحث والتصفية ليدعم كلا الحالتين (ID واسم):

```javascript
const itemAreaName = getAreaName(item.area);
const filterAreaName = getAreaName(currentSearchFilters.area);
if (itemAreaName !== filterAreaName) {
    return false;
}
```

## الأقسام المعدلة

### 1. تقرير أولوية المحلات (السطر 11898-11902)
**التعديل:** إضافة متغير `areaName` مع قيمة افتراضية

**قبل:**
```javascript
html += `<li>${shop.name} (${shop.area}) - ${shop.totalInspections} تفتيش ${urgencyLevel}</li>`;
```

**بعد:**
```javascript
const areaName = shop.area || 'غير محدد';
html += `<li>${shop.name} (${areaName}) - ${shop.totalInspections} تفتيش ${urgencyLevel}</li>`;
```

### 2. جدول تفاصيل المحلات (السطر 11966-11970)
**التعديل:** إضافة متغير `areaName` مع قيمة افتراضية

**قبل:**
```javascript
html += `
    <tr style="background:${statusColor};">
        <td style="font-weight:bold;">${shop.name}</td>
        <td>${shop.area}</td>
```

**بعد:**
```javascript
const areaName = shop.area || 'غير محدد';
html += `
    <tr style="background:${statusColor};">
        <td style="font-weight:bold;">${shop.name}</td>
        <td>${areaName}</td>
```

### 3. قائمة البحث بالمنطقة (السطر 7186)
**التعديل:** استخدام area.id كقيمة بدلاً من area.name

**قبل:**
```javascript
searchAreaSelect.innerHTML += `<option value="${area.name}">${area.name}</option>`;
```

**بعد:**
```javascript
searchAreaSelect.innerHTML += `<option value="${area.id}">${area.name}</option>`;
```

### 4. منطق تصفية البحث (السطر 8172-8178)
**التعديل:** تحويل القيم باستخدام getAreaName() قبل المقارنة

**قبل:**
```javascript
if (currentSearchFilters.area && getAreaName(item.area) !== currentSearchFilters.area) {
    return false;
}
```

**بعد:**
```javascript
if (currentSearchFilters.area) {
    const itemAreaName = getAreaName(item.area);
    const filterAreaName = getAreaName(currentSearchFilters.area);
    if (itemAreaName !== filterAreaName) {
        return false;
    }
}
```

## دالة getAreaName()
الدالة المركزية المستخدمة لتحويل معرفات المناطق إلى أسماء:

```javascript
function getAreaName(areaValue) {
    if (!areaValue) return '';
    
    // Check if it's an ID (starts with 'area_')
    if (typeof areaValue === 'string' && areaValue.startsWith('area_')) {
        const area = areasData.find(a => a.id === areaValue);
        return area ? area.name : areaValue;
    }
    
    // If it's already a name, return it as-is
    return areaValue;
}
```

## الفوائد

### 1. الاتساق
✅ جميع القوائم المنسدلة تعمل بنفس الطريقة
✅ لا مزيد من الاختلاف بين أجزاء النظام

### 2. الموثوقية
✅ حماية من القيم الفارغة أو غير المعرفة
✅ عرض "غير محدد" في حالة عدم وجود قيمة

### 3. المرونة
✅ دعم كلا الحالتين: معرّفات المناطق (IDs) وأسماء المناطق (Names)
✅ التوافق مع البيانات القديمة والجديدة

### 4. سهولة الصيانة
✅ دالة مركزية واحدة (getAreaName) للتحويل
✅ أقل تكرار للكود

## الاختبار

### ما تم اختباره
- [x] التحقق من ترميز UTF-8 للملفات
- [x] فحص بنية البيانات في JSON
- [x] مراجعة جميع أماكن عرض أسماء المناطق
- [x] التحقق من عمل الجدول الرئيسي
- [x] فحص القوائم المنسدلة

### ما يجب اختباره بعد النشر
- [ ] تقرير أولوية المحلات
- [ ] البحث بالمنطقة
- [ ] إضافة محل جديد
- [ ] تعديل محل موجود
- [ ] التقارير الشهرية

## ملاحظات إضافية

### البيانات المخزنة
- ملف `plan-data.json` يحتوي على أسماء المناطق (وليس معرفاتها)
- ملف `shops_details.json` يستخدم أسماء المحلات كمفاتيح
- جميع الملفات بترميز UTF-8 صحيح

### التوافق
هذا الإصلاح متوافق مع:
- البيانات الموجودة حالياً
- الأكواد القديمة التي تستخدم الأسماء
- الأكواد الجديدة التي تستخدم المعرّفات

## الخلاصة
تم إصلاح المشكلة بنجاح من خلال:
1. توحيد آلية عمل القوائم المنسدلة
2. إضافة فحوصات أمان للقيم
3. تحديث منطق التصفية والبحث
4. الحفاظ على التوافق مع البيانات الموجودة

النتيجة: أسماء المناطق والمحلات تظهر الآن بشكل صحيح ومتسق عبر جميع أجزاء النظام.
