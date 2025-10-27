#!/usr/bin/env python3
"""
Script to simplify shop addresses in shops_details.json
Changes the 'address' field to match the 'area' field for each shop
"""

import json
import sys

def simplify_addresses(input_file, output_file=None):
    """
    Read shops_details.json and update address field to match area name
    """
    if output_file is None:
        output_file = input_file
    
    try:
        # Read the file
        with open(input_file, 'r', encoding='utf-8') as f:
            shops_data = json.load(f)
        
        # Update each shop's address to be the same as area
        shops_updated = 0
        for shop_name, shop_info in shops_data.items():
            if 'area' in shop_info:
                # Set address to the area name
                old_address = shop_info.get('address', '')
                shop_info['address'] = shop_info['area']
                if old_address != shop_info['area']:
                    shops_updated += 1
        
        # Write back to file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(shops_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ تم تحديث {shops_updated} محل بنجاح")
        print(f"📝 تم حفظ التغييرات في: {output_file}")
        return True
        
    except Exception as e:
        print(f"❌ خطأ: {str(e)}", file=sys.stderr)
        return False

if __name__ == '__main__':
    input_file = 'shops_details.json'
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    
    success = simplify_addresses(input_file)
    sys.exit(0 if success else 1)
