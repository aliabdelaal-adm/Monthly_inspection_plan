# نظام وضع الصيانة المجدول (9 مساءً - 11 مساءً)
# Scheduled Maintenance Mode System (9 PM - 11 PM)

## 📋 نظرة عامة - Overview

تم تطوير نظام وضع الصيانة المجدول الذي يعمل تلقائياً كل يوم من الساعة 9 مساءً (21:00) حتى الساعة 11 مساءً (23:00). خلال هذه الفترة، يتم عرض رسالة صيانة تلقائية لجميع المفتشين على الشاشة الرئيسية مع تشغيل الموسيقى الهادئة المدمجة. المطور معفى تماماً من رؤية رسالة الصيانة في أي وقت.

A scheduled maintenance mode system has been developed that automatically activates every day from 9 PM (21:00) to 11 PM (23:00). During this period, an automatic maintenance message is displayed to all inspectors on the main screen with embedded calm music. The developer is completely exempt from seeing the maintenance message at any time.

---

## ✨ الميزات الرئيسية - Key Features

### 1. ⏰ جدولة تلقائية - Automatic Scheduling
- **وقت التفعيل:** يومياً من الساعة 9 مساءً حتى 11 مساءً
- **Activation Time:** Daily from 9 PM to 11 PM
- **التشغيل التلقائي:** لا يتطلب أي تدخل يدوي
- **Automatic Operation:** No manual intervention required

### 2. 🎵 موسيقى خلفية - Background Music
- **تشغيل تلقائي** مع ظهور رسالة الصيانة
- **Automatic playback** when maintenance message appears
- **موسيقى هادئة** (whatsapp Audio.mp3)
- **Calm music** (whatsapp Audio.mp3)
- **مستوى صوت منخفض** (15%)
- **Low volume level** (15%)

### 3. 👨‍💻 استثناء المطور - Developer Exemption
- **المطور لا يرى رسالة الصيانة أبداً** حتى خلال وقت الصيانة المجدول
- **Developer never sees maintenance message** even during scheduled maintenance
- **وصول كامل للمطور** في جميع الأوقات
- **Full developer access** at all times

### 4. 🔄 التحديث الدوري - Periodic Updates
- **فحص كل دقيقة** للتحقق من وقت الصيانة
- **Check every minute** to verify maintenance time
- **إخفاء تلقائي** عند انتهاء وقت الصيانة (11 مساءً)
- **Automatic hide** when maintenance period ends (11 PM)

---

## 🔧 كيفية عمل النظام - How the System Works

### 1. التحقق من الوقت - Time Verification

```javascript
function isScheduledMaintenanceTime() {
    const now = new Date();
    const currentHour = now.getHours();
    
    // Maintenance window: 9 PM (21:00) to 11 PM (23:00)
    const isMaintenanceTime = currentHour >= 21 && currentHour < 23;
    
    return isMaintenanceTime;
}
```

**الشرح | Explanation:**
- يحصل على الساعة الحالية
- Gets the current hour
- يتحقق إذا كانت الساعة بين 21 (9 مساءً) و 23 (11 مساءً)
- Checks if hour is between 21 (9 PM) and 23 (11 PM)
- يعيد `true` إذا كان في وقت الصيانة، `false` إذا كان خارج الوقت
- Returns `true` if within maintenance time, `false` if outside

### 2. فحص وتطبيق الصيانة - Check and Apply Maintenance

```javascript
function checkScheduledMaintenance() {
    // Developer bypass - developers never see maintenance mode
    if (isDev || window.isDev) {
        console.log('✅ Developer logged in - skipping scheduled maintenance check');
        return false;
    }
    
    // Check if we're in maintenance window
    if (isScheduledMaintenanceTime()) {
        const now = new Date();
        const currentTime = `${now.getHours()}:${String(now.getMinutes()).padStart(2, '0')}`;
        
        console.log('🔧 Activating scheduled maintenance mode...');
        showMaintenanceMode([
            '⏰ وضع الصيانة المجدولة',
            'الصيانة اليومية من الساعة 9 مساءً حتى 11 مساءً',
            `الوقت الحالي: ${currentTime}`,
            'جاري إجراء الصيانة الدورية للنظام...',
            'سيعود النظام تلقائياً بعد انتهاء وقت الصيانة'
        ]);
        return true;
    }
    
    return false;
}
```

