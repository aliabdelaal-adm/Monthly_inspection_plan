# Bell Notifications GitHub Sync System
# نظام مزامنة إشعارات الجرس مع GitHub

## المشكلة | Problem
The issue was: **"لأأستطيع رفع وتحميل اشعارات الجرس علي GitHub"** (Cannot upload and download bell notifications to GitHub)

## الحل | Solution
تم إصلاح نظام رفع إشعارات الجرس تلقائياً إلى GitHub من خلال:
The bell notifications auto-upload system to GitHub has been fixed through:

### 1. تثبيت المتطلبات | Installing Dependencies
- تم تثبيت مكتبة `watchdog` المطلوبة لمراقبة تغييرات الملفات
- The required `watchdog` library for file monitoring has been installed

### 2. إصلاح أخطاء الكود | Code Bug Fixes
- تم إصلاح مشكلة اكتشاف الفرع الحالي في `auto_push_on_change.py`
- Fixed current branch detection issue in `auto_push_on_change.py`
- السكريبت الآن يكتشف الفرع الحالي تلقائياً بدلاً من استخدام "main" بشكل ثابت
- The script now automatically detects the current branch instead of hardcoding "main"

### 3. سكريبت إعداد شامل | Comprehensive Setup Script
- تم إنشاء `setup_bell_notifications.sh` للإعداد التلقائي
- Created `setup_bell_notifications.sh` for automatic setup
- يتحقق من جميع المتطلبات ويثبت ما هو مفقود
- Checks all requirements and installs missing components

## كيفية الاستخدام | How to Use

### الطريقة السريعة | Quick Method
```bash
# 1. تشغيل سكريبت الإعداد
./setup_bell_notifications.sh

# 2. تشغيل نظام المراقبة التلقائي
python3 auto_push_on_change.py
```

### الطريقة اليدوية | Manual Method
```bash
# 1. تثبيت المتطلبات
pip install watchdog

# 2. التحقق من إعداد Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 3. تشغيل النظام
python3 auto_push_on_change.py
```

## كيف يعمل النظام | How the System Works

### 1. مراقبة الملفات | File Monitoring
- النظام يراقب ملف `plan-data.json` باستمرار
- The system continuously monitors `plan-data.json` file
- عند اكتشاف أي تغيير، يبدأ عملية الرفع التلقائي
- When changes are detected, automatic upload process begins

### 2. العمليات التلقائية | Automatic Operations
```
تغيير في plan-data.json → اكتشاف التغيير → انتظار 5 ثوان → git add → git commit → git push
plan-data.json change → detect change → wait 5 seconds → git add → git commit → git push
```

### 3. رسائل الcommit | Commit Messages
```
Auto-update: تم تحديث الملفات تلقائياً - plan-data.json - 2025-09-29 22:59:42
```

## مميزات النظام المُحدث | Updated System Features

### ✅ تم إصلاحها | Fixed Issues
- [x] تثبيت مكتبة `watchdog` المفقودة
- [x] إصلاح اكتشاف الفرع الحالي
- [x] إضافة سكريبت إعداد شامل
- [x] اختبار النظام الكامل

### ✅ ميزات جديدة | New Features
- [x] اكتشاف تلقائي للفرع الحالي
- [x] رسائل سجل باللغتين العربية والإنجليزية
- [x] تحقق شامل من المتطلبات
- [x] معالجة أخطاء محسنة

## إشعارات الجرس | Bell Notifications

### كيفية عمل النظام | How the System Works
1. **إنشاء الإشعارات** | **Creating Notifications**: عند إضافة إشعار جديد في نافذة الجرس
2. **الحفظ التلقائي** | **Auto Save**: يتم حفظ الإشعار في `plan-data.json`
3. **الاكتشاف التلقائي** | **Auto Detection**: `auto_push_on_change.py` يكتشف التغيير
4. **الرفع التلقائي** | **Auto Upload**: يتم رفع التغييرات لـ GitHub تلقائياً

### بنية البيانات | Data Structure
```json
{
  "bellNotes": {
    "notifications": [
      {
        "id": "unique_id",
        "text": "نص الإشعار",
        "timestamp": "2025-09-29T22:59:30.000Z",
        "author": "د. علي عبدالعال",
        "lastModified": "2025-09-29T22:59:35.000Z"
      }
    ]
  }
}
```

## تشغيل النظام في الخلفية | Running System in Background

### Linux/Mac
```bash
# تشغيل في الخلفية
nohup python3 auto_push_on_change.py &

# مراقبة السجلات
tail -f auto_push.log
```

### Windows
```cmd
# تشغيل في نافذة جديدة
start python3 auto_push_on_change.py

# أو باستخدام PowerShell
Start-Process python3 -ArgumentList "auto_push_on_change.py"
```

## مراقبة النظام | System Monitoring

### ملف السجل | Log File
- جميع العمليات يتم تسجيلها في `auto_push.log`
- All operations are logged in `auto_push.log`

### رسائل النظام | System Messages
```
✅ Success: تم commit بنجاح
✅ Success: تم رفع التغييرات بنجاح إلى GitHub
❌ Error: خطأ في git push
⚠️  Warning: ملف غير موجود
🔍 Info: اكتشاف تغيير في الملف
```

## استكشاف الأخطاء | Troubleshooting

### مشاكل شائعة | Common Issues

#### 1. watchdog غير مثبت | watchdog not installed
```bash
pip install watchdog
# أو
pip3 install watchdog
```

#### 2. مشكلة في الصلاحيات | Permission issues
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### 3. مشكلة في remote origin | Remote origin issue
```bash
git remote -v
git remote add origin https://github.com/username/repo.git
```

#### 4. خطأ في المصادقة | Authentication error
- تأكد من إعداد GitHub token أو SSH keys
- Make sure GitHub token or SSH keys are properly configured

## اختبار النظام | Testing the System

### اختبار سريع | Quick Test
```bash
# 1. تشغيل النظام
python3 auto_push_on_change.py

# 2. في نافذة أخرى، تعديل ملف plan-data.json
echo "test" >> plan-data.json

# 3. مراقبة السجلات
tail -f auto_push.log
```

## الأمان | Security

### أفضل الممارسات | Best Practices
- استخدم GitHub Personal Access Tokens بدلاً من كلمات المرور
- Use GitHub Personal Access Tokens instead of passwords
- قم بإعداد صلاحيات محدودة للـ tokens
- Set limited permissions for tokens
- راقب ملف السجل بانتظام للتأكد من عدم وجود مشاكل
- Monitor log file regularly to ensure no issues

## الدعم الفني | Technical Support

في حالة وجود مشاكل، يرجى التحقق من:
If you encounter issues, please check:

1. **ملف السجل** | **Log file**: `auto_push.log`
2. **حالة Git** | **Git status**: `git status`
3. **اتصال الشبكة** | **Network connection**
4. **صلاحيات GitHub** | **GitHub permissions**

---

## خلاصة | Summary

تم إصلاح مشكلة رفع إشعارات الجرس إلى GitHub بنجاح! 🎉
The bell notifications GitHub upload issue has been successfully fixed! 🎉

النظام الآن يعمل تلقائياً ويراقب التغييرات ويرفعها لـ GitHub دون تدخل يدوي.
The system now works automatically, monitors changes, and uploads them to GitHub without manual intervention.