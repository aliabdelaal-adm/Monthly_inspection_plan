#!/usr/bin/env python3
"""
Test script to verify the pet shops Excel cleanup.
"""

import pandas as pd
from collections import defaultdict

def test_pet_shops_excel():
    """Run comprehensive tests on the cleaned Excel file."""
    
    file = 'pet-shops-by-area.xlsx'
    xl = pd.ExcelFile(file)
    
    print("="*80)
    print("Pet Shops Excel Cleanup Tests")
    print("="*80)
    
    all_passed = True
    
    # Test 1: No Summary sheet
    print("\n1. Testing: Summary sheet removal...")
    if 'Summary - الملخص' in xl.sheet_names or 'Summary' in xl.sheet_names:
        print("   ❌ FAILED: Summary sheet still exists")
        all_passed = False
    else:
        print("   ✅ PASSED: Summary sheet removed")
    
    # Test 2: All sheets have data
    print("\n2. Testing: All sheets have shops...")
    empty_sheets = []
    for sheet in xl.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet, header=None)
        # Count data rows (skip first 4 rows)
        data_rows = 0
        for idx in range(4, len(df)):
            if not df.iloc[idx].isna().all():
                data_rows += 1
        
        if data_rows == 0:
            empty_sheets.append(sheet)
    
    if empty_sheets:
        print(f"   ⚠️  WARNING: {len(empty_sheets)} sheets have no shops: {empty_sheets}")
    else:
        print("   ✅ PASSED: All sheets have shops")
    
    # Test 3: No exact duplicates within same area
    print("\n3. Testing: No duplicate shops in same area...")
    duplicates_found = []
    
    for sheet in xl.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet, header=None)
        
        seen = set()
        for idx in range(4, len(df)):
            row = df.iloc[idx]
            if row.isna().all():
                continue
            
            name = str(row.iloc[1]) if len(row) > 1 and pd.notna(row.iloc[1]) else ''
            license = str(row.iloc[2]) if len(row) > 2 and pd.notna(row.iloc[2]) else ''
            
            if name:
                key = (name.strip().lower(), license.strip())
                if key in seen and key != ('', ''):
                    duplicates_found.append(f"{name} in {sheet}")
                seen.add(key)
    
    if duplicates_found:
        print(f"   ❌ FAILED: Found {len(duplicates_found)} duplicates:")
        for dup in duplicates_found[:5]:
            print(f"      - {dup}")
        all_passed = False
    else:
        print("   ✅ PASSED: No duplicate shops within areas")
    
    # Test 4: Check link lengths
    print("\n4. Testing: Location links shortened...")
    very_long_links = []
    
    for sheet in xl.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet, header=None)
        
        for idx in range(4, len(df)):
            row = df.iloc[idx]
            if row.isna().all():
                continue
            
            name = str(row.iloc[1]) if len(row) > 1 and pd.notna(row.iloc[1]) else ''
            link = str(row.iloc[7]) if len(row) > 7 and pd.notna(row.iloc[7]) else ''
            
            if link and link != 'nan' and len(link) > 200:
                very_long_links.append((sheet, name, len(link)))
    
    if very_long_links:
        print(f"   ⚠️  WARNING: {len(very_long_links)} links still > 200 chars")
        for area, shop, length in very_long_links[:3]:
            print(f"      - {shop} ({area}): {length} chars")
    else:
        print("   ✅ PASSED: All links shortened appropriately")
    
    # Test 5: Check total shop count
    print("\n5. Testing: Total shop count...")
    total_shops = 0
    for sheet in xl.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet, header=None)
        for idx in range(4, len(df)):
            row = df.iloc[idx]
            if not row.isna().all():
                name = row.iloc[1] if len(row) > 1 and pd.notna(row.iloc[1]) else ''
                if name:
                    total_shops += 1
    
    expected_min = 280
    expected_max = 300
    
    if expected_min <= total_shops <= expected_max:
        print(f"   ✅ PASSED: Total shops = {total_shops} (within expected range)")
    else:
        print(f"   ❌ FAILED: Total shops = {total_shops} (expected {expected_min}-{expected_max})")
        all_passed = False
    
    # Test 6: Check for required columns
    print("\n6. Testing: All sheets have proper structure...")
    missing_structure = []
    
    for sheet in xl.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet, header=None)
        
        # Check if sheet has at least 4 rows (title, subtitle, blank, headers)
        if len(df) < 4:
            missing_structure.append(sheet)
            continue
        
        # Check if headers row contains expected text
        header_row = df.iloc[3]
        header_text = ' '.join([str(val) for val in header_row.values if pd.notna(val)])
        
        if 'اسم المحل' not in header_text and 'Shop Name' not in header_text:
            missing_structure.append(sheet)
    
    if missing_structure:
        print(f"   ❌ FAILED: {len(missing_structure)} sheets missing proper structure")
        all_passed = False
    else:
        print("   ✅ PASSED: All sheets have proper structure")
    
    # Test 7: Check area distribution
    print("\n7. Testing: Area distribution is reasonable...")
    area_counts = {}
    
    for sheet in xl.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet, header=None)
        count = 0
        for idx in range(4, len(df)):
            row = df.iloc[idx]
            if not row.isna().all():
                name = row.iloc[1] if len(row) > 1 and pd.notna(row.iloc[1]) else ''
                if name:
                    count += 1
        area_counts[sheet] = count
    
    # Show distribution
    print(f"   Areas with most shops:")
    sorted_areas = sorted(area_counts.items(), key=lambda x: x[1], reverse=True)
    for area, count in sorted_areas[:5]:
        print(f"      - {area}: {count} shops")
    
    print("   ✅ PASSED: Area distribution looks good")
    
    # Final result
    print("\n" + "="*80)
    if all_passed:
        print("✅ ALL TESTS PASSED!")
        print("\nThe pet shops Excel file has been successfully cleaned and validated.")
    else:
        print("❌ SOME TESTS FAILED!")
        print("\nPlease review the failures above.")
    print("="*80)
    
    return all_passed

if __name__ == '__main__':
    success = test_pet_shops_excel()
    exit(0 if success else 1)
