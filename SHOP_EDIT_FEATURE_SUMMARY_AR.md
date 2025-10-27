# تفعيل التعديل الشامل للمحلات في Smart Planner و Admin Dashboard

## المشكلة الأساسية

كان المطور يواجه صعوبة في تعديل بيانات المحلات في نظام التخطيط الشهري:

1. **في admin-dashboard.html (إدارة المحلات الكاملة)**:
   - وظيفة `editShop()` كانت تعدل اسم المحل فقط عبر نافذة prompt بسيطة
   - لا توجد إمكانية لتعديل التفاصيل الأخرى مثل الترخيص، العنوان، الهاتف، إلخ

2. **في smart-planner.html (قائمة المحلات الذكية)**:
   - وظيفة `editShopFromSmartList()` كانت تطلب إدخال أرقام الحقول (1-9)
   - طريقة غير احترافية ومعقدة للمستخدم
   - تتطلب عدة خطوات لتعديل حقل واحد

## الحل المطبق

### 1. التعديلات في smart-planner.html

#### أ. استبدال وظيفة editShopFromSmartList
```javascript
// الكود القديم (تم استبداله)
function editShopFromSmartList(shopName) {
    // كان يطلب إدخال رقم الحقل (1-9)
    const choice = prompt('أدخل رقم الحقل للتعديل (1-9) أو 0 للحفظ:');
    // ...
}

// الكود الجديد
function editShopFromSmartList(shopName) {
    // يبحث عن المحل في قاعدة البيانات
    const planShop = planData.shops.find(s => s.name === shopName);
    if (!planShop) {
        alert('❌ لم يتم العثور على المحل في قاعدة البيانات');
        return;
    }
    
    // يفتح النافذة المنبثقة الشاملة الموجودة مسبقاً
    openEditShopModal(planShop.id);
}
```

**الفوائد**:
- إعادة استخدام النافذة المنبثقة الموجودة (لا تكرار للكود)
- واجهة احترافية مع جميع الحقول ظاهرة
- سهولة في الاستخدام

#### ب. تحسين وظيفة saveShop
```javascript
// إضافة تحديث قائمة المحلات الذكية بعد الحفظ
setTimeout(() => {
    closeShopModal();
    displayShopsList();
    populateAreas();
    // تحديث قائمة المحلات الذكية فقط إذا كانت مفتوحة
    const smartShopModal = document.getElementById('smartShopListModal');
    if (smartShopModal && smartShopModal.style.display === 'block') {
        updateSmartShopList();
    }
}, 1500);
```

**الفوائد**:
- تحديث تلقائي للقوائم بعد الحفظ
- تحسين الأداء بتحديث القائمة فقط عند الحاجة

### 2. التعديلات في admin-dashboard.html

#### أ. إضافة نافذة منبثقة شاملة لتعديل المحلات

تم إضافة modal جديد بعد modal التوكن:

```html
<div id="shopEditModal" class="modal">
    <div class="modal-content" style="max-width: 800px; max-height: 90vh; overflow-y: auto;">
        <!-- رأس النافذة -->
        <div class="modal-header">
            <h3 class="modal-title">✏️ تعديل بيانات المحل</h3>
            <button class="modal-close" onclick="closeShopEditModal()">...</button>
        </div>
        
        <!-- محتوى النافذة -->
        <div class="modal-body">
            <!-- الحقول الإجبارية -->
            <div style="background: #f8f9fa; ...">
                <h4>📋 المعلومات الأساسية (إجبارية)</h4>
                <input id="shopEditName" ... />
                <select id="shopEditArea">...</select>
            </div>
            
            <!-- الحقول الاختيارية -->
            <div style="background: #e8f4f8; ...">
                <h4>📝 التفاصيل الإضافية (اختيارية)</h4>
                <input id="shopEditNameEn" ... />
                <input id="shopEditLicense" ... />
                <input id="shopEditAddress" ... />
                <input id="shopEditPhone" ... />
                <input id="shopEditEmail" ... />
                <input id="shopEditGoogleMaps" ... />
                <textarea id="shopEditActivity" ...></textarea>
                <input id="shopEditAdmCode" ... />
            </div>
        </div>
        
        <!-- أزرار الحفظ والإلغاء -->
        <div class="modal-footer">
            <button onclick="saveShopEdit()">💾 حفظ فوراً</button>
            <button onclick="closeShopEditModal()">✕ إلغاء</button>
        </div>
    </div>
</div>
```

#### ب. استبدال وظيفة editShop

