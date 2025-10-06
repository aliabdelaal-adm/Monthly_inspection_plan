# تحسين عرض اختيار المحلات - قائمة منسدلة مخصصة
## Custom Dropdown for Shop Selection - Feature Documentation

---

## 📋 نظرة عامة / Overview

تم تطوير قائمة منسدلة مخصصة لاختيار المحلات في نموذج تخطيط التفتيش، تحل مشكلة عدم ظهور المحلات بوضوح في شاشة الويندوز بسبب قيود عنصر `<select multiple>` التقليدي.

A custom dropdown has been developed for selecting shops in the inspection planning form, solving the issue of shops not displaying clearly on Windows screens due to the limitations of the traditional `<select multiple>` element.

---

## ❌ المشكلة الأصلية / Original Problem

### بالعربية:
في شاشة الويندوز، عند تخطيط تفتيش جديد من لوحة المطور، كانت المحلات لا تظهر جيداً بسبب:
- المحلات محصورة داخل حدود مربع `<select multiple>` 
- عدم القدرة على رؤية جميع المحلات في نفس الوقت
- القائمة لا تتجاوز حدود الحاوية (container)
- صعوبة اختيار المحلات خاصة عند وجود قائمة طويلة

### In English:
On Windows screens, when planning a new inspection from the developer panel, shops weren't displaying well due to:
- Shops confined within the boundaries of a `<select multiple>` box
- Inability to see all shops at once
- List doesn't overflow the container boundaries
- Difficulty selecting shops especially with long lists

---

## ✅ الحل المطبق / Solution Implemented

### القائمة المنسدلة المخصصة / Custom Dropdown

تم استبدال `<select multiple>` بقائمة منسدلة مخصصة تتميز بـ:

**الخصائص التقنية:**
- `position: fixed` - تظهر خارج حدود أي حاوية
- `z-index: 10000` - تظهر فوق جميع العناصر الأخرى
- `max-height: 400px` - ارتفاع مناسب مع إمكانية التمرير
- `min-width: 350px, max-width: 600px` - عرض مرن

**Technical Properties:**
- `position: fixed` - Appears outside any container boundaries
- `z-index: 10000` - Displays above all other elements
- `max-height: 400px` - Appropriate height with scrolling
- `min-width: 350px, max-width: 600px` - Flexible width

---

## 🎨 الميزات الرئيسية / Key Features

### 1. الزر الرئيسي (Trigger) / Main Button

**يعرض:**
- "اختر المحلات" - عند عدم وجود اختيار
- "اسم المحل" - عند اختيار محل واحد
- "X محل محدد" - عند اختيار عدة محلات

**Displays:**
- "Select Shops" - When no selection
- "Shop Name" - When one shop selected
- "X Shops Selected" - When multiple shops selected

