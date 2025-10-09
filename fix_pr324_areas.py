#!/usr/bin/env python3
"""
Fix PR #324: Remove 15 incorrectly added areas

Problem:
--------
PR #324 added 15 areas to plan-data.json that should NOT have been added:
- 13 areas with area IDs as names (e.g., "area_1758831413471" instead of "محمد بن زايد")
- 2 duplicate areas ("الحصن" and "سوق الميناء") that already existed

Solution:
---------
Remove these 15 areas and keep only the original 23 areas with correct Arabic names.

Author: Fix for PR #324
Date: October 2025
"""

import json
import sys
from datetime import datetime

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
    print("=" * 80)
    print("Fix PR #324: Remove Incorrectly Added Areas")
    print("=" * 80)
    print()
    
    # Load the plan-data.json from PR #324 branch
    print("📂 Loading plan-data.json from PR #324 branch...")
    data = load_json_file('plan-data.json')
    if not data:
        return False
    
    print(f"✅ Loaded successfully")
    print(f"   Current area count: {len(data.get('areas', []))}")
    print()
    
    # The 15 IDs that should be removed (these were incorrectly added in PR #324)
    incorrect_area_ids = [
        'area_1759930928836',  # name: area_1758831413471 (should be محمد بن زايد)
        'area_1759931062466',  # name: area_1758831448230 (should be المصفح)
        'area_1759931154959',  # name: area_1758831500163 (should be مدينة خليفة)
        'area_1759931231228',  # name: area_1758839353326 (should be سوق التراث)
        'area_1759931325657',  # name: area_1758839345230 (should be سوق الميناء)
        'area_1759931487027',  # name: area_1758831528008 (should be الوثبة جنوب)
        'area_1759931561485',  # name: area_1759754614634 (should be المشرف)
        'area_1759932183820',  # name: area_1758831360486 (should be الخالدية)
        'area_1759932266870',  # name: area_1758839345230 (should be سوق الميناء)
        'area_1759932485052',  # name: area_1758831340793 (should be الحصن)
        'area_1759932597806',  # name: area_1758839353326 (should be سوق التراث)
        'area_1759932745921',  # name: area_1758913423620 (should be آل نهيان)
        'area_1759933076366',  # name: area_1758831328093 (should be الدانة)
        'area_1727365643326',  # name: الحصن (DUPLICATE of area_1758831340793)
        'area_1727365653326',  # name: سوق الميناء (DUPLICATE of area_1758839345230)
    ]
    
    print("🔍 Analyzing incorrect areas...")
    areas = data.get('areas', [])
    incorrect_areas = []
    correct_areas = []
    
    for area in areas:
        if area['id'] in incorrect_area_ids:
            incorrect_areas.append(area)
        else:
            correct_areas.append(area)
    
    print(f"   Found {len(incorrect_areas)} incorrect areas to remove")
    print(f"   Keeping {len(correct_areas)} correct areas")
    print()
    
    if incorrect_areas:
        print("❌ Incorrect areas being removed:")
        for area in incorrect_areas:
            print(f"   - ID: {area['id']}, Name: {area['name']}")
        print()
    
    # Create backup
    backup_filename = f"plan-data.json.backup_pr324_fix_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    print(f"💾 Creating backup: {backup_filename}")
    if not save_json_file(backup_filename, data):
        print("❌ Failed to create backup!")
        return False
    print("✅ Backup created")
    print()
    
    # Update the areas array
    data['areas'] = correct_areas
    data['lastUpdate'] = datetime.now().isoformat()
    
    # Save the corrected data
    print("💾 Saving corrected plan-data.json...")
    if not save_json_file('plan-data.json', data):
        print("❌ Failed to save corrected data!")
        return False
    
    print("✅ Fix completed successfully!")
    print()
    print("📊 Summary:")
    print(f"   Areas before: {len(areas)}")
    print(f"   Areas removed: {len(incorrect_areas)}")
    print(f"   Areas after: {len(correct_areas)}")
    print(f"   Last update: {data['lastUpdate']}")
    print()
    print("=" * 80)
    print("✅ PR #324 has been corrected!")
    print("=" * 80)
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
