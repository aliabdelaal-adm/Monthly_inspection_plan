#!/usr/bin/env python3
"""
Validation script to verify the bird market shops replacement was successful.
Checks:
1. All old shops are removed
2. All new shops from Excel are present
3. No duplicate IDs or ADM codes
4. Area IDs are correct
5. All required fields are present
"""

import json
import pandas as pd

HERITAGE_MARKET = 'سوق التراث'
PORT_MARKET = 'سوق الميناء'
HERITAGE_AREA_ID = 'area_1758839353326'
PORT_AREA_ID = 'area_1758839345230'

def validate_replacement():
    """Validate the shop replacement"""
    print("Starting validation...")
    
    # Read plan-data.json
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Read Excel file
    df = pd.read_excel('bird-market-shops.xlsx', skiprows=3)
    headers = df.iloc[0].tolist()
    df = df[1:]
    df.columns = headers
    df = df.dropna(how='all')
    df['المنطقة'] = df['المنطقة'].str.strip()
    
    # Get shops from plan-data
    heritage_shops = [s for s in data.get('shops', []) if s.get('area') == HERITAGE_MARKET]
    port_shops = [s for s in data.get('shops', []) if s.get('area') == PORT_MARKET]
    
    # Get shops from Excel
    excel_heritage = df[df['المنطقة'] == HERITAGE_MARKET]
    excel_port = df[df['المنطقة'] == PORT_MARKET]
    
    errors = []
    warnings = []
    
    # Check 1: Count validation
    print("\n1. Checking shop counts...")
    if len(heritage_shops) != len(excel_heritage):
        errors.append(f"Heritage Market count mismatch: {len(heritage_shops)} in JSON vs {len(excel_heritage)} in Excel")
    else:
        print(f"   ✓ Heritage Market: {len(heritage_shops)} shops")
    
    if len(port_shops) != len(excel_port):
        errors.append(f"Port Market count mismatch: {len(port_shops)} in JSON vs {len(excel_port)} in Excel")
    else:
        print(f"   ✓ Port Market: {len(port_shops)} shops")
    
    # Check 2: No duplicate IDs
    print("\n2. Checking for duplicate shop IDs...")
    all_shop_ids = [s['id'] for s in data['shops']]
    if len(all_shop_ids) != len(set(all_shop_ids)):
        errors.append("Duplicate shop IDs found!")
    else:
        print(f"   ✓ No duplicate IDs ({len(all_shop_ids)} unique)")
    
    # Check 3: No duplicate ADM codes in bird markets
    print("\n3. Checking for duplicate ADM codes...")
    bird_market_shops = heritage_shops + port_shops
    adm_codes = [s.get('admCode') for s in bird_market_shops if s.get('admCode')]
    if len(adm_codes) != len(set(adm_codes)):
        errors.append("Duplicate ADM codes found in bird markets!")
    else:
        print(f"   ✓ No duplicate ADM codes ({len(adm_codes)} unique)")
    
    # Check 4: Area IDs are correct
    print("\n4. Checking area IDs...")
    for shop in heritage_shops:
        if shop.get('areaId') != HERITAGE_AREA_ID:
            errors.append(f"Wrong area ID for Heritage shop: {shop['id']}")
    for shop in port_shops:
        if shop.get('areaId') != PORT_AREA_ID:
            errors.append(f"Wrong area ID for Port shop: {shop['id']}")
    
    if not errors or not any('Wrong area ID' in e for e in errors):
        print(f"   ✓ All area IDs are correct")
    
    # Check 5: All shops have required fields
    print("\n5. Checking required fields...")
    for shop in bird_market_shops:
        if not shop.get('id'):
            errors.append(f"Shop missing ID: {shop.get('name', 'Unknown')}")
        if not shop.get('name'):
            errors.append(f"Shop missing name: {shop.get('id', 'Unknown')}")
        if not shop.get('area'):
            errors.append(f"Shop missing area: {shop['id']}")
        if not shop.get('areaId'):
            errors.append(f"Shop missing areaId: {shop['id']}")
        if not shop.get('admCode'):
            warnings.append(f"Shop missing ADM Code: {shop['id']} - {shop.get('name', 'Unknown')}")
    
    if not errors or not any('missing' in e for e in errors):
        print(f"   ✓ All required fields present")
    
    # Check 6: ADM codes match Excel
    print("\n6. Checking ADM codes match Excel...")
    excel_adm_codes = set(df['ADM Code'].dropna().str.strip())
    json_adm_codes = set(s.get('admCode') for s in bird_market_shops if s.get('admCode'))
    
    missing_from_json = excel_adm_codes - json_adm_codes
    extra_in_json = json_adm_codes - excel_adm_codes
    
    if missing_from_json:
        errors.append(f"ADM codes in Excel but not in JSON: {missing_from_json}")
    if extra_in_json:
        warnings.append(f"ADM codes in JSON but not in Excel: {extra_in_json}")
    
    if not missing_from_json and not extra_in_json:
        print(f"   ✓ All ADM codes match ({len(json_adm_codes)} codes)")
    
    # Check 7: No old shops remain
    print("\n7. Checking for old shops...")
    old_shop_names = [
        'فورس أند فيذرس للحيوانات الأليفة',
        'فورس اند فذيرس للحيوانات الاليفة',
        'محل ريفرز هب - منطقة الميناء'
    ]
    
    for shop in data['shops']:
        if shop.get('name') in old_shop_names:
            errors.append(f"Old shop still present: {shop['name']}")
    
    if not errors or not any('Old shop' in e for e in errors):
        print(f"   ✓ No old shops found")
    
    # Print summary
    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    
    if errors:
        print("\n❌ ERRORS FOUND:")
        for error in errors:
            print(f"  - {error}")
    
    if warnings:
        print("\n⚠️  WARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
    
    if not errors and not warnings:
        print("\n✅ ALL CHECKS PASSED!")
        print(f"   - Heritage Market: {len(heritage_shops)} shops")
        print(f"   - Port Market: {len(port_shops)} shops")
        print(f"   - Total: {len(heritage_shops) + len(port_shops)} shops")
        print(f"   - All ADM codes present and unique")
        print(f"   - All area IDs correct")
        print(f"   - No duplicates found")
        return True
    elif not errors:
        print("\n✅ VALIDATION PASSED (with warnings)")
        return True
    else:
        print("\n❌ VALIDATION FAILED")
        return False

if __name__ == '__main__':
    success = validate_replacement()
    exit(0 if success else 1)