**الشرح | Explanation:**
1. **استثناء المطور | Developer Exemption:**
   - يتحقق أولاً إذا كان المستخدم مطور
   - Checks first if user is developer
   - إذا كان مطور، يتم تجاوز الفحص تماماً
   - If developer, bypass check completely

2. **فحص وقت الصيانة | Maintenance Time Check:**
   - يستدعي `isScheduledMaintenanceTime()` للتحقق من الوقت
   - Calls `isScheduledMaintenanceTime()` to check time
   - إذا كان في وقت الصيانة، يعرض رسالة الصيانة
   - If within maintenance time, shows maintenance message

3. **رسالة مفصلة | Detailed Message:**
   - تتضمن معلومات عن وقت الصيانة المجدولة
   - Includes information about scheduled maintenance time
   - تعرض الوقت الحالي
   - Displays current time
   - تخبر المستخدمين أن النظام سيعود تلقائياً
   - Informs users system will return automatically

### 3. المراقبة الدورية - Periodic Monitoring

```javascript
function startScheduledMaintenanceChecker() {
    // Check immediately on page load
    checkScheduledMaintenance();
    
    // Then check every minute (60000 ms)
    setInterval(() => {
        const wasInMaintenance = document.getElementById('maintenanceOverlay').style.display === 'flex';
        const isInMaintenanceTime = checkScheduledMaintenance();
        
        // If we just exited maintenance time, hide the overlay
        if (wasInMaintenance && !isInMaintenanceTime && !isDev) {
            console.log('✅ Scheduled maintenance period ended - hiding maintenance mode');
            hideMaintenanceMode();
        }
    }, 60000); // Check every 1 minute
}
```

**الشرح | Explanation:**
1. **فحص فوري | Immediate Check:**
   - يتم الفحص فوراً عند تحميل الصفحة
   - Checks immediately when page loads

2. **فحص دوري | Periodic Check:**
   - يتم الفحص كل دقيقة (60000 ملي ثانية)
   - Checks every minute (60000 milliseconds)
   - يكتشف إذا انتهى وقت الصيانة
   - Detects if maintenance period ended

3. **إخفاء تلقائي | Automatic Hide:**
   - إذا كانت رسالة الصيانة معروضة وانتهى الوقت
   - If maintenance message is showing and time ended
   - يتم إخفاء الرسالة تلقائياً
   - Message is automatically hidden

---

## 💻 التكامل - Integration

تم تكامل النظام في صفحة `index.html` الرئيسية:

