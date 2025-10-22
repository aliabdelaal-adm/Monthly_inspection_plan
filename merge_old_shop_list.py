#!/usr/bin/env python3
"""
Merge old-shop-list-updated.xlsx into plan-data.json
This script reads shop data from the Excel file and merges it into the JSON plan data.
"""

import json
import sys
import io
import pandas as pd
from datetime import datetime

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def load_json_file(filename):
    """Load and parse a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error loading {filename}: {e}")
        return None

def save_json_file(filename, data):
    """Save data to a JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"❌ Error saving {filename}: {e}")
        return False

def load_excel_shops(filename):
    """Load shop data from Excel file."""
    try:
        # Read Excel file, skipping the first row
        df = pd.read_excel(filename, skiprows=1, header=0)
        
        # Get the first 8 columns that contain shop data
        df_clean = df.iloc[:, :8]
        df_clean.columns = ['Index', 'ADM Code', 'License No', 'Trade Name (EN)', 'Trade Name (AR)', 'Location', 'Area', 'Contact']
        
        # Remove rows where all important columns are NaN
        df_clean = df_clean.dropna(how='all')
        
        # Convert to list of dictionaries
        shops = []
        for idx, row in df_clean.iterrows():
            # Skip header row (first row after cleanup)
            if idx == 0 or str(row['Trade Name (AR)']).strip() in ['TRADE NAME AR.', 'Trade Name (AR)']:
                continue
                
            # Skip if no trade name
            if pd.isna(row['Trade Name (AR)']):
                continue
                
            shop = {
                'adm_code': str(row['ADM Code']) if pd.notna(row['ADM Code']) else None,
                'license_no': str(row['License No']) if pd.notna(row['License No']) else None,
                'name_en': str(row['Trade Name (EN)']).strip() if pd.notna(row['Trade Name (EN)']) else None,
                'name_ar': str(row['Trade Name (AR)']).strip() if pd.notna(row['Trade Name (AR)']) else None,
                'location': str(row['Location']).strip() if pd.notna(row['Location']) else None,
                'map_url': str(row['Area']).strip() if pd.notna(row['Area']) and 'http' in str(row['Area']) else None,
                'contact': str(row['Contact']).strip() if pd.notna(row['Contact']) else None
            }
            shops.append(shop)
        
        return shops
    except Exception as e:
        print(f"❌ Error loading Excel file {filename}: {e}")
        import traceback
        traceback.print_exc()
        return None

def find_area_by_location(location, areas):
    """Find area ID by location name."""
    if not location:
        return None
    
    # Normalize location string
    location = location.strip()
    
    # Map common location names and variations to area names
    location_map = {
        'سوق الميناء': 'سوق الميناء',
        'سوق التراث': 'سوق التراث',
        'الحصن': 'الحصن',
        'جزيرة ابوظبي, الحصن': 'الحصن',
        'الخالدية': 'الخالدية',
        'الدانة': 'الدانة',
        'الدانة الفلاح بلازا': 'الدانة',
        'شارع الفلاح': 'الدانة',
        'الشامخة': 'الشامخة',
        'الشامخة ': 'الشامخة',
        'المصفح': 'المصفح',
        'المصفح ': 'المصفح',
        'بني ياس': 'بني ياس',
        'مدينة خليفة': 'مدينة خليفة',
        'مدينة خليفة ': 'مدينة خليفة',
        'ﻣﺪﻳﻨﺔ ﺧﻠﻴﻔﺔ ': 'مدينة خليفة',
        'محمد بن زايد': 'محمد بن زايد',
        'محمد بن زايد ': 'محمد بن زايد',
        'جزيرة ياس': 'جزيرة ياس',
        'جزيرة الريم': 'جزيرة الريم',
        'الباهية': 'الباهية',
        'الباهية ': 'الباهية',
        'الباهية مزرعة 278': 'الباهية',
        'البطين': 'البطين',
        ' البطين': 'البطين',
        'الزاهية': 'الزاهية',
        'الشهامة': 'الشهامة',
        'الشهامه ': 'الشهامة',
        'الوثبة جنوب': 'الوثبة جنوب',
        'جزيرة السعديات': 'جزيرة السعديات',
        'شاطيء الراحة': 'شاطيء الراحة',
        'شاطئ الراحة': 'شاطيء الراحة',
        'شاطئ الراحة ': 'شاطيء الراحة',
        'شاطىء الراحة': 'شاطيء الراحة',
        'آل نهيان': 'آل نهيان',
        ' آل نهيان': 'آل نهيان',
        'ربدان': 'ربدان',
        'المشرف': 'المشرف',
        'المشرف  ': 'المشرف',
        'المشرف مول ': 'محلات المولات',
        'الوحدة مول': 'محلات المولات',
        'شارع المطار ': 'محلات المولات',
        'شارع مبارك بن محمد': 'محلات المولات',
        'شارع خليفة بن زايد ': 'محلات المولات',
        'الريف': 'محلات المولات',
        'المنتزه ': 'محلات المولات',
        'المنهل': 'محلات المولات',
        'أبوظبي': 'محلات المولات',
        'ميناء  زايد': 'محلات المولات'
    }
    
    area_name = location_map.get(location, location)
    
    # Find matching area
    for area in areas:
        if area['name'] == area_name:
            return area['id']
    
    return None

