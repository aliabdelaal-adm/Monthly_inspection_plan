#!/usr/bin/env python3
"""
Smart Merge Script for Shop Details
This script intelligently merges shop data from Excel files into shops_details.json
It fixes shops that have license numbers as names (from shop #74 to #510)
"""

import json
import pandas as pd
import sys
from datetime import datetime

def normalize_license_number(license_no):
    """Normalize license number for matching"""
    if not license_no or pd.isna(license_no):
        return None
    license_str = str(license_no).strip()
    return license_str

def find_match_in_excel(license_no, df_licenses):
    """Find matching shop in Excel data"""
    if not license_no:
        return None
    
    # Try exact match first
    exact_match = df_licenses[df_licenses['LICENSE_NO'].astype(str) == license_no]
    if not exact_match.empty:
        return exact_match.iloc[0]
    
    # Try base license number without suffix (e.g., CN-1193301 from CN-1193301-1)
    if '-' in license_no:
        parts = license_no.split('-')
        if len(parts) >= 2:
            base_license = '-'.join(parts[:2])
            base_match = df_licenses[df_licenses['LICENSE_NO'].astype(str).str.startswith(base_license)]
            if not base_match.empty:
                return base_match.iloc[0]
    
    return None

def safe_str(value):
    """Convert value to string safely"""
    if value is None or pd.isna(value):
        return ""
    return str(value).strip()

def generate_adm_code(index):
    """Generate ADM code based on index"""
    return f"ADM{str(index).zfill(4)}"

def main():
    print("=" * 80)
    print("SMART MERGE SCRIPT - Fixing Shop Names and Data")
    print("=" * 80)
    
    # Load existing shops_details.json
    print("\n[1/6] Loading shops_details.json...")
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    print(f"   ✓ Loaded {len(shops_details)} shops")
    
    # Create backup
    backup_filename = f'shops_details.json.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    print(f"\n[2/6] Creating backup: {backup_filename}")
    with open(backup_filename, 'w', encoding='utf-8') as f:
        json.dump(shops_details, f, ensure_ascii=False, indent=2)
    print("   ✓ Backup created")
    
    # Load Excel data
    print("\n[3/6] Loading Excel data from رخص المحلات الجديدة.xlsx...")
    df_licenses = pd.read_excel('رخص المحلات الجديدة.xlsx')
    print(f"   ✓ Loaded {len(df_licenses)} licenses")
    
    # Identify problem shops
    print("\n[4/6] Identifying shops with license numbers as names...")
    shop_names = list(shops_details.keys())
    problem_shops = []
    good_shops = []
    
    for idx, shop_name in enumerate(shop_names, start=1):
        if shop_name.startswith('CN-'):
            problem_shops.append((idx, shop_name))
        else:
            good_shops.append((idx, shop_name))
    
    print(f"   ✓ Found {len(problem_shops)} shops with license numbers as names")
    print(f"   ✓ Found {len(good_shops)} shops with proper names")
    
    # Fix problem shops
    print("\n[5/6] Fixing shop data...")
    new_shops_details = {}
    matched_count = 0
    unmatched_count = 0
    
    for idx, shop_name in enumerate(shop_names, start=1):
        shop_data = shops_details[shop_name]
        
        # If this is a problem shop (name is a license number)
        if shop_name.startswith('CN-'):
            # Try to find match in Excel
            excel_match = find_match_in_excel(shop_name, df_licenses)
            
            if excel_match is not None:
                # Update with proper data from Excel
                new_name_ar = safe_str(excel_match['TRADE_NAME_AR'])
                new_name_en = safe_str(excel_match['TRADE_NAME_EN'])
                license_no = safe_str(excel_match['LICENSE_NO'])
                
                # Use Arabic name as key if available, otherwise use English name
                if new_name_ar:
                    new_key = new_name_ar
                elif new_name_en:
                    new_key = new_name_en
                else:
                    new_key = shop_name  # Fallback to license number
                
                # Build updated shop data
                updated_shop = {
                    'nameAr': new_name_ar,
                    'nameEn': new_name_en,
                    'licenseNo': license_no,
                    'locationMap': shop_data.get('locationMap', ''),
                    'admCode': shop_data.get('admCode', generate_adm_code(idx)),
                    'address': safe_str(excel_match.get('ADDRESS', shop_data.get('address', ''))),
                    'contact': safe_str(excel_match.get('PHONE', shop_data.get('contact', ''))),
                    'email': safe_str(excel_match.get('EMAIL', shop_data.get('email', ''))),
                    'activity': safe_str(excel_match.get('ACTIVITY_NAME_AR', shop_data.get('activity', '')))
                }
                
                new_shops_details[new_key] = updated_shop
                matched_count += 1
                
                if matched_count <= 5:
                    print(f"   ✓ Fixed: {shop_name} -> {new_key}")
            else:
                # Keep the old data if no match found
                new_shops_details[shop_name] = shop_data
                unmatched_count += 1
                if unmatched_count <= 3:
                    print(f"   ⚠ No match found: {shop_name} (keeping original)")
        else:
            # This is a good shop, keep as is
            new_shops_details[shop_name] = shop_data
    
    print(f"\n   Summary:")
    print(f"   - Total shops: {len(shop_names)}")
    print(f"   - Fixed with Excel data: {matched_count}")
    print(f"   - Unmatched (kept original): {unmatched_count}")
    print(f"   - Already had proper names: {len(good_shops)}")
    
    # Save updated data
    print("\n[6/6] Saving updated shops_details.json...")
    with open('shops_details.json', 'w', encoding='utf-8') as f:
        json.dump(new_shops_details, f, ensure_ascii=False, indent=2)
    print("   ✓ Saved successfully")
    
    print("\n" + "=" * 80)
    print("✅ MERGE COMPLETED SUCCESSFULLY!")
    print("=" * 80)
    print(f"\nBackup saved as: {backup_filename}")
    print(f"Updated file: shops_details.json")
    print(f"\nStatistics:")
    print(f"  - Original shop count: {len(shops_details)}")
    print(f"  - Updated shop count: {len(new_shops_details)}")
    print(f"  - Shops fixed: {matched_count}")
    print(f"  - Shops with proper names preserved: {len(good_shops)}")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n❌ ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
