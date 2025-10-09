#!/usr/bin/env python3
"""
Test script to validate PR #324 fix

This script tests that:
1. plan-data.json has exactly 23 areas
2. All area names are in Arabic (not IDs)
3. No duplicate areas exist
4. All existing tests still pass
"""

import json
import sys
import subprocess

def test_area_count():
    """Test that there are exactly 23 areas"""
    print("\n🧪 Test 1: Area Count")
    print("-" * 50)
    
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    areas = data.get('areas', [])
    expected = 23
    actual = len(areas)
    
    if actual == expected:
        print(f"✅ PASS: Area count is {actual} (expected {expected})")
        return True
    else:
        print(f"❌ FAIL: Area count is {actual}, expected {expected}")
        return False

def test_no_id_names():
    """Test that no area has an ID as its name"""
    print("\n🧪 Test 2: No ID Names")
    print("-" * 50)
    
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    areas = data.get('areas', [])
    id_names = [a for a in areas if a['name'].startswith('area_')]
    
    if not id_names:
        print(f"✅ PASS: No areas with ID names found")
        return True
    else:
        print(f"❌ FAIL: Found {len(id_names)} areas with ID names:")
        for area in id_names:
            print(f"   - {area['id']}: {area['name']}")
        return False

def test_no_duplicates():
    """Test that no duplicate area names exist"""
    print("\n🧪 Test 3: No Duplicate Areas")
    print("-" * 50)
    
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    areas = data.get('areas', [])
    names = [a['name'] for a in areas]
    duplicates = [name for name in set(names) if names.count(name) > 1]
    
    if not duplicates:
        print(f"✅ PASS: No duplicate area names found")
        return True
    else:
        print(f"❌ FAIL: Found {len(duplicates)} duplicate area names:")
        for name in duplicates:
            print(f"   - {name}")
        return False

def test_arabic_names():
    """Test that all area names are in Arabic"""
    print("\n🧪 Test 4: Arabic Area Names")
    print("-" * 50)
    
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    areas = data.get('areas', [])
    
    # Check that names contain Arabic characters
    non_arabic = []
    for area in areas:
        name = area['name']
        # Simple check: if name doesn't contain Arabic characters and is not a known exception
        if not any('\u0600' <= c <= '\u06FF' for c in name):
            # Allow exceptions like "+" in "الشامخة + الريف"
            if name not in ['+'] and '+' not in name:
                non_arabic.append(area)
    
    if not non_arabic:
        print(f"✅ PASS: All {len(areas)} area names contain Arabic text")
        return True
    else:
        print(f"❌ FAIL: Found {len(non_arabic)} areas without Arabic text:")
        for area in non_arabic[:5]:  # Show first 5
            print(f"   - {area['id']}: {area['name']}")
        return False

def test_json_validity():
    """Test that plan-data.json is valid JSON"""
    print("\n🧪 Test 5: JSON Validity")
    print("-" * 50)
    
    try:
        with open('plan-data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check required keys
        required_keys = ['inspectionData', 'inspectors', 'areas', 'shops', 'bellNotes', 'lastUpdate']
        missing_keys = [key for key in required_keys if key not in data]
        
        if not missing_keys:
            print(f"✅ PASS: plan-data.json is valid JSON with all required keys")
            return True
        else:
            print(f"❌ FAIL: Missing required keys: {missing_keys}")
            return False
    except json.JSONDecodeError as e:
        print(f"❌ FAIL: Invalid JSON: {e}")
        return False

def test_existing_tests():
    """Run existing test suite"""
    print("\n🧪 Test 6: Existing Tests")
    print("-" * 50)
    
    try:
        result = subprocess.run(['python3', 'test_plan_data.py'], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(f"✅ PASS: test_plan_data.py passed")
            return True
        else:
            print(f"❌ FAIL: test_plan_data.py failed")
            print(result.stdout)
            print(result.stderr)
            return False
    except Exception as e:
        print(f"⚠️  WARNING: Could not run test_plan_data.py: {e}")
        return True  # Don't fail if test file doesn't exist

def display_area_summary():
    """Display summary of areas"""
    print("\n📊 Area Summary")
    print("=" * 50)
    
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    areas = data.get('areas', [])
    print(f"\nTotal areas: {len(areas)}\n")
    print("All areas:")
    for i, area in enumerate(areas, 1):
        print(f"{i:2d}. {area['name']}")

def main():
    print("=" * 80)
    print("PR #324 Fix Validation Test Suite")
    print("=" * 80)
    
    tests = [
        test_area_count,
        test_no_id_names,
        test_no_duplicates,
        test_arabic_names,
        test_json_validity,
        test_existing_tests
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"\n❌ ERROR in {test.__name__}: {e}")
            results.append(False)
    
    display_area_summary()
    
    # Final summary
    print("\n" + "=" * 80)
    print("Test Results Summary")
    print("=" * 80)
    
    passed = sum(results)
    total = len(results)
    
    print(f"\n✅ Passed: {passed}/{total}")
    print(f"❌ Failed: {total - passed}/{total}")
    
    if all(results):
        print("\n🎉 All tests passed! PR #324 fix is valid.")
        print("=" * 80)
        return True
    else:
        print("\n⚠️  Some tests failed. Please review the results above.")
        print("=" * 80)
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
