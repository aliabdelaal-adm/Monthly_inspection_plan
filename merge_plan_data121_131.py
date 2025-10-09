#!/usr/bin/env python3
"""
Merge plan-data121.json and plan-data131.json into the main plan-data.json file.
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
    
    Returns:
        tuple: (is_valid, duplicate_info_list)
        - is_valid: True if no duplicates found, False otherwise
        - duplicate_info_list: List of dictionaries with duplicate information
    """
    # Track shop assignments by day: {day: {shop: [inspector1, inspector2, ...]}}
    day_shop_inspectors = {}
    duplicates = []
    
    for entry in inspection_data:
        day = entry.get('day')
        inspector = entry.get('inspector')
        shops = entry.get('shops', [])
        
        if not day or not inspector or not shops:
            continue
            
        if day not in day_shop_inspectors:
            day_shop_inspectors[day] = {}
        
        for shop in shops:
            if shop not in day_shop_inspectors[day]:
                day_shop_inspectors[day][shop] = []
            day_shop_inspectors[day][shop].append(inspector)
    
    # Find duplicates
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

def merge_inspection_data(main_data, source_data, source_name):
    """Merge inspection data from source into main, avoiding duplicates."""
    main_inspections = main_data.get('inspectionData', [])
    source_inspections = source_data.get('inspectionData', [])
    
    # Create a set of existing inspection keys
    existing_keys = set()
    for entry in main_inspections:
        key = create_inspection_key(entry)
        existing_keys.add(key)
    
    # Find new entries to add and conflicts
    new_entries = []
    conflicts = []
    for entry in source_inspections:
        key = create_inspection_key(entry)
        if key not in existing_keys:
            new_entries.append(entry)
            existing_keys.add(key)
        else:
            # Check if it's truly the same entry or a conflict
            existing_entry = next((e for e in main_inspections if create_inspection_key(e) == key), None)
            if existing_entry and json.dumps(existing_entry, sort_keys=True) != json.dumps(entry, sort_keys=True):
                conflicts.append({
                    'key': key,
                    'existing': existing_entry,
                    'source': entry,
                    'source_file': source_name
                })
    
    return main_inspections + new_entries, len(new_entries), conflicts

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

