# نظام الأولوية العالية جداً من 15 الشهر
## Very High Priority System from 15th of Month

### نظرة عامة / Overview

تم تطوير نظام جديد لتعزيز أولوية المحلات من اليوم 15 من كل شهر وحتى نهاية الشهر، لضمان تفتيش المحلات ذات الأولوية العالية قبل نهاية الشهر.

A new system has been developed to boost shop priority from the 15th of each month until the end of the month, ensuring high-priority shops are inspected before month-end.

---

### كيف يعمل النظام / How It Works

#### 📅 من 1-14 من الشهر (النصف الأول)
**النظام المرن العادي:**
- **أولوية عالية** (High): النقاط >= 80
- **أولوية متوسطة** (Medium): النقاط >= 50
- **أولوية منخفضة** (Low): النقاط < 50

#### 🎯 من 15-نهاية الشهر (النصف الثاني)
**النظام المحسّن مع الأولوية العالية جداً:**
- **أولوية عالية جداً** (Very High): النقاط >= 130
  - المحلات التي لم يتم تفتيشها من قبل
  - المحلات التي مر على آخر تفتيش لها أكثر من 30 يوم
  - يتم إضافة 50 نقطة للمحلات ذات النقاط >= 80
- **أولوية عالية** (High): النقاط >= 80
  - المحلات التي مر على آخر تفتيش لها 21-30 يوم
  - يتم إضافة 20 نقطة للمحلات ذات النقاط >= 50
- **أولوية متوسطة** (Medium): النقاط >= 50
- **أولوية منخفضة** (Low): النقاط < 50

---

### التغييرات التقنية / Technical Changes

#### 1. دالة حساب الأولوية / Priority Calculation Function

تم تحديث دالة `calculateShopPriority` في كل من:
- `smart-planner.html`
- `index.html`

**المنطق الجديد:**
```javascript
// Check if we're in the second half of the month (from 15th onwards)
const targetDate = new Date(date);
const dayOfMonth = targetDate.getDate();

if (dayOfMonth >= 15) {
    // From the 15th onwards, boost high priority shops to "very high"
    if (score >= 80) {
        score += 50; // Boost very high priority shops even more
        reasons.push('أولوية النصف الثاني من الشهر');
    } else if (score >= 50) {
        score += 20; // Moderate boost for medium priority
    }
}

// Determine priority level
let level = 'low';
if (score >= 130) level = 'very-high'; // Very high priority (from 15th onwards)
else if (score >= 80) level = 'high';
else if (score >= 50) level = 'medium';
```

#### 2. تصميم CSS / CSS Styling

**أنماط جديدة للأولوية العالية جداً:**
```css
.shop-card.very-high-priority {
    border-left: 5px solid #8b0000;
    background: linear-gradient(135deg, #fff5f5 0%, #ffe0e0 100%);
}

.priority-badge.very-high {
    background: #8b0000;
    color: white;
    animation: pulse 1.5s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.8; }
}
```

#### 3. النصوص / Text Labels

تم إضافة النص العربي للأولوية العالية جداً:
```javascript
priorityBadge.textContent = shop.priority === 'very-high' ? 'أولوية عالية جداً' :
                            shop.priority === 'high' ? 'أولوية عالية' : 
                            shop.priority === 'medium' ? 'أولوية متوسطة' : 'أولوية منخفضة';
```

---

### أمثلة / Examples

#### مثال 1: محل لم يتم تفتيشه من قبل
**قبل 15 الشهر (10 أكتوبر):**
- النقاط: 100
- الأولوية: عالية

**بعد 15 الشهر (19 أكتوبر):**
- النقاط: 150 (100 + 50)
- الأولوية: عالية جداً ⭐
- السبب: "لم يتم تفتيشه من قبل - أولوية النصف الثاني من الشهر"

#### مثال 2: محل آخر تفتيش 35 يوم
**قبل 15 الشهر:**
- النقاط: 80
- الأولوية: عالية

**بعد 15 الشهر:**
- النقاط: 130 (80 + 50)
- الأولوية: عالية جداً ⭐
- السبب: "آخر تفتيش قبل 35 يوم - أولوية النصف الثاني من الشهر"

#### مثال 3: محل آخر تفتيش 25 يوم
**قبل 15 الشهر:**
- النقاط: 60
- الأولوية: متوسطة

**بعد 15 الشهر:**
- النقاط: 80 (60 + 20)
- الأولوية: عالية (تم ترقيتها من متوسطة)

---

### الاختبار / Testing

تم إنشاء ملف اختبار شامل: `test_priority_logic.py`

**نتائج الاختبار:**
```
✅ Test 1 Passed: Never inspected on 10th = high (score: 100)
✅ Test 2 Passed: Never inspected on 15th = very-high (score: 150)
✅ Test 3 Passed: 35 days ago on 20th = very-high (score: 130)
✅ Test 4 Passed: 14th of month (no boost) = high (score: 100)
✅ Test 5 Passed: 15th of month (with boost) = very-high (score: 150)
✅ Test 6 Passed: First day of new month = high (score: 100) - rotation complete
```

---

### الفوائد / Benefits

1. ✅ **تحسين التخطيط**: يتم التركيز على المحلات الأكثر أهمية في النصف الثاني من الشهر
2. ✅ **الشفافية**: يعرف المفتشون بوضوح أي المحلات لها الأولوية
3. ✅ **الدورة الشهرية**: يتم إعادة تعيين الأولويات في بداية كل شهر جديد
4. ✅ **المرونة**: النظام الذكي يعمل بشكل طبيعي في النصف الأول من الشهر
5. ✅ **التأكيد البصري**: تصميم مميز باللون الأحمر الداكن والحركة النابضة

---

### الملفات المعدلة / Modified Files

1. **smart-planner.html** - أداة التخطيط الذكي
2. **index.html** - الصفحة الرئيسية
3. **test_priority_logic.py** - اختبارات شاملة
4. **test_very_high_priority.html** - صفحة اختبار تفاعلية

---

### لقطات الشاشة / Screenshots

#### قبل 15 الشهر (النظام العادي)
![Before 15th](https://github.com/user-attachments/assets/c6c9b5dd-cb17-47f9-8d10-a37826ceb04e)

#### بعد 15 الشهر (الأولوية العالية جداً)
![After 15th](https://github.com/user-attachments/assets/60d2d40c-e347-4d9e-9f3c-12485fb6c5af)

---

### الخلاصة / Summary

تم تطبيق نظام الأولوية العالية جداً بنجاح، مما يضمن:
- عرض المحلات ذات الأولوية العالية جداً أولاً من 15 كل شهر
- التركيز على تفتيش هذه المحلات قبل نهاية الشهر
- بداية دورة جديدة في أول كل شهر
- نظام مرن وذكي يتكيف مع احتياجات التفتيش

The very high priority system has been successfully implemented, ensuring:
- Very high priority shops appear first from the 15th of each month
- Focus on inspecting these shops before month-end
- New cycle starts at the beginning of each month
- Flexible and smart system that adapts to inspection needs
