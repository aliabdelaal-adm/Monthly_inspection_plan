#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to standardize the geographical location and address for all shops
in سوق التراث (Heritage Market) and سوق الميناء (Mina Market) to match
the reference shop "زون تايم لطيور الزينة"
"""

import json
import sys
import io

# Ensure UTF-8 encoding for output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Reference shop data
REFERENCE_SHOP_NAME = "زون تايم لطيور الزينة"
REFERENCE_LOCATION_MAP = "https://maps.app.goo.gl/WLKn2FPk9gN7MSNC8"
HERITAGE_ADDRESS_BASE = "سوق التراث - شارع الميناء - الزاهية"
MINA_ADDRESS_BASE = "سوق الميناء - شارع الميناء - الزاهية"

def main():
    # Load the shops_details.json file
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops_data = json.load(f)
    
    # Counters for reporting
    heritage_updated = 0
    mina_updated = 0
    
    # Process each shop
    for shop_name, shop_data in shops_data.items():
        address = shop_data.get('address', '')
        
        # Update shops in Heritage Market (سوق التراث)
        if 'سوق التراث' in address:
            # Update location map
            shop_data['locationMap'] = REFERENCE_LOCATION_MAP
            
            # Update address: keep the market name but use consistent format
            shop_data['address'] = HERITAGE_ADDRESS_BASE
            
            heritage_updated += 1
            
        # Update shops in Mina Market (سوق الميناء)
        elif 'سوق الميناء' in address:
            # Update location map
            shop_data['locationMap'] = REFERENCE_LOCATION_MAP
            
            # Update address: keep the market name but use consistent format
            shop_data['address'] = MINA_ADDRESS_BASE
            
            mina_updated += 1
    
    # Save the updated data
    with open('shops_details.json', 'w', encoding='utf-8') as f:
        json.dump(shops_data, f, ensure_ascii=False, indent=2)
    
    # Report results
    print(f"✓ Standardization completed successfully!")
    print(f"  - Heritage Market (سوق التراث) shops updated: {heritage_updated}")
    print(f"  - Mina Market (سوق الميناء) shops updated: {mina_updated}")
    print(f"  - Total shops updated: {heritage_updated + mina_updated}")
    print(f"\nAll shops now use the same geographical location as '{REFERENCE_SHOP_NAME}':")
    print(f"  Location: {REFERENCE_LOCATION_MAP}")

if __name__ == '__main__':
    main()