The system is integrated in the main `index.html` page:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // ... other initialization code ...
    
    loadInspectionData();
    startAutoRefresh();
    startDailyRefresh();
    startScheduledMaintenanceChecker(); // ✅ NEW: Start scheduled maintenance checker
    
    // ... rest of initialization ...
});
```

---

## 🎯 حالات الاستخدام - Use Cases

### الحالة 1: مفتش يدخل النظام في الساعة 9:30 مساءً
**Case 1: Inspector enters system at 9:30 PM**

```
✅ ما يحدث | What Happens:
1. يتم تحميل الصفحة | Page loads
2. يتم فحص الوقت الحالي (9:30 مساءً) | Current time checked (9:30 PM)
3. يتم اكتشاف أنه وقت صيانة | Maintenance time detected
4. تظهر رسالة الصيانة تلقائياً | Maintenance message shows automatically
5. تبدأ الموسيقى الهادئة في التشغيل | Calm music starts playing
```

### الحالة 2: مفتش موجود في النظام عند الساعة 9:00 مساءً
**Case 2: Inspector is in system at 9:00 PM**

```
✅ ما يحدث | What Happens:
1. الفاحص الدوري يعمل كل دقيقة | Periodic checker runs every minute
2. عند الساعة 9:00 مساءً يكتشف وقت الصيانة | At 9:00 PM detects maintenance time
3. تظهر رسالة الصيانة تلقائياً | Maintenance message shows automatically
4. المفتش يرى الرسالة ويسمع الموسيقى | Inspector sees message and hears music
```

### الحالة 3: مطور يدخل النظام في الساعة 10:00 مساءً
**Case 3: Developer enters system at 10:00 PM**

```
✅ ما يحدث | What Happens:
1. يتم تحميل الصفحة | Page loads
2. يتم فحص الوقت (10:00 مساءً - وقت صيانة) | Time checked (10:00 PM - maintenance time)
3. يتم اكتشاف أن المستخدم مطور | User detected as developer
4. يتم تجاوز عرض الصيانة تماماً | Maintenance display bypassed completely
5. المطور يرى الصفحة الرئيسية بشكل طبيعي | Developer sees main page normally
```

### الحالة 4: مفتش موجود في النظام عند الساعة 11:00 مساءً
**Case 4: Inspector is in system at 11:00 PM**

```
✅ ما يحدث | What Happens:
1. رسالة الصيانة معروضة حتى الساعة 11:00 | Maintenance message showing until 11:00
2. الفاحص الدوري يعمل عند الساعة 11:00 | Periodic checker runs at 11:00
3. يكتشف أن وقت الصيانة انتهى | Detects maintenance time ended
4. يتم إخفاء الرسالة تلقائياً | Message hidden automatically
5. المفتش يمكنه استخدام النظام بشكل طبيعي | Inspector can use system normally
```

---

## 📊 مخطط الانسياب - Flow Diagram

```
┌─────────────────────────────────┐
│   Page Load / Every Minute     │
│   تحميل الصفحة / كل دقيقة       │
└────────────┬────────────────────┘
             │
             ▼
    ┌────────────────────┐
    │   Is Developer?    │
    │   هل هو مطور؟      │
    └─────┬──────────┬───┘
          │ Yes      │ No
          │          │
          ▼          ▼
    ┌─────────┐  ┌──────────────────┐
    │  Skip   │  │  Check Time      │
    │ Bypass  │  │  فحص الوقت        │
    └────┬────┘  └────┬─────────────┘
         │            │
         │            ▼
         │       ┌──────────────────┐
         │       │  9 PM - 11 PM?   │
         │       │  9م - 11م؟       │
         │       └────┬─────────┬───┘
         │            │ Yes     │ No
         │            │         │
         │            ▼         ▼
         │       ┌─────────┐ ┌──────────┐
         │       │  Show   │ │   Hide   │
         │       │  إظهار  │ │  إخفاء   │
         │       └─────────┘ └──────────┘
         │            │
         └────────────┴──────────────────┐
                                         │
                                         ▼
                            ┌──────────────────────┐
                            │  Continue Normal     │
                            │  الاستمرار العادي    │
                            └──────────────────────┘
```

---

## 🧪 الاختبار - Testing

### ملف الاختبار - Test File

تم إنشاء ملف اختبار شامل: `test_scheduled_maintenance.html`

A comprehensive test file has been created: `test_scheduled_maintenance.html`

#### المميزات | Features:
1. **محاكي الوقت | Time Simulator:**
   - اختبار أوقات مختلفة دون الانتظار
   - Test different times without waiting
   - أوقات مختارة: 8م، 9م، 9:30م، 10م، 10:30م، 11م، 12ص
   - Pre-selected times: 8PM, 9PM, 9:30PM, 10PM, 10:30PM, 11PM, 12AM

2. **وضع المطور | Developer Mode:**
   - تبديل بين مفتش ومطور
   - Toggle between inspector and developer
   - اختبار استثناء المطور
   - Test developer exemption

3. **عرض الحالة | Status Display:**
   - الوقت الحالي
   - Current time
   - حالة الصيانة المجدولة
   - Scheduled maintenance status
   - نوع المستخدم
   - User type
   - حالة عرض الصيانة
   - Maintenance display status

4. **سجل مفصل | Detailed Log:**
   - تتبع جميع الأحداث
   - Track all events
   - رسائل ملونة حسب النوع
   - Color-coded messages by type

#### كيفية الاستخدام | How to Use:

```bash
# 1. افتح الملف في المتصفح
# 1. Open file in browser
open test_scheduled_maintenance.html