def normalize_shop_name(name):
    """Normalize shop name for comparison."""
    if not name:
        return ""
    # Remove extra spaces and normalize
    return ' '.join(name.strip().split())

def find_existing_shop(shop_name, existing_shops):
    """Find existing shop by name."""
    normalized_name = normalize_shop_name(shop_name)
    
    for shop in existing_shops:
        existing_normalized = normalize_shop_name(shop.get('name', ''))
        if normalized_name == existing_normalized:
            return shop
    
    return None

def generate_shop_id():
    """Generate a unique shop ID."""
    timestamp = int(datetime.now().timestamp() * 1000)
    return f"shop_{timestamp}"

def merge_excel_to_json(excel_file, json_file):
    """Merge Excel shop data into JSON plan data."""
    print("=== Merging old-shop-list-updated.xlsx into plan-data.json ===")
    print()
    
    # Load files
    print("📂 Loading files...")
    excel_shops = load_excel_shops(excel_file)
    plan_data = load_json_file(json_file)
    
    if not excel_shops or not plan_data:
        print("❌ Failed to load required files!")
        return False
    
    print(f"✅ Excel file loaded: {len(excel_shops)} shops")
    print(f"✅ JSON file loaded: {len(plan_data.get('shops', []))} existing shops")
    print()
    
    # Create backup
    backup_filename = f"{json_file}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    print(f"💾 Creating backup: {backup_filename}")
    if not save_json_file(backup_filename, plan_data):
        print("❌ Failed to create backup!")
        return False
    
    # Merge data
    print("🔄 Merging shop data...")
    
    existing_shops = plan_data.get('shops', [])
    areas = plan_data.get('areas', [])
    
    updated_count = 0
    new_count = 0
    skipped_count = 0
    
    for excel_shop in excel_shops:
        # Use Arabic name as primary, fallback to English
        shop_name = excel_shop['name_ar'] or excel_shop['name_en']
        if not shop_name:
            skipped_count += 1
            continue
        
        # Check if shop already exists
        existing_shop = find_existing_shop(shop_name, existing_shops)
        
        if existing_shop:
            # Update existing shop with additional data from Excel
            if excel_shop['adm_code']:
                existing_shop['admCode'] = excel_shop['adm_code']
            if excel_shop['license_no']:
                existing_shop['licenseNo'] = excel_shop['license_no']
            if excel_shop['name_en']:
                existing_shop['nameEn'] = excel_shop['name_en']
            if excel_shop['contact']:
                existing_shop['contact'] = excel_shop['contact']
            if excel_shop['map_url']:
                existing_shop['mapUrl'] = excel_shop['map_url']
            
            # Update area if location is specified and we can find matching area
            if excel_shop['location']:
                area_id = find_area_by_location(excel_shop['location'], areas)
                if area_id:
                    existing_shop['areaId'] = area_id
            
            updated_count += 1
        else:
            # Create new shop
            area_id = find_area_by_location(excel_shop['location'], areas)
            
            new_shop = {
                'id': generate_shop_id(),
                'name': shop_name
            }
            
            if area_id:
                new_shop['areaId'] = area_id
            if excel_shop['adm_code']:
                new_shop['admCode'] = excel_shop['adm_code']
            if excel_shop['license_no']:
                new_shop['licenseNo'] = excel_shop['license_no']
            if excel_shop['name_en']:
                new_shop['nameEn'] = excel_shop['name_en']
            if excel_shop['contact']:
                new_shop['contact'] = excel_shop['contact']
            if excel_shop['map_url']:
                new_shop['mapUrl'] = excel_shop['map_url']
            
            existing_shops.append(new_shop)
            new_count += 1
    
    # Update plan data
    plan_data['shops'] = existing_shops
    plan_data['lastUpdate'] = datetime.now().isoformat()
    
    # Save merged data
    print("💾 Saving merged data...")
    if not save_json_file(json_file, plan_data):
        print("❌ Failed to save merged data!")
        return False
    
    # Report results
    print()
    print("✅ Merge completed successfully!")
    print("📊 Merge Summary:")
    print(f"   🔄 Shops updated with Excel data: {updated_count}")
    print(f"   ➕ New shops added: {new_count}")
    print(f"   ⏭️  Shops skipped (no name): {skipped_count}")
    print()
    print(f"📈 Final counts:")
    print(f"   🏪 Total shops: {len(plan_data.get('shops', []))}")
    print(f"   📅 Last update: {plan_data.get('lastUpdate')}")
    
    return True

def main():
    excel_file = 'old-shop-list-updated.xlsx'
    json_file = 'plan-data.json'
    
    success = merge_excel_to_json(excel_file, json_file)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
