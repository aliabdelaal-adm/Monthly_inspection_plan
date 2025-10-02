# Quick Reference: Duplicate Shop Validation

## 🚀 Quick Start

### Check for Duplicates
```bash
python3 validate_plan.py
```

### Merge Data with Validation
```bash
python3 merge_plan_data.py
```

### Run Tests
```bash
python3 test_duplicate_validation.py
python3 test_merge_with_duplicates.py
```

## 📖 What It Does

✅ Automatically detects if the same shop is assigned to multiple inspectors on the same day
✅ Rejects invalid plans before saving
✅ Shows detailed error messages in Arabic and English

## 🎯 Validation Rules

### ✅ Allowed
- Same shop on **different days** for different inspectors
- Multiple shops for same inspector on same day

### ❌ Blocked
- Same shop on **same day** for multiple inspectors

## 📊 Example Output

### Valid Plan
```
✅ Validation passed: No duplicate shops found
```

### Invalid Plan
```
❌ خطأ: تم اكتشاف تكرار محلات لعدة مفتشين في نفس اليوم!
❌ Error: Duplicate shop assignments detected!

📅 Date: 2025-09-26
🏪 Shop: محل بيت الطيور
👥 Inspectors:
   - د. آمنه بن صرم
   - د. علي عبدالعال

❌ الدمج ملغى / Merge cancelled
```

## 📁 Key Files

| File | Purpose |
|------|---------|
| `merge_plan_data.py` | Main merge script with validation |
| `validate_plan.py` | Standalone validation tool |
| `test_duplicate_validation.py` | Unit tests (4 tests) |
| `test_merge_with_duplicates.py` | Integration test |

## 💡 Common Use Cases

### 1. Before Merging New Data
```bash
# Check current data first
python3 validate_plan.py

# Then merge (validation runs automatically)
python3 merge_plan_data.py
```

### 2. Quick Health Check
```bash
python3 validate_plan.py
```

### 3. After Manual Edits
```bash
# Edit plan-data.json manually, then validate
python3 validate_plan.py
```

## 🆘 Troubleshooting

### If Validation Fails During Merge
1. Review the error message - it shows exact duplicates
2. Edit the source data file (plan-data1.json)
3. Remove or reassign duplicate shops
4. Try merge again

### If Current Data Has Duplicates
1. Run `python3 validate_plan.py` to see all duplicates
2. Manually edit `plan-data.json`
3. Remove duplicate shop assignments
4. Validate again

## 📚 Full Documentation

- **English**: `DUPLICATE_VALIDATION_FEATURE.md`
- **Arabic**: `DUPLICATE_VALIDATION_SUMMARY_AR.md`
- **Implementation**: `SOLUTION_IMPLEMENTATION.md`

## ✅ Verification

To verify the feature is working:
```bash
python3 test_duplicate_validation.py
# Should show: Passed: 4/4 ✅ All tests passed!
```