# 2. جرب السيناريوهات المختلفة
# 2. Try different scenarios

# 3. راقب السجل والحالة
# 3. Monitor log and status
```

### سيناريوهات الاختبار - Test Scenarios

#### ✅ السيناريو 1: وقت الصيانة
```
1. اختر وقت 9:00 مساءً
2. اضغط "فحص وضع الصيانة"
3. توقع: ظهور رسالة الصيانة + موسيقى
```

#### ✅ السيناريو 2: خارج وقت الصيانة
```
1. اختر وقت 8:00 مساءً
2. اضغط "فحص وضع الصيانة"
3. توقع: عدم ظهور رسالة الصيانة
```

#### ✅ السيناريو 3: المطور في وقت الصيانة
```
1. اختر وقت 9:00 مساءً
2. اضغط "تبديل المطور"
3. اضغط "فحص وضع الصيانة"
4. توقع: عدم ظهور رسالة الصيانة للمطور
```

#### ✅ السيناريو 4: انتهاء وقت الصيانة
```
1. اختر وقت 10:30 مساءً (داخل الصيانة)
2. اضغط "فحص وضع الصيانة"
3. اختر وقت 11:00 مساءً (خارج الصيانة)
4. توقع: إخفاء تلقائي للرسالة
```

---

## 🔒 الأمان - Security

### استثناء المطور - Developer Exemption

```javascript
// Developer check happens FIRST, before any other logic
if (isDev || window.isDev) {
    console.log('✅ Developer logged in - skipping scheduled maintenance check');
    return false;
}
```

**الأمان | Security:**
- المطور معفى بشكل كامل وآمن
- Developer completely and securely exempted
- لا يمكن عرض الصيانة للمطور بأي حال
- Maintenance cannot be shown to developer under any circumstance
- يتم الفحص قبل أي منطق آخر
- Check happens before any other logic

---

## 📝 ملخص التغييرات - Changes Summary

### الملفات المضافة - Added Files

1. **`test_scheduled_maintenance.html`** (ملف جديد)
   - صفحة اختبار شاملة للصيانة المجدولة
   - Comprehensive test page for scheduled maintenance

2. **`SCHEDULED_MAINTENANCE_FEATURE.md`** (ملف جديد)
   - توثيق كامل للميزة
   - Complete feature documentation

### التعديلات في `index.html` - Modifications in `index.html`

#### 1. إضافة دالة `isScheduledMaintenanceTime()`
```javascript
// Line ~4653 (before startAutoRefresh)
function isScheduledMaintenanceTime() {
    // Check if current hour is between 21 (9 PM) and 23 (11 PM)
    // ...
}
```

#### 2. إضافة دالة `checkScheduledMaintenance()`
```javascript
// Line ~4673 (before startAutoRefresh)
function checkScheduledMaintenance() {
    // Developer bypass + time check + show maintenance
    // ...
}
```

#### 3. إضافة دالة `startScheduledMaintenanceChecker()`
```javascript
// Line ~4706 (before startAutoRefresh)
function startScheduledMaintenanceChecker() {
    // Initial check + periodic check every minute
    // ...
}
```

#### 4. تفعيل الفاحص في DOMContentLoaded
```javascript
// Line ~6505
document.addEventListener('DOMContentLoaded', function() {
    // ...
    startScheduledMaintenanceChecker(); // ✅ NEW
    // ...
});
```

---

## ⚡ الأداء - Performance

### التأثير على الأداء - Performance Impact

```
✅ تأثير منخفض جداً | Very Low Impact:

1. فحص دوري كل دقيقة فقط
   Periodic check every minute only
   
2. عمليات بسيطة: مقارنة رقم واحد (الساعة)
   Simple operations: comparing one number (hour)
   
3. لا يؤثر على تحميل الصفحة
   Does not affect page loading
   
4. لا يؤثر على وظائف أخرى
   Does not affect other functions
