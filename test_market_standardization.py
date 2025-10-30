#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify the standardization of shop locations in Heritage and Mina markets
"""

import json
import sys
import io

# Ensure UTF-8 encoding for output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

REFERENCE_LOCATION_MAP = "https://maps.app.goo.gl/WLKn2FPk9gN7MSNC8"
HERITAGE_ADDRESS_BASE = "سوق التراث - شارع الميناء - الزاهية"
MINA_ADDRESS_BASE = "سوق الميناء - شارع الميناء - الزاهية"

def test_standardization():
    """Test that all shops in both markets have standardized locations"""
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops_data = json.load(f)
    
    heritage_shops = []
    mina_shops = []
    errors = []
    
    for shop_name, shop_data in shops_data.items():
        address = shop_data.get('address', '')
        location_map = shop_data.get('locationMap', '')
        
        # Check Heritage Market shops
        if 'سوق التراث' in address:
            heritage_shops.append(shop_name)
            
            # Verify location map
            if location_map != REFERENCE_LOCATION_MAP:
                errors.append(f"❌ {shop_name}: Wrong location map")
            
            # Verify address format
            if address != HERITAGE_ADDRESS_BASE:
                errors.append(f"❌ {shop_name}: Wrong address format - got '{address}'")
        
        # Check Mina Market shops
        elif 'سوق الميناء' in address:
            mina_shops.append(shop_name)
            
            # Verify location map
            if location_map != REFERENCE_LOCATION_MAP:
                errors.append(f"❌ {shop_name}: Wrong location map")
            
            # Verify address format
            if address != MINA_ADDRESS_BASE:
                errors.append(f"❌ {shop_name}: Wrong address format - got '{address}'")
    
    # Report results
    print("=" * 70)
    print("Test Results: Shop Location Standardization")
    print("=" * 70)
    
    print(f"\n📊 Summary:")
    print(f"  - Heritage Market shops: {len(heritage_shops)}")
    print(f"  - Mina Market shops: {len(mina_shops)}")
    print(f"  - Total shops checked: {len(heritage_shops) + len(mina_shops)}")
    
    if errors:
        print(f"\n❌ Found {len(errors)} error(s):")
        for error in errors:
            print(f"  {error}")
        return False
    else:
        print(f"\n✓ All tests passed!")
        print(f"✓ All shops have standardized location: {REFERENCE_LOCATION_MAP}")
        print(f"✓ Heritage shops have address: {HERITAGE_ADDRESS_BASE}")
        print(f"✓ Mina shops have address: {MINA_ADDRESS_BASE}")
        return True

if __name__ == '__main__':
    success = test_standardization()
    sys.exit(0 if success else 1)
