#!/usr/bin/env python3
"""
Fix PR #333: Remove duplicate shop assignments in plan-data.json

Strategy:
1. For each shop assigned to multiple inspectors on the same day:
   - Keep the morning shift (صباحية) assignment
   - Remove from evening shift (مسائية) assignment
   - If both are same shift, keep the first occurrence

2. Update lastUpdate timestamp
3. Create detailed report of changes
"""

import json
import sys
from datetime import datetime
from collections import defaultdict

def load_plan_data(filepath):
    """Load plan-data.json"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_plan_data(filepath, data):
    """Save plan-data.json"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def find_duplicates(inspection_data):
    """Find all duplicate shop assignments"""
    shop_assignments = defaultdict(list)
    
    for idx, inspection in enumerate(inspection_data):
        day = inspection['day']
        inspector = inspection['inspector']
        shift = inspection.get('shift', 'N/A')
        
        for shop in inspection['shops']:
            key = f"{day}|{shop}"
            shop_assignments[key].append({
                'index': idx,
                'inspector': inspector,
                'day': day,
                'shop': shop,
                'shift': shift,
                'area': inspection.get('area', 'N/A')
            })
    
    # Return only duplicates
    return {k: v for k, v in shop_assignments.items() if len(v) > 1}

def resolve_duplicates(data):
    """
    Resolve duplicate shop assignments by removing shops from less preferred assignments
    
    Priority:
    1. Keep morning shift (صباحية) over evening shift (مسائية)
    2. If same shift, keep first occurrence
    """
    duplicates = find_duplicates(data['inspectionData'])
    
    if not duplicates:
        print("✅ No duplicates found!")
        return data, []
    
    print(f"🔍 Found {len(duplicates)} duplicate shop assignments")
    print("="*80)
    
    changes = []
    
    for dup_key, assignments in duplicates.items():
        day, shop = dup_key.split('|')
        
        # Sort by shift priority: صباحية first, then by index
        # This ensures morning shift is kept, and if tied, first occurrence
        sorted_assignments = sorted(assignments, key=lambda x: (
            0 if x['shift'] == 'صباحية' else 1,  # Morning shift first
            x['index']  # Then by occurrence order
        ))
        
        # Keep the first (highest priority) assignment
        keep_assignment = sorted_assignments[0]
        remove_assignments = sorted_assignments[1:]
        
        print(f"\n📅 {day} - 🏪 {shop}")
        print(f"   ✅ KEEP: {keep_assignment['inspector']} ({keep_assignment['shift']}, Index: {keep_assignment['index']})")
        
        # Remove shop from the other assignments
        for remove_assignment in remove_assignments:
            idx = remove_assignment['index']
            inspector = remove_assignment['inspector']
            
            # Remove the shop from this inspection
            if shop in data['inspectionData'][idx]['shops']:
                data['inspectionData'][idx]['shops'].remove(shop)
                
                print(f"   ❌ REMOVE FROM: {inspector} ({remove_assignment['shift']}, Index: {idx})")
                
                changes.append({
                    'day': day,
                    'shop': shop,
                    'removed_from': inspector,
                    'removed_shift': remove_assignment['shift'],
                    'kept_with': keep_assignment['inspector'],
                    'kept_shift': keep_assignment['shift']
                })
    
    print("\n" + "="*80)
    print(f"✅ Resolved {len(changes)} duplicate assignments")
    
    return data, changes

def main():
    print("="*80)
    print("🔧 PR #333: Fix Duplicate Shop Assignments")
    print("="*80)
    print()
    
    filepath = '/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/plan-data.json'
    
    # Load data
    print("📂 Loading plan-data.json...")
    data = load_plan_data(filepath)
    print(f"   ✅ Loaded {len(data['inspectionData'])} inspections")
    print()
    
    # Count shops before
    total_shops_before = sum(len(insp['shops']) for insp in data['inspectionData'])
    print(f"📊 Total shop assignments before: {total_shops_before}")
    print()
    
    # Resolve duplicates
    data, changes = resolve_duplicates(data)
    print()
    
    # Count shops after
    total_shops_after = sum(len(insp['shops']) for insp in data['inspectionData'])
    print(f"📊 Total shop assignments after: {total_shops_after}")
    print(f"📉 Removed: {total_shops_before - total_shops_after} duplicate assignments")
    print()
    
    # Update timestamp
    data['lastUpdate'] = datetime.now().isoformat()
    
    # Save data
    print("💾 Saving updated plan-data.json...")
    save_plan_data(filepath, data)
    print("   ✅ Saved successfully!")
    print()
    
    # Summary
    print("="*80)
    print("✅ PR #333 FIX COMPLETED")
    print("="*80)
    print()
    print("📋 Summary:")
    print(f"   • Duplicate shop assignments found: {len(changes)}")
    print(f"   • Duplicate assignments removed: {len(changes)}")
    print(f"   • Total shop assignments reduced: {total_shops_before} → {total_shops_after}")
    print()
    print("🎯 Strategy Applied:")
    print("   • Kept morning shift (صباحية) assignments")
    print("   • Removed evening shift (مسائية) duplicates")
    print("   • Maintained data integrity")
    print()
    print("✅ Ready for validation!")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