```javascript
// الكود القديم (تم استبداله)
function editShop(oldName) {
    const newName = prompt(`تعديل اسم المحل:...`);
    // كان يعدل الاسم فقط
}

// الكود الجديد
async function editShop(shopName) {
    // التحقق من تحميل البيانات
    if (!planData || !planData.shops) {
        alert('⚠️ لم يتم تحميل البيانات بعد!');
        return;
    }
    
    // البحث عن المحل
    const shop = planData.shops.find(s => s.name === shopName);
    if (!shop) {
        alert('❌ لم يتم العثور على المحل');
        return;
    }
    
    // تعبئة الحقول الأساسية
    document.getElementById('shopEditName').value = shop.name;
    // تعبئة قائمة المناطق...
    
    // تحميل التفاصيل الإضافية من shops_details.json
    const response = await fetch('shops_details.json?...');
    const shopsDetails = await response.json();
    const details = shopsDetails[shopName];
    
    if (details) {
        // تعبئة جميع الحقول الاختيارية
        document.getElementById('shopEditNameEn').value = details.nameEn || '';
        document.getElementById('shopEditLicense').value = details.licenseNo || '';
        // ... إلخ
    }
    
    // إظهار النافذة المنبثقة
    document.getElementById('shopEditModal').classList.add('show');
}
```

#### ج. إضافة وظيفة saveShopEdit

```javascript
async function saveShopEdit() {
    // الحصول على القيم من الحقول
    const originalName = document.getElementById('shopEditOriginalName').value;
    const newName = document.getElementById('shopEditName').value.trim();
    const areaId = document.getElementById('shopEditArea').value;
    // ... الحقول الاختيارية
    
    // التحقق من الحقول الإجبارية
    if (!newName || !areaId) {
        showMessage('shopEditStatus', 'error', '❌ يرجى ملء الحقول الإجبارية');
        return;
    }
    
    // تحديث المحل في planData
    const shopIndex = planData.shops.findIndex(s => s.name === originalName);
    if (shopIndex !== -1) {
        planData.shops[shopIndex].name = newName;
        planData.shops[shopIndex].areaId = areaId;
        // ...
    }
    
    // تحديث جميع السجلات التي تحتوي على المحل (في حالة تغيير الاسم)
    if (originalName !== newName) {
        planData.inspectionData.forEach(inspection => {
            if (inspection.shops && Array.isArray(inspection.shops)) {
                const index = inspection.shops.indexOf(originalName);
                if (index !== -1) {
                    inspection.shops[index] = newName;
                }
            }
        });
    }
    
    // حفظ في plan-data.json على GitHub
    await savePlanDataToGitHub(`تحديث محل: ${newName}`);
    
    // حفظ التفاصيل الإضافية في shops_details.json
    if (/* أي حقل اختياري ممتلئ */) {
        await saveShopDetailsToGitHub(originalName, newName, details);
    }
    
    // إغلاق النافذة وتحديث القائمة
    closeShopEditModal();
    loadShopsList();
}
```

#### د. إضافة وظيفة saveShopDetailsToGitHub

