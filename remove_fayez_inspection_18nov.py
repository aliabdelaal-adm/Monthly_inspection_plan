#!/usr/bin/env python3
"""
Script to remove the inspection for Dr. Fayez Al-Masalmeh on 18-11-2025 
from the shelter inspection table (shelterInspectionData)
"""

import json
import sys
from datetime import datetime

def remove_inspection():
    """Remove the specific inspection from shelterInspectionData"""
    
    # Read the current plan-data.json
    print("Reading plan-data.json...")
    try:
        with open('plan-data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Error reading plan-data.json: {e}")
        return False
    
    # Check if shelterInspectionData exists
    if 'shelterInspectionData' not in data:
        print("❌ shelterInspectionData not found in plan-data.json")
        return False
    
    # Find and remove the specific inspection
    target_date = "2025-11-18"
    target_inspector = "د. فايز المسالمة"
    
    print(f"\nSearching for inspection:")
    print(f"  Inspector: {target_inspector}")
    print(f"  Date: {target_date}")
    print(f"  Area: الملاجىء")
    
    # Filter out the inspection to be removed
    original_count = len(data['shelterInspectionData'])
    removed_items = []
    
    # Keep all inspections except the one we want to remove
    data['shelterInspectionData'] = [
        item for item in data['shelterInspectionData']
        if not (item.get('day') == target_date and 
                target_inspector in item.get('inspectors', []))
    ]
    
    # Calculate how many items were removed
    new_count = len(data['shelterInspectionData'])
    removed_count = original_count - new_count
    
    if removed_count == 0:
        print("\n❌ No matching inspection found to remove")
        return False
    
    print(f"\n✅ Successfully removed {removed_count} inspection(s)")
    print(f"   Original count: {original_count}")
    print(f"   New count: {new_count}")
    
    # Update lastUpdate timestamp
    data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Write the updated data back to plan-data.json
    print("\nWriting updated data to plan-data.json...")
    try:
        with open('plan-data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("✅ File updated successfully!")
        return True
    except Exception as e:
        print(f"❌ Error writing plan-data.json: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Remove Inspection for Dr. Fayez Al-Masalmeh (18-11-2025)")
    print("=" * 60)
    
    success = remove_inspection()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ Task completed successfully!")
        print("=" * 60)
        sys.exit(0)
    else:
        print("\n" + "=" * 60)
        print("❌ Task failed!")
        print("=" * 60)
        sys.exit(1)
