#!/usr/bin/env python3
"""
Verify that all 306 shops are accessible in the Smart Planner
Checks both shops_details.json and plan-data.json
"""

import json

def verify_shops():
    """Verify all shops have proper area assignments"""
    
    print("="*70)
    print("VERIFICATION: All Shops Accessible for Smart Planner")
    print("="*70)
    
    # Load shops_details.json
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    
    # Load plan-data.json
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    print(f"\n📊 shops_details.json:")
    print(f"  Total shops: {len(shops_details)}")
    
    # Verify all shops in shops_details have area and areaId
    shops_with_area = 0
    shops_with_areaid = 0
    shops_complete = 0
    
    for shop_name, shop_info in shops_details.items():
        if 'area' in shop_info and shop_info['area']:
            shops_with_area += 1
        if 'areaId' in shop_info and shop_info['areaId']:
            shops_with_areaid += 1
        if 'area' in shop_info and shop_info['area'] and 'areaId' in shop_info and shop_info['areaId']:
            shops_complete += 1
    
    print(f"  Shops with 'area': {shops_with_area}")
    print(f"  Shops with 'areaId': {shops_with_areaid}")
    print(f"  Shops with both fields: {shops_complete}")
    
    status1 = "✅" if shops_complete == len(shops_details) else "❌"
    print(f"  {status1} All shops have complete area data: {shops_complete == len(shops_details)}")
    
    print(f"\n📊 plan-data.json:")
    shops = plan_data.get('shops', [])
    print(f"  Total shops: {len(shops)}")
    
    # Verify all shops in plan-data have area and areaId
    plan_shops_with_area = 0
    plan_shops_with_areaid = 0
    plan_shops_complete = 0
    
    for shop in shops:
        if 'area' in shop and shop['area']:
            plan_shops_with_area += 1
        if 'areaId' in shop and shop['areaId']:
            plan_shops_with_areaid += 1
        if 'area' in shop and shop['area'] and 'areaId' in shop and shop['areaId']:
            plan_shops_complete += 1
    
    print(f"  Shops with 'area': {plan_shops_with_area}")
    print(f"  Shops with 'areaId': {plan_shops_with_areaid}")
    print(f"  Shops with both fields: {plan_shops_complete}")
    
    status2 = "✅" if plan_shops_complete == len(shops) else "❌"
    print(f"  {status2} All shops have complete area data: {plan_shops_complete == len(shops)}")
    
    # Count unique areas
    print(f"\n📍 Areas:")
    areas = plan_data.get('areas', [])
    print(f"  Total areas defined: {len(areas)}")
    
    # Area distribution from shops_details
    area_distribution = {}
    for shop_name, shop_info in shops_details.items():
        area = shop_info.get('area', 'Unknown')
        if area not in area_distribution:
            area_distribution[area] = 0
        area_distribution[area] += 1
    
    print(f"\n📈 Distribution of shops by area (from shops_details.json):")
    for area, count in sorted(area_distribution.items(), key=lambda x: x[1], reverse=True):
        print(f"  {area}: {count} shops")
    
    # Final summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    total_accessible = shops_complete
    all_complete = shops_complete == len(shops_details) and plan_shops_complete == len(shops)
    
    status = "✅ PASS" if all_complete else "❌ FAIL"
    print(f"{status}")
    print(f"  shops_details.json: {shops_complete}/{len(shops_details)} shops complete")
    print(f"  plan-data.json: {plan_shops_complete}/{len(shops)} shops complete")
    print(f"  Total shops accessible in Smart Planner: {total_accessible}")
    
    if all_complete:
        print("\n🎉 SUCCESS! All shops are properly configured with area assignments.")
        print("   The Smart Planner should now display all 306 shops correctly.")
    else:
        print("\n⚠️  WARNING! Some shops are missing area data.")
        print("   Please run fix_plan_data_areas.py to fix the issue.")
    
    return all_complete

if __name__ == '__main__':
    success = verify_shops()
    exit(0 if success else 1)
