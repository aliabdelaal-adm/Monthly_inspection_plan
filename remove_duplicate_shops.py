#!/usr/bin/env python3
"""
Remove and merge duplicate shops from the inspection plan system.

This script handles:
1. Exact duplicate shops (same name appearing multiple times)
2. Shops differing only by "محل" prefix
3. Shops with same license number or English name but different Arabic names

Strategy:
- Keep the version with more complete data (license, English name, location map)
- Merge references in plan-data.json to use the kept version
- Remove duplicates from shops_details.json
"""

import json
import sys
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Tuple, Set


def load_json(filepath: str) -> dict:
    """Load a JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(filepath: str, data: dict) -> None:
    """Save a JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def normalize_shop_name(name: str) -> str:
    """Normalize shop name by removing محل prefix"""
    normalized = name.strip()
    if normalized.startswith('محل '):
        normalized = normalized[4:].strip()
    return normalized


def score_shop_completeness(name: str, details: dict) -> int:
    """Score how complete a shop's details are (higher is better)"""
    score = 0
    
    # Check for English name
    if details.get('nameEn') and details['nameEn'] not in ['N/A', '', None]:
        score += 10
    
    # Check for license number
    if details.get('licenseNo') and details['licenseNo'] not in ['N/A', '', None, 'Business', 'Professional', 'Agriculture and Fish and Animal Wealth', 'Industrial']:
        score += 10
    
    # Check for location map
    if details.get('locationMap') and details['locationMap'] not in ['', None]:
        score += 5
    
    # Check for address
    if details.get('address') and details['address'] not in ['', None, 'N/A']:
        score += 3
    
    # Check for contact
    if details.get('contact') and details['contact'] not in ['', None, 'N/A']:
        score += 2
    
    # Prefer names without محل prefix (shorter)
    if not name.startswith('محل '):
        score += 1
    
    return score


def find_mahal_duplicates(shops_dict: Dict[str, dict]) -> List[Tuple[str, str]]:
    """Find shops that differ only by محل prefix"""
    duplicates = []
    shop_names = list(shops_dict.keys())
    
    for name in shop_names:
        if name.startswith('محل '):
            base_name = name[4:].strip()
            if base_name in shop_names:
                duplicates.append((name, base_name))
    
    return duplicates


def find_license_duplicates(shops_dict: Dict[str, dict]) -> Dict[str, List[str]]:
    """Find shops with the same license number"""
    by_license = defaultdict(list)
    
    for name, details in shops_dict.items():
        license = details.get('licenseNo', '')
        # Skip invalid licenses
        if license and license not in ['N/A', '', None, 'Business', 'Professional', 'Agriculture and Fish and Animal Wealth', 'Industrial']:
            by_license[license].append(name)
    
    # Return only duplicates
    return {lic: names for lic, names in by_license.items() if len(names) > 1}


def find_english_name_duplicates(shops_dict: Dict[str, dict]) -> Dict[str, List[str]]:
    """Find shops with the same English name"""
    by_english = defaultdict(list)
    
    for name, details in shops_dict.items():
        english = details.get('nameEn', '')
        if english and english not in ['N/A', '', None]:
            by_english[english.lower()].append(name)
    
    # Return only duplicates
    return {en: names for en, names in by_english.items() if len(names) > 1}


def merge_shop_details(name1: str, details1: dict, name2: str, details2: dict) -> Tuple[str, dict]:
    """Merge two shop entries, keeping the one with more complete data"""
    score1 = score_shop_completeness(name1, details1)
    score2 = score_shop_completeness(name2, details2)
    
    if score1 >= score2:
        return name1, details1
    else:
        return name2, details2


def remove_duplicates_from_shops_details(shops_dict: Dict[str, dict]) -> Tuple[Dict[str, dict], Dict[str, str]]:
    """
    Remove duplicates from shops_details.json
    Returns: (cleaned_dict, rename_map) where rename_map[old_name] = new_name
    """
    cleaned = shops_dict.copy()
    rename_map = {}  # Maps old names to new names
    removed_count = 0
    
    print("="*80)
    print("🔍 Finding duplicates in shops_details.json")
    print("="*80)
    
    # 1. Handle محل prefix duplicates
    mahal_dups = find_mahal_duplicates(shops_dict)
    print(f"\n📋 Found {len(mahal_dups)} محل prefix duplicate pairs")
    
    for with_mahal, without_mahal in mahal_dups:
        if with_mahal in cleaned and without_mahal in cleaned:
            # Merge and keep the better one
            keep_name, keep_details = merge_shop_details(
                with_mahal, cleaned[with_mahal],
                without_mahal, cleaned[without_mahal]
            )
            remove_name = without_mahal if keep_name == with_mahal else with_mahal
            
            print(f"\n  ✅ KEEP: {keep_name}")
            print(f"  ❌ REMOVE: {remove_name}")
            
            del cleaned[remove_name]
            rename_map[remove_name] = keep_name
            removed_count += 1
    
    # 2. Handle license duplicates
    license_dups = find_license_duplicates(shops_dict)
    print(f"\n📋 Found {len(license_dups)} license duplicate groups")
    
    for license, names in license_dups.items():
        if len(names) <= 1:
            continue
        
        # Keep the one with the best completeness score
        names_in_cleaned = [n for n in names if n in cleaned]
        if len(names_in_cleaned) <= 1:
            continue
        
        best_name = max(names_in_cleaned, key=lambda n: score_shop_completeness(n, cleaned[n]))
        
        print(f"\n  License: {license}")
        print(f"  ✅ KEEP: {best_name}")
        
        for name in names_in_cleaned:
            if name != best_name:
                print(f"  ❌ REMOVE: {name}")
                del cleaned[name]
                rename_map[name] = best_name
                removed_count += 1
    
    # 3. Handle English name duplicates (only if they're not already handled)
    english_dups = find_english_name_duplicates(cleaned)
    print(f"\n📋 Found {len(english_dups)} English name duplicate groups (after previous cleaning)")
    
    for english, names in english_dups.items():
        if len(names) <= 1:
            continue
        
        # Keep the one with the best completeness score
        best_name = max(names, key=lambda n: score_shop_completeness(n, cleaned[n]))
        
        print(f"\n  English: {english}")
        print(f"  ✅ KEEP: {best_name}")
        
        for name in names:
            if name != best_name:
                print(f"  ❌ REMOVE: {name}")
                del cleaned[name]
                rename_map[name] = best_name
                removed_count += 1
    
    print(f"\n📊 Total shops removed from shops_details.json: {removed_count}")
    print(f"📊 Shops before: {len(shops_dict)}, after: {len(cleaned)}")
    
    return cleaned, rename_map


