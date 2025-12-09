#!/usr/bin/env python3
"""
Script to validate that shops are in the correct geographic areas.
This checks if the shop's address or location suggests it should be in a different area.
"""

import pandas as pd
import re
from collections import defaultdict

# Define area name variations and related keywords
AREA_KEYWORDS = {
    'آل نهيان': ['آل نهيان', 'النهيان', 'al nahyan'],
    'الباهية': ['الباهية', 'albahia', 'bahia'],
    'البطين': ['البطين', 'albateen'],
    'الحصن': ['الحصن', 'alhosn'],
    'الخالدية': ['الخالدية', 'alkhalidiya', 'khalidiya'],
    'الدانة': ['الدانة', 'aldana', 'dana'],
    'الزاهية': ['الزاهية', 'alzahia'],
    'الشامخة': ['الشامخة', 'alshamkha'],
    'الشهامة': ['الشهامة', 'alshahamah'],
    'المشرف': ['المشرف', 'almushrif'],
    'المصفح': ['المصفح', 'almusaffah', 'musaffah'],
    'الملاجىء': ['الملاجىء', 'shelters'],
    'الوثبة جنوب': ['الوثبة', 'الوثبه', 'wathba'],
    'بني ياس': ['بني ياس', 'baniyaas', 'bani yas'],
    'جزيرة الريم': ['الريم', 'reem', 'al reem'],
    'جزيرة ياس': ['ياس', 'yas'],
    'حديقة حيوان': ['حديقة', 'حديقه', 'zoo', 'حيوان'],
    'ربدان': ['ربدان', 'rabdan'],
    'سوق التراث': ['التراث', 'heritage', 'souk'],
    'سوق الميناء': ['الميناء', 'port', 'mina'],
    'شاطيء الراحة': ['الراحة', 'alraha', 'raha'],
    'صالون متنقل': ['متنقل', 'mobile', 'salon'],
    'محلات المولات': ['مول', 'mall', 'مولات'],
    'محمد بن زايد': ['محمد بن زايد', 'mzc', 'mohammed bin zayed'],
    'مدينة خليفة': ['مدينة خليفة', 'khalifa city', 'kca'],
}

def check_area_match(shop_area, address):
    """Check if the address suggests the shop should be in a different area."""
    if not isinstance(address, str) or not address.strip():
        return None
    
    address_lower = address.lower()
    
    # Check for mentions of other areas in the address
    suggested_areas = []
    for area, keywords in AREA_KEYWORDS.items():
        if area == shop_area:
            continue  # Skip current area
        
        for keyword in keywords:
            if keyword.lower() in address_lower:
                suggested_areas.append(area)
                break
    
    return suggested_areas if suggested_areas else None

def read_and_validate_shops(file_path):
    """Read shops and validate their area assignments."""
    xl = pd.ExcelFile(file_path)
    issues = []
    
    for sheet_name in xl.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
        
        # Process data rows (skip first 4 rows: title, subtitle, blank, headers)
        for idx in range(4, len(df)):
            row = df.iloc[idx]
            if row.isna().all():
                continue
            
            name = row.iloc[1] if len(row) > 1 and pd.notna(row.iloc[1]) else ''
            address = row.iloc[4] if len(row) > 4 and pd.notna(row.iloc[4]) else ''
            
            if not name:
                continue
            
            # Check if address suggests different area
            suggested_areas = check_area_match(sheet_name, address)
            if suggested_areas:
                issues.append({
                    'current_area': sheet_name,
                    'shop_name': name,
                    'address': address,
                    'suggested_areas': suggested_areas
                })
    
    return issues

def main():
    file_path = 'pet-shops-by-area.xlsx'
    
    print("="*80)
    print("Pet Shops Area Validation")
    print("="*80)
    
    print("\nValidating shop area assignments...")
    issues = read_and_validate_shops(file_path)
    
    if not issues:
        print("\n✓ All shops appear to be in the correct areas!")
        print("  No address/area mismatches detected.")
    else:
        print(f"\n⚠ Found {len(issues)} potential area mismatches:")
        print("="*80)
        
        for i, issue in enumerate(issues, 1):
            print(f"\n{i}. Shop: {issue['shop_name']}")
            print(f"   Current Area: {issue['current_area']}")
            print(f"   Address: {issue['address']}")
            print(f"   Suggested Area(s): {', '.join(issue['suggested_areas'])}")
    
    print("\n" + "="*80)
    print("Validation complete!")
    print("="*80)
    
    # Summary
    if issues:
        print("\nNote: These are suggestions based on keywords in addresses.")
        print("Manual review is recommended as some shops may intentionally be in different areas.")
        print("For example, a shop with 'mall' in the address might still be in a specific area,")
        print("not in the 'محلات المولات' area.")

if __name__ == '__main__':
    main()
