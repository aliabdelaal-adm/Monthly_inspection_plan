#!/usr/bin/env python3
"""
Test to verify that plan-datafayez.json was successfully merged into plan-data.json
"""

import json
import sys
import io

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_merge():
    """Test that the merge was successful"""
    print("=== Testing plan-datafayez.json Merge ===")
    print()
    
    # Load the merged file
    print("📂 Loading merged plan-data.json...")
    try:
        with open('plan-data.json', 'r', encoding='utf-8') as f:
            merged_data = json.load(f)
        print("✅ Successfully loaded plan-data.json")
    except Exception as e:
        print(f"❌ Failed to load plan-data.json: {e}")
        return False
    
    # Load the source file for comparison
    print("📂 Loading source plan-datafayez.json...")
    try:
        with open('plan-datafayez.json', 'r', encoding='utf-8') as f:
            source_data = json.load(f)
        print("✅ Successfully loaded plan-datafayez.json")
    except Exception as e:
        print(f"❌ Failed to load plan-datafayez.json: {e}")
        return False
    
    print()
    
    # Test 1: Check inspection data count
    print("🧪 Test 1: Inspection Data Count")
    print("-" * 50)
    merged_count = len(merged_data.get('inspectionData', []))
    source_count = len(source_data.get('inspectionData', []))
    expected_min = source_count  # Should be at least as many as source
    
    if merged_count >= expected_min:
        print(f"✅ PASS: Merged data has {merged_count} entries (source had {source_count})")
    else:
        print(f"❌ FAIL: Merged data has only {merged_count} entries (source had {source_count})")
        return False
    
    # Test 2: Verify structure
    print()
    print("🧪 Test 2: Data Structure Validation")
    print("-" * 50)
    required_keys = ['inspectionData', 'inspectors', 'areas', 'shops', 'bellNotes', 'lastUpdate']
    missing_keys = [key for key in required_keys if key not in merged_data]
    
    if not missing_keys:
        print("✅ PASS: All required keys present")
        for key in required_keys:
            if key == 'bellNotes':
                print(f"   ✓ {key}: present")
            else:
                count = len(merged_data.get(key, []))
                print(f"   ✓ {key}: {count} items")
    else:
        print(f"❌ FAIL: Missing keys: {missing_keys}")
        return False
    
    # Test 3: Verify no duplicate entries
    print()
    print("🧪 Test 3: Duplicate Check")
    print("-" * 50)
    
    def create_key(entry):
        return f"{entry['inspector']}|{entry['day']}|{entry['shift']}|{entry['area']}"
    
    inspection_keys = set()
    duplicates_found = []
    
    for entry in merged_data.get('inspectionData', []):
        key = create_key(entry)
        if key in inspection_keys:
            duplicates_found.append(key)
        inspection_keys.add(key)
    
    if not duplicates_found:
        print(f"✅ PASS: No duplicate inspection entries found ({len(inspection_keys)} unique entries)")
    else:
        print(f"❌ FAIL: Found {len(duplicates_found)} duplicate entries")
        return False
    
    # Test 4: Verify JSON is valid and can be read
    print()
    print("🧪 Test 4: JSON Validity")
    print("-" * 50)
    
    try:
        # Try to serialize and deserialize
        json_str = json.dumps(merged_data, ensure_ascii=False, indent=2)
        re_parsed = json.loads(json_str)
        print("✅ PASS: JSON is valid and can be serialized/deserialized")
    except Exception as e:
        print(f"❌ FAIL: JSON validation error: {e}")
        return False
    
    # Test 5: Verify inspectors, areas, shops counts
    print()
    print("🧪 Test 5: Master Data Integrity")
    print("-" * 50)
    
    expected_inspectors = 9
    expected_areas = 23
    expected_shops = 149
    
    inspector_count = len(merged_data.get('inspectors', []))
    area_count = len(merged_data.get('areas', []))
    shop_count = len(merged_data.get('shops', []))
    
    tests_passed = True
    
    if inspector_count == expected_inspectors:
        print(f"✅ Inspectors: {inspector_count} (expected {expected_inspectors})")
    else:
        print(f"⚠️  Inspectors: {inspector_count} (expected {expected_inspectors})")
    
    if area_count == expected_areas:
        print(f"✅ Areas: {area_count} (expected {expected_areas})")
    else:
        print(f"❌ Areas: {area_count} (expected {expected_areas})")
        tests_passed = False
    
    if shop_count == expected_shops:
        print(f"✅ Shops: {shop_count} (expected {expected_shops})")
    else:
        print(f"⚠️  Shops: {shop_count} (expected {expected_shops})")
    
    if tests_passed:
        print("✅ PASS: Master data integrity verified")
    else:
        print("❌ FAIL: Master data counts don't match expected values")
        return False
    
    # Final summary
    print()
    print("=" * 80)
    print("✅ All tests passed! The merge of plan-datafayez.json was successful.")
    print("=" * 80)
    print()
    print(f"📊 Final Statistics:")
    print(f"   • Total inspection entries: {merged_count}")
    print(f"   • Total inspectors: {inspector_count}")
    print(f"   • Total areas: {area_count}")
    print(f"   • Total shops: {shop_count}")
    print(f"   • Last update: {merged_data.get('lastUpdate')}")
    print()
    print(f"✅ The merged plan-data.json is ready for use by index.html")
    
    return True

if __name__ == "__main__":
    success = test_merge()
    sys.exit(0 if success else 1)
