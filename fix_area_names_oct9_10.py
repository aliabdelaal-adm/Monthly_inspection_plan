#!/usr/bin/env python3
"""
Fix area names in inspection data for October 9-10, 2025.

This script replaces area IDs (like 'area_1758831413471') with their proper 
Arabic names in the inspection data.

Issue: Inspector reports show area IDs instead of proper area names for 
October 9 and 10 entries.
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

def main():
    print("🔧 Starting area names fix for October 9-10 inspections...")
    print()
    
    # Load plan-data.json
    print("📂 Loading plan-data.json...")
    data = load_json_file('plan-data.json')
    if not data:
        return False
    
    # Create backup
    backup_filename = f"plan-data.json.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    print(f"💾 Creating backup: {backup_filename}")
    if not save_json_file(backup_filename, data):
        print("❌ Failed to create backup!")
        return False
    
    # Build area ID to name mapping
    area_id_to_name = {}
    for area in data.get('areas', []):
        area_id_to_name[area['id']] = area['name']
    
    print(f"📋 Found {len(area_id_to_name)} areas in the database")
    print()
    
    # Find and fix inspections with area IDs instead of names
    fixed_count = 0
    inspections = data.get('inspectionData', [])
    
    print("🔍 Scanning inspections for area ID issues...")
    for inspection in inspections:
        area = inspection.get('area', '')
        
        # Check if this is an area ID (starts with 'area_' followed by digits)
        if area.startswith('area_') and area[5:].replace('_', '').isdigit():
            # This is an area ID, need to replace with name
            if area in area_id_to_name:
                old_area = area
                new_area = area_id_to_name[area]
                inspection['area'] = new_area
                fixed_count += 1
                
                day = inspection.get('day', 'N/A')
                inspector = inspection.get('inspector', 'N/A')
                print(f"  ✓ Fixed: {inspector} on {day}")
                print(f"    {old_area} → {new_area}")
            else:
                print(f"  ⚠️  Warning: Area ID '{area}' not found in areas list")
                print(f"    Inspector: {inspection.get('inspector', 'N/A')}")
                print(f"    Day: {inspection.get('day', 'N/A')}")
    
    print()
    print(f"📊 Fixed {fixed_count} inspection entries")
    
    if fixed_count > 0:
        # Update timestamp
        data['lastUpdate'] = datetime.now().isoformat()
        
        # Save updated data
        print("💾 Saving updated plan-data.json...")
        if not save_json_file('plan-data.json', data):
            print("❌ Failed to save updated data!")
            return False
        
        print()
        print("✅ Successfully fixed area names in inspection data!")
        print(f"📁 Backup saved as: {backup_filename}")
    else:
        print("ℹ️  No issues found - all area names are already correct")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
