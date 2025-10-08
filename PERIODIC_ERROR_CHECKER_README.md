# مدقق الأخطاء الدوري - Periodic Error Checker

## نظرة عامة / Overview

مدقق الأخطاء الدوري هو نظام تلقائي للفحص الدوري لأخطاء خطة التفتيش الشهرية. يتم جدولة الفحص للتشغيل يومياً في الساعة 1:00 صباحاً ويستمر حتى إكمال جميع الفحوصات.

The Periodic Error Checker is an automated system for routine error checking of the monthly inspection plan. It is scheduled to run daily at 1:00 AM and continues until all checks are complete.

---

## المميزات / Features

### ✅ الفحوصات التلقائية / Automatic Checks

1. **فحص تكرارات المحلات / Shop Duplicate Detection**
   - يتحقق من عدم تعيين نفس المحل لعدة مفتشين في نفس اليوم
   - Verifies that no shop is assigned to multiple inspectors on the same day
   - يطبق القاعدة على التواريخ من 7 أكتوبر 2024 فصاعداً
   - Applies validation to dates from October 7, 2024 onwards

2. **فحص اكتمال البيانات / Data Completeness Check**
   - يتحقق من وجود جميع الحقول المطلوبة
   - Verifies all required fields are present
   - يكشف السجلات الناقصة أو الفارغة
   - Detects missing or empty records

### 📊 التقارير والسجلات / Reports and Logs

- **سجلات يومية مفصلة / Detailed Daily Logs**
  - يتم حفظ سجل منفصل لكل يوم
  - A separate log file is saved for each day
  - موقع السجلات: `logs/error_checker/error_check_YYYYMMDD.log`
  - Log location: `logs/error_checker/error_check_YYYYMMDD.log`

- **تقارير ثنائية اللغة / Bilingual Reports**
  - جميع الرسائل بالعربية والإنجليزية
  - All messages in Arabic and English

### ⏰ الجدولة التلقائية / Automatic Scheduling

- **التشغيل اليومي / Daily Execution**
  - يعمل تلقائياً كل يوم في الساعة 1:00 صباحاً
  - Runs automatically every day at 1:00 AM
  - يستمر حتى إتمام جميع الفحوصات
  - Continues until all checks are complete

---

## التثبيت والإعداد / Installation and Setup

### المتطلبات / Requirements

- Python 3.6 أو أحدث / Python 3.6 or higher
- نظام Linux/Mac مع Cron أو Systemd / Linux/Mac system with Cron or Systemd
- صلاحيات المستخدم (sudo للـ systemd) / User permissions (sudo for systemd)

### خطوات التثبيت / Installation Steps

#### 1. تنزيل الملفات / Download Files

تأكد من وجود الملفات التالية:
Ensure the following files are present:

- `periodic_error_checker.py` - السكريبت الرئيسي / Main script
- `setup_periodic_checker.sh` - سكريبت الإعداد / Setup script

#### 2. تشغيل سكريبت الإعداد / Run Setup Script

```bash
# إعطاء صلاحية التنفيذ / Make executable
chmod +x setup_periodic_checker.sh

# تشغيل الإعداد / Run setup
./setup_periodic_checker.sh
```

#### 3. اختيار طريقة الجدولة / Choose Scheduling Method

سيطلب منك السكريبت اختيار إحدى الطرق:
The script will ask you to choose one method:

**الخيار 1: Cron (موصى به لـ Linux/Mac)**
```
- سهل الاستخدام
- Easy to use
- يعمل على معظم أنظمة Linux/Mac
- Works on most Linux/Mac systems
```

**الخيار 2: Systemd Timer (للـ Linux فقط)**
```
- أكثر تطوراً
- More advanced
- يتطلب صلاحيات sudo
- Requires sudo permissions
```

**الخيار 3: يدوي / Manual**
```
- للتشغيل اليدوي فقط
- For manual execution only
```

---

## الاستخدام / Usage

### التشغيل اليدوي / Manual Execution

يمكنك تشغيل الفحص يدوياً في أي وقت:
You can run the check manually at any time:

```bash
cd /path/to/Monthly_inspection_plan
python3 periodic_error_checker.py
```

### التشغيل التلقائي / Automatic Execution

بعد الإعداد، سيعمل الفحص تلقائياً في الساعة 1:00 صباحاً كل يوم.
After setup, the check will run automatically at 1:00 AM every day.

---

## إدارة الجدولة / Managing the Schedule

### باستخدام Cron / Using Cron

#### عرض الجدولة الحالية / View Current Schedule
```bash
crontab -l
```

#### تعديل الجدولة / Edit Schedule
```bash
crontab -e
```

#### حذف الجدولة / Remove Schedule
```bash
crontab -e
# ثم احذف السطر الذي يحتوي على periodic_error_checker.py
# Then delete the line containing periodic_error_checker.py
```

### باستخدام Systemd / Using Systemd

#### عرض حالة المؤقت / View Timer Status
```bash
sudo systemctl status periodic-error-checker.timer
```

#### عرض السجلات / View Logs
```bash
sudo journalctl -u periodic-error-checker.service
```

#### إيقاف المؤقت / Stop Timer
```bash
sudo systemctl stop periodic-error-checker.timer
```

#### تعطيل المؤقت / Disable Timer
```bash
sudo systemctl disable periodic-error-checker.timer
```

#### تعديل التوقيت / Modify Timing
```bash
sudo systemctl edit periodic-error-checker.timer
```

---

## السجلات / Logs

### موقع السجلات / Log Location

جميع السجلات محفوظة في:
All logs are saved in:

```
logs/error_checker/
├── error_check_20250127.log
├── error_check_20250128.log
├── error_check_20250129.log
└── cron.log (إذا استخدمت Cron)
```

