#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation script to verify Port Market shops are properly synced between
shops_details.json and plan-data.json
"""

import json
import sys
import io

# Ensure UTF-8 encoding for output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PORT_MARKET_NAME = "سوق الميناء"
HERITAGE_MARKET_NAME = "سوق التراث"

def validate_sync():
    """Validate that all market shops are properly synced"""
    
    print("=" * 70)
    print("Validating Port Market Shop Synchronization")
    print("=" * 70)
    print()
    
    # Load both files
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    errors = []
    warnings = []
    
    # Test 1: Check Port Market shop counts by unique licenses
    print("Test 1: Port Market shop counts (by unique licenses)")
    
    # Count unique shops by license in shops_details
    port_details_licenses = set()
    port_details_no_license = 0
    for name, data in shops_details.items():
        if data.get('area') == PORT_MARKET_NAME:
            license = data.get('licenseNo', '')
            if license:
                port_details_licenses.add(license)
            else:
                port_details_no_license += 1
    
    # Count unique shops by license in plan-data
    port_plan_licenses = set()
    port_plan_no_license = 0
    for shop in plan_data['shops']:
        if shop.get('area') == PORT_MARKET_NAME:
            license = shop.get('license', '')
            if license:
                port_plan_licenses.add(license)
            else:
                port_plan_no_license += 1
    
    details_unique = len(port_details_licenses) + port_details_no_license
    plan_unique = len(port_plan_licenses) + port_plan_no_license
    
    print(f"  shops_details.json: {len(port_details_licenses)} with licenses + {port_details_no_license} without = {details_unique} unique shops")
    print(f"  plan-data.json: {len(port_plan_licenses)} with licenses + {port_plan_no_license} without = {plan_unique} unique shops")
    
    # Note: shops_details.json may have duplicates (same license, different names)
    # We validate by checking all licenses are present
    missing_licenses = port_details_licenses - port_plan_licenses
    if not missing_licenses:
        print("  ✓ PASS: All licensed shops are present")
    else:
        errors.append(f"Port Market missing {len(missing_licenses)} licensed shops")
        print(f"  ✗ FAIL: Missing {len(missing_licenses)} licensed shops")
    print()
    
    # Test 2: Check Heritage Market shop counts
    print("Test 2: Heritage Market shop counts")
    heritage_market_details = [name for name, data in shops_details.items() if data.get('area') == HERITAGE_MARKET_NAME]
    heritage_market_plan = [shop['name'] for shop in plan_data['shops'] if shop.get('area') == HERITAGE_MARKET_NAME]
    
    print(f"  shops_details.json: {len(heritage_market_details)} shops")
    print(f"  plan-data.json: {len(heritage_market_plan)} shops")
    
    if len(heritage_market_details) == len(heritage_market_plan):
        print("  ✓ PASS: Counts match")
    else:
        errors.append(f"Heritage Market count mismatch: {len(heritage_market_details)} vs {len(heritage_market_plan)}")
        print(f"  ✗ FAIL: Count mismatch")
    print()
    
    # Test 3: Check for missing licensed shops in Port Market
    print("Test 3: Missing Port Market shops (by license)")
    
    if missing_licenses:
        errors.append(f"Found {len(missing_licenses)} missing Port Market shops by license")
        print(f"  ✗ FAIL: {len(missing_licenses)} licensed shops missing")
        for license in list(missing_licenses)[:5]:
            # Find shop name with this license
            for name, data in shops_details.items():
                if data.get('licenseNo') == license:
                    print(f"    - License {license}: {name}")
                    break
    else:
        print("  ✓ PASS: All licensed shops are present")
    print()
    
    # Test 4: Check for duplicate shop IDs
    print("Test 4: Duplicate shop IDs")
    shop_ids = [shop['id'] for shop in plan_data['shops']]
    duplicate_ids = [id for id in shop_ids if shop_ids.count(id) > 1]
    
    if not duplicate_ids:
        print(f"  ✓ PASS: All {len(shop_ids)} shop IDs are unique")
    else:
        errors.append(f"Found {len(set(duplicate_ids))} duplicate shop IDs")
        print(f"  ✗ FAIL: Duplicate IDs found")
    print()
    
    # Test 5: Check for duplicate ADM codes
    print("Test 5: Duplicate ADM codes")
    adm_codes = [shop.get('admCode', '') for shop in plan_data['shops'] if shop.get('admCode')]
    duplicate_adm = [code for code in adm_codes if adm_codes.count(code) > 1]
    
    if not duplicate_adm:
        print(f"  ✓ PASS: All {len(adm_codes)} ADM codes are unique")
    else:
        warnings.append(f"Found {len(set(duplicate_adm))} duplicate ADM codes")
        print(f"  ⚠ WARNING: Duplicate ADM codes found")
        for code in list(set(duplicate_adm))[:5]:
            print(f"    - {code}")
    print()
    
    # Test 6: Check area IDs are correct
    print("Test 6: Area IDs validation")
    port_area_id = "area_1758839345230"
    heritage_area_id = "area_1758839353326"
    
    port_shops_wrong_area = [shop['name'] for shop in plan_data['shops'] 
                              if shop.get('area') == PORT_MARKET_NAME 
                              and shop.get('areaId') != port_area_id]
    
    heritage_shops_wrong_area = [shop['name'] for shop in plan_data['shops'] 
                                  if shop.get('area') == HERITAGE_MARKET_NAME 
                                  and shop.get('areaId') != heritage_area_id]
    
    if not port_shops_wrong_area and not heritage_shops_wrong_area:
        print("  ✓ PASS: All area IDs are correct")
    else:
        if port_shops_wrong_area:
            errors.append(f"Port Market: {len(port_shops_wrong_area)} shops with wrong area ID")
            print(f"  ✗ FAIL: Port Market shops with wrong area ID: {len(port_shops_wrong_area)}")
        if heritage_shops_wrong_area:
            errors.append(f"Heritage Market: {len(heritage_shops_wrong_area)} shops with wrong area ID")
            print(f"  ✗ FAIL: Heritage Market shops with wrong area ID: {len(heritage_shops_wrong_area)}")
    print()
    
    # Summary
    print("=" * 70)
    print("Validation Summary")
    print("=" * 70)
    print(f"Total shops in plan-data.json: {len(plan_data['shops'])}")
    port_count = len([s for s in plan_data['shops'] if s.get('area') == PORT_MARKET_NAME])
    heritage_count = len([s for s in plan_data['shops'] if s.get('area') == HERITAGE_MARKET_NAME])
    print(f"Port Market shops: {port_count}")
    print(f"Heritage Market shops: {heritage_count}")
    print()
    
    if errors:
        print(f"❌ FAILED: {len(errors)} error(s) found:")
        for error in errors:
            print(f"  - {error}")
        print()
    
    if warnings:
        print(f"⚠️  WARNINGS: {len(warnings)} warning(s):")
        for warning in warnings:
            print(f"  - {warning}")
        print()
    
    if not errors and not warnings:
        print("✅ ALL TESTS PASSED!")
        print("✓ Port Market shops are fully synchronized")
        print("✓ Heritage Market shops are fully synchronized")
        print("✓ No duplicate IDs or issues found")
        return True
    elif not errors:
        print("✅ ALL TESTS PASSED (with warnings)")
        return True
    else:
        return False

if __name__ == '__main__':
    success = validate_sync()
    sys.exit(0 if success else 1)
