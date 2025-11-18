# دليل البدء السريع - شاشة الفيديو التمهيدية
# Quick Start Guide - Video Splash Screen

## 🚀 البدء السريع / Quick Start

### للمستخدمين / For Users

**ما هي هذه الميزة؟ / What is this feature?**
- شاشة فيديو تمهيدية تعرض علم الإمارات (uae54.mp4) عند فتح الموقع
- A video splash screen displaying UAE flag (uae54.mp4) when opening the website

**كيف تعمل؟ / How does it work?**
1. افتح الموقع / Open the website
2. يظهر الفيديو تلقائياً / Video appears automatically
3. يغلق الفيديو تلقائياً بعد الانتهاء / Video closes automatically when done
4. لن يظهر مرة أخرى لمدة 10 دقائق / Won't show again for 10 minutes

**لا يتطلب أي إجراء من المستخدم!**  
**No user action required!**

---

## 🔧 للمطورين / For Developers

### الملفات المهمة / Important Files

```
index.html                          - الصفحة الرئيسية / Main page
test_video_splash_screen.html       - صفحة الاختبار / Test page
uae54.mp4                          - ملف الفيديو / Video file
VIDEO_SPLASH_SCREEN_FEATURE.md      - التوثيق الكامل / Full documentation
```

### أوامر التصحيح / Debug Commands

```javascript
// إظهار الفيديو يدوياً / Show video manually
window.showSplash()

// إخفاء الفيديو يدوياً / Hide video manually
window.hideSplash()

// إعادة تعيين فترة الانتظار / Reset cooldown
window.resetSplashCooldown()
```

### تغيير الإعدادات / Change Settings

**فترة الانتظار / Cooldown Duration:**
```javascript
// في index.html، السطر ~5124
// In index.html, line ~5124
const SPLASH_COOLDOWN = 10 * 60 * 1000; // 10 دقائق / 10 minutes
```

**استبدال الفيديو / Replace Video:**
```html
<!-- في index.html، السطر ~5115 -->
<!-- In index.html, line ~5115 -->
<source src="uae54.mp4" type="video/mp4">
```

---

## 🧪 الاختبار / Testing

### الاختبار السريع / Quick Test

1. **افتح صفحة الاختبار / Open test page:**
   ```
   http://localhost:8888/test_video_splash_screen.html
   ```

2. **أزرار الاختبار / Test buttons:**
   - 🎬 عرض الفيديو الآن / Show Video Now
   - ❌ إخفاء الفيديو / Hide Video
   - 📊 حالة النظام / Check Status
   - 🔄 إعادة تعيين الفترة / Reset Cooldown

3. **راقب السجل / Watch the log:**
   - سجل الحالة يعرض جميع الأحداث
   - Status log shows all events

---

## ⚡ حل المشاكل السريع / Quick Troubleshooting

### الفيديو لا يظهر / Video Not Showing

**السبب / Reason:** فترة الانتظار نشطة / Cooldown active

**الحل / Solution:**
```javascript
window.resetSplashCooldown()
// ثم أعد تحميل الصفحة / Then reload page
location.reload()
```

### الفيديو لا يغلق / Video Not Closing

**الحل / Solution:**
```javascript
window.hideSplash()
```

### اختبار متكرر / Repeated Testing

**الحل / Solution:**
```javascript
// قبل كل اختبار / Before each test
window.resetSplashCooldown()
location.reload()
```

---

## 📊 معلومات سريعة / Quick Info

| المعلومة / Info | القيمة / Value |
|-----------------|----------------|
| **حجم الفيديو / Video size** | 7.6 MB |
| **مدة الفيديو / Video duration** | ~38 ثانية / ~38 seconds |
| **فترة الانتظار / Cooldown** | 10 دقائق / 10 minutes |
| **التخزين / Storage** | localStorage |
| **المفتاح / Key** | lastSplashScreenTime |
| **Z-Index** | 999999999 |

---

## 🎯 نقاط مهمة / Key Points

✅ **تلقائي بالكامل / Fully Automatic**
- لا يتطلب تفاعل المستخدم / No user interaction needed

✅ **ذكي / Smart**
- لا يزعج المستخدمين / Doesn't annoy users
- فترة انتظار 10 دقائق / 10-minute cooldown

✅ **متوافق / Compatible**
- جميع المتصفحات / All browsers
- جميع الأجهزة / All devices

✅ **قابل للتخصيص / Customizable**
- سهل التعديل / Easy to modify
- موثق جيداً / Well documented

---

## 📚 المزيد من المعلومات / More Information

للحصول على معلومات تفصيلية، راجع:  
For detailed information, see:

- **VIDEO_SPLASH_SCREEN_FEATURE.md** - التوثيق الكامل / Full documentation
- **test_video_splash_screen.html** - صفحة الاختبار التفاعلية / Interactive test page
- **index.html (lines 5109-5204)** - الكود المصدري / Source code

---

## 🎉 الخلاصة / Summary

**تم إضافة شاشة فيديو تمهيدية احترافية تعمل بذكاء وتلقائياً**  
**A professional video splash screen has been added that works smartly and automatically**

✅ يعمل تلقائياً / Works automatically  
✅ يغلق تلقائياً / Closes automatically  
✅ فترة انتظار ذكية / Smart cooldown  
✅ سهل الاستخدام / Easy to use  
✅ موثق جيداً / Well documented

---

**التاريخ / Date:** 18 نوفمبر 2025 / November 18, 2025  
**المطور / Developer:** د. علي عبدالعال / Dr. Ali Abdelaal

🌟 **استمتع! / Enjoy!** 🌟