### قراءة السجلات / Reading Logs

#### عرض آخر سجل / View Latest Log
```bash
cd logs/error_checker
ls -lt | head -5  # عرض أحدث 5 ملفات / Show latest 5 files
cat error_check_$(date +%Y%m%d).log  # عرض سجل اليوم / View today's log
```

#### متابعة السجل الحي / Follow Live Log
```bash
tail -f logs/error_checker/cron.log
```

#### البحث عن أخطاء محددة / Search for Specific Errors
```bash
grep "❌" logs/error_checker/*.log
grep "تكرار" logs/error_checker/*.log
```

---

## مثال على السجل / Log Example

```
================================================================================
🔍 بدء الفحص الدوري للأخطاء / Starting Periodic Error Check
⏰ التاريخ والوقت / Date & Time: 2025-01-27 01:00:00
================================================================================
✅ تم تحميل plan-data.json بنجاح
✅ Successfully loaded plan-data.json
📊 عدد السجلات / Total entries: 85

🔍 الفحص 1: اكتمال البيانات / Check 1: Data Completeness
--------------------------------------------------------------------------------
✅ جميع البيانات كاملة / All data is complete

🔍 الفحص 2: تكرار المحلات / Check 2: Duplicate Shop Assignments
--------------------------------------------------------------------------------
❌ وجدت 15 حالات تكرار
❌ Found 15 duplicate cases

📋 تفاصيل التكرارات / Duplicate Details:

1. 📅 التاريخ / Date: 2025-09-26
   🏪 المحل / Shop: محل بيت الطيور
   👥 المفتشين / Inspectors (2):
      - د. آمنه بن صرم
      - د. علي عبدالعال
...

================================================================================
⚠️  تحذير: وجدت أخطاء تحتاج إلى تصحيح
⚠️  Warning: Errors found that need correction
📧 يرجى مراجعة السجلات ومعالجة الأخطاء
📧 Please review the logs and address the errors
================================================================================
```

---

## استكشاف الأخطاء / Troubleshooting

### المشكلة: الفحص لا يعمل تلقائياً
**Problem: Check not running automatically**

#### الحلول / Solutions:

1. **تحقق من الجدولة / Check Scheduling**
   ```bash
   # لـ Cron
   crontab -l
   
   # لـ Systemd
   sudo systemctl status periodic-error-checker.timer
   ```

2. **تحقق من السجلات / Check Logs**
   ```bash
   cat logs/error_checker/cron.log
   # أو / or
   sudo journalctl -u periodic-error-checker.service
   ```

3. **تحقق من الصلاحيات / Check Permissions**
   ```bash
   ls -la periodic_error_checker.py
   # يجب أن تكون قابلة للتنفيذ / Should be executable
   ```

### المشكلة: خطأ في تحميل البيانات
**Problem: Error loading data**

#### الحلول / Solutions:

1. **تحقق من وجود الملف / Check File Exists**
   ```bash
   ls -la plan-data.json
   ```

2. **تحقق من صحة JSON / Validate JSON**
   ```bash
   python3 -m json.tool plan-data.json > /dev/null
   ```

### المشكلة: السجلات لا تُحفظ
**Problem: Logs not being saved**

#### الحلول / Solutions:

1. **إنشاء مجلد السجلات / Create Log Directory**
   ```bash
   mkdir -p logs/error_checker
   ```

2. **تحقق من الصلاحيات / Check Permissions**
   ```bash
   ls -ld logs/error_checker
   ```

---

## التخصيص / Customization

### تغيير وقت التشغيل / Change Execution Time

#### لـ Cron:
```bash
crontab -e
# غيّر "0 1" إلى الوقت المطلوب (ساعة دقيقة)
# Change "0 1" to desired time (hour minute)
# مثال: "0 2" للساعة 2:00 صباحاً
# Example: "0 2" for 2:00 AM
```

#### لـ Systemd:
```bash
sudo systemctl edit periodic-error-checker.timer
# غيّر OnCalendar=*-*-* 01:00:00
# Change OnCalendar=*-*-* 01:00:00
# مثال: OnCalendar=*-*-* 02:00:00 للساعة 2:00 صباحاً
# Example: OnCalendar=*-*-* 02:00:00 for 2:00 AM
```

### إضافة فحوصات جديدة / Add New Checks

افتح `periodic_error_checker.py` وأضف فحوصات جديدة في دالة `run_error_check()`:

Open `periodic_error_checker.py` and add new checks in the `run_error_check()` function:

```python
# Check 3: Your Custom Check
logger.info("🔍 الفحص 3: فحصك المخصص / Check 3: Your Custom Check")
logger.info("-" * 80)
# Add your validation logic here
```

---

## الدعم / Support

للمساعدة أو الإبلاغ عن المشاكل:
For help or to report issues:

- راجع السجلات في `logs/error_checker/`
- Check logs in `logs/error_checker/`
- افتح مشكلة في GitHub
- Open an issue on GitHub

---

## الملخص / Summary

✅ **تم إعداد مدقق الأخطاء الدوري بنجاح!**
✅ **Periodic Error Checker Setup Complete!**

- ⏰ يعمل يومياً في الساعة 1:00 صباحاً
- ⏰ Runs daily at 1:00 AM
- 🔍 يفحص تكرارات المحلات واكتمال البيانات
- 🔍 Checks shop duplicates and data completeness
- 📊 يُنشئ سجلات مفصلة ثنائية اللغة
- 📊 Generates detailed bilingual logs
- 🔧 سهل الإدارة والتخصيص
- 🔧 Easy to manage and customize

---

**تاريخ الإنشاء / Created:** 2025-01-27  
**الإصدار / Version:** 1.0.0
