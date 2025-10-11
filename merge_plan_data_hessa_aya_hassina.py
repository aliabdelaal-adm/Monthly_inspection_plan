#!/usr/bin/env python3
"""
Merge plan-datahessa.json, plan-dataaya.json, and plan-datahassina.json into the main plan-data.json file.
This script safely merges inspection data while avoiding duplicates.
"""

import json
import sys
import io
from datetime import datetime

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def load_json_file(filename):
    """Load and parse a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️  File not found: {filename}")
        return None
    except Exception as e:
        print(f"❌ Error loading {filename}: {e}")
        return None

def save_json_file(filename, data):
    """Save data to a JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"❌ Error saving {filename}: {e}")
        return False

def create_inspection_key(entry):
    """Create a unique key for an inspection entry."""
    return f"{entry['inspector']}|{entry['day']}|{entry['shift']}|{entry['area']}"

def validate_shop_duplicates(inspection_data):
    """Validate that no shop is assigned to multiple inspectors on the same day.
    
    Only applies validation to dates from October 7, 2024 onwards.
    Dates before this cutoff are not subject to the duplicate validation rule.
    
    Returns:
        tuple: (is_valid, duplicate_info_list)
        - is_valid: True if no duplicates found, False otherwise
        - duplicate_info_list: List of dictionaries with duplicate information
    """
    from datetime import datetime
    
    # Track shop assignments by day: {day: {shop: [inspector1, inspector2, ...]}}
    day_shop_inspectors = {}
    duplicates = []
    
    # Date cutoff: Only apply validation from October 7, 2024 onwards
    # بداية تطبيق القاعدة: من 7 أكتوبر 2024 فصاعداً
    VALIDATION_START_DATE = datetime(2024, 10, 7)
    
    for entry in inspection_data:
        day = entry.get('day')
        inspector = entry.get('inspector')
        shops = entry.get('shops', [])
        
        if not day or not inspector or not shops:
            continue
        
        # Skip validation for dates before October 7, 2024
        # تخطي التحقق للتواريخ قبل 7 أكتوبر 2024
        try:
            entry_date = datetime.strptime(day, '%Y-%m-%d')
            if entry_date < VALIDATION_START_DATE:
                continue
        except ValueError:
            # If date parsing fails, skip this entry
            continue
            
        if day not in day_shop_inspectors:
            day_shop_inspectors[day] = {}
        
        for shop in shops:
            if shop not in day_shop_inspectors[day]:
                day_shop_inspectors[day][shop] = []
            day_shop_inspectors[day][shop].append(inspector)
    
    # Find duplicates (only for dates >= October 7, 2024)
    # البحث عن التكرارات (فقط للتواريخ >= 7 أكتوبر 2024)
    for day, shops_dict in day_shop_inspectors.items():
        for shop, inspectors in shops_dict.items():
            if len(inspectors) > 1:
                duplicates.append({
                    'day': day,
                    'shop': shop,
                    'inspectors': inspectors
                })
    
    is_valid = len(duplicates) == 0
    return is_valid, duplicates

def merge_inspection_data(main_data, source_data):
    """Merge inspection data from source into main, avoiding duplicates."""
    main_inspections = main_data.get('inspectionData', [])
    source_inspections = source_data.get('inspectionData', [])
    
    # Create a set of existing inspection keys
    existing_keys = set()
    for entry in main_inspections:
        key = create_inspection_key(entry)
        existing_keys.add(key)
    
    # Find new entries to add
    new_entries = []
    for entry in source_inspections:
        key = create_inspection_key(entry)
        if key not in existing_keys:
            new_entries.append(entry)
            existing_keys.add(key)
    
    return main_inspections + new_entries, len(new_entries)

def merge_list_data(main_list, source_list, id_field='id'):
    """Merge list data (inspectors, areas, shops) avoiding duplicates by ID."""
    if not source_list:
        return main_list, 0
    
    existing_ids = set()
    for item in main_list:
        if id_field in item:
            existing_ids.add(item[id_field])
    
    new_items = []
    for item in source_list:
        if id_field in item and item[id_field] not in existing_ids:
            new_items.append(item)
            existing_ids.add(item[id_field])
    
    return main_list + new_items, len(new_items)

