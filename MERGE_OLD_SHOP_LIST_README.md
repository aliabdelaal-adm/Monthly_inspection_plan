# Merge old-shop-list.xlsx into plan-data.json - Summary

## Overview
This document describes the merge of shop data from `old-shop-list-updated.xlsx` into `plan-data.json` to enrich the inspection plan system with additional shop information.

## What Was Merged

### Source File
- **File**: `old-shop-list-updated.xlsx`
- **Shops**: 126 shop records
- **Fields**: ADM Code, License Number, Trade Names (AR/EN), Location, Map URLs, Contact Numbers

### Target File
- **File**: `plan-data.json`
- **Original shops**: 151 shops
- **Final shops**: 273 shops

## Merge Results

### Summary
- **4 shops updated** with enriched data from Excel (shops that already existed)
- **122 new shops added** from Excel
- **0 shops skipped**
- **Total shops after merge**: 273 shops

### New Fields Added
The merge script added the following fields to shop records in plan-data.json:

1. **admCode**: ADM administrative code (e.g., ADM0001)
2. **licenseNo**: License number (e.g., CN-4777884)
3. **nameEn**: English trade name
4. **contact**: Contact phone number
5. **mapUrl**: Google Maps URL for shop location

### Example Before and After

**Before (existing shop)**:
```json
{
  "id": "shop_1758913104995",
  "name": "محل جرين لندز",
  "areaId": "area_1758839345230"
}
```

**After (enriched with Excel data)**:
```json
{
  "id": "shop_1758913104995",
  "name": "محل جرين لندز",
  "areaId": "area_1758839345230",
  "admCode": "ADM0001",
  "licenseNo": "CN-4777884",
  "nameEn": "Green Lands Store",
  "contact": "525182727",
  "mapUrl": "https://maps.google.com/maps/search/..."
}
```

## Area Mapping
The merge script intelligently mapped shop locations from the Excel file to existing areas in plan-data.json:

- سوق الميناء → 31 shops
- شاطيء الراحة → 26 shops
- سوق التراث → 26 shops
- مدينة خليفة → 24 shops
- محلات المولات → 19 shops
- الدانة → 19 shops
- And more...

Only 7 shops could not be automatically mapped to areas due to ambiguous location data.

## How to Use the Merge Script

### Prerequisites
```bash
pip install pandas openpyxl
```

### Running the Script
```bash
python3 merge_old_shop_list.py
```

### What the Script Does
1. Loads the Excel file (`old-shop-list-updated.xlsx`)
2. Loads the JSON file (`plan-data.json`)
3. Creates an automatic backup with timestamp
4. Matches shops by name to avoid duplicates
5. Maps Excel locations to JSON area IDs
6. Updates existing shops with new fields
7. Adds new shops to the system
8. Validates all area references
9. Saves the merged data

### Safety Features
- **Automatic backup**: Creates timestamped backup before any changes
- **Duplicate prevention**: Uses name matching to avoid duplicate shops
- **Data validation**: Ensures all required fields are present
- **Area validation**: Verifies all area IDs are valid

## Verification

The merged data was verified to:
- ✅ Load correctly in index.html
- ✅ Display shop details with new fields (license, contact, etc.)
- ✅ Pass all data validation checks
- ✅ Maintain data integrity
- ✅ Pass security scans (CodeQL)

## Files Modified
- `plan-data.json` - Updated with merged shop data
- `merge_old_shop_list.py` - New merge script created

## Files Created as Backup
- `plan-data.json.backup_20251022_144721` - Original backup
- `plan-data.json.backup_20251022_144803` - Second backup
- Additional timestamped backups created during development

## Impact on index.html
The index.html application now has access to richer shop information:
- License numbers for regulatory tracking
- Contact information for coordination
- English names for bilingual support
- Map URLs for location services
- ADM codes for administrative reference

This enhancement improves the inspection planning system by providing inspectors with more comprehensive shop information.
