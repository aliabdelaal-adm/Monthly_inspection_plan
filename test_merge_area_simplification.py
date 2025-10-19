#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integration test for area name simplification in merge process
Verifies that area names are properly simplified when merging new licenses
"""

import sys
import os
import json
import openpyxl
import tempfile
import shutil

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from merge_new_pet_shop_licenses import extract_area_name, merge_to_json, generate_adm_code

def test_extract_area_name():
    """Test the extract_area_name function with real-world examples"""
    print("="*80)
    print("Test 1: Area Name Extraction")
    print("="*80)
    
    test_cases = [
        # Common patterns from the new licenses file
        ("شمال الوثبة, شمال الوثبة 59, ق 10 - مستودع 31", "شمال الوثبة"),
        ("المصفح, م 43, 0 : ~, مبنى", "المصفح"),
        ("مصفح جنوب, ايكاد 3, 0 : ~", "مصفح جنوب"),
        ("الوثبة, مسلخ الوثبة - زريبة 39", "الوثبة"),
        ("أبو ظبي - شارع الميناء - بناية", "أبو ظبي"),
        (" أبو ظبي - شارع  الميناء -  بناية دائرة بلدية أبوظبي, ", "أبو ظبي"),
        ("مدينة خليفة, مدينة خليفة أ - شارع 12", "مدينة خليفة"),
        ("الشهامة, الشهامة 35, م 4", "الشهامة"),
        ("الدانة, شارع الدانة - مبنى 5", "الدانة"),
        ("الحصن, الحصن - شارع 8", "الحصن"),
    ]
    
    passed = 0
    failed = 0
    
    for original, expected in test_cases:
        result = extract_area_name(original)
        if result == expected:
            print(f"✅ '{original[:50]}...' -> '{result}'")
            passed += 1
        else:
            print(f"❌ FAILED: '{original}'")
            print(f"   Expected: '{expected}'")
            print(f"   Got: '{result}'")
            failed += 1
    
    print(f"\nResult: {passed} passed, {failed} failed\n")
    return failed == 0

def test_merge_json_with_simplified_areas():
    """Test that merge_to_json properly uses simplified area names"""
    print("="*80)
    print("Test 2: JSON Merge with Simplified Areas")
    print("="*80)
    
    # Create sample shop data with detailed addresses
    sample_shops = [
        {
            'A': 'TEST-001',
            'B': 'محل اختبار الوثبة',
            'C': 'Test Shop Wathba',
            'M': 'test@example.com',
            'Q': 'شمال الوثبة, شمال الوثبة 59, ق 10 - مستودع 31, وحدة',
            'S': 'تجارة الحيوانات',
            'T': 'Animal Trading'
        },
        {
            'A': 'TEST-002',
            'B': 'محل اختبار المصفح',
            'C': 'Test Shop Musaffah',
            'M': 'test2@example.com',
            'Q': 'المصفح, م 43, 0 : ~, مبنى, السيد غانم',
            'S': 'تجارة الطيور',
            'T': 'Bird Trading'
        }
    ]
    
    # Create empty shops_details structure
    shops_details = {}
    
    # Merge the sample shops
    added = merge_to_json(sample_shops, shops_details)
    
    print(f"✅ Added {added} shops to JSON")
    
    # Verify that addresses are simplified
    passed = 0
    failed = 0
    
    for shop_name, shop_data in shops_details.items():
        address = shop_data.get('address', '')
        
        # Check that address doesn't contain detailed info
        if ',' not in address and '-' not in address:
            print(f"✅ {shop_name}: '{address}' (simplified)")
            passed += 1
        elif address in ['شمال الوثبة', 'المصفح']:  # Expected simplified names
            print(f"✅ {shop_name}: '{address}' (correctly simplified)")
            passed += 1
        else:
            print(f"❌ {shop_name}: '{address}' (still contains details)")
            failed += 1
    
    print(f"\nResult: {passed} passed, {failed} failed\n")
    return failed == 0

def test_common_area_examples():
    """Test extraction of common area names mentioned in the problem statement"""
    print("="*80)
    print("Test 3: Common Area Names from Problem Statement")
    print("="*80)
    
    # Areas mentioned in problem: الوثبة جنوب، المصفح، الشهامة، مدينة خليفة، الدانة، الحصن
    test_cases = [
        "الوثبة جنوب, شارع 12 - مبنى 5",
        "المصفح, م 43, ايكاد",
        "الشهامة, الشهامة 35, م 4",
        "مدينة خليفة, مدينة خليفة أ - شارع 12",
        "الدانة, شارع الدانة - مبنى 5",
        "الحصن, الحصن - شارع 8",
    ]
    
    expected_areas = [
        "الوثبة جنوب", "المصفح", "الشهامة", "مدينة خليفة", "الدانة", "الحصن"
    ]
    
    passed = 0
    failed = 0
    
    for address, expected in zip(test_cases, expected_areas):
        result = extract_area_name(address)
        if result == expected:
            print(f"✅ '{address}' -> '{result}'")
            passed += 1
        else:
            print(f"❌ '{address}'")
            print(f"   Expected: '{expected}'")
            print(f"   Got: '{result}'")
            failed += 1
    
    print(f"\nResult: {passed} passed, {failed} failed\n")
    return failed == 0

def main():
    """Run all integration tests"""
    print("\n")
    print("🧪 Integration Tests for Area Name Simplification")
    print("="*80)
    print()
    
    results = []
    
    # Run all tests
    results.append(("Area Name Extraction", test_extract_area_name()))
    results.append(("JSON Merge with Simplified Areas", test_merge_json_with_simplified_areas()))
    results.append(("Common Area Names", test_common_area_examples()))
    
    # Summary
    print("="*80)
    print("Test Summary")
    print("="*80)
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{status}: {test_name}")
        if not passed:
            all_passed = False
    
    print()
    
    if all_passed:
        print("✅ All integration tests passed!")
        return 0
    else:
        print("❌ Some tests failed")
        return 1

if __name__ == '__main__':
    sys.exit(main())