def main():
    print("=" * 80)
    print("=== Plan Data Merge Tool ===")
    print("Merging plan-data121.json and plan-data131.json into plan-data.json")
    print("=" * 80)
    print()
    
    # Load files
    print("📂 Loading files...")
    main_data = load_json_file('plan-data.json')
    source_121 = load_json_file('plan-data121.json')
    source_131 = load_json_file('plan-data131.json')
    
    if not main_data or not source_121 or not source_131:
        print("❌ Failed to load required files!")
        return False
    
    print(f"✅ Main file loaded: {len(main_data.get('inspectionData', []))} inspection entries")
    print(f"✅ Source 121 loaded: {len(source_121.get('inspectionData', []))} inspection entries")
    print(f"✅ Source 131 loaded: {len(source_131.get('inspectionData', []))} inspection entries")
    print()
    
    # Create backup
    backup_filename = f"plan-data.json.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    print(f"💾 Creating backup: {backup_filename}")
    if not save_json_file(backup_filename, main_data):
        print("❌ Failed to create backup!")
        return False
    print()
    
    # Merge data from both sources
    print("🔄 Merging data from plan-data121.json...")
    merged_data = main_data.copy()
    
    # Merge inspection data from 121
    merged_inspections, new_from_121, conflicts_121 = merge_inspection_data(main_data, source_121, "plan-data121.json")
    merged_data['inspectionData'] = merged_inspections
    
    # Merge inspection data from 131
    print("🔄 Merging data from plan-data131.json...")
    temp_data = {'inspectionData': merged_inspections}
    merged_inspections, new_from_131, conflicts_131 = merge_inspection_data(temp_data, source_131, "plan-data131.json")
    merged_data['inspectionData'] = merged_inspections
    
    # Report conflicts
    all_conflicts = conflicts_121 + conflicts_131
    if all_conflicts:
        print()
        print("⚠️  Conflicts detected (keeping existing data):")
        print("=" * 80)
        for conflict in all_conflicts:
            print(f"\n📋 Key: {conflict['key']}")
            print(f"   Source: {conflict['source_file']}")
            print(f"   Existing shops: {conflict['existing'].get('shops', [])}")
            print(f"   Source shops: {conflict['source'].get('shops', [])}")
        print("=" * 80)
        print()
    
    # Validate for duplicate shop assignments on the same day (informational only)
    print("🔍 Checking inspection data for duplicate shops...")
    is_valid, duplicates = validate_shop_duplicates(merged_data['inspectionData'])
    
    if not is_valid:
        print(f"⚠️  Found {len(duplicates)} shop(s) assigned to multiple inspectors on the same day")
        print("   (This may be intentional for team inspections or different shifts)")
    else:
        print("✅ No duplicate shops found")
    print()
    
    # Merge inspectors from both sources
    print("🔄 Merging inspectors...")
    merged_inspectors, new_insp_121 = merge_list_data(
        main_data.get('inspectors', []), 
        source_121.get('inspectors', [])
    )
    merged_inspectors, new_insp_131 = merge_list_data(
        merged_inspectors, 
        source_131.get('inspectors', [])
    )
    merged_data['inspectors'] = merged_inspectors
    
    # Merge areas from both sources
    print("🔄 Merging areas...")
    merged_areas, new_area_121 = merge_list_data(
        main_data.get('areas', []), 
        source_121.get('areas', [])
    )
    merged_areas, new_area_131 = merge_list_data(
        merged_areas, 
        source_131.get('areas', [])
    )
    merged_data['areas'] = merged_areas
    
    # Merge shops from both sources
    print("🔄 Merging shops...")
    merged_shops, new_shop_121 = merge_list_data(
        main_data.get('shops', []), 
        source_121.get('shops', [])
    )
    merged_shops, new_shop_131 = merge_list_data(
        merged_shops, 
        source_131.get('shops', [])
    )
    merged_data['shops'] = merged_shops
    
    # Merge bell notifications from both sources
    print("🔄 Merging bell notifications...")
    merged_bell, new_notif_121 = merge_bell_notes(main_data, source_121)
    merged_bell, new_notif_131 = merge_bell_notes({'bellNotes': merged_bell}, source_131)
    merged_data['bellNotes'] = merged_bell
    
    # Update timestamp
    merged_data['lastUpdate'] = datetime.now().isoformat()
    
    # Save merged data
    print("💾 Saving merged data...")
    if not save_json_file('plan-data.json', merged_data):
        print("❌ Failed to save merged data!")
        return False
    
    # Report results
    print()
    print("=" * 80)
    print("✅ Merge completed successfully!")
    print("=" * 80)
    print()
    print("📊 Merge Summary:")
    print(f"   From plan-data121.json:")
    print(f"      📝 New inspection entries: {new_from_121}")
    print(f"      👥 New inspectors: {new_insp_121}")
    print(f"      🏘️  New areas: {new_area_121}")
    print(f"      🏪 New shops: {new_shop_121}")
    print(f"      🔔 New notifications: {new_notif_121}")
    print()
    print(f"   From plan-data131.json:")
    print(f"      📝 New inspection entries: {new_from_131}")
    print(f"      👥 New inspectors: {new_insp_131}")
    print(f"      🏘️  New areas: {new_area_131}")
    print(f"      🏪 New shops: {new_shop_131}")
    print(f"      🔔 New notifications: {new_notif_131}")
    print()
    print(f"   ⚠️  Conflicts (kept existing): {len(all_conflicts)}")
    print()
    print(f"📈 Final counts:")
    print(f"   📝 Total inspection entries: {len(merged_data.get('inspectionData', []))}")
    print(f"   👥 Total inspectors: {len(merged_data.get('inspectors', []))}")
    print(f"   🏘️  Total areas: {len(merged_data.get('areas', []))}")
    print(f"   🏪 Total shops: {len(merged_data.get('shops', []))}")
    print(f"   🔔 Total notifications: {len(merged_data.get('bellNotes', {}).get('notifications', []))}")
    print(f"   📅 Last update: {merged_data.get('lastUpdate')}")
    print()
    print("=" * 80)
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
