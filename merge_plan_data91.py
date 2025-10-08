#!/usr/bin/env python3
"""
Merge plan-data91.json into the main plan-data.json file.
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

def main():
    print("=== Plan Data Merge Tool ===")
    print("Merging plan-data91.json into plan-data.json")
    print()
    
    # Load files
    print("📂 Loading files...")
    main_data = load_json_file('plan-data.json')
    source_data = load_json_file('plan-data91.json')
    
    if not main_data or not source_data:
        print("❌ Failed to load required files!")
        return False
    
    print(f"✅ Main file loaded: {len(main_data.get('inspectionData', []))} inspection entries")
    print(f"✅ Source file loaded: {len(source_data.get('inspectionData', []))} inspection entries")
    print()
    
    # Create backup
    backup_filename = f"plan-data.json.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    print(f"💾 Creating backup: {backup_filename}")
    if not save_json_file(backup_filename, main_data):
        print("❌ Failed to create backup!")
        return False
    
    # Merge data
    print("🔄 Merging data...")
    merged_data = main_data.copy()
    
    # Merge inspection data
    merged_inspections, new_inspections = merge_inspection_data(main_data, source_data)
    merged_data['inspectionData'] = merged_inspections
    
    # Merge inspectors
    merged_inspectors, new_inspectors = merge_list_data(
        main_data.get('inspectors', []), 
        source_data.get('inspectors', [])
    )
    merged_data['inspectors'] = merged_inspectors
    
    # Merge areas
    merged_areas, new_areas = merge_list_data(
        main_data.get('areas', []), 
        source_data.get('areas', [])
    )
    merged_data['areas'] = merged_areas
    
    # Merge shops
    merged_shops, new_shops = merge_list_data(
        main_data.get('shops', []), 
        source_data.get('shops', [])
    )
    merged_data['shops'] = merged_shops
    
    # Merge bell notifications
    merged_bell, new_notifications = merge_bell_notes(main_data, source_data)
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
    print("✅ Merge completed successfully!")
    print("📊 Merge Summary:")
    print(f"   📝 New inspection entries added: {new_inspections}")
    print(f"   👥 New inspectors added: {new_inspectors}")
    print(f"   🏘️  New areas added: {new_areas}")
    print(f"   🏪 New shops added: {new_shops}")
    print(f"   🔔 New notifications added: {new_notifications}")
    print()
    print(f"📈 Final counts:")
    print(f"   📝 Total inspection entries: {len(merged_data.get('inspectionData', []))}")
    print(f"   👥 Total inspectors: {len(merged_data.get('inspectors', []))}")
    print(f"   🏘️  Total areas: {len(merged_data.get('areas', []))}")
    print(f"   🏪 Total shops: {len(merged_data.get('shops', []))}")
    print(f"   🔔 Total notifications: {len(merged_data.get('bellNotes', {}).get('notifications', []))}")
    print(f"   📅 Last update: {merged_data.get('lastUpdate')}")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
