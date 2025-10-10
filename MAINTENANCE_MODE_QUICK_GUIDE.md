# 📖 دليل سريع: وضع الصيانة
# Quick Guide: Maintenance Mode

---

## 🚀 بدء الصيانة - Starting Maintenance

```
1. 👨‍💻 سجّل دخول كمطور
   Log in as developer

2. 🔒 اضغط "تفعيل وضع الصيانة للجميع"
   Click "Enable maintenance mode for all"

3. ✅ تم! جميع المستخدمين سيرون رسالة الصيانة
   Done! All users will see maintenance message
```

---

## ✅ إنهاء الصيانة - Ending Maintenance

```
1. 👨‍💻 سجّل دخول كمطور (إن لم تكن مسجلاً)
   Log in as developer (if not already logged in)

2. ✅ اضغط "إلغاء وضع الصيانة للجميع"
   Click "Cancel maintenance mode for all"

3. ✅ تم! جميع المستخدمين يمكنهم الوصول للنظام
   Done! All users can access the system
```

---

## ⚠️ تنبيه هام - Important Warning

### ❌ خطأ شائع - Common Mistake:
```
"سأسجل خروج، وضع الصيانة سيتوقف تلقائياً"
"I'll log out, maintenance mode will stop automatically"
```

### ✅ الصحيح - Correct:
```
"وضع الصيانة يبقى مفعلاً حتى بعد تسجيل الخروج"
"Maintenance mode stays active even after logout"
```

### 💡 تذكّر - Remember:
- 🔒 **تفعيل وضع الصيانة = يدوياً**
- 🔒 **Enable maintenance = manually**
- ✅ **إلغاء وضع الصيانة = يدوياً**
- ✅ **Disable maintenance = manually**
- 🚪 **تسجيل الخروج ≠ إلغاء الصيانة**
- 🚪 **Logout ≠ Disable maintenance**

---

## 🎯 أمثلة عملية - Practical Examples

### مثال 1: صيانة سريعة (10 دقائق)
**Example 1: Quick maintenance (10 minutes)**

```
09:00 - تسجيل دخول + تفعيل وضع الصيانة
        Login + Enable maintenance

09:05 - تعديلات على النظام
        Make system changes

09:10 - إلغاء وضع الصيانة + تسجيل خروج
        Disable maintenance + Logout

✅ الجميع يمكنهم الوصول للنظام
✅ Everyone can access the system
```

### مثال 2: صيانة طويلة (يومين)
**Example 2: Long maintenance (2 days)**

```
اليوم 1 - Day 1:
09:00 - تسجيل دخول + تفعيل وضع الصيانة
        Login + Enable maintenance

10:00 - تعديلات
        Make changes

17:00 - تسجيل خروج (الصيانة لا تزال مفعلة!)
        Logout (maintenance still active!)

اليوم 2 - Day 2:
09:00 - تسجيل دخول
        Login

12:00 - إكمال التعديلات
        Complete changes

13:00 - إلغاء وضع الصيانة
        Disable maintenance

✅ الجميع يمكنهم الوصول للنظام
✅ Everyone can access the system
```

---

## 🔍 التحقق من الحالة - Check Status

### في المتصفح - In Browser Console:
```javascript
// F12 → Console
localStorage.getItem('systemMaintenanceMode')

// If returns 'true' → Maintenance is ON
// If returns null → Maintenance is OFF
```

---

## 🆘 المساعدة - Help

### المشكلة: وضع الصيانة لا يزال مفعلاً
**Problem: Maintenance mode still active**

**الحل - Solution:**
```
1. سجّل دخول كمطور
   Login as developer

2. اضغط "إلغاء وضع الصيانة للجميع"
   Click "Cancel maintenance mode for all"

3. انتظر 10-30 ثانية
   Wait 10-30 seconds

4. تحقق من الحالة على الأجهزة الأخرى
   Check status on other devices
```

### المشكلة: نسيت إلغاء وضع الصيانة
**Problem: Forgot to disable maintenance**

**الحل - Solution:**
```
1. سجّل دخول من أي جهاز
   Login from any device

2. ألغِ وضع الصيانة
   Disable maintenance

3. تم! ✅
   Done! ✅
```

---

## 📞 الاتصال - Contact

إذا واجهتك أي مشاكل:
If you face any issues:

📧 **البريد الإلكتروني - Email:** ali.abdelaal@adm.gov.ae
📱 **الدعم الفني - Technical Support:** [اتصل بفريق التطوير]

---

**📅 آخر تحديث - Last Updated:** 2025-10-10
**✍️ النسخة - Version:** 1.0
