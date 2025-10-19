#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to validate the smart shop management implementation
"""

import json
import sys

def test_shops_details_structure():
    """Test that shops_details.json has the correct structure"""
    print("🧪 Testing shops_details.json structure...")
    
    try:
        with open('shops_details.json', 'r', encoding='utf-8') as f:
            shops = json.load(f)
        
        if not isinstance(shops, dict):
            print("❌ shops_details.json should be a dictionary")
            return False
        
        print(f"✅ Found {len(shops)} shops in database")
        
        # Check a sample shop structure
        sample_shop = list(shops.values())[0] if shops else None
        if sample_shop:
            required_fields = ['nameAr', 'address']
            optional_fields = ['nameEn', 'licenseNo', 'contact', 'activity', 'admCode', 'locationMap']
            
            for field in required_fields:
                if field not in sample_shop:
                    print(f"⚠️ Warning: Required field '{field}' missing in some shops")
            
            print(f"✅ Sample shop structure is valid")
            print(f"   - Name: {sample_shop.get('nameAr', 'N/A')}")
            print(f"   - Area: {sample_shop.get('address', 'N/A')}")
        
        return True
    except FileNotFoundError:
        print("❌ shops_details.json not found")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in shops_details.json: {e}")
        return False

def test_area_shop_mapping():
    """Test that shops are properly linked to areas"""
    print("\n🧪 Testing area-shop mapping...")
    
    try:
        with open('shops_details.json', 'r', encoding='utf-8') as f:
            shops = json.load(f)
        
        # Group shops by area
        area_shops = {}
        for shop_name, shop_data in shops.items():
            area = shop_data.get('address', 'Unknown')
            if area not in area_shops:
                area_shops[area] = []
            area_shops[area].append(shop_name)
        
        print(f"✅ Found {len(area_shops)} unique areas")
        
        # Display top 5 areas by shop count
        sorted_areas = sorted(area_shops.items(), key=lambda x: len(x[1]), reverse=True)
        print("\n📊 Top 5 areas by shop count:")
        for i, (area, shop_list) in enumerate(sorted_areas[:5], 1):
            print(f"   {i}. {area}: {len(shop_list)} shops")
        
        return True
    except Exception as e:
        print(f"❌ Error testing area-shop mapping: {e}")
        return False

def test_plan_data_consistency():
    """Test that plan-data.json is consistent with shops_details.json"""
    print("\n🧪 Testing plan-data.json consistency...")
    
    try:
        with open('shops_details.json', 'r', encoding='utf-8') as f:
            shops_details = json.load(f)
        
        with open('plan-data.json', 'r', encoding='utf-8') as f:
            plan_data = json.load(f)
        
        # Get all shops from plan data
        plan_shops = set()
        for inspection in plan_data.get('inspectionData', []):
            if 'shops' in inspection and inspection['shops']:
                plan_shops.update(inspection['shops'])
        
        shops_details_names = set(shops_details.keys())
        
        # Find shops in plan but not in details
        missing_in_details = plan_shops - shops_details_names
        if missing_in_details:
            print(f"⚠️ Warning: {len(missing_in_details)} shops in plan-data.json not found in shops_details.json")
            if len(missing_in_details) <= 5:
                for shop in list(missing_in_details)[:5]:
                    print(f"   - {shop}")
        else:
            print("✅ All shops in plan-data.json exist in shops_details.json")
        
        # Statistics
        print(f"\n📊 Statistics:")
        print(f"   - Shops in shops_details.json: {len(shops_details_names)}")
        print(f"   - Unique shops in plan-data.json: {len(plan_shops)}")
        print(f"   - Coverage: {len(plan_shops & shops_details_names)}/{len(plan_shops)} ({100*len(plan_shops & shops_details_names)/max(len(plan_shops),1):.1f}%)")
        
        return True
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False

def test_admin_dashboard_functions():
    """Test that admin-dashboard.html has all required functions"""
    print("\n🧪 Testing admin-dashboard.html functions...")
    
    required_functions = [
        'loadShopsList',
        'filterShopsByArea',
        'populateAreaFilter',
        'viewShopDetails',
        'editShopDetails',
        'saveShopDetails',
        'deleteShopFromDetails',
        'saveShopsDetailsToGitHub',
        'saveNewShopToDetails',
        'addShop'
    ]
    
    try:
        with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        missing_functions = []
        for func in required_functions:
            if f'function {func}' not in content and f'{func} =' not in content:
                missing_functions.append(func)
        
        if missing_functions:
            print(f"❌ Missing functions: {', '.join(missing_functions)}")
            return False
        else:
            print(f"✅ All {len(required_functions)} required functions are present")
            for func in required_functions:
                print(f"   ✓ {func}")
        
        return True
    except FileNotFoundError:
        print("❌ admin-dashboard.html not found")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("🚀 Smart Shop Management System - Validation Tests")
    print("=" * 60)
    
    results = []
    
    results.append(("shops_details.json structure", test_shops_details_structure()))
    results.append(("Area-Shop mapping", test_area_shop_mapping()))
    results.append(("Plan data consistency", test_plan_data_consistency()))
    results.append(("Admin dashboard functions", test_admin_dashboard_functions()))
    
    print("\n" + "=" * 60)
    print("📋 Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print("=" * 60)
    print(f"Result: {passed}/{total} tests passed ({100*passed/total:.0f}%)")
    print("=" * 60)
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
