#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add Google Maps links for missing shops in shops_details.json
"""

import json
import urllib.parse

def generate_google_maps_link(shop_name, area=None):
    """Generate a Google Maps search link for a shop"""
    # Build search query
    query_parts = [shop_name]
    
    # Add area if available
    if area:
        query_parts.append(area)
    
    # Add Abu Dhabi
    query_parts.append("أبو ظبي")
    
    # Create the search query
    query = " ".join(query_parts)
    encoded_query = urllib.parse.quote(query)
    
    # Use Google Maps Search API format
    return f"https://www.google.com/maps/search/?api=1&query={encoded_query}"

def main():
    # Load plan data
    with open('plan-data.json', 'r', encoding='utf-8') as f:
        plan_data = json.load(f)
    
    # Load shops details
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops_details = json.load(f)
    
    print(f"📊 Statistics:")
    print(f"  Total shops in shops_details.json: {len(shops_details)}")
    
    # Collect all shop names with their areas from plan-data.json
    shop_areas = {}
    for entry in plan_data['inspectionData']:
        area = entry.get('area', '')
        for shop in entry.get('shops', []):
            if shop not in shop_areas:
                shop_areas[shop] = area
    
    print(f"  Total unique shops in plan-data.json: {len(shop_areas)}")
    
    # Find shops that need to be added
    added_count = 0
    updated_count = 0
    
    for shop_name, area in shop_areas.items():
        # Check if shop exists with exact name
        if shop_name not in shops_details:
            # Try with cleaned name
            cleaned_name = shop_name.replace('محل ', '')
            
            # Try fuzzy match to find similar shop
            found_similar = False
            similar_shop_key = None
            for key in shops_details.keys():
                if cleaned_name in key or key in cleaned_name:
                    found_similar = True
                    similar_shop_key = key
                    # Update the original entry if it doesn't have a locationMap
                    if not shops_details[key].get('locationMap'):
                        shops_details[key]['locationMap'] = generate_google_maps_link(shop_name, area)
                        updated_count += 1
                        print(f"✅ Updated locationMap for existing shop: {key}")
                    break
            
            # Always add shop with exact name from plan-data.json for perfect matching
            # Even if a similar shop exists, we add it with the exact name
            shops_details[shop_name] = {
                "nameAr": shop_name,
                "nameEn": "",
                "licenseNo": "",
                "locationMap": generate_google_maps_link(shop_name, area),
                "admCode": "",
                "address": area if area else "",
                "contact": "",
                "activity": "بيع الحيوانات والمنتجات البيطرية"
            }
            added_count += 1
            if found_similar:
                print(f"➕ Added shop with exact name (similar exists as '{similar_shop_key}'): {shop_name}")
            else:
                print(f"➕ Added new shop: {shop_name}")
            print(f"   Area: {area}")
            print(f"   Map Link: {shops_details[shop_name]['locationMap']}")
        else:
            # Shop exists with exact name, check if it has a locationMap
            if not shops_details[shop_name].get('locationMap'):
                shops_details[shop_name]['locationMap'] = generate_google_maps_link(shop_name, area)
                updated_count += 1
                print(f"✅ Updated locationMap for: {shop_name}")
    
    # Save updated shops details
    with open('shops_details.json', 'w', encoding='utf-8') as f:
        json.dump(shops_details, f, ensure_ascii=False, indent=2)
    
    print(f"\n📈 Summary:")
    print(f"  New shops added: {added_count}")
    print(f"  Shops updated with maps: {updated_count}")
    print(f"  Total shops now: {len(shops_details)}")
    print(f"\n✅ shops_details.json has been updated!")
    
    # Verify all shops in plan-data now have maps
    missing_maps = 0
    for shop_name in shop_areas.keys():
        if shop_name not in shops_details:
            # Try fuzzy match
            found = False
            for key in shops_details.keys():
                cleaned_name = shop_name.replace('محل ', '')
                if cleaned_name in key or key in cleaned_name:
                    if shops_details[key].get('locationMap'):
                        found = True
                        break
            if not found:
                missing_maps += 1
                print(f"⚠️  Still no map for: {shop_name}")
    
    if missing_maps == 0:
        print(f"\n🎉 All shops now have Google Maps links!")
    else:
        print(f"\n⚠️  {missing_maps} shops still don't have maps")

if __name__ == '__main__':
    main()
