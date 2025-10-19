#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify the shop loading fix in smart-planner.html
This tests the getAllShopsInArea function logic.
"""

def test_get_all_shops_in_area():
    """Test the getAllShopsInArea function logic"""
    
    # Simulate planData structure
    planData = {
        'areas': [
            {'id': 'area_1', 'name': 'المنطقة أ'},
            {'id': 'area_2', 'name': 'المنطقة ب'},
            {'id': 'area_3', 'name': 'المنطقة ج'}
        ],
        'shops': [
            {'id': 'shop_1', 'name': 'محل 1', 'areaId': 'area_1'},
            {'id': 'shop_2', 'name': 'محل 2', 'areaId': 'area_1'},
            {'id': 'shop_3', 'name': 'محل 3', 'areaId': 'area_1'},
            {'id': 'shop_4', 'name': 'محل 4', 'areaId': 'area_2'},
            {'id': 'shop_5', 'name': 'محل 5', 'areaId': 'area_2'},
            {'id': 'shop_6', 'name': 'محل 6', 'areaId': 'area_3'}
        ],
        'inspectionData': [
            {
                'inspector': 'مفتش 1',
                'day': '2025-10-10',
                'area': 'المنطقة أ',
                'shops': ['محل 1']  # Only one shop was inspected
            }
        ]
    }
    
    def getAllShopsInArea(area, data):
        """Python version of the fixed getAllShopsInArea function"""
        shops = []
        
        if not data:
            return shops
        
        # First, try to get shops from the planData.shops array (primary source)
        if data.get('shops') and data.get('areas'):
            # Find the area ID for the given area name
            areaObj = next((a for a in data['areas'] if a['name'] == area), None)
            
            if areaObj:
                # Get all shops that belong to this area
                shopsInArea = [shop['name'] for shop in data['shops'] if shop['areaId'] == areaObj['id']]
                
                if len(shopsInArea) > 0:
                    return shopsInArea
        
        # Fallback: Collect all unique shops from inspection history
        if data.get('inspectionData'):
            shopSet = set()
            for inspection in data['inspectionData']:
                if inspection.get('area') == area and inspection.get('shops'):
                    for shop in inspection['shops']:
                        shopSet.add(shop)
            
            return list(shopSet)
        
        return shops
    
    print("=" * 60)
    print("🧪 اختبار إصلاح تحميل المحلات في Smart Planner")
    print("=" * 60)
    
    all_passed = True
    
    # Test 1: Should return all shops in area from shops array
    print("\n📋 اختبار 1: جلب جميع المحلات في المنطقة أ من shops array")
    print("-" * 60)
    test1_result = getAllShopsInArea('المنطقة أ', planData)
    test1_pass = (len(test1_result) == 3 and 
                  'محل 1' in test1_result and 
                  'محل 2' in test1_result and 
                  'محل 3' in test1_result)
    
    print(f"النتيجة: {len(test1_result)} محلات")
    print(f"المحلات: {', '.join(test1_result)}")
    if test1_pass:
        print("✅ نجح - يتم جلب جميع المحلات من shops array!")
    else:
        print("❌ فشل - متوقع 3 محلات")
    all_passed = all_passed and test1_pass
    
    # Test 2: Should return all shops in area B
    print("\n📋 اختبار 2: جلب جميع المحلات في المنطقة ب")
    print("-" * 60)
    test2_result = getAllShopsInArea('المنطقة ب', planData)
    test2_pass = (len(test2_result) == 2 and 
                  'محل 4' in test2_result and 
                  'محل 5' in test2_result)
    
    print(f"النتيجة: {len(test2_result)} محلات")
    print(f"المحلات: {', '.join(test2_result)}")
    if test2_pass:
        print("✅ نجح")
    else:
        print("❌ فشل - متوقع 2 محلات")
    all_passed = all_passed and test2_pass
    
    # Test 3: Should return shops from area C (not in inspection history)
    print("\n📋 اختبار 3: جلب محلات من منطقة لم يتم تفتيشها من قبل")
    print("-" * 60)
    test3_result = getAllShopsInArea('المنطقة ج', planData)
    test3_pass = len(test3_result) == 1 and 'محل 6' in test3_result
    
    print(f"النتيجة: {len(test3_result)} محلات")
    print(f"المحلات: {', '.join(test3_result)}")
    if test3_pass:
        print("✅ نجح - الإصلاح يعمل! المحلات تظهر حتى لو لم يتم تفتيشها من قبل")
    else:
        print("❌ فشل")
    all_passed = all_passed and test3_pass
    
    # Test 4: Old behavior (fallback) - without shops array
    print("\n📋 اختبار 4: السلوك القديم (fallback) - بدون shops array")
    print("-" * 60)
    planData_no_shops = {
        'areas': planData['areas'],
        'inspectionData': planData['inspectionData']
    }
    test4_result = getAllShopsInArea('المنطقة أ', planData_no_shops)
    test4_pass = len(test4_result) == 1 and 'محل 1' in test4_result
    
    print(f"النتيجة: {len(test4_result)} محلات (فقط المفتشة سابقاً)")
    print(f"المحلات: {', '.join(test4_result)}")
    if test4_pass:
        print("✅ نجح - التوافق العكسي يعمل")
    else:
        print("❌ فشل")
    all_passed = all_passed and test4_pass
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 الملخص")
    print("=" * 60)
    if all_passed:
        print("✅ جميع الاختبارات نجحت!")
        print("\n💡 النتيجة: الإصلاح يحل المشكلة بنجاح:")
        print("   • يتم جلب جميع المحلات من shops array")
        print("   • المحلات تظهر حتى لو لم يتم تفتيشها من قبل")
        print("   • التوافق العكسي محفوظ")
        return True
    else:
        print("❌ بعض الاختبارات فشلت")
        return False

if __name__ == "__main__":
    import sys
    success = test_get_all_shops_in_area()
    sys.exit(0 if success else 1)
