#!/usr/bin/env python3
"""
Verification script for the smart shop merge
This script verifies that the merge was successful and the data is correct
"""

import json
import sys

def main():
    print("=" * 80)
    print("VERIFICATION REPORT: Smart Shop Merge")
    print("=" * 80)
    
    # Load shops_details.json
    print("\n[1] Loading shops_details.json...")
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops = json.load(f)
    print(f"   ✓ Loaded {len(shops)} shops")
    
    # Check for shops with license numbers as names
    print("\n[2] Checking for shops with license numbers as names...")
    shops_with_cn_names = [name for name in shops.keys() if name.startswith('CN-')]
    print(f"   ✓ Found {len(shops_with_cn_names)} shops with CN- prefix as name")
    if shops_with_cn_names:
        print(f"   ⚠ WARNING: These shops still have license numbers as names:")
        for shop_name in shops_with_cn_names[:10]:
            print(f"      - {shop_name}")
    
    # Check data completeness
    print("\n[3] Checking data completeness...")
    complete_shops = 0
    missing_nameAr = 0
    missing_nameEn = 0
    missing_license = 0
    missing_contact = 0
    
    for name, info in shops.items():
        has_all = True
        if not info.get('nameAr'):
            missing_nameAr += 1
            has_all = False
        if not info.get('nameEn'):
            missing_nameEn += 1
            has_all = False
        if not info.get('licenseNo'):
            missing_license += 1
            has_all = False
        if not info.get('contact'):
            missing_contact += 1
            has_all = False
        
        if has_all:
            complete_shops += 1
    
    print(f"   ✓ Complete shops (all fields): {complete_shops}/{len(shops)}")
    print(f"   - Missing Arabic name: {missing_nameAr}")
    print(f"   - Missing English name: {missing_nameEn}")
    print(f"   - Missing license: {missing_license}")
    print(f"   - Missing contact: {missing_contact}")
    
    # Sample quality check
    print("\n[4] Sample quality check (first 5 shops with complete data)...")
    sample_count = 0
    for name, info in shops.items():
        if info.get('nameAr') and info.get('nameEn') and info.get('licenseNo'):
            print(f"\n   Shop: {name}")
            print(f"   Arabic: {info.get('nameAr')}")
            print(f"   English: {info.get('nameEn')}")
            print(f"   License: {info.get('licenseNo')}")
            sample_count += 1
            if sample_count >= 5:
                break
    
    # Check for shops in the range 74-510
    print("\n[5] Verifying shop range (positions 74-510)...")
    shop_names = list(shops.keys())
    if len(shop_names) >= 74:
        print(f"   Shop at position 74: {shop_names[73]}")
        print(f"   Details: nameAr={shops[shop_names[73]].get('nameAr', 'N/A')[:40]}...")
    
    if len(shop_names) >= 490:
        print(f"   Shop at position 490: {shop_names[489]}")
        print(f"   Details: nameAr={shops[shop_names[489]].get('nameAr', 'N/A')[:40]}...")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total shops: {len(shops)}")
    print(f"Shops with proper names: {len(shops) - len(shops_with_cn_names)}")
    print(f"Shops still with CN- prefix: {len(shops_with_cn_names)}")
    print(f"Completeness rate: {complete_shops}/{len(shops)} ({100*complete_shops/len(shops):.1f}%)")
    
    if len(shops_with_cn_names) == 0:
        print("\n✅ SUCCESS: All shops have proper Arabic and English names!")
        return 0
    else:
        print(f"\n⚠ WARNING: {len(shops_with_cn_names)} shops still need attention")
        return 1

if __name__ == '__main__':
    sys.exit(main())
