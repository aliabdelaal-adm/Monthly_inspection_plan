#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for area name extraction functionality
Tests the extract_area_name function with various address formats
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from merge_new_pet_shop_licenses import extract_area_name

def test_area_name_extraction():
    """Test the area name extraction with various formats"""
    
    test_cases = [
        # (input_address, expected_output)
        ("شمال الوثبة, شمال الوثبة 59, ق 10 - مستودع 31, وحدة, دائرة بلدية ابوظبي", "شمال الوثبة"),
        ("المصفح, م 43, 0 : ~, مبنى, السيد غانم حبروت سيف", "المصفح"),
        ("الوثبة, مسلخ الوثبة - زريبة 39, بناية / بلدية أبوظبي", "الوثبة"),
        ("مصفح جنوب, ايكاد 3, 0 : ~, مبنى", "مصفح جنوب"),
        ("أبو ظبي - شارع الميناء - بناية دائرة بلدية أبوظبي", "أبو ظبي"),
        ("ابو ظبي - بني ياس - شرق 11 - مصلخ البلدية", "ابو ظبي"),
        ("جزيرة أبوظبي, شارع حمدان, بناية درويش بن كرم", "جزيرة أبوظبي"),
        ("مدينة الرياض, مدينة الرياض 109, 0 : ~, مبنى", "مدينة الرياض"),
        ("ميناء زايد, المنطقة الحرة, 0 : ~, مبنى", "ميناء زايد"),
        ("أبوظبي, ابو ظبي - شارع الميناء الحر -432, مستودع", "أبوظبي"),
        ("أبو ظبي, الرحبة  مزرعة : 1026, مبنى", "أبو ظبي"),
        ("مصفح, م 41 ايكاد 2, المؤسسة العليا للمناطق الصناعية", "مصفح"),
        # Test edge cases
        ("سوق الميناء", "سوق الميناء"),  # Already simple
        ("سوق التراث", "سوق التراث"),  # Already simple
        ("", ""),  # Empty
        (None, ""),  # None
    ]
    
    print("="*80)
    print("Testing Area Name Extraction Function")
    print("="*80)
    print()
    
    passed = 0
    failed = 0
    
    for i, (input_addr, expected) in enumerate(test_cases, 1):
        result = extract_area_name(input_addr)
        
        if result == expected:
            print(f"✅ Test {i}: PASSED")
            passed += 1
        else:
            print(f"❌ Test {i}: FAILED")
            print(f"   Input:    {input_addr}")
            print(f"   Expected: {expected}")
            print(f"   Got:      {result}")
            failed += 1
        
        if i % 5 == 0:
            print()  # Add spacing for readability
    
    print()
    print("="*80)
    print(f"Test Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("="*80)
    
    return failed == 0

if __name__ == '__main__':
    success = test_area_name_extraction()
    sys.exit(0 if success else 1)
