#!/usr/bin/env python3
"""
Test script to verify that all inspectors from PR #269 are correctly linked 
to all inspection plans starting from September 26, 2025.
"""

import json
import sys
from datetime import datetime

# The 9 official inspectors from PR #269
OFFICIAL_INSPECTORS = [
    'د. آمنه بن صرم',
    'د. آيه سلامة',
    'د. حسينة العامري',
    'د. حصة العلي',
    'د. هاجر الغافري',
    'د. علي عبدالعال',
    'د. محمد إسماعيل',
    'د. محمد سعيد',
    'د. فايز المسالمة'
]

CUTOFF_DATE = '2025-09-26'

def test_file(filename):
    """Test a single plan-data file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        return False, f"File not found"
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"
    
    errors = []
    warnings = []
    
    # Test 1: Check number of inspectors
    inspectors = data.get('inspectors', [])
    if len(inspectors) != 9:
        errors.append(f"Expected 9 inspectors, found {len(inspectors)}")
    
    # Test 2: Check all inspector names are from PR #269
    inspector_names = [i.get('name') for i in inspectors]
    non_official = [name for name in inspector_names if name not in OFFICIAL_INSPECTORS]
    if non_official:
        errors.append(f"Found non-official inspectors: {non_official}")
    
    # Test 3: Check for duplicates
    if len(inspector_names) != len(set(inspector_names)):
        errors.append(f"Found duplicate inspectors")
    
    # Test 4: Check all PR #269 inspectors are present
    missing = [name for name in OFFICIAL_INSPECTORS if name not in inspector_names]
    if missing:
        errors.append(f"Missing inspectors: {missing}")
    
    # Test 5: Check inspection data
    inspection_data = data.get('inspectionData', [])
    if not inspection_data:
        warnings.append("No inspection data found")
    
    # Test 6: Check all inspections reference official inspectors
    inspectors_in_data = set([entry.get('inspector') for entry in inspection_data])
    invalid_in_data = [i for i in inspectors_in_data if i not in OFFICIAL_INSPECTORS]
    if invalid_in_data:
        errors.append(f"Inspection data references non-official inspectors: {invalid_in_data}")
    
    # Test 7: Check date range
    dates = [entry.get('day') for entry in inspection_data if entry.get('day')]
    if dates:
        min_date = min(dates)
        max_date = max(dates)
        
        if min_date < CUTOFF_DATE:
            warnings.append(f"Some inspections are before {CUTOFF_DATE} (earliest: {min_date})")
    
    # Test 8: Verify all PR #269 inspectors have at least one inspection
    inspectors_with_data = set([entry.get('inspector') for entry in inspection_data])
    missing_data = [name for name in OFFICIAL_INSPECTORS if name not in inspectors_with_data]
    if missing_data:
        warnings.append(f"Inspectors with no inspection data: {missing_data}")
    
    return len(errors) == 0, {
        'errors': errors,
        'warnings': warnings,
        'stats': {
            'inspectors': len(inspectors),
            'inspections': len(inspection_data),
            'date_range': f"{min(dates) if dates else 'N/A'} to {max(dates) if dates else 'N/A'}"
        }
    }

def main():
    """Run tests on all plan-data files."""
    files = [
        'plan-data.json',
        'plan-data10.json',
        'plan-data11.json',
        'plan-data13.json',
        'plan-data15.json',
        'plan-data65.json',
        'plan-data91.json'
    ]
    
    print("="*70)
    print("PR #269 INSPECTORS LINKING - TEST SUITE")
    print("="*70)
    print(f"\nVerifying that all 9 inspectors from PR #269 are linked to")
    print(f"inspection plans starting from {CUTOFF_DATE}\n")
    
    print("Official inspectors from PR #269:")
    for i, inspector in enumerate(OFFICIAL_INSPECTORS, 1):
        print(f"  {i}. {inspector}")
    print()
    
    all_passed = True
    results = {}
    
    for filename in files:
        print(f"\n{'─'*70}")
        print(f"Testing: {filename}")
        print('─'*70)
        
        passed, result = test_file(filename)
        results[filename] = (passed, result)
        
        if isinstance(result, dict):
            stats = result.get('stats', {})
            print(f"📊 Stats:")
            print(f"   - Inspectors: {stats.get('inspectors', 'N/A')}")
            print(f"   - Inspections: {stats.get('inspections', 'N/A')}")
            print(f"   - Date range: {stats.get('date_range', 'N/A')}")
            
            errors = result.get('errors', [])
            warnings = result.get('warnings', [])
            
            if errors:
                print(f"\n❌ Errors:")
                for error in errors:
                    print(f"   - {error}")
                all_passed = False
            else:
                print(f"\n✅ All checks passed")
            
            if warnings:
                print(f"\n⚠️  Warnings:")
                for warning in warnings:
                    print(f"   - {warning}")
        else:
            print(f"❌ {result}")
            all_passed = False
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    for filename, (passed, _) in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status} - {filename}")
    
    print()
    if all_passed:
        print("🎉 ALL TESTS PASSED!")
        print("\nAll 9 inspectors from PR #269 are successfully linked to all")
        print("inspection plans starting from September 26, 2025.")
        return 0
    else:
        print("❌ SOME TESTS FAILED")
        print("\nPlease review the errors above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
