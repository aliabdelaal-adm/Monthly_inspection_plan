# كيفية تصحيح PR #324
# How to Fix PR #324

## الخطوات البسيطة / Simple Steps

### الطريقة 1: استخدام السكريبت الآلي / Method 1: Use Automated Script

```bash
# 1. اذهب إلى فرع PR #324
# 1. Go to PR #324 branch
git checkout copilot/merge-plan-data-files-3

# 2. نزّل السكريبت من الفرع المصحح
# 2. Download the fix script from the correction branch
git checkout copilot/fix-pull-request-324-issues -- fix_pr324_areas.py

# 3. شغّل السكريبت
# 3. Run the script
python3 fix_pr324_areas.py

# 4. تحقق من النتيجة
# 4. Verify the result
python3 -c "
import json
with open('plan-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(f'✅ Total areas: {len(data[\"areas\"])} (should be 23)')
print(f'✅ First 5 areas:')
for i, area in enumerate(data['areas'][:5], 1):
    print(f'   {i}. {area[\"name\"]}')
"

# 5. احفظ التغييرات
# 5. Commit the changes
git add plan-data.json
git commit -m "Fix: Remove 15 incorrectly added areas (IDs as names + duplicates)"
git push origin copilot/merge-plan-data-files-3
```

---

### الطريقة 2: يدوياً / Method 2: Manual Fix

#### الخيار أ: استعادة من الفرع الرئيسي / Option A: Restore from Main

```bash
# 1. اذهب إلى فرع PR #324
git checkout copilot/merge-plan-data-files-3

# 2. استعد plan-data.json من الفرع الرئيسي (يحتوي على 23 منطقة صحيحة)
# Restore plan-data.json from main branch (contains 23 correct areas)
git checkout main -- plan-data.json

# 3. حدّث lastUpdate
python3 -c "
import json
from datetime import datetime

with open('plan-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['lastUpdate'] = datetime.now().isoformat()

with open('plan-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('✅ Updated lastUpdate')
"

# 4. احفظ
git add plan-data.json
git commit -m "Fix: Restore correct plan-data.json with 23 areas from main"
git push origin copilot/merge-plan-data-files-3
```

#### الخيار ب: تحرير يدوي / Option B: Manual Edit

```bash
# 1. افتح plan-data.json في محرر نصوص
# Open plan-data.json in a text editor
nano plan-data.json  # أو استخدم محررك المفضل

# 2. ابحث عن مصفوفة "areas"
# Find the "areas" array

# 3. احذف العناصر من 24 إلى 38 (آخر 15 عنصر)
# Delete elements 24 to 38 (last 15 elements)
# يجب أن يتبقى 23 عنصر فقط
# Only 23 elements should remain

# 4. احفظ الملف
# Save the file

# 5. تحقق
python3 -c "
import json
with open('plan-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(f'✅ Total areas: {len(data[\"areas\"])} (should be 23)')
"

# 6. احفظ في Git
git add plan-data.json
git commit -m "Fix: Remove 15 incorrectly added areas"
git push origin copilot/merge-plan-data-files-3
```

---

### الطريقة 3: إغلاق PR #324 وإنشاء واحد جديد / Method 3: Close PR #324 and Create New

```bash
# إذا كان الأفضل البدء من جديد:
# If it's better to start fresh:

# 1. أغلق PR #324 على GitHub
# Close PR #324 on GitHub

# 2. احذف الفرع
git branch -D copilot/merge-plan-data-files-3
git push origin --delete copilot/merge-plan-data-files-3

# 3. لا تفعل شيئاً! plan-data.json في الفرع الرئيسي صحيح بالفعل
# Do nothing! plan-data.json in main branch is already correct
```

---

## التحقق النهائي / Final Verification

بعد أي طريقة، تحقق من:

After any method, verify:

```bash
# 1. عدد المناطق
# Area count
python3 -c "
import json
with open('plan-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
areas = data.get('areas', [])
print(f'Total areas: {len(areas)}')
assert len(areas) == 23, f'Expected 23 areas, got {len(areas)}'
print('✅ Correct number of areas!')
"

# 2. لا أسماء بمعرّفات
# No ID names
python3 -c "
import json
with open('plan-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
id_names = [a for a in data['areas'] if a['name'].startswith('area_')]
if id_names:
    print(f'❌ Found {len(id_names)} areas with ID names:')
    for a in id_names:
        print(f'   - {a[\"id\"]}: {a[\"name\"]}')
else:
    print('✅ No areas with ID names!')
"

# 3. لا تكرار
# No duplicates
python3 -c "
import json
with open('plan-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
names = [a['name'] for a in data['areas']]
dups = [n for n in set(names) if names.count(n) > 1]
if dups:
    print(f'❌ Found duplicate area names: {dups}')
else:
    print('✅ No duplicate area names!')
"

# 4. اختبارات موجودة
# Existing tests
python3 test_plan_data.py
python3 test_pr269_inspectors_linking.py
```

---

## الخلاصة / Summary

**الهدف:** إزالة 15 منطقة خاطئة من plan-data.json في PR #324

**Goal:** Remove 15 incorrect areas from plan-data.json in PR #324

**النتيجة المطلوبة:** 23 منطقة بأسماء عربية صحيحة

**Desired Result:** 23 areas with correct Arabic names

---

## الأسئلة الشائعة / FAQ

### س: لماذا لا نحتفظ بالـ 15 منطقة؟
**ج:** لأنها خاطئة! 13 منها بأسماء معرّفات و 2 مكررة.

### Q: Why not keep the 15 areas?
**A:** Because they're wrong! 13 have ID names and 2 are duplicates.

---

### س: هل سنفقد بيانات؟
**ج:** لا! جميع المناطق الصحيحة موجودة بالفعل في الـ 23 منطقة الأصلية.

### Q: Will we lose data?
**A:** No! All correct areas already exist in the original 23 areas.

---

### س: ماذا عن بيانات التفتيش؟
**ج:** بيانات التفتيش لن تتأثر. فقط قائمة المناطق ستُصحح.

### Q: What about inspection data?
**A:** Inspection data won't be affected. Only the areas list will be corrected.

---

**التاريخ / Date**: 2025-10-09  
**المطور / Developer**: Copilot
