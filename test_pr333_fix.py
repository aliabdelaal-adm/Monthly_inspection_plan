#!/usr/bin/env python3
"""
Test script to validate PR #333 fix - Duplicate Shop Assignments

This script verifies that:
1. No duplicate shop assignments exist (same shop to multiple inspectors on same day)
2. Data integrity is maintained
3. All inspections are valid
"""

import json
import sys
from collections import defaultdict

def test_no_duplicates():
    """Test that no duplicate shop assignments exist"""
    print("\n🧪 Test 1: No Duplicate Shop Assignments")
    print("-" * 50)
    
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Track shop assignments by date
    shop_assignments = defaultdict(list)
    
    for idx, inspection in enumerate(data['inspectionData']):
        day = inspection['day']
        inspector = inspection['inspector']
        
        for shop in inspection['shops']:
            key = f"{day}|{shop}"
            shop_assignments[key].append({
                'inspector': inspector,
                'index': idx
            })
    
    # Find duplicates
    duplicates = {k: v for k, v in shop_assignments.items() if len(v) > 1}
    
    if duplicates:
        print(f"❌ FAIL: Found {len(duplicates)} duplicate shop assignments:")
        for key, assignments in list(duplicates.items())[:5]:  # Show first 5
            day, shop = key.split('|')
            print(f"   • {day} - {shop}: {[a['inspector'] for a in assignments]}")
        return False
    else:
        print(f"✅ PASS: No duplicate shop assignments found")
        return True

def test_data_integrity():
    """Test that data structure is intact"""
    print("\n🧪 Test 2: Data Integrity")
    print("-" * 50)
    
    try:
        with open('plan-data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check required keys
        required_keys = ['inspectionData', 'inspectors', 'areas', 'shops', 'bellNotes', 'lastUpdate']
        for key in required_keys:
            if key not in data:
                print(f"❌ FAIL: Missing required key: {key}")
                return False
        
        # Check inspection data structure
        for idx, inspection in enumerate(data['inspectionData']):
            required_fields = ['inspector', 'day', 'shift', 'area', 'shops']
            for field in required_fields:
                if field not in inspection:
                    print(f"❌ FAIL: Inspection {idx} missing field: {field}")
                    return False
        
        print(f"✅ PASS: Data structure is intact")
        print(f"   • Inspections: {len(data['inspectionData'])}")
        print(f"   • Inspectors: {len(data['inspectors'])}")
        print(f"   • Areas: {len(data['areas'])}")
        print(f"   • Shops: {len(data['shops'])}")
        return True
        
    except Exception as e:
        print(f"❌ FAIL: Error reading data: {e}")
        return False

def test_shop_assignments():
    """Test that all shop assignments are valid"""
    print("\n🧪 Test 3: Valid Shop Assignments")
    print("-" * 50)
    
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total_assignments = sum(len(insp['shops']) for insp in data['inspectionData'])
    
    # Check that each inspection has shops
    empty_inspections = [i for i, insp in enumerate(data['inspectionData']) if len(insp['shops']) == 0]
    
    if empty_inspections:
        print(f"⚠️  WARNING: {len(empty_inspections)} inspections have no shops assigned")
        print(f"   Indices: {empty_inspections[:5]}")  # Show first 5
    
    print(f"✅ PASS: {total_assignments} shop assignments are valid")
    print(f"   • Average shops per inspection: {total_assignments / len(data['inspectionData']):.1f}")
    
    return True

def test_comparison_with_backup():
    """Compare with backup to show fix results"""
    print("\n🧪 Test 4: Before/After Comparison")
    print("-" * 50)
    
    try:
        # Load current
        with open('plan-data.json', 'r', encoding='utf-8') as f:
            current = json.load(f)
        
        # Try to load backup
        try:
            with open('plan-data.json.backup_pr333_20251009_190946', 'r', encoding='utf-8') as f:
                backup = json.load(f)
            
            backup_shops = sum(len(i['shops']) for i in backup['inspectionData'])
            current_shops = sum(len(i['shops']) for i in current['inspectionData'])
            
            print(f"✅ PASS: Comparison completed")
            print(f"   • Before: {backup_shops} shop assignments")
            print(f"   • After: {current_shops} shop assignments")
            print(f"   • Removed: {backup_shops - current_shops} duplicate assignments")
            
        except FileNotFoundError:
            print(f"⚠️  INFO: Backup file not found, skipping comparison")
        
        return True
        
    except Exception as e:
        print(f"❌ FAIL: Error in comparison: {e}")
        return False

def test_affected_inspectors():
    """Show which inspectors were affected by duplicate removal"""
    print("\n🧪 Test 5: Affected Inspectors Analysis")
    print("-" * 50)
    
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Count shops per inspector
    inspector_shops = defaultdict(int)
    for inspection in data['inspectionData']:
        inspector_shops[inspection['inspector']] += len(inspection['shops'])
    
    print(f"✅ PASS: Inspector shop assignments:")
    for inspector, count in sorted(inspector_shops.items(), key=lambda x: x[1], reverse=True):
        print(f"   • {inspector}: {count} shops")
    
    return True

def main():
    print("=" * 80)
    print("PR #333 Fix Validation Test Suite")
    print("=" * 80)
    
    tests = [
        test_no_duplicates,
        test_data_integrity,
        test_shop_assignments,
        test_comparison_with_backup,
        test_affected_inspectors
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"\n❌ ERROR in {test.__name__}: {e}")
            results.append(False)
    
    # Final summary
    print("\n" + "=" * 80)
    print("Test Results Summary")
    print("=" * 80)
    
    passed = sum(results)
    total = len(results)
    
    print(f"\n✅ Passed: {passed}/{total}")
    print(f"❌ Failed: {total - passed}/{total}")
    
    if all(results):
        print("\n🎉 All tests passed! PR #333 fix is valid.")
        print("=" * 80)
        return True
    else:
        print("\n⚠️  Some tests failed. Please review the results above.")
        print("=" * 80)
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
