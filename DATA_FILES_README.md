# Data Files Documentation

## Primary Data File

### `plan-data.json`
**This is the main data file used by the application.**

**Structure:**
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
  "lastUpdate": "2025-01-01T00:00:00.000Z"
}
```

**Usage:**
- ✅ Main application (`index.html`) loads data from this file
- ✅ Developer panel saves/exports data to this file
- ✅ Admin panel (`admin.html`) edits this file
- ✅ Auto-push script (`auto_push_on_change.py`) monitors this file

## Important Notes

1. **Only `plan-data.json` should be used** - this is the single source of truth for all inspection data
2. **Do not create `inspection_plan.json`** - this was an obsolete file with different structure and has been removed
3. **Backup recommendations**: The application automatically saves data to localStorage as backup
4. **Developer workflow**: Use the "تصدير البيانات إلى ملف JSON" button to export changes to the file system

## File Locations

- **Production data**: `plan-data.json` (in repository root)
- **Backup data**: Browser localStorage (`allPlanData` key)
- **Exported data**: Downloaded as `plan-data.json` when using export function

## Data Consolidation (Completed)

✅ **Multiple files merged successfully** - All inspection data from `plan-data.json`, `plan-data20.json`, `plan-data (17) (1).json`, and `plan-dataAli1.json` have been consolidated into a single `plan-data.json` file as the validated active main source for screen preview for all inspectors.

**Latest Merge Results (September 30, 2025):**
- **44 inspection entries** (consolidated from multiple sources including plan-dataAli1.json)
- **9 inspectors** (no duplicates)
- **22 areas** (comprehensive coverage)
- **114 shops** (complete database with 2 new shops added from plan-dataAli1.json)
- **4 bell notifications** (all unique)
- **Single source of truth** established for all inspection data

**Recent Merge:**
- ✅ Merged `plan-dataAli1.json` into `plan-data.json` (September 30, 2025)
  - Added 7 new inspection entries
  - Added 2 new shops
  - No duplicate inspectors, areas, or notifications