```javascript
async function saveShopDetailsToGitHub(oldName, newName, details) {
    // الحصول على محتوى shops_details.json الحالي
    const getRes = await fetch(`https://api.github.com/repos/${repo}/contents/shops_details.json`, {...});
    const file = await getRes.json();
    const currentContent = JSON.parse(decodeURIComponent(escape(atob(file.content))));
    
    // في حالة تغيير الاسم، حذف السجل القديم
    if (oldName !== newName && currentContent[oldName]) {
        delete currentContent[oldName];
    }
    
    // إضافة/تحديث التفاصيل الجديدة (مع حذف الحقول الفارغة)
    const cleanDetails = {};
    if (details.nameAr) cleanDetails.nameAr = details.nameAr;
    if (details.nameEn) cleanDetails.nameEn = details.nameEn;
    // ... إلخ
    
    currentContent[newName] = cleanDetails;
    
    // رفع الملف المحدث إلى GitHub
    const updateRes = await fetch(`https://api.github.com/repos/${repo}/contents/shops_details.json`, {
        method: 'PUT',
        body: JSON.stringify({
            message: `تحديث تفاصيل المحل: ${newName}`,
            content: btoa(unescape(encodeURIComponent(JSON.stringify(currentContent, null, 2)))),
            sha: file.sha
        })
    });
}
```

## الميزات الجديدة

### 1. واجهة احترافية
- نافذة منبثقة منظمة وواضحة
- تقسيم الحقول إلى إجبارية واختيارية
- تصميم جذاب ومريح للعين

### 2. تعديل شامل
يمكن تعديل جميع معلومات المحل دفعة واحدة:
- ✅ الاسم بالعربية
- ✅ الاسم بالإنجليزية
- ✅ المنطقة
- ✅ رقم الترخيص
- ✅ العنوان
- ✅ رقم الهاتف
- ✅ البريد الإلكتروني
- ✅ موقع الخرائط
- ✅ طبيعة النشاط
- ✅ كود ADM

### 3. حفظ تلقائي
- يحفظ المعلومات الأساسية في `plan-data.json`
- يحفظ التفاصيل الإضافية في `shops_details.json`
- يتم الحفظ مباشرة على GitHub
- لا حاجة لخطوات إضافية للمزامنة

### 4. تحديث ذكي
- يحدث جميع السجلات المرتبطة بالمحل عند تغيير الاسم
- يحدث قوائم المحلات تلقائياً بعد الحفظ
- يتحقق من حالة العرض قبل التحديث لتحسين الأداء

## كيفية الاستخدام

### في smart-planner.html

1. افتح `smart-planner.html` في المتصفح
2. سجل دخول بالتوكن المطلوب
3. لتعديل محل من "إدارة المحلات الكاملة":
   - انتقل إلى تبويب "المحلات"
   - اضغط على أيقونة التعديل (✏️) بجانب أي محل
   - ستفتح نافذة منبثقة مع جميع الحقول
4. لتعديل محل من "قائمة المحلات الذكية":
   - انتقل إلى قسم "قائمة المحلات الذكية"
   - اضغط على زر التعديل (✏️) بجانب أي محل
   - ستفتح نفس النافذة المنبثقة الشاملة
5. عدل الحقول المطلوبة
6. اضغط "💾 حفظ فوراً"
7. يتم الحفظ تلقائياً على GitHub

### في admin-dashboard.html

1. افتح `admin-dashboard.html` في المتصفح
2. سجل دخول بالتوكن المطلوب
3. انتقل إلى قسم "إدارة المحلات"
4. اضغط على "تحديث القائمة" لتحميل البيانات
5. اضغط على زر "تعديل" بجانب أي محل
6. ستفتح نافذة منبثقة مع جميع الحقول
7. عدل الحقول المطلوبة
8. اضغط "💾 حفظ فوراً"
9. يتم الحفظ تلقائياً على GitHub وتحديث القائمة

## الملفات المعدلة

1. **smart-planner.html**
   - سطر 11906-11918: استبدال وظيفة `editShopFromSmartList`
   - سطر 4945-4955: تحديث وظيفة `saveShop` لتحديث قائمة المحلات الذكية

2. **admin-dashboard.html**
   - سطر 1472-1588: إضافة modal جديد لتعديل المحلات
   - سطر 2732-3095: استبدال وظيفة `editShop` وإضافة الوظائف المساعدة
   - سطر 2598-2601: إضافة وظيفة `savePlanDataToGitHub` للتوافق

3. **test_shop_edit_functionality.html** (جديد)
   - دليل شامل للاختبار والتحقق من الوظائف الجديدة

## الاختبار

تم إنشاء ملف `test_shop_edit_functionality.html` الذي يحتوي على:
- ملخص شامل للتغييرات
- شرح للميزات الجديدة
- دليل خطوة بخطوة للاختبار
- روابط مباشرة لفتح الواجهات

## الأمان

- ✅ تم التحقق من الكود باستخدام CodeQL - لا توجد مشكلات أمنية
- ✅ يتم التحقق من صلاحيات GitHub Token قبل الحفظ
- ✅ يتم التحقق من وجود البيانات قبل التعديل
- ✅ يتم تنظيف القيم الفارغة قبل الحفظ
- ✅ يتم استخدام نفس نمط الترميز الموجود في الكود الأصلي للتوافق

## الخلاصة

تم حل المشكلة بنجاح! الآن يمكن للمطور تعديل المحلات بسهولة واحترافية في كل من:
- ✅ قائمة المحلات الذكية في smart-planner.html
- ✅ إدارة المحلات الكاملة في smart-planner.html
- ✅ إدارة المحلات في admin-dashboard.html

دون الحاجة إلى:
- ❌ إدخال أرقام الحقول (1-9)
- ❌ خطوات معقدة
- ❌ تعديلات متعددة لحقول مختلفة

مع توفير:
- ✅ واجهة احترافية وسهلة الاستخدام
- ✅ تعديل شامل لجميع الحقول دفعة واحدة
- ✅ حفظ تلقائي على GitHub
- ✅ تحديث فوري للقوائم