**التصميم:**
- خلفية رمادية فاتحة (#f8f9fa)
- حدود زرقاء (2px solid #007bff)
- يتحول للون أزرق فاتح عند التمرير
- أيقونة سهم للأسفل (▼)

---

### 2. القائمة المنسدلة / Dropdown Menu

**المكونات:**

#### أ. مربع البحث / Search Box
```
🔍 ابحث عن محل...
```
- بحث فوري في أسماء المحلات
- تصفية تلقائية للنتائج
- يخفي المجموعات التي لا تحتوي على نتائج

**Features:**
- Instant search in shop names
- Automatic filtering of results
- Hides groups with no results

---

#### ب. قائمة المحلات / Shops List

**التجميع:**
1. **محلات المنطقة المحددة** (بالخط العريض)
   - محلات المنطقة المختارة في الأعلى
   - تسمية واضحة: "محلات [المنطقة] (المنطقة المحددة)"

2. **محلات من مناطق أخرى** (اختياري)
   - بقية المحلات مجمعة
   - مع ذكر اسم المنطقة بين قوسين

**Grouping:**
1. **Selected Area Shops** (Bold)
   - Shops from selected area at the top
   - Clear label: "Shops of [Area] (Selected Area)"

2. **Shops from Other Areas** (Optional)
   - Remaining shops grouped
   - With area name in parentheses

---

#### ج. عرض المحلات / Shops Display

**للمحل غير المحدد:**
- خلفية بيضاء
- حد رمادي فاتح
- يتحول للون أزرق فاتح عند التمرير

**للمحل المحدد:**
- خلفية زرقاء متدرجة (gradient)
- نص أبيض
- خط عريض (font-weight: 600)
- علامة ✓ بجانب الاسم

**For Unselected Shop:**
- White background
- Light gray border
- Turns light blue on hover

**For Selected Shop:**
- Blue gradient background
- White text
- Bold font
- ✓ checkmark next to name

---

#### د. أزرار التحكم / Control Buttons

**في الأسفل:**
1. **اختر الكل** (Select All) - أزرق سماوي (#17a2b8)
   - يختار جميع المحلات الظاهرة (بعد البحث)

2. **مسح** (Clear) - رمادي (#6c757d)
   - يلغي جميع الاختيارات

3. **تم ✓** (Done) - أخضر (#28a745)
   - يغلق القائمة المنسدلة
   - يحفظ الاختيارات

**At Bottom:**
1. **Select All** - Cyan (#17a2b8)
   - Selects all visible shops (after search)

2. **Clear** - Gray (#6c757d)
   - Clears all selections

3. **Done ✓** - Green (#28a745)
   - Closes dropdown
   - Saves selections

---

### 3. العداد / Counter

**موقع:** أسفل الزر الرئيسي
**يعرض:** "X محل" بشكل ديناميكي
**الألوان:**
- أزرق (#007bff) - عند 0 محل
- أخضر (#28a745) - عند اختيار محل أو أكثر

**Location:** Below main button
**Displays:** "X Shop(s)" dynamically
**Colors:**
- Blue (#007bff) - At 0 shops
- Green (#28a745) - When shops selected

---

## 💻 التفاصيل التقنية / Technical Details

### ملفات معدلة / Modified Files

| الملف / File | التغييرات / Changes |
|-------------|---------------------|
| `index.html` | +544 lines, -58 lines |

### أقسام الكود المضافة / Code Sections Added

#### 1. CSS (حوالي 180 سطر / ~180 lines)

**أ. تنسيق الزر الرئيسي:**
```css
.custom-shops-dropdown
.custom-shops-trigger
.custom-shops-trigger-text
.custom-shops-trigger-icon
```

**ب. تنسيق القائمة المنسدلة:**
```css
.custom-shops-dropdown-menu
.custom-shops-search
.custom-shops-group
.custom-shops-group-label
.custom-shops-option
.custom-shops-dropdown-footer
```

**ج. أنماط الأزرار:**
```css
.custom-shops-select-all
.custom-shops-clear
.custom-shops-close
```

---

#### 2. HTML Structure

**قبل / Before:**
```html
<select id="formShops" multiple style="..." required>
    <option value="">اختر المحلات</option>
</select>
```

**بعد / After:**
```html
<div class="custom-shops-dropdown">
    <div class="custom-shops-trigger" id="customShopsTrigger">
        <span class="custom-shops-trigger-text">اختر المحلات</span>
        <span class="custom-shops-trigger-icon">▼</span>
    </div>
    
    <div class="custom-shops-dropdown-menu" id="customShopsDropdownMenu">
        <!-- Search box -->
        <div class="custom-shops-search">
            <input type="text" id="customShopsSearch" placeholder="🔍 ابحث عن محل...">
        </div>
        
        <!-- Shops content -->
        <div id="customShopsContent">
            <!-- Populated dynamically -->
        </div>
        
        <!-- Footer buttons -->
        <div class="custom-shops-dropdown-footer">
            <button type="button" class="custom-shops-select-all">اختر الكل</button>
            <button type="button" class="custom-shops-clear">مسح</button>
            <button type="button" class="custom-shops-close">تم ✓</button>
        </div>
    </div>
</div>

<!-- Hidden select for form submission -->
<select id="formShops" multiple style="display:none;" required>
</select>
```

---

#### 3. JavaScript Functions (حوالي 300+ سطر / ~300+ lines)

**أ. متغيرات جديدة:**
```javascript
let customSelectedShops = []; // Array to track selected shops
```

**ب. دوال جديدة:**

| الدالة / Function | الوصف / Description |
|------------------|---------------------|
| `toggleShopSelection(shopName, element)` | تبديل اختيار محل معين |
| `syncCustomSelectionToHiddenSelect()` | مزامنة الاختيارات مع select المخفي |
| `updateCustomTriggerText()` | تحديث نص الزر الرئيسي |
| `toggleCustomShopsDropdown()` | فتح/إغلاق القائمة |
| `openCustomShopsDropdown()` | فتح القائمة وتحديد موقعها |
| `closeCustomShopsDropdown()` | إغلاق القائمة والتنظيف |
| `filterCustomShops(searchTerm)` | تصفية المحلات حسب البحث |
| `customSelectAllShops()` | اختيار جميع المحلات الظاهرة |
| `customClearShopsSelection()` | مسح جميع الاختيارات |

**ج. دوال محدثة:**
```javascript
fillShopsDropdowns() // Updated to populate custom dropdown
editPlan() // Updated to restore selections
resetFormToggles() // Updated to clear custom dropdown
```

---

## 🔄 سير العمل / Workflow

### 1. فتح القائمة / Opening Dropdown

```
المستخدم ينقر على الزر ← toggleCustomShopsDropdown()
                    ↓
           openCustomShopsDropdown()
                    ↓
          حساب موقع الزر (getBoundingClientRect)
                    ↓
          تحديد موقع القائمة (position: fixed)
                    ↓
          عرض القائمة (show class)
                    ↓
          تركيز على مربع البحث
```

---

### 2. اختيار محل / Selecting Shop

```
المستخدم ينقر على محل ← toggleShopSelection(shopName, element)
                        ↓
          هل المحل محدد؟ ← نعم → إزالة من customSelectedShops
               ↓ لا              ↓ إزالة class "selected"
          إضافة إلى customSelectedShops
               ↓
          إضافة class "selected"
               ↓
          syncCustomSelectionToHiddenSelect()
               ↓
          updateSelectedShopsCount()
               ↓
          updateCustomTriggerText()
```

---

### 3. البحث / Searching

```
المستخدم يكتب في مربع البحث ← filterCustomShops(searchTerm)
                              ↓
                  تحويل النص لحروف صغيرة
                              ↓
              لكل محل: هل الاسم يحتوي على النص؟
                   ↓ نعم          ↓ لا
              عرض المحل      إخفاء المحل
                              ↓
              إخفاء المجموعات الفارغة
```

---

### 4. إغلاق القائمة / Closing Dropdown

```
المستخدم ينقر "تم ✓" أو خارج القائمة ← closeCustomShopsDropdown()
                                        ↓
                              إزالة class "show"
                                        ↓
                              مسح مربع البحث
                                        ↓
                    استعادة جميع المحلات (filterCustomShops(''))
```

---

### 5. إرسال النموذج / Form Submission

```
المستخدم ينقر "إضافة/تعديل" ← النموذج يقرأ من formShops
                             ↓
                   customSelectedShops محفوظة في
                   formShops options (selected)
                             ↓
                      يتم إرسال البيانات بشكل طبيعي
```

---

## 🧪 الاختبار / Testing

### السيناريوهات المختبرة / Tested Scenarios

| السيناريو / Scenario | النتيجة / Result |
|---------------------|-----------------|
| فتح القائمة المنسدلة | ✅ تظهر خارج حدود النموذج |
| اختيار محل واحد | ✅ يظهر اسم المحل في الزر |
| اختيار عدة محلات | ✅ يظهر "X محل محدد" |
| البحث عن محل | ✅ تصفية فورية وصحيحة |
| اختيار جميع المحلات | ✅ جميع المحلات الظاهرة محددة |
| مسح الاختيارات | ✅ جميع الاختيارات ملغاة |
| إغلاق القائمة | ✅ الاختيارات محفوظة |
| إرسال النموذج | ✅ البيانات مرسلة بشكل صحيح |
| تعديل خطة موجودة | ✅ الاختيارات مستعادة |
| التمرير في القائمة | ✅ التمرير سلس ومريح |

---

## 📱 التوافق / Compatibility

### المتصفحات / Browsers

| المتصفح / Browser | الإصدار / Version | الحالة / Status |
|------------------|------------------|----------------|
| Google Chrome | Latest | ✅ مختبر |
| Mozilla Firefox | Latest | ✅ مختبر |
| Microsoft Edge | Latest | ✅ مختبر |
| Safari | Latest | ✅ متوافق |

### الأنظمة / Operating Systems

- ✅ Windows 10/11
- ✅ macOS
- ✅ Linux

---

## 🎯 الفوائد / Benefits

### للمستخدم / For Users

1. **رؤية واضحة** - جميع المحلات مرئية بوضوح
2. **سهولة الاختيار** - نقرة واحدة لاختيار أي محل
3. **بحث سريع** - العثور على المحل المطلوب بسرعة
4. **اختيار مرن** - إمكانية اختيار أي عدد من المحلات
5. **تجربة محسنة** - واجهة عصرية وسهلة الاستخدام

**Clear Visibility** - All shops clearly visible
**Easy Selection** - One click to select any shop
**Quick Search** - Find desired shop quickly
**Flexible Selection** - Can select any number of shops
**Improved Experience** - Modern and user-friendly interface

---

### للمطورين / For Developers

1. **كود منظم** - دوال واضحة ومنفصلة
2. **سهولة الصيانة** - تعديلات بسيطة ومباشرة
3. **توافق خلفي** - يعمل مع النموذج الموجود
4. **قابلية التوسع** - يمكن إضافة ميزات جديدة بسهولة
5. **أداء جيد** - لا يؤثر على سرعة التطبيق

**Organized Code** - Clear and separated functions
**Easy Maintenance** - Simple and direct modifications
**Backward Compatible** - Works with existing form
**Extensible** - Easy to add new features
**Good Performance** - Doesn't affect app speed

---

## 🔧 التخصيص / Customization

### تغيير الألوان / Change Colors

```css
/* الزر الرئيسي / Main Button */
.custom-shops-trigger {
    background: #YOUR_COLOR;
    border-color: #YOUR_BORDER_COLOR;
}

/* المحل المحدد / Selected Shop */
.custom-shops-option.selected {
    background: linear-gradient(135deg, #COLOR1 0%, #COLOR2 100%);
}
```

---

### تغيير الأحجام / Change Sizes

```css
/* عرض القائمة / Dropdown Width */
.custom-shops-dropdown-menu {
    min-width: 350px; /* غير هذه القيمة / Change this value */
    max-width: 600px; /* غير هذه القيمة / Change this value */
}

/* ارتفاع القائمة / Dropdown Height */
.custom-shops-dropdown-menu {
    max-height: 400px; /* غير هذه القيمة / Change this value */
}
```

---

### تغيير السلوك / Change Behavior

```javascript
// فتح القائمة تلقائياً عند اختيار منطقة
// Auto-open dropdown when area selected
document.getElementById('formArea').addEventListener('change', function() {
    openCustomShopsDropdown();
});

// إغلاق القائمة بعد اختيار محل واحد
// Close dropdown after selecting one shop
function toggleShopSelection(shopName, optionElement) {
    // ... existing code ...
    
    if (customSelectedShops.length === 1) {
        closeCustomShopsDropdown();
    }
}
```

---

## 📊 الإحصائيات / Statistics

### حجم الكود / Code Size

| المكون / Component | الحجم / Size |
|-------------------|-------------|
| CSS | ~180 lines |
| JavaScript | ~300+ lines |
| HTML | ~30 lines |
| **الإجمالي / Total** | **~510 lines** |

### التغييرات في الملفات / File Changes

```
index.html: +544 lines, -58 lines
```

---

## 🚀 المستقبل / Future Enhancements

### ميزات محتملة / Potential Features

1. **التحديد الجماعي حسب المنطقة**
   - إمكانية تحديد جميع محلات منطقة معينة بنقرة واحدة
   
2. **الذاكرة المؤقتة**
   - حفظ آخر اختيارات المستخدم

3. **الاختصارات**
   - استخدام لوحة المفاتيح للتنقل والاختيار

4. **الإحصائيات**
   - عرض عدد المحلات في كل منطقة

5. **التصدير**
   - تصدير قائمة المحلات المختارة

**Bulk Selection by Area**
- Select all shops in a specific area with one click

**Cache**
- Save user's last selections

**Keyboard Shortcuts**
- Use keyboard for navigation and selection

**Statistics**
- Show shop count per area

**Export**
- Export selected shops list

---

## 📞 الدعم / Support

### للمساعدة / For Help

إذا واجهت أي مشكلة أو لديك اقتراح:
1. تأكد من تحديث الصفحة (F5 أو Ctrl+R)
2. امسح ذاكرة التخزين المؤقت للمتصفح
3. تحقق من console المتصفح للأخطاء
4. راجع التوثيق أعلاه

If you encounter any issues or have suggestions:
1. Refresh the page (F5 or Ctrl+R)
2. Clear browser cache
3. Check browser console for errors
4. Review documentation above

---

## ✍️ المطور / Developer

**د. علي عبدالعال / Dr. Ali Abdelaal**
- GitHub: [@aliabdelaal-adm](https://github.com/aliabdelaal-adm)
- Repository: [Monthly_inspection_plan](https://github.com/aliabdelaal-adm/Monthly_inspection_plan)

---

## 📅 التاريخ / Date

**تاريخ التطوير:** 2025-10-06
**Development Date:** October 6, 2025

---

## 📄 الترخيص / License

هذا المشروع جزء من نظام خطة التفتيش الشهرية.

This project is part of the Monthly Inspection Plan system.

---

**✅ الميزة مكتملة وجاهزة للاستخدام / Feature Complete and Ready for Use**

🎉 **تم بنجاح / Successfully Implemented** 🎉
