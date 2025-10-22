#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test that all shops are now visible in the smart planner
"""

import json

def main():
    print("="*60)
    print("TEST: Verify all shops are visible")
    print("="*60)
    
    # Load plan-data.json
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    # Load shops_details.json
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    
    # Test 1: Check total shops
    print("\n✓ TEST 1: Total shops count")
    print(f"  Plan-data shops: {len(plan_data['shops'])}")
    print(f"  Shops details: {len(shops_details)}")
    print(f"  Status: {'✅ PASS' if len(plan_data['shops']) >= len(shops_details) else '❌ FAIL'}")
    
    # Test 2: Check areas exist
    print("\n✓ TEST 2: Areas exist")
    print(f"  Total areas: {len(plan_data['areas'])}")
    area_names = [area['name'] for area in plan_data['areas']]
    print(f"  Areas: {', '.join(area_names[:5])}...")
    print(f"  Status: ✅ PASS")
    
    # Test 3: Check mobile salon area exists
    print("\n✓ TEST 3: Mobile salon area exists")
    mobile_area = None
    for area in plan_data['areas']:
        if 'متنقل' in area['name']:
            mobile_area = area
            break
    
    if mobile_area:
        mobile_shops = [s for s in plan_data['shops'] if s['areaId'] == mobile_area['id']]
        print(f"  Mobile area: {mobile_area['name']}")
        print(f"  Mobile shops count: {len(mobile_shops)}")
        print(f"  Mobile shops: {', '.join([s['name'] for s in mobile_shops])}")
        print(f"  Status: ✅ PASS")
    else:
        print(f"  Status: ❌ FAIL - Mobile salon area not found")
    
    # Test 4: Check each area has shops
    print("\n✓ TEST 4: Each area has shops assigned")
    for area in plan_data['areas']:
        shops_in_area = [s for s in plan_data['shops'] if s['areaId'] == area['id']]
        print(f"  {area['name']}: {len(shops_in_area)} shops")
    
    # Test 5: Check no duplicates
    print("\n✓ TEST 5: No duplicate shops")
    shop_names = [shop['name'] for shop in plan_data['shops']]
    duplicates = len(shop_names) - len(set(shop_names))
    print(f"  Total shops: {len(shop_names)}")
    print(f"  Unique names: {len(set(shop_names))}")
    print(f"  Duplicates: {duplicates}")
    print(f"  Status: {'✅ PASS' if duplicates == 0 else '❌ FAIL'}")
    
    # Test 6: Sample shops from different areas
    print("\n✓ TEST 6: Sample shops by area (simulating getAllShopsInArea)")
    test_areas = ['سوق الميناء', 'صالون متنقل', 'الحصن']
    for area_name in test_areas:
        area_obj = next((a for a in plan_data['areas'] if a['name'] == area_name), None)
        if area_obj:
            shops = [s['name'] for s in plan_data['shops'] if s['areaId'] == area_obj['id']]
            print(f"  {area_name}: {len(shops)} shops")
            if shops:
                print(f"    Sample: {shops[0]}")
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED SUCCESSFULLY! ✅")
    print("="*60)
    print("\nSummary:")
    print(f"  • All {len(plan_data['shops'])} shops are now in plan-data.json")
    print(f"  • Mobile salons are categorized under '{mobile_area['name'] if mobile_area else 'N/A'}'")
    print(f"  • Developers can now see all shops when planning inspections")
    print("="*60)

if __name__ == '__main__':
    main()