def merge_bell_notes(main_data, source_data):
    """Merge bell notifications, preserving main data and adding unique source notifications."""
    main_bell = main_data.get('bellNotes', {})
    source_bell = source_data.get('bellNotes', {})
    
    if not source_bell:
        return main_bell, 0
    
    # Keep main bell structure but merge notifications
    merged_bell = main_bell.copy()
    main_notifications = main_bell.get('notifications', [])
    source_notifications = source_bell.get('notifications', [])
    
    if not source_notifications:
        return merged_bell, 0
    
    # Create set of existing notification IDs
    existing_ids = set()
    for notif in main_notifications:
        if 'id' in notif:
            existing_ids.add(notif['id'])
    
    # Add new notifications
    new_notifications = []
    for notif in source_notifications:
        if 'id' in notif and notif['id'] not in existing_ids:
            new_notifications.append(notif)
            existing_ids.add(notif['id'])
    
    if new_notifications:
        merged_bell['notifications'] = main_notifications + new_notifications
    
    return merged_bell, len(new_notifications)

def merge_source_into_main(main_data, source_data, source_name):
    """Merge a source data file into main data."""
    print(f"\n🔄 Merging {source_name}...")
    
    # Merge inspection data (without validation yet)
    merged_inspections, new_inspections = merge_inspection_data(main_data, source_data)
    main_data['inspectionData'] = merged_inspections
    
    # Merge inspectors
    merged_inspectors, new_inspectors = merge_list_data(
        main_data.get('inspectors', []), 
        source_data.get('inspectors', [])
    )
    main_data['inspectors'] = merged_inspectors
    
    # Merge areas
    merged_areas, new_areas = merge_list_data(
        main_data.get('areas', []), 
        source_data.get('areas', [])
    )
    main_data['areas'] = merged_areas
    
    # Merge shops
    merged_shops, new_shops = merge_list_data(
        main_data.get('shops', []), 
        source_data.get('shops', [])
    )
    main_data['shops'] = merged_shops
    
    # Merge bell notifications
    merged_bell, new_notifications = merge_bell_notes(main_data, source_data)
    main_data['bellNotes'] = merged_bell
    
    print(f"   📝 New inspection entries: {new_inspections}")
    print(f"   👥 New inspectors: {new_inspectors}")
    print(f"   🏘️  New areas: {new_areas}")
    print(f"   🏪 New shops: {new_shops}")
    print(f"   🔔 New notifications: {new_notifications}")
    
    return {
        'inspections': new_inspections,
        'inspectors': new_inspectors,
        'areas': new_areas,
        'shops': new_shops,
        'notifications': new_notifications
    }

