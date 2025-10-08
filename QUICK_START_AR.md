# 🚀 دليل البداية السريعة - Quick Start Guide

## ⚡ تفعيل الفحص الدوري في 3 خطوات

### الخطوة 1: فتح Terminal أو Command Prompt
```bash
cd /path/to/Monthly_inspection_plan
```

### الخطوة 2: تشغيل سكريبت الإعداد
```bash
./setup_periodic_checker.sh
```

### الخطوة 3: اختر الخيار 1
```
Choose your preferred scheduling method:
1. Cron (Linux/Mac) - للينكس/ماك         ← اختر هذا
2. Systemd Timer (Linux) - للينكس
3. Manual/Skip - يدوي/تخطي

Enter your choice (1-3): 1
```

---

## ✅ تم! النظام الآن يعمل

سيعمل الفحص التلقائي:
- ⏰ **الوقت**: 1:00 صباحاً كل يوم
- 🔍 **الفحص**: تكرارات المحلات + اكتمال البيانات
- 📁 **السجلات**: `logs/error_checker/`

---

## 📋 التحقق من التشغيل

### عرض الجدولة:
```bash
crontab -l
```

### تشغيل فحص تجريبي:
```bash
python3 periodic_error_checker.py
```

### عرض السجلات:
```bash
ls -l logs/error_checker/
cat logs/error_checker/error_check_$(date +%Y%m%d).log
```

---

## 🆘 المساعدة

- **الدليل الشامل**: `PERIODIC_ERROR_CHECKER_README.md`
- **الدليل السريع**: `PERIODIC_ERROR_CHECKER_AR.md`
- **الملخص**: `PERIODIC_CHECKER_SUMMARY.md`

---

**🎉 جاهز! الآن نظامك يراقب الأخطاء تلقائياً كل يوم!**
