#!/usr/bin/env python3
"""
Script to replace all shops in Heritage Market (سوق التراث) and Port Market (سوق الميناء)
with the complete shop data from bird-market-shops.xlsx.

This ensures:
1. Old incomplete shops are removed
2. New complete shops from Excel are added
3. Area IDs are preserved
4. No inspection data is affected (verified: no inspections exist for these shops)
"""

import json
import pandas as pd
import time

# Define target areas
HERITAGE_MARKET = 'سوق التراث'
PORT_MARKET = 'سوق الميناء'
HERITAGE_AREA_ID = 'area_1758839353326'
PORT_AREA_ID = 'area_1758839345230'

def read_excel_shops():
    """Read shops from bird-market-shops.xlsx"""
    # Read Excel file, skip first 3 rows
    df = pd.read_excel('bird-market-shops.xlsx', skiprows=3)
    
    # First row contains headers
    headers = df.iloc[0].tolist()
    df = df[1:]  # Remove header row from data
    df.columns = headers
    
    # Clean up
    df = df.dropna(how='all')
    
    # Clean up area names (remove extra spaces)
    df['المنطقة'] = df['المنطقة'].str.strip()
    
    return df

def create_shop_object(row, area_id):
    """Create a shop object from Excel row"""
    # Generate unique shop ID
    shop_id = f"shop_{int(time.time() * 1000)}"
    time.sleep(0.001)  # Small delay to ensure unique IDs
    
    # Get area name
    area = row['المنطقة']
    
    # Create shop object
    shop = {
        'id': shop_id,
        'name': str(row['الإسم باللغة العربية']).strip(),
        'area': area,
        'areaId': area_id
    }
    
    # Add optional fields if they exist and are not NaN
    if pd.notna(row.get('ADM Code')):
        shop['admCode'] = str(row['ADM Code']).strip()
    
    if pd.notna(row.get('رقم الترخيص')):
        shop['license'] = str(row['رقم الترخيص']).strip()
    
    if pd.notna(row.get('الإسم باللغة الإنجليزية')):
        shop['englishName'] = str(row['الإسم باللغة الإنجليزية']).strip()
    
    if pd.notna(row.get('الموقع علي خرائط جوجل')):
        shop['googleMapsUrl'] = str(row['الموقع علي خرائط جوجل']).strip()
    
    if pd.notna(row.get('رقم الهاتف')):
        phone = str(row['رقم الهاتف']).strip()
        # Remove .0 from phone numbers if they exist
        if phone.endswith('.0'):
            phone = phone[:-2]
        shop['phone'] = phone
    
    return shop

def replace_bird_market_shops():
    """Main function to replace shops"""
    print("Starting shop replacement process...")
    
    # Read current plan-data.json
    print("\n1. Reading plan-data.json...")
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Count current shops
    total_shops_before = len(data.get('shops', []))
    print(f"   Total shops before: {total_shops_before}")
    
    # Find and remove existing shops in target areas
    print("\n2. Removing existing shops in Heritage and Port Markets...")
    old_shops = []
    new_shops = []
    
    for shop in data.get('shops', []):
        if shop.get('area') in [HERITAGE_MARKET, PORT_MARKET]:
            old_shops.append(shop)
            print(f"   Removing: {shop['id']} - {shop.get('name', 'N/A')}")
        else:
            new_shops.append(shop)
    
    print(f"   Removed {len(old_shops)} shops")
    
    # Read new shops from Excel
    print("\n3. Reading new shops from bird-market-shops.xlsx...")
    df = read_excel_shops()
    print(f"   Found {len(df)} shops in Excel")
    
    # Add new shops
    print("\n4. Adding new shops...")
    heritage_shops = df[df['المنطقة'] == HERITAGE_MARKET]
    port_shops = df[df['المنطقة'] == PORT_MARKET]
    
    print(f"   Heritage Market shops: {len(heritage_shops)}")
    for idx, row in heritage_shops.iterrows():
        shop = create_shop_object(row, HERITAGE_AREA_ID)
        new_shops.append(shop)
        print(f"   Added: {shop['id']} - {shop['name']}")
    
    print(f"\n   Port Market shops: {len(port_shops)}")
    for idx, row in port_shops.iterrows():
        shop = create_shop_object(row, PORT_AREA_ID)
        new_shops.append(shop)
        print(f"   Added: {shop['id']} - {shop['name']}")
    
    # Update data
    data['shops'] = new_shops
    
    # Count final shops
    total_shops_after = len(data['shops'])
    print(f"\n5. Summary:")
    print(f"   Total shops before: {total_shops_before}")
    print(f"   Shops removed: {len(old_shops)}")
    print(f"   Shops added: {len(heritage_shops) + len(port_shops)}")
    print(f"   Total shops after: {total_shops_after}")
    print(f"   Net change: {total_shops_after - total_shops_before:+d}")
    
    # Save updated data
    print("\n6. Saving updated plan-data.json...")
    with open('plan-data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("\n✓ Shop replacement completed successfully!")
    print(f"  Heritage Market (سوق التراث): {len(heritage_shops)} shops")
    print(f"  Port Market (سوق الميناء): {len(port_shops)} shops")
    print(f"  Total: {len(heritage_shops) + len(port_shops)} shops")
    
    return True

if __name__ == '__main__':
    try:
        replace_bird_market_shops()
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
