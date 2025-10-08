#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for security feature
"""

def validate_data_integrity(data):
    """Validate data integrity - Python version for testing"""
    MIN_INSPECTORS = 5
    MIN_AREAS = 35
    MIN_SHOPS = 140
    
    issues = []
    
    # Check required fields exist
    if 'inspectionData' not in data or not isinstance(data['inspectionData'], list):
        issues.append('بيانات التفتيش مفقودة أو تالفة')
    
    if 'inspectors' not in data or not isinstance(data['inspectors'], list):
        issues.append('بيانات المفتشين مفقودة أو تالفة')
    elif len(data['inspectors']) < MIN_INSPECTORS:
        issues.append(f'عدد المفتشين أقل من المتوقع ({len(data["inspectors"])} من {MIN_INSPECTORS})')
    
    if 'areas' not in data or not isinstance(data['areas'], list):
        issues.append('بيانات المناطق مفقودة أو تالفة')
    elif len(data['areas']) < MIN_AREAS:
        issues.append(f'عدد المناطق أقل من المتوقع ({len(data["areas"])} من {MIN_AREAS})')
    
    if 'shops' not in data or not isinstance(data['shops'], list):
        issues.append('بيانات المحلات مفقودة أو تالفة')
    elif len(data['shops']) < MIN_SHOPS:
        issues.append(f'عدد المحلات أقل من المتوقع ({len(data["shops"])} من {MIN_SHOPS})')
    
    if 'lastUpdate' not in data or not data['lastUpdate']:
        issues.append('تاريخ آخر تحديث مفقود')
    
    return {
        'isValid': len(issues) == 0,
        'issues': issues
    }

def run_tests():
    """Run test cases"""
    print("=" * 80)
    print("اختبار نظام الحماية والأمان - Security System Test")
    print("=" * 80)
    
    # Test 1: Valid data
    print("\nTest 1: Valid data with correct counts")
    valid_data = {
        'inspectionData': [{'inspector': 'Test'}],
        'inspectors': [{'name': f'Inspector {i}'} for i in range(23)],
        'areas': [{'name': f'Area {i}'} for i in range(38)],
        'shops': [{'name': f'Shop {i}'} for i in range(149)],
        'lastUpdate': '2025-10-08T16:24:47.224963'
    }
    result1 = validate_data_integrity(valid_data)
    print(f"Result: {'✅ PASS' if result1['isValid'] else '❌ FAIL'}")
    if result1['issues']:
        print(f"Issues: {', '.join(result1['issues'])}")
    
    # Test 2: Tampered data (too few shops)
    print("\nTest 2: Tampered data - too few shops (50 instead of 149)")
    tampered_data = valid_data.copy()
    tampered_data['shops'] = [{'name': f'Shop {i}'} for i in range(50)]
    result2 = validate_data_integrity(tampered_data)
    print(f"Result: {'✅ PASS (correctly detected tampering)' if not result2['isValid'] else '❌ FAIL'}")
    if result2['issues']:
        print(f"Issues detected: {', '.join(result2['issues'])}")
    
    # Test 3: Missing inspectors
    print("\nTest 3: Missing inspectors data")
    missing_inspectors = valid_data.copy()
    missing_inspectors['inspectors'] = None
    result3 = validate_data_integrity(missing_inspectors)
    print(f"Result: {'✅ PASS (correctly detected missing data)' if not result3['isValid'] else '❌ FAIL'}")
    if result3['issues']:
        print(f"Issues detected: {', '.join(result3['issues'])}")
    
    # Test 4: Too few inspectors
    print("\nTest 4: Too few inspectors (3 instead of 9)")
    few_inspectors = valid_data.copy()
    few_inspectors['inspectors'] = [{'name': f'Inspector {i}'} for i in range(3)]
    result4 = validate_data_integrity(few_inspectors)
    print(f"Result: {'✅ PASS (correctly detected tampering)' if not result4['isValid'] else '❌ FAIL'}")
    if result4['issues']:
        print(f"Issues detected: {', '.join(result4['issues'])}")
    
    # Test 5: Missing lastUpdate
    print("\nTest 5: Missing lastUpdate field")
    no_update = valid_data.copy()
    no_update['lastUpdate'] = None
    result5 = validate_data_integrity(no_update)
    print(f"Result: {'✅ PASS (correctly detected missing field)' if not result5['isValid'] else '❌ FAIL'}")
    if result5['issues']:
        print(f"Issues detected: {', '.join(result5['issues'])}")
    
    # Test 6: Load actual plan-data.json
    print("\nTest 6: Validate actual plan-data.json")
    try:
        import json
        with open('plan-data.json', 'r', encoding='utf-8') as f:
            actual_data = json.load(f)
        result6 = validate_data_integrity(actual_data)
        print(f"Result: {'✅ PASS (actual data is valid)' if result6['isValid'] else '❌ FAIL'}")
        if result6['issues']:
            print(f"Issues detected: {', '.join(result6['issues'])}")
        else:
            print("✅ The actual plan-data.json passes all integrity checks!")
            print(f"   - Inspectors: {len(actual_data.get('inspectors', []))}")
            print(f"   - Areas: {len(actual_data.get('areas', []))}")
            print(f"   - Shops: {len(actual_data.get('shops', []))}")
            print(f"   - Inspection entries: {len(actual_data.get('inspectionData', []))}")
    except Exception as e:
        print(f"❌ Error loading plan-data.json: {e}")
    
    print("\n" + "=" * 80)
    print("All tests completed!")
    print("=" * 80)

if __name__ == '__main__':
    run_tests()
