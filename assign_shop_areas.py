#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to assign area and areaId to all shops in shops_details.json
based on their address field by matching with areas from plan-data.json
"""

import json
import re
from datetime import datetime

def load_json_file(filename):
    """Load JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(filename, data):
    """Save JSON file with proper formatting"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def normalize_text(text):
    """Normalize Arabic text for comparison"""
    if not text:
        return ""
    # Remove extra spaces and normalize
    text = re.sub(r'\s+', ' ', text.strip())
    return text.lower()

def find_area_match(address, areas):
    """
    Find the best matching area for a given address
    Returns (area_id, area_name) or (None, None) if no match
    """
    if not address:
        return None, None
    
    normalized_address = normalize_text(address)
    
    # Create area mapping with normalized names for matching
    area_map = []
    for area in areas:
        area_map.append({
            'id': area['id'],
            'name': area['name'],
            'normalized': normalize_text(area['name'])
        })
    
    # Try exact match first
    for area in area_map:
        if area['normalized'] in normalized_address:
            return area['id'], area['name']
    
    # Try partial matches for special cases
    # Handle "الوثبة الجنوبية" as "الوثبة جنوب"
    if 'الوثبة الجنوبية' in address or 'الوثبة جنوب' in address:
        for area in area_map:
            if area['name'] == 'الوثبة جنوب':
                return area['id'], area['name']
    
    # Handle "جزيرة ابوظبي" addresses with specific areas
    if 'جزيرة ابوظبي' in address:
        # Check for specific areas mentioned after "جزيرة ابوظبي"
        for area in area_map:
            if area['normalized'] in normalized_address and area['name'] not in ['محلات المولات']:
                return area['id'], area['name']
    
    # Handle "المصفح صناعية" or "مصفح" as "المصفح"
    if 'المصفح' in address or 'مصفح' in address:
        for area in area_map:
            if area['name'] == 'المصفح':
                return area['id'], area['name']
    
    # Handle "أبو ظبي - شارع الميناء" as "سوق الميناء"
    if 'شارع  الميناء' in address or 'شارع الميناء' in address:
        for area in area_map:
            if area['name'] == 'سوق الميناء':
                return area['id'], area['name']
    
    # Handle "الشهامه الجديدة" as "الشهامة"
    if 'الشهامه' in address or 'الشهامة' in address:
        for area in area_map:
            if area['name'] == 'الشهامة':
                return area['id'], area['name']
    
    # Handle "حدائق الراحة" as "شاطيء الراحة"
    if 'حدائق الراحة' in address or 'شاطئ الراحة' in address or 'شاطيء الراحة' in address:
        for area in area_map:
            if area['name'] == 'شاطيء الراحة':
                return area['id'], area['name']
    
    # Handle mobile salon
    if 'صالون متنقل' in address:
        for area in area_map:
            if area['name'] == 'صالون متنقل':
                return area['id'], area['name']
    
    # Handle "الميناء" as "سوق الميناء"
    if 'الميناء' in address and 'سوق الميناء' not in address:
        for area in area_map:
            if area['name'] == 'سوق الميناء':
                return area['id'], area['name']
    
    # Handle "شمال الوثبة" as "الوثبة جنوب"
    if 'شمال الوثبة' in address or 'الوثبة' in address:
        for area in area_map:
            if area['name'] == 'الوثبة جنوب':
                return area['id'], area['name']
    
    # Handle any "شاطئ الراحة" variations
    if 'الراحة' in address or 'الراحه' in address:
        for area in area_map:
            if area['name'] == 'شاطيء الراحة':
                return area['id'], area['name']
    
    # Handle "شارع المطار" - usually in Abu Dhabi island areas
    if 'شارع المطار' in address or 'شارع الفلاح' in address:
        for area in area_map:
            if area['name'] == 'الخالدية':  # Default to Khalidiya for central Abu Dhabi
                return area['id'], area['name']
    
    # Handle generic "جزيرة أبوظبي" or "أبوظبي" - default to a central area
    if 'جزيرة أبوظبي' in address or 'جزيرة ابوظبي' in address or address.startswith('أبوظبي'):
        # Default to Khalidiya for unspecified Abu Dhabi locations
        for area in area_map:
            if area['name'] == 'الخالدية':
                return area['id'], area['name']
    
    # Handle "شارع حمدان" or "شارع زايد الثاني" - central Abu Dhabi areas
    if 'شارع حمدان' in address or 'شارع  حمدان' in address or 'شارع  زايد الثاني' in address or 'شارع زايد الثاني' in address or 'شارع  خليفة بن زايد' in address or 'النادي السياحي' in address:
        for area in area_map:
            if area['name'] == 'الخالدية':
                return area['id'], area['name']
    
    # Handle "ميناء زايد" as "سوق الميناء"
    if 'ميناء زايد' in address or 'ميناء' in address:
        for area in area_map:
            if area['name'] == 'سوق الميناء':
                return area['id'], area['name']
    
    # Handle "الرحبة" - farm/rural area
    if 'الرحبة' in address or 'مزارع الرحبة' in address:
        # Create default for farms - can be mapped to a specific area if needed
        for area in area_map:
            if area['name'] == 'حديقة حيوانات':  # Use zoo area for farms
                return area['id'], area['name']
    
    # Handle industrial areas - default to المصفح
    if 'الصناعية' in address or 'ايكاد' in address or 'مدينة أبوظبي الصناعية' in address:
        for area in area_map:
            if area['name'] == 'المصفح':
                return area['id'], area['name']
    
    # Handle residential areas like "المنهل", "المنتزه", "الريف"
    if 'المنهل' in address or 'المنتزه' in address or 'الريف' in address:
        # These are residential areas, default to محمد بن زايد
        for area in area_map:
            if area['name'] == 'محمد بن زايد':
                return area['id'], area['name']
    
    # Handle "المفرق" - far area, could be a new area or mapped to existing
    if 'المفرق' in address:
        # Map to a general area like الشامخة
        for area in area_map:
            if area['name'] == 'الشامخة':
                return area['id'], area['name']
    
    return None, None

def main():
    print("🔄 بدء عملية تعيين المناطق للمحلات...")
    print("=" * 60)
    
    # Load data files
    print("\n📥 تحميل ملفات البيانات...")
    plan_data = load_json_file('plan-data.json')
    shops_details = load_json_file('shops_details.json')
    
    areas = plan_data.get('areas', [])
    print(f"✅ تم تحميل {len(areas)} منطقة من plan-data.json")
    print(f"✅ تم تحميل {len(shops_details)} محل من shops_details.json")
    
    # Create backup
    backup_filename = f'shops_details.json.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    save_json_file(backup_filename, shops_details)
    print(f"\n💾 تم إنشاء نسخة احتياطية: {backup_filename}")
    
    # Process each shop
    print("\n🔍 معالجة المحلات...")
    updated_count = 0
    no_match_count = 0
    already_assigned_count = 0
    no_match_shops = []
    
    for shop_name, shop_data in shops_details.items():
        # Check if already has area assignment
        if shop_data.get('area') and shop_data.get('areaId'):
            already_assigned_count += 1
            continue
        
        # Try to find matching area
        address = shop_data.get('address', '')
        area_id, area_name = find_area_match(address, areas)
        
        if area_id and area_name:
            shop_data['area'] = area_name
            shop_data['areaId'] = area_id
            updated_count += 1
        else:
            no_match_count += 1
            no_match_shops.append({
                'name': shop_name,
                'address': address
            })
    
    # Save updated shops_details.json
    print("\n💾 حفظ التحديثات...")
    save_json_file('shops_details.json', shops_details)
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 ملخص العملية:")
    print("=" * 60)
    print(f"✅ إجمالي المحلات: {len(shops_details)}")
    print(f"✅ محلات تم تعيين منطقتها: {updated_count}")
    print(f"📌 محلات لها منطقة مسبقاً: {already_assigned_count}")
    print(f"⚠️  محلات بدون تطابق: {no_match_count}")
    print(f"🎯 إجمالي المحلات مع مناطق: {updated_count + already_assigned_count}")
    
    if no_match_shops:
        print("\n⚠️  المحلات التي لم يتم العثور على منطقة مطابقة لها:")
        print("-" * 60)
        for shop in no_match_shops[:10]:  # Show first 10
            print(f"  - {shop['name']}")
            print(f"    العنوان: {shop['address']}")
        if len(no_match_shops) > 10:
            print(f"\n  ... و {len(no_match_shops) - 10} محل آخر")
    
    print("\n✅ تمت العملية بنجاح!")
    print("=" * 60)

if __name__ == '__main__':
    main()