def main():
    print("=" * 80)
    print("=== Plan Data Merge Tool ===")
    print("Merging plan-datahessa.json, plan-dataaya.json, and plan-datahassina.json")
    print("into plan-data.json")
    print("=" * 80)
    print()
    
    # Load main file
    print("📂 Loading plan-data.json...")
    main_data = load_json_file('plan-data.json')
    
    if not main_data:
        print("❌ Failed to load plan-data.json!")
        return False
    
    print(f"✅ Main file loaded: {len(main_data.get('inspectionData', []))} inspection entries")
    
    # Load source files
    print("\n📂 Loading source files...")
    hessa_data = load_json_file('plan-datahessa.json')
    aya_data = load_json_file('plan-dataaya.json')
    hassina_data = load_json_file('plan-datahassina.json')
    
    # Check if at least one source file exists
    if not hessa_data and not aya_data and not hassina_data:
        print("\n❌ Error: None of the source files found!")
        print("   Please create plan-datahessa.json, plan-dataaya.json, or plan-datahassina.json")
        return False
    
    if hessa_data:
        print(f"✅ plan-datahessa.json loaded: {len(hessa_data.get('inspectionData', []))} inspection entries")
    else:
        print("⚠️  plan-datahessa.json not found, skipping...")
    
    if aya_data:
        print(f"✅ plan-dataaya.json loaded: {len(aya_data.get('inspectionData', []))} inspection entries")
    else:
        print("⚠️  plan-dataaya.json not found, skipping...")
    
    if hassina_data:
        print(f"✅ plan-datahassina.json loaded: {len(hassina_data.get('inspectionData', []))} inspection entries")
    else:
        print("⚠️  plan-datahassina.json not found, skipping...")
    
    # Create backup
    backup_filename = f"plan-data.json.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    print(f"\n💾 Creating backup: {backup_filename}")
    if not save_json_file(backup_filename, main_data):
        print("❌ Failed to create backup!")
        return False
    print("✅ Backup created successfully")
    
    # Track total merge statistics
    total_stats = {
        'inspections': 0,
        'inspectors': 0,
        'areas': 0,
        'shops': 0,
        'notifications': 0
    }
    
    # Merge all source files
    if hessa_data:
        stats = merge_source_into_main(main_data, hessa_data, "plan-datahessa.json")
        for key in total_stats:
            total_stats[key] += stats[key]
    
    if aya_data:
        stats = merge_source_into_main(main_data, aya_data, "plan-dataaya.json")
        for key in total_stats:
            total_stats[key] += stats[key]
    
    if hassina_data:
        stats = merge_source_into_main(main_data, hassina_data, "plan-datahassina.json")
        for key in total_stats:
            total_stats[key] += stats[key]
    
    # Validate for duplicate shop assignments on the same day
    print("\n🔍 Validating inspection data for duplicate shops...")
    is_valid, duplicates = validate_shop_duplicates(main_data['inspectionData'])
    
    if not is_valid:
        print()
        print("❌ خطأ: تم اكتشاف تكرار محلات لعدة مفتشين في نفس اليوم!")
        print("❌ Error: Duplicate shop assignments detected for multiple inspectors on the same day!")
        print()
        print("🔔 تفاصيل التكرارات / Duplicate Details:")
        print("=" * 80)
        
        for dup in duplicates:
            print(f"\n📅 التاريخ / Date: {dup['day']}")
            print(f"🏪 المحل / Shop: {dup['shop']}")
            print(f"👥 المفتشين / Inspectors:")
            for inspector in dup['inspectors']:
                print(f"   - {inspector}")
        
        print()
        print("=" * 80)
        print("⚠️  يرجى تصحيح الخطة واختيار محلات مختلفة للمفتشين في نفس اليوم")
        print("⚠️  Please correct the plan and choose different shops for inspectors on the same day")
        print("❌ الدمج ملغى / Merge cancelled")
        return False
    
    print("✅ Validation passed: No duplicate shops found")
    
    # Update timestamp
    main_data['lastUpdate'] = datetime.now().isoformat()
    
    # Save merged data
    print("\n💾 Saving merged data to plan-data.json...")
    if not save_json_file('plan-data.json', main_data):
        print("❌ Failed to save merged data!")
        return False
    
    # Report results
    print()
    print("=" * 80)
    print("✅ Merge completed successfully!")
    print("=" * 80)
    print("\n📊 Total Merge Summary:")
    print(f"   📝 New inspection entries added: {total_stats['inspections']}")
    print(f"   👥 New inspectors added: {total_stats['inspectors']}")
    print(f"   🏘️  New areas added: {total_stats['areas']}")
    print(f"   🏪 New shops added: {total_stats['shops']}")
    print(f"   🔔 New notifications added: {total_stats['notifications']}")
    print()
    print(f"📈 Final counts in plan-data.json:")
    print(f"   📝 Total inspection entries: {len(main_data.get('inspectionData', []))}")
    print(f"   👥 Total inspectors: {len(main_data.get('inspectors', []))}")
    print(f"   🏘️  Total areas: {len(main_data.get('areas', []))}")
    print(f"   🏪 Total shops: {len(main_data.get('shops', []))}")
    print(f"   🔔 Total notifications: {len(main_data.get('bellNotes', {}).get('notifications', []))}")
    print(f"   📅 Last update: {main_data.get('lastUpdate')}")
    print()
    print("=" * 80)
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
