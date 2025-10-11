# Quick Start Guide: Merging plan-dataamna.json and plan-dataismail.json

## تعليمات سريعة / Quick Instructions

### الخطوات / Steps:

#### 1. إنشاء ملفات البيانات / Create Data Files

أنشئ ملف واحد أو كلا الملفين التاليين:
Create one or both of the following files:

**plan-dataamna.json**
```json
{
  "inspectionData": [
    {
      "inspector": "د. آمنه بن صرم",
      "day": "2025-10-15",
      "shift": "صباحية",
      "area": "المنطقة",
      "shops": ["محل 1", "محل 2"]
    }
  ],
  "inspectors": [{"id": "amna_01", "name": "د. آمنه بن صرم"}],
  "areas": [{"id": "area_01", "name": "المنطقة"}],
  "shops": [
    {"id": "shop_01", "name": "محل 1", "areaId": "area_01"},
    {"id": "shop_02", "name": "محل 2", "areaId": "area_01"}
  ],
  "bellNotes": {"notifications": []},
  "lastUpdate": "2025-10-11T00:00:00.000Z"
}
```

**plan-dataismail.json**
```json
{
  "inspectionData": [
    {
      "inspector": "د. إسماعيل",
      "day": "2025-10-15",
      "shift": "مسائية",
      "area": "المنطقة",
      "shops": ["محل 3", "محل 4"]
    }
  ],
  "inspectors": [{"id": "ismail_01", "name": "د. إسماعيل"}],
  "areas": [{"id": "area_01", "name": "المنطقة"}],
  "shops": [
    {"id": "shop_03", "name": "محل 3", "areaId": "area_01"},
    {"id": "shop_04", "name": "محل 4", "areaId": "area_01"}
  ],
  "bellNotes": {"notifications": []},
  "lastUpdate": "2025-10-11T00:00:00.000Z"
}
```

**ملاحظة:** يمكن استخدام ملفات القالب كنقطة بداية:
**Note:** You can use the template files as a starting point:
- `plan-dataamna.json.template`
- `plan-dataismail.json.template`

#### 2. تشغيل الدمج / Run the Merge

```bash
python3 merge_plan_dataamna_ismail.py
```

#### 3. التحقق / Verify

```bash
python3 -c "import json; data = json.load(open('plan-data.json', 'r', encoding='utf-8')); print(f'Total: {len(data[\"inspectionData\"])} inspections')"
```

## ماذا يفعل السكريبت؟ / What Does the Script Do?

### ✅ يدمج البيانات / Merges Data
- بيانات التفتيش / Inspection data
- المفتشين / Inspectors
- المناطق / Areas
- المحلات / Shops
- الإشعارات / Notifications

### ✅ يتجنب التكرار / Avoids Duplicates
- يتحقق من عدم تكرار البيانات / Checks for duplicate data
- يستخدم المفاتيح الفريدة / Uses unique keys
- يتحقق من عدم تعيين محل واحد لعدة مفتشين في نفس اليوم / Validates no shop assigned to multiple inspectors on same day

### ✅ يحمي البيانات / Protects Data
- ينشئ نسخة احتياطية تلقائية / Creates automatic backup
- التسمية: `plan-data.json.backup_YYYYMMDD_HHMMSS`

## مثال على النتيجة / Example Output

```
✅ Merge completed successfully!

📊 Total Merge Summary:
   📝 New inspection entries added: 30
   👥 New inspectors added: 2
   🏘️  New areas added: 5
   🏪 New shops added: 12
   
📈 Final counts in plan-data.json:
   📝 Total inspection entries: 111
   👥 Total inspectors: 11
   🏘️  Total areas: 41
   🏪 Total shops: 154
```

## حل المشاكل / Troubleshooting

### ❌ الملفات غير موجودة / Files Not Found
```
❌ Error: Neither plan-dataamna.json nor plan-dataismail.json found!
```
**الحل / Solution:** أنشئ واحداً أو كلا الملفين / Create one or both files

### ❌ تكرار المحلات / Duplicate Shops
```
❌ Error: Duplicate shop assignments detected!
```
**الحل / Solution:** 
- راجع التفاصيل المعروضة / Review the details shown
- عدّل الملفات لتعيين محلات مختلفة / Edit files to assign different shops
- أعد المحاولة / Try again

## موارد إضافية / Additional Resources

للمزيد من التفاصيل، راجع:
For more details, see:
- `MERGE_AMNA_ISMAIL_README.md` - وثائق كاملة / Full documentation
- `DATA_FILES_README.md` - معلومات عن ملفات البيانات / Data files information
- Templates: `plan-dataamna.json.template`, `plan-dataismail.json.template`

## دعم / Support

إذا واجهت أي مشاكل:
If you encounter any issues:
1. تحقق من صيغة JSON / Check JSON format
2. تأكد من وجود جميع الحقول المطلوبة / Ensure all required fields exist
3. راجع الوثائق الكاملة / Review full documentation
