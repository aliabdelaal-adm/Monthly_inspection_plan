#!/usr/bin/env python3
"""
Test script for duplicate shop validation functionality.
Tests the validation function to ensure duplicate shops are detected correctly.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
from merge_plan_data import validate_shop_duplicates

def test_no_duplicates():
    """Test case where there are no duplicate shops on the same day."""
    print("Test 1: No duplicates")
    print("-" * 50)
    
    inspection_data = [
        {
            "inspector": "د. آمنه بن صرم",
            "day": "2025-09-26",
            "shift": "صباحية",
            "area": "سوق الميناء",
            "shops": ["محل بيت الطيور", "محل الميناء للطيور"]
        },
        {
            "inspector": "د. آيه سلامة",
            "day": "2025-09-26",
            "shift": "صباحية",
            "area": "الحصن",
            "shops": ["محل فورس أند فيذرس", "محل أكوا ريست هب"]
        }
    ]
    
    is_valid, duplicates = validate_shop_duplicates(inspection_data)
    
    if is_valid and len(duplicates) == 0:
        print("✅ PASSED: No duplicates detected as expected")
        return True
    else:
        print(f"❌ FAILED: Expected no duplicates but found {len(duplicates)}")
        return False

def test_with_duplicates_same_day():
    """Test case where same shop is assigned to multiple inspectors on the same day."""
    print("\nTest 2: Duplicates on same day")
    print("-" * 50)
    
    inspection_data = [
        {
            "inspector": "د. آمنه بن صرم",
            "day": "2025-09-26",
            "shift": "صباحية",
            "area": "سوق الميناء",
            "shops": ["محل بيت الطيور", "محل الميناء للطيور"]
        },
        {
            "inspector": "د. آيه سلامة",
            "day": "2025-09-26",
            "shift": "مسائية",
            "area": "سوق الميناء",
            "shops": ["محل بيت الطيور", "محل أكوا ريست هب"]  # محل بيت الطيور مكرر
        }
    ]
    
    is_valid, duplicates = validate_shop_duplicates(inspection_data)
    
    if not is_valid and len(duplicates) == 1:
        dup = duplicates[0]
        if (dup['shop'] == "محل بيت الطيور" and 
            dup['day'] == "2025-09-26" and
            len(dup['inspectors']) == 2):
            print("✅ PASSED: Duplicate detected correctly")
            print(f"   Shop: {dup['shop']}")
            print(f"   Day: {dup['day']}")
            print(f"   Inspectors: {', '.join(dup['inspectors'])}")
            return True
    
    print(f"❌ FAILED: Expected 1 duplicate but found {len(duplicates)}")
    return False

def test_same_shop_different_days():
    """Test case where same shop is assigned on different days (should be valid)."""
    print("\nTest 3: Same shop on different days (valid)")
    print("-" * 50)
    
    inspection_data = [
        {
            "inspector": "د. آمنه بن صرم",
            "day": "2025-09-26",
            "shift": "صباحية",
            "area": "سوق الميناء",
            "shops": ["محل بيت الطيور"]
        },
        {
            "inspector": "د. آيه سلامة",
            "day": "2025-09-27",  # يوم مختلف
            "shift": "صباحية",
            "area": "سوق الميناء",
            "shops": ["محل بيت الطيور"]  # نفس المحل لكن في يوم مختلف
        }
    ]
    
    is_valid, duplicates = validate_shop_duplicates(inspection_data)
    
    if is_valid and len(duplicates) == 0:
        print("✅ PASSED: Same shop on different days is allowed")
        return True
    else:
        print(f"❌ FAILED: Expected no duplicates but found {len(duplicates)}")
        return False

def test_multiple_duplicates():
    """Test case with multiple duplicate shops."""
    print("\nTest 4: Multiple duplicates")
    print("-" * 50)
    
    inspection_data = [
        {
            "inspector": "د. آمنه بن صرم",
            "day": "2025-09-26",
            "shift": "صباحية",
            "area": "سوق الميناء",
            "shops": ["محل أ", "محل ب"]
        },
        {
            "inspector": "د. آيه سلامة",
            "day": "2025-09-26",
            "shift": "صباحية",
            "area": "الحصن",
            "shops": ["محل أ", "محل ج"]  # محل أ مكرر
        },
        {
            "inspector": "د. حسينة العامري",
            "day": "2025-09-26",
            "shift": "مسائية",
            "area": "سوق الميناء",
            "shops": ["محل ب", "محل د"]  # محل ب مكرر
        }
    ]
    
    is_valid, duplicates = validate_shop_duplicates(inspection_data)
    
    if not is_valid and len(duplicates) == 2:
        print("✅ PASSED: Multiple duplicates detected correctly")
        for dup in duplicates:
            print(f"   Shop: {dup['shop']}, Inspectors: {len(dup['inspectors'])}")
        return True
    else:
        print(f"❌ FAILED: Expected 2 duplicates but found {len(duplicates)}")
        return False

def main():
    print("=" * 50)
    print("🧪 Testing Duplicate Shop Validation")
    print("=" * 50)
    
    results = []
    results.append(test_no_duplicates())
    results.append(test_with_duplicates_same_day())
    results.append(test_same_shop_different_days())
    results.append(test_multiple_duplicates())
    
    print("\n" + "=" * 50)
    print("📊 Test Summary")
    print("=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("✅ All tests passed!")
        return True
    else:
        print(f"❌ {total - passed} test(s) failed")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
