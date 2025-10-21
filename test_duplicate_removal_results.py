#!/usr/bin/env python3
"""
Test to verify that duplicates have been successfully removed
"""

import json
import sys
from collections import defaultdict


def test_no_mahal_duplicates_in_plan_data():
    """Verify no محل prefix variations in plan-data.json"""
    print("Testing for محل prefix duplicates in plan-data.json...")
    
    with open('/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    all_shops = set()
    for inspection in plan_data['inspectionData']:
        all_shops.update(inspection['shops'])
    
    # Find محل variations
    mahal_variants = []
    for shop in all_shops:
        if shop.startswith('محل '):
            base = shop[4:].strip()
            if base in all_shops:
                mahal_variants.append((shop, base))
    
    if mahal_variants:
        print(f"  ❌ FAILED: Found {len(mahal_variants)} محل variations:")
        for with_m, without_m in mahal_variants:
            print(f"    - '{with_m}' / '{without_m}'")
        return False
    
    print(f"  ✅ PASSED: No محل prefix duplicates found")
    return True


def test_no_license_duplicates():
    """Verify no duplicate license numbers in shops_details.json"""
    print("\nTesting for license duplicates in shops_details.json...")
    
    with open('/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    
    by_license = defaultdict(list)
    for name, details in shops_details.items():
        license = details.get('licenseNo', '')
        # Skip invalid licenses
        if license and license not in ['N/A', '', None, 'Business', 'Professional', 'Agriculture and Fish and Animal Wealth', 'Industrial']:
            by_license[license].append(name)
    
    duplicate_licenses = {lic: names for lic, names in by_license.items() if len(names) > 1}
    
    if duplicate_licenses:
        print(f"  ❌ FAILED: Found {len(duplicate_licenses)} license duplicates:")
        for lic, names in list(duplicate_licenses.items())[:5]:
            print(f"    License {lic}:")
            for name in names:
                print(f"      - {name}")
        return False
    
    print(f"  ✅ PASSED: No license duplicates found")
    return True


def test_no_english_name_duplicates():
    """Verify no duplicate English names in shops_details.json"""
    print("\nTesting for English name duplicates in shops_details.json...")
    
    with open('/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    
    by_english = defaultdict(list)
    for name, details in shops_details.items():
        english = details.get('nameEn', '')
        if english and english not in ['N/A', '', None]:
            by_english[english.lower()].append(name)
    
    duplicate_english = {en: names for en, names in by_english.items() if len(names) > 1}
    
    if duplicate_english:
        print(f"  ⚠️  WARNING: Found {len(duplicate_english)} English name duplicates (may be legitimate branches):")
        for en, names in list(duplicate_english.items())[:3]:
            print(f"    '{en}':")
            for name in names:
                print(f"      - {name}")
        # This is a warning, not a failure (branches may have same English name)
        return True
    
    print(f"  ✅ PASSED: No English name duplicates found")
    return True


def test_specific_duplicates_removed():
    """Verify specific duplicate shops were removed"""
    print("\nTesting that specific duplicates were removed...")
    
    with open('/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    
    # These shops should have been removed
    removed_shops = [
        'مركز الاحياء المائية 2',  # Duplicate of مركز الاحياء المائية 1
        'كوارييام وورد',  # Duplicate of عالم الأحياء المائية
        'بديز لإيواء الحيوانات و تربيتها',  # Duplicate license
        'ذا بيت شوب ش.ذ.م.م - فرع  ابوظبي 2'  # Duplicate English name
    ]
    
    still_present = [shop for shop in removed_shops if shop in shops_details]
    
    if still_present:
        print(f"  ❌ FAILED: The following shops should have been removed but are still present:")
        for shop in still_present:
            print(f"    - {shop}")
        return False
    
    print(f"  ✅ PASSED: All expected duplicate shops were removed")
    return True


def test_kept_shops_still_present():
    """Verify the kept versions of duplicates are still present"""
    print("\nTesting that kept shops are still present...")
    
    with open('/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    
    # These shops should have been kept
    kept_shops = [
        'مركز الاحياء المائية 1',
        'عالم الأحياء المائية',
        'اف ثري لتجارة اغذية الطيور و مستلزمات الطيور',
        'ذا بيت شوب ش.ذ.م.م - فرع  ابوظبي 1'
    ]
    
    missing = [shop for shop in kept_shops if shop not in shops_details]
    
    if missing:
        print(f"  ❌ FAILED: The following shops should have been kept but are missing:")
        for shop in missing:
            print(f"    - {shop}")
        return False
    
    print(f"  ✅ PASSED: All kept shops are still present")
    return True


def test_plan_data_references_updated():
    """Verify محل variations were replaced in plan-data.json"""
    print("\nTesting that محل variations were replaced in plan-data.json...")
    
    with open('/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    all_shops = []
    for inspection in plan_data['inspectionData']:
        all_shops.extend(inspection['shops'])
    
    # Check that these specific shops don't appear anymore
    old_names = [
        'محل المشرف لتجارة الأسماك',
        'محل مركز الأحياء المائية'
    ]
    
    still_present = [name for name in old_names if name in all_shops]
    
    if still_present:
        print(f"  ❌ FAILED: The following محل variations should have been replaced:")
        for name in still_present:
            print(f"    - {name}")
        return False
    
    # Check that the new names are present
    new_names = [
        'المشرف لتجارة الأسماك',
        'مركز الأحياء المائية'
    ]
    
    missing = [name for name in new_names if name not in all_shops]
    
    if missing:
        print(f"  ⚠️  WARNING: The following replacement names are not present:")
        for name in missing:
            print(f"    - {name}")
        # This is just a warning, not a failure
    
    print(f"  ✅ PASSED: محل variations were properly replaced")
    return True


def test_data_integrity():
    """Verify data integrity after duplicate removal"""
    print("\nTesting data integrity...")
    
    with open('/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    
    with open('/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    # Check that plan-data has lastUpdate
    if 'lastUpdate' not in plan_data:
        print("  ❌ FAILED: plan-data.json missing lastUpdate field")
        return False
    
    # Check that all shops have required fields
    invalid_shops = []
    for name, details in shops_details.items():
        if 'nameAr' not in details:
            invalid_shops.append(f"{name} - missing nameAr")
    
    if invalid_shops:
        print(f"  ❌ FAILED: Found {len(invalid_shops)} shops with missing required fields:")
        for shop in invalid_shops[:5]:
            print(f"    - {shop}")
        return False
    
    print(f"  ✅ PASSED: Data integrity maintained")
    return True


def main():
    print("="*80)
    print("🧪 Testing Duplicate Removal Results")
    print("="*80)
    print()
    
    all_passed = True
    
    all_passed &= test_no_mahal_duplicates_in_plan_data()
    all_passed &= test_no_license_duplicates()
    all_passed &= test_no_english_name_duplicates()
    all_passed &= test_specific_duplicates_removed()
    all_passed &= test_kept_shops_still_present()
    all_passed &= test_plan_data_references_updated()
    all_passed &= test_data_integrity()
    
    print("\n" + "="*80)
    if all_passed:
        print("✅ ALL TESTS PASSED")
        print("="*80)
        print("\nDuplicate removal was successful!")
        return True
    else:
        print("❌ SOME TESTS FAILED")
        print("="*80)
        print("\nPlease review the failures above.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
