#!/usr/bin/env python3
"""
Test the duplicate removal logic before applying it to real data
"""

import json
import sys
from remove_duplicate_shops import (
    normalize_shop_name,
    score_shop_completeness,
    find_mahal_duplicates,
    find_license_duplicates,
    find_english_name_duplicates,
    merge_shop_details
)


def test_normalize_shop_name():
    """Test shop name normalization"""
    print("Testing normalize_shop_name()...")
    
    assert normalize_shop_name("محل المشرف") == "المشرف"
    assert normalize_shop_name("المشرف") == "المشرف"
    assert normalize_shop_name("  محل العيادة  ") == "العيادة"
    
    print("  ✅ All normalization tests passed")


def test_score_completeness():
    """Test completeness scoring"""
    print("\nTesting score_shop_completeness()...")
    
    # Complete shop
    complete = {
        'nameEn': 'Test Shop',
        'licenseNo': 'CN-12345',
        'locationMap': 'https://maps.google.com/...',
        'address': 'Test Address',
        'contact': '0501234567'
    }
    score_complete = score_shop_completeness('تست', complete)
    
    # Incomplete shop
    incomplete = {
        'nameEn': 'N/A',
        'licenseNo': '',
        'locationMap': '',
        'address': '',
        'contact': ''
    }
    score_incomplete = score_shop_completeness('محل تست', incomplete)
    
    assert score_complete > score_incomplete
    print(f"  Complete shop score: {score_complete}")
    print(f"  Incomplete shop score: {score_incomplete}")
    print("  ✅ Completeness scoring works correctly")


def test_find_mahal_duplicates():
    """Test finding محل prefix duplicates"""
    print("\nTesting find_mahal_duplicates()...")
    
    test_shops = {
        'محل المشرف': {'nameEn': 'Test 1'},
        'المشرف': {'nameEn': 'Test 2'},
        'محل العيادة': {'nameEn': 'Clinic'},
        'المركز': {'nameEn': 'Center'}
    }
    
    duplicates = find_mahal_duplicates(test_shops)
    
    assert len(duplicates) == 1
    assert ('محل المشرف', 'المشرف') in duplicates
    
    print(f"  Found {len(duplicates)} duplicate pair(s)")
    print("  ✅ محل duplicate detection works correctly")


def test_merge_logic():
    """Test merging logic"""
    print("\nTesting merge_shop_details()...")
    
    # Shop with more complete data
    complete = {
        'nameEn': 'Complete Shop',
        'licenseNo': 'CN-12345',
        'locationMap': 'https://maps.google.com/...',
        'address': 'Address',
        'contact': '0501234567'
    }
    
    # Shop with less data
    incomplete = {
        'nameEn': 'N/A',
        'licenseNo': '',
        'locationMap': '',
        'address': '',
        'contact': ''
    }
    
    # Should keep the complete one
    keep_name, keep_details = merge_shop_details(
        'محل الكامل', complete,
        'الكامل', incomplete
    )
    
    assert keep_name == 'محل الكامل'
    assert keep_details == complete
    
    print(f"  Kept: {keep_name}")
    print("  ✅ Merge logic works correctly")


def test_with_real_data():
    """Test with actual data from the files"""
    print("\nTesting with real data...")
    
    # Load real data
    with open('/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/shops_details.json', 'r', encoding='utf-8') as f:
        shops = json.load(f)
    
    with open('/home/runner/work/Monthly_inspection_plan/Monthly_inspection_plan/plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    print(f"  Loaded {len(shops)} shops from shops_details.json")
    print(f"  Loaded {len(plan_data['inspectionData'])} inspections")
    
    # Find duplicates
    mahal_dups = find_mahal_duplicates(shops)
    license_dups = find_license_duplicates(shops)
    english_dups = find_english_name_duplicates(shops)
    
    print(f"\n  محل prefix duplicates: {len(mahal_dups)}")
    if mahal_dups:
        for with_m, without_m in mahal_dups[:5]:
            print(f"    - {with_m} / {without_m}")
    
    print(f"\n  License duplicates: {len(license_dups)} groups")
    for i, (lic, names) in enumerate(list(license_dups.items())[:3]):
        print(f"    License {lic}: {len(names)} shops")
        for name in names[:3]:
            print(f"      - {name}")
    
    print(f"\n  English name duplicates: {len(english_dups)} groups")
    for i, (eng, names) in enumerate(list(english_dups.items())[:3]):
        print(f"    '{eng}': {len(names)} shops")
        for name in names:
            print(f"      - {name}")
    
    # Check plan-data for محل variations
    plan_shops = set()
    for inspection in plan_data['inspectionData']:
        plan_shops.update(inspection['shops'])
    
    plan_mahal_variants = []
    for shop in plan_shops:
        if shop.startswith('محل '):
            base = shop[4:].strip()
            if base in plan_shops:
                plan_mahal_variants.append((shop, base))
    
    print(f"\n  محل variants in plan-data.json: {len(plan_mahal_variants)}")
    if plan_mahal_variants:
        for with_m, without_m in plan_mahal_variants:
            print(f"    - '{with_m}' / '{without_m}'")
    
    print("\n  ✅ Real data analysis complete")


def main():
    print("="*80)
    print("🧪 Testing Duplicate Removal Logic")
    print("="*80)
    print()
    
    try:
        test_normalize_shop_name()
        test_score_completeness()
        test_find_mahal_duplicates()
        test_merge_logic()
        test_with_real_data()
        
        print("\n" + "="*80)
        print("✅ ALL TESTS PASSED")
        print("="*80)
        print("\nThe duplicate removal script is ready to run!")
        
        return True
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
