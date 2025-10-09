#!/usr/bin/env python3
"""
Validation script to check for area ID issues in inspection data.

This script can be run anytime to verify that all inspections use proper 
area names instead of area IDs.

Usage:
    python3 validate_area_names.py
"""

import json
import sys
import io

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def validate_area_names():
    """Check if all inspections use proper area names."""
    
    print("🔍 Validating area names in inspection data...")
    print()
    
    try:
        with open('plan-data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Error loading plan-data.json: {e}")
        return False
    
    inspections = data.get('inspectionData', [])
    areas_list = data.get('areas', [])
    
    print(f"📊 Total inspections: {len(inspections)}")
    print(f"📊 Total areas: {len(areas_list)}")
    print()
    
    # Find inspections with area IDs instead of names
    issues = []
    for inspection in inspections:
        area = inspection.get('area', '')
        
        # Check if this looks like an area ID
        if area.startswith('area_') and area[5:].replace('_', '').isdigit():
            issues.append({
                'inspector': inspection.get('inspector', 'N/A'),
                'day': inspection.get('day', 'N/A'),
                'area': area,
                'shift': inspection.get('shift', 'N/A')
            })
    
    if issues:
        print(f"❌ Found {len(issues)} inspections with area IDs instead of names:")
        print()
        for issue in issues:
            print(f"  Inspector: {issue['inspector']}")
            print(f"  Date: {issue['day']}")
            print(f"  Area: {issue['area']} ← This should be a proper name")
            print(f"  Shift: {issue['shift']}")
            print()
        
        print("💡 To fix this issue, run: python3 fix_area_names_oct9_10.py")
        return False
    else:
        print("✅ All inspections use proper area names!")
        print()
        
        # Show some sample area names
        sample_areas = set()
        for inspection in inspections[:20]:
            sample_areas.add(inspection.get('area', ''))
        
        print("📝 Sample area names (first 10):")
        for area in sorted(list(sample_areas))[:10]:
            print(f"  • {area}")
        print()
        
        return True

if __name__ == "__main__":
    success = validate_area_names()
    
    if success:
        print("✅ Validation passed - all area names are correct!")
    else:
        print("❌ Validation failed - some issues need to be fixed")
    
    sys.exit(0 if success else 1)
