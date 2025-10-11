# Merge plan-dataamna.json and plan-dataismail.json into plan-data.json

## Overview
This document describes the merge operation that combines data from `plan-dataamna.json` and `plan-dataismail.json` into the main `plan-data.json` file.

## What Was Done

### 1. Created merge script: `merge_plan_dataamna_ismail.py`
   - Based on existing merge scripts in the repository
   - Merges both `plan-dataamna.json` and `plan-dataismail.json` into `plan-data.json` sequentially
   - Implements intelligent duplicate detection to avoid data duplication
   - Validates for duplicate shop assignments on the same day (for dates from October 7, 2024 onwards)

### 2. Key Features
   - **Automatic Backup**: Creates a timestamped backup of `plan-data.json` before merging
   - **Duplicate Prevention**: Uses composite key (inspector + day + shift + area) for inspection entries
   - **Smart Merging**: 
     - Merges inspection data avoiding duplicates
     - Merges inspectors, areas, and shops by ID
     - Merges bell notifications
   - **Validation**: Checks for duplicate shop assignments on the same day
   - **Flexible**: Can merge one or both files - works even if only one file exists

## How to Use

### Prerequisites
1. Ensure you have Python 3 installed
2. Place your data files in the repository root:
   - `plan-dataamna.json` (optional - can merge without it)
   - `plan-dataismail.json` (optional - can merge without it)
   - At least one of the above files must exist

### File Structure
Both source files should follow the same structure as `plan-data.json`:
```json
{
  "inspectionData": [
    {
      "inspector": "اسم المفتش",
      "day": "2025-01-15",
      "shift": "صباحية/مسائية",
      "area": "اسم المنطقة",
      "shops": ["محل 1", "محل 2"]
    }
  ],
  "inspectors": [
    {"id": "unique_id", "name": "اسم المفتش"}
  ],
  "areas": [
    {"id": "unique_id", "name": "اسم المنطقة"}
  ],
  "shops": [
    {"id": "unique_id", "name": "اسم المحل", "areaId": "area_id"}
  ],
  "bellNotes": {
    "notifications": []
  },
  "lastUpdate": "2025-01-01T00:00:00.000Z"
}
```

### Running the Merge

```bash
python3 merge_plan_dataamna_ismail.py
```

The script will:
1. Create an automatic backup of `plan-data.json`
2. Load both source files (if they exist)
3. Merge data intelligently, avoiding duplicates
4. Validate for duplicate shop assignments
5. Update timestamps
6. Provide detailed merge summary

### Example Output

```
================================================================================
=== Plan Data Merge Tool ===
Merging plan-dataamna.json and plan-dataismail.json into plan-data.json
================================================================================

📂 Loading plan-data.json...
✅ Main file loaded: 81 inspection entries

📂 Loading source files...
✅ plan-dataamna.json loaded: 25 inspection entries
✅ plan-dataismail.json loaded: 30 inspection entries

💾 Creating backup...
✅ Backup created: plan-data.json.backup_20251011_190000

🔄 Merging plan-dataamna.json...
   📝 New inspection entries: 12
   👥 New inspectors: 0
   🏘️  New areas: 3
   🏪 New shops: 5
   🔔 New notifications: 0

🔄 Merging plan-dataismail.json...
   📝 New inspection entries: 18
   👥 New inspectors: 1
   🏘️  New areas: 2
   🏪 New shops: 7
   🔔 New notifications: 0

🔍 Validating inspection data for duplicate shops...
✅ Validation passed: No duplicate shops found

💾 Saving merged data to plan-data.json...

================================================================================
✅ Merge completed successfully!
================================================================================

📊 Total Merge Summary:
   📝 New inspection entries added: 30
   👥 New inspectors added: 1
   🏘️  New areas added: 5
   🏪 New shops added: 12
   🔔 New notifications added: 0

📈 Final counts in plan-data.json:
   📝 Total inspection entries: 111
   👥 Total inspectors: 9
   🏘️  Total areas: 41
   🏪 Total shops: 154
   🔔 Total notifications: 4
   📅 Last update: 2025-10-11T19:00:00.000000

================================================================================
```

## Important Notes

### Duplicate Prevention
The merge script prevents duplicates by:
- **Inspection entries**: Using a composite key of (inspector + day + shift + area)
- **Inspectors, Areas, Shops**: Using their unique ID fields
- **Bell notifications**: Using notification IDs

### Validation Rules
- **Duplicate Shop Check**: Validates that no shop is assigned to multiple inspectors on the same day
- **Date Cutoff**: Validation only applies to dates from October 7, 2024 onwards
- If duplicates are found, the merge is cancelled and details are shown

### Data Integrity
- All existing data in `plan-data.json` is preserved
- Automatic backup is created before any changes
- All JSON structure and required fields remain intact

## Verification

To verify the merge was successful:

```bash
# Check the merged data
python3 -c "import json; data = json.load(open('plan-data.json', 'r', encoding='utf-8')); print(f'Inspections: {len(data[\"inspectionData\"])}, Inspectors: {len(data[\"inspectors\"])}, Areas: {len(data[\"areas\"])}, Shops: {len(data[\"shops\"])}')"
```

## Front Screen Display

The application (`index.html`) loads data from `plan-data.json` using:
```javascript
const response = await fetch('./plan-data.json?t=' + Date.now());
```

After the merge, all data will be immediately available to the application:
- Inspection schedules from all three files
- Inspector information
- Area details
- Shop information
- Bell notifications

## Troubleshooting

### Files Not Found
If you get an error about files not being found:
1. Make sure `plan-dataamna.json` and/or `plan-dataismail.json` exist in the repository root
2. Check file names are spelled correctly
3. At least one of the two files must exist

### Duplicate Shop Errors
If the merge is cancelled due to duplicate shops:
1. Review the duplicate details shown in the output
2. Edit the source files to assign different shops to inspectors on the same day
3. Run the merge again

### Backup Files
- Backup files are created in the format: `plan-data.json.backup_YYYYMMDD_HHMMSS`
- Keep these for safety until you verify the merge is correct
- You can restore by copying a backup file back to `plan-data.json`

## Related Scripts

- `merge_plan_data.py` - Template for merging single files
- `merge_plan_data10.py`, `merge_plan_data91.py`, etc. - Other merge scripts
- All merge scripts follow the same pattern and can be used as references

## Support

For issues or questions about the merge process, please refer to:
- `DATA_FILES_README.md` - General data files documentation
- Other `MERGE_*_README.md` files - Examples of previous merges
