#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script to test that all shops are properly displayed
"""

import json

def main():
    print("🔍 التحقق من عرض جميع المحلات...")
    print("=" * 60)
    
    # Load shops_details.json
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    
    # Load plan-data.json
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    total_shops_in_details = len(shops_details)
    total_shops_in_plan = len(plan_data.get('shops', []))
    total_areas = len(plan_data.get('areas', []))
    
    # Count shops with area assignments
    shops_with_areas = sum(1 for shop in shops_details.values() 
                          if shop.get('area') and shop.get('areaId'))
    
    # Group shops by area
    shops_by_area = {}
    for shop_name, shop_info in shops_details.items():
        area = shop_info.get('area', 'غير محدد')
        if area not in shops_by_area:
            shops_by_area[area] = []
        shops_by_area[area].append(shop_name)
    
    print(f"\n📊 إحصائيات المحلات:")
    print(f"  ✅ إجمالي المحلات في shops_details.json: {total_shops_in_details}")
    print(f"  ✅ إجمالي المحلات في plan-data.json: {total_shops_in_plan}")
    print(f"  ✅ محلات لها مناطق محددة: {shops_with_areas}")
    print(f"  ✅ نسبة التغطية: {shops_with_areas/total_shops_in_details*100:.1f}%")
    print(f"  ✅ عدد المناطق: {total_areas}")
    
    print(f"\n📍 توزيع المحلات حسب المناطق:")
    print("-" * 60)
    
    # Sort areas by shop count
    sorted_areas = sorted(shops_by_area.items(), key=lambda x: len(x[1]), reverse=True)
    
    for area, shops in sorted_areas[:15]:  # Show top 15 areas
        print(f"  {area}: {len(shops)} محل")
    
    if len(sorted_areas) > 15:
        remaining = sum(len(shops) for area, shops in sorted_areas[15:])
        print(f"  ... و {len(sorted_areas) - 15} مناطق أخرى ({remaining} محل)")
    
    print("\n" + "=" * 60)
    
    # Verify all shops can be displayed
    if shops_with_areas == total_shops_in_details:
        print("✅ نجح الاختبار: جميع المحلات ({}) لها مناطق محددة".format(total_shops_in_details))
        print("✅ يمكن عرض جميع المحلات في Smart Planner")
        print("✅ يمكن تنظيم المحلات حسب المناطق")
        return 0
    else:
        print("⚠️  تحذير: {} محل بدون منطقة محددة".format(
            total_shops_in_details - shops_with_areas))
        return 1

if __name__ == '__main__':
    exit(main())