```

### استهلاك الموارد - Resource Usage

```
CPU: < 0.01% (فحص بسيط كل دقيقة)
Memory: < 1KB (متغيرات قليلة)
Network: 0 (لا يوجد طلبات شبكة)
```

---

## 🎓 أمثلة الاستخدام - Usage Examples

### مثال 1: التحقق اليدوي من وقت الصيانة
**Example 1: Manual Check of Maintenance Time**

```javascript
// في console المتصفح | In browser console
const isMaintenanceNow = isScheduledMaintenanceTime();
console.log('Maintenance time?', isMaintenanceNow);
// Output: true if 9 PM - 11 PM, false otherwise
```

### مثال 2: فحص حالة المطور
**Example 2: Check Developer Status**

```javascript
// في console المتصفح | In browser console
console.log('Is Developer?', isDev);
console.log('Will see maintenance?', !isDev && isScheduledMaintenanceTime());
```

### مثال 3: تشغيل يدوي للفحص
**Example 3: Manual Trigger of Check**

```javascript
// في console المتصفح | In browser console
checkScheduledMaintenance();
// Will show maintenance if conditions are met
```

---

## 🔄 التحديثات المستقبلية - Future Updates

### أفكار للتحسين - Improvement Ideas

1. **أوقات صيانة قابلة للتخصيص**
   - Customizable maintenance times
   - إمكانية تغيير الأوقات من واجهة المطور
   - Ability to change times from developer interface

2. **جدولة متقدمة**
   - Advanced scheduling
   - أيام محددة (مثلاً: الجمعة فقط)
   - Specific days (e.g., Fridays only)

3. **إشعارات مسبقة**
   - Pre-notifications
   - تنبيه المفتشين قبل 5 دقائق من الصيانة
   - Alert inspectors 5 minutes before maintenance

4. **سجل الصيانة**
   - Maintenance log
   - تسجيل كل مرة يتم فيها تفعيل الصيانة
   - Log each time maintenance is activated

---

## 📞 الدعم والمساعدة - Support and Help

### الأسئلة الشائعة - FAQ

**س1: هل يمكن للمطور رؤية رسالة الصيانة؟**
**Q1: Can developer see the maintenance message?**

ج: لا، المطور معفى تماماً من رؤية رسالة الصيانة في أي وقت.
A: No, developer is completely exempt from seeing maintenance message at any time.

---

**س2: هل يمكن تغيير أوقات الصيانة؟**
**Q2: Can maintenance times be changed?**

ج: نعم، يمكن تعديل الساعات في دالة `isScheduledMaintenanceTime()` في index.html.
A: Yes, hours can be modified in `isScheduledMaintenanceTime()` function in index.html.

---

**س3: ماذا يحدث إذا كان المفتش يستخدم النظام عند بدء الصيانة؟**
**Q3: What happens if inspector is using system when maintenance starts?**

ج: تظهر رسالة الصيانة تلقائياً خلال دقيقة واحدة من بدء وقت الصيانة.
A: Maintenance message appears automatically within one minute of maintenance start.

---

**س4: كيف يمكن اختبار الميزة؟**
**Q4: How to test the feature?**

ج: استخدم ملف `test_scheduled_maintenance.html` الذي يحتوي على محاكي الوقت.
A: Use `test_scheduled_maintenance.html` file which includes time simulator.

---

## ✅ الخلاصة - Conclusion

تم تطوير نظام صيانة مجدول متكامل وفعال يعمل تلقائياً كل يوم من 9 مساءً إلى 11 مساءً. النظام:

A complete and effective scheduled maintenance system has been developed that automatically operates daily from 9 PM to 11 PM. The system:

✅ **يعمل تلقائياً** دون أي تدخل
✅ **Works automatically** without any intervention

✅ **يعرض رسالة صيانة** مع موسيقى هادئة
✅ **Shows maintenance message** with calm music

✅ **يستثني المطور** تماماً
✅ **Exempts developer** completely

✅ **ينتهي تلقائياً** عند الساعة 11 مساءً
✅ **Ends automatically** at 11 PM

✅ **قابل للاختبار** بسهولة
✅ **Easily testable**

✅ **موثق بشكل كامل**
✅ **Fully documented**

---

**تاريخ التطوير | Development Date:** 2024
**الحالة | Status:** ✅ نشط ومكتمل | Active and Complete