def find_plan_data_mahal_duplicates(plan_data: dict) -> Dict[str, str]:
    """Find محل prefix variations in plan-data.json and return rename map"""
    # Get all unique shop names
    all_shops = set()
    for inspection in plan_data['inspectionData']:
        all_shops.update(inspection['shops'])
    
    rename_map = {}
    
    # Find shops with محل prefix that have a version without it
    for shop in all_shops:
        if shop.startswith('محل '):
            base_name = shop[4:].strip()
            if base_name in all_shops:
                # Prefer the version without محل (shorter)
                rename_map[shop] = base_name
    
    return rename_map


def update_plan_data_references(plan_data: dict, rename_map: Dict[str, str]) -> Tuple[dict, int]:
    """Update shop references in plan-data.json according to rename_map"""
    updates_count = 0
    
    print("\n" + "="*80)
    print("🔄 Updating shop references in plan-data.json")
    print("="*80)
    
    for inspection in plan_data['inspectionData']:
        new_shops = []
        for shop in inspection['shops']:
            if shop in rename_map:
                new_name = rename_map[shop]
                print(f"  📝 Renaming: {shop} → {new_name}")
                new_shops.append(new_name)
                updates_count += 1
            else:
                new_shops.append(shop)
        
        # Remove duplicates that might have been introduced by renaming
        inspection['shops'] = list(dict.fromkeys(new_shops))
    
    print(f"\n📊 Total shop references updated: {updates_count}")
    
    return plan_data, updates_count


def main():
    print("="*80)
    print("🔧 Remove and Merge Duplicate Shops")
    print("="*80)
    print()
    
    # File paths
    shops_details_path = '/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/shops_details.json'
    plan_data_path = '/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/plan-data.json'
    
    # Load data
    print("📂 Loading data files...")
    shops_details = load_json(shops_details_path)
    plan_data = load_json(plan_data_path)
    print(f"   ✅ Loaded {len(shops_details)} shops from shops_details.json")
    print(f"   ✅ Loaded {len(plan_data['inspectionData'])} inspections from plan-data.json")
    print()
    
    # Remove duplicates from shops_details.json
    cleaned_shops, rename_map_details = remove_duplicates_from_shops_details(shops_details)
    
    # Find محل duplicates in plan-data.json
    print("\n" + "="*80)
    print("🔍 Finding محل prefix duplicates in plan-data.json")
    print("="*80)
    
    rename_map_plan = find_plan_data_mahal_duplicates(plan_data)
    
    if rename_map_plan:
        print(f"\n📋 Found {len(rename_map_plan)} محل prefix variations in plan-data.json:")
        for old_name, new_name in rename_map_plan.items():
            print(f"  {old_name} → {new_name}")
    else:
        print("\n✅ No محل prefix variations found in plan-data.json")
    
    # Combine both rename maps
    combined_rename_map = {**rename_map_details, **rename_map_plan}
    
    # Update references in plan-data.json
    if combined_rename_map:
        updated_plan, updates_count = update_plan_data_references(plan_data, combined_rename_map)
        
        # Update timestamp
        updated_plan['lastUpdate'] = datetime.now().isoformat()
    else:
        print("\n✅ No shop references need updating in plan-data.json")
        updated_plan = plan_data
        updates_count = 0
    
    # Save updated files
    print("\n" + "="*80)
    print("💾 Saving updated files")
    print("="*80)
    
    save_json(shops_details_path, cleaned_shops)
    print(f"   ✅ Saved updated shops_details.json")
    
    save_json(plan_data_path, updated_plan)
    print(f"   ✅ Saved updated plan-data.json")
    
    # Summary
    print("\n" + "="*80)
    print("✅ DUPLICATE REMOVAL COMPLETED")
    print("="*80)
    print()
    print("📋 Summary:")
    print(f"   • Shops before: {len(shops_details)}")
    print(f"   • Shops after: {len(cleaned_shops)}")
    print(f"   • Duplicates removed: {len(shops_details) - len(cleaned_shops)}")
    print(f"   • Shop references updated in plan-data.json: {updates_count}")
    print()
    print("✅ Files updated successfully!")
    
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
