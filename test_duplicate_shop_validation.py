#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify duplicate shop validation works correctly.
This tests the validation function for preventing duplicate shop assignments.
"""

import json
import sys
import io
from datetime import datetime

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def validate_shop_duplicates(inspection_data):
    """Validate that no shop is assigned to multiple inspectors on the same day.
    
    Only applies validation to dates from October 7, 2024 onwards.
    
    Returns:
        tuple: (is_valid, duplicate_info_list)
    """
    # Track shop assignments by day: {day: {shop: [inspector1, inspector2, ...]}}
    day_shop_inspectors = {}
    duplicates = []
    
    # Date cutoff: Only apply validation from October 7, 2024 onwards
    VALIDATION_START_DATE = datetime(2024, 10, 7)
    
    for entry in inspection_data:
        day = entry.get('day')
        inspector = entry.get('inspector')
        shops = entry.get('shops', [])
        
        if not day or not inspector or not shops:
            continue
        
        # Skip validation for dates before October 7, 2024
        try:
            entry_date = datetime.strptime(day, '%Y-%m-%d')
            if entry_date < VALIDATION_START_DATE:
                continue
        except ValueError:
            continue
            
        if day not in day_shop_inspectors:
            day_shop_inspectors[day] = {}
        
        for shop in shops:
            if shop not in day_shop_inspectors[day]:
                day_shop_inspectors[day][shop] = []
            day_shop_inspectors[day][shop].append(inspector)
    
    # Find duplicates
    for day, shops_dict in day_shop_inspectors.items():
        for shop, inspectors in shops_dict.items():
            if len(inspectors) > 1:
                duplicates.append({
                    'day': day,
                    'shop': shop,
                    'inspectors': inspectors
                })
    
    is_valid = len(duplicates) == 0
    return is_valid, duplicates

def test_case_1():
    """Test: No duplicates - should pass"""
    print("Test 1: No duplicates")
    print("-" * 60)
    
    inspection_data = [
        {
            "inspector": "د. آمنه بن صرم",
            "day": "2025-10-24",
            "shops": ["محل أ", "محل ب"]
        },
        {
            "inspector": "د. هاجر الغافري",
            "day": "2025-10-24",
            "shops": ["محل ج", "محل د"]
        }
    ]
    
    is_valid, duplicates = validate_shop_duplicates(inspection_data)
    
    if is_valid and len(duplicates) == 0:
        print("✅ PASSED: No duplicates detected\n")
        return True
    else:
        print(f"❌ FAILED: Expected no duplicates but found {len(duplicates)}\n")
        return False

def test_case_2():
    """Test: Duplicate shops on same day - should fail"""
    print("Test 2: Duplicate shops on same day")
    print("-" * 60)
    
    inspection_data = [
        {
            "inspector": "د. آمنه بن صرم",
            "day": "2025-10-24",
            "shops": ["محل أ", "محل ب"]
        },
        {
            "inspector": "د. هاجر الغافري",
            "day": "2025-10-24",
            "shops": ["محل أ", "محل د"]  # محل أ is duplicated
        }
    ]
    
    is_valid, duplicates = validate_shop_duplicates(inspection_data)
    
    if not is_valid and len(duplicates) == 1:
        dup = duplicates[0]
        if (dup['shop'] == "محل أ" and 
            dup['day'] == "2025-10-24" and
            len(dup['inspectors']) == 2):
            print(f"✅ PASSED: Duplicate detected correctly")
            print(f"   Shop: {dup['shop']}")
            print(f"   Inspectors: {', '.join(dup['inspectors'])}\n")
            return True
    
    print(f"❌ FAILED: Expected 1 duplicate but found {len(duplicates)}\n")
    return False

def test_case_3():
    """Test: Same shop on different days - should pass"""
    print("Test 3: Same shop on different days")
    print("-" * 60)
    
    inspection_data = [
        {
            "inspector": "د. آمنه بن صرم",
            "day": "2025-10-24",
            "shops": ["محل أ"]
        },
        {
            "inspector": "د. هاجر الغافري",
            "day": "2025-10-25",  # Different day
            "shops": ["محل أ"]
        }
    ]
    
    is_valid, duplicates = validate_shop_duplicates(inspection_data)
    
    if is_valid and len(duplicates) == 0:
        print("✅ PASSED: Same shop on different days is allowed\n")
        return True
    else:
        print(f"❌ FAILED: Expected no duplicates but found {len(duplicates)}\n")
        return False

def test_case_4():
    """Test: Multiple duplicate shops - should fail"""
    print("Test 4: Multiple duplicate shops")
    print("-" * 60)
    
    inspection_data = [
        {
            "inspector": "د. آمنه بن صرم",
            "day": "2025-10-24",
            "shops": ["محل أ", "محل ب", "محل ج"]
        },
        {
            "inspector": "د. هاجر الغافري",
            "day": "2025-10-24",
            "shops": ["محل أ", "محل ب", "محل د"]  # محل أ و محل ب duplicated
        }
    ]
    
    is_valid, duplicates = validate_shop_duplicates(inspection_data)
    
    if not is_valid and len(duplicates) == 2:
        print(f"✅ PASSED: Multiple duplicates detected correctly")
        for dup in duplicates:
            print(f"   - {dup['shop']}: {len(dup['inspectors'])} inspectors")
        print()
        return True
    else:
        print(f"❌ FAILED: Expected 2 duplicates but found {len(duplicates)}\n")
        return False

def test_case_5():
    """Test: Dates before Oct 7, 2024 are ignored - should pass"""
    print("Test 5: Dates before Oct 7, 2024 are ignored")
    print("-" * 60)
    
    inspection_data = [
        {
            "inspector": "د. آمنه بن صرم",
            "day": "2024-10-06",  # Before cutoff date
            "shops": ["محل أ", "محل ب"]
        },
        {
            "inspector": "د. هاجر الغافري",
            "day": "2024-10-06",  # Before cutoff date
            "shops": ["محل أ", "محل ب"]  # Same shops, but ignored
        }
    ]
    
    is_valid, duplicates = validate_shop_duplicates(inspection_data)
    
    if is_valid and len(duplicates) == 0:
        print("✅ PASSED: Dates before Oct 7, 2024 are correctly ignored\n")
        return True
    else:
        print(f"❌ FAILED: Expected no duplicates but found {len(duplicates)}\n")
        return False

def main():
    print("=" * 70)
    print("🧪 اختبار آلية منع تكرار المحلات")
    print("   Testing Duplicate Shop Prevention Validation")
    print("=" * 70)
    print()
    
    results = []
    results.append(test_case_1())
    results.append(test_case_2())
    results.append(test_case_3())
    results.append(test_case_4())
    results.append(test_case_5())
    
    print("=" * 70)
    print("📊 Test Summary / ملخص الاختبارات")
    print("=" * 70)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("✅ جميع الاختبارات نجحت!")
        print("✅ All tests passed!")
        return True
    else:
        print(f"❌ {total - passed} اختبار(ات) فشل")
        print(f"❌ {total - passed} test(s) failed")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
