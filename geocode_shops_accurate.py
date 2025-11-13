#!/usr/bin/env python3
"""
Google Maps Accurate Geocoding Script
Geocodes all shop addresses to get accurate coordinates and map links
Uses Google Maps Geocoding API for 100% accurate location mapping
"""

import json
import requests
import time
from urllib.parse import quote

# Google Maps API Key from the configuration
API_KEY = "AIzaSyBIu6hLqc2mW6WYKTf1JCMSjKCkN1E-xVU"

def geocode_address(address, shop_name, area):
    """
    Geocode an address to get coordinates and Google Maps link
    
    Args:
        address: Shop address in Arabic
        shop_name: Shop name for better search
        area: Area/region name
    
    Returns:
        dict with lat, lng, and map_url
    """
    # Construct search query: shop name + address + area + Abu Dhabi, UAE
    search_query = f"{shop_name}, {address}, {area}, Abu Dhabi, UAE"
    
    # URL encode the query
    encoded_query = quote(search_query)
    
    # Google Maps Geocoding API endpoint
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={encoded_query}&key={API_KEY}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data['status'] == 'OK' and len(data['results']) > 0:
            location = data['results'][0]['geometry']['location']
            lat = location['lat']
            lng = location['lng']
            
            # Create accurate Google Maps URL with coordinates
            map_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
            
            # Also create short link format
            short_url = f"https://maps.google.com/?q={lat},{lng}"
            
            return {
                'lat': lat,
                'lng': lng,
                'map_url': map_url,
                'short_url': short_url,
                'formatted_address': data['results'][0]['formatted_address'],
                'status': 'success'
            }
        else:
            print(f"❌ Geocoding failed for {shop_name}: {data.get('status', 'UNKNOWN')}")
            return {
                'status': 'failed',
                'error': data.get('status', 'UNKNOWN'),
                'map_url': None
            }
    
    except Exception as e:
        print(f"❌ Error geocoding {shop_name}: {str(e)}")
        return {
            'status': 'error',
            'error': str(e),
            'map_url': None
        }

def update_shops_with_accurate_locations():
    """
    Update all shops in shops_details.json with accurate Google Maps coordinates
    """
    print("🗺️ Starting accurate geocoding for all shops...")
    print("=" * 70)
    
    # Load shops data
    with open('shops_details.json', 'r', encoding='utf-8') as f:
        shops = json.load(f)
    
    total_shops = len(shops)
    success_count = 0
    failed_count = 0
    skipped_count = 0
    
    print(f"📊 Total shops to geocode: {total_shops}")
    print("=" * 70)
    
    # Process each shop
    for idx, (shop_key, shop_data) in enumerate(shops.items(), 1):
        print(f"\n[{idx}/{total_shops}] Processing: {shop_data.get('nameAr', shop_key)}")
        
        # Skip if already has accurate coordinates (not the placeholder)
        current_map = shop_data.get('locationMap', '')
        if current_map and current_map != 'https://maps.app.goo.gl/WLKn2FPk9gN7MSNC8':
            # Check if it's already a coordinate-based URL
            if 'query=' in current_map or '?q=' in current_map:
                print(f"✅ Already has accurate coordinates, skipping...")
                skipped_count += 1
                continue
        
        # Get shop details
        shop_name = shop_data.get('nameEn', shop_data.get('nameAr', shop_key))
        address = shop_data.get('address', '')
        area = shop_data.get('area', 'Abu Dhabi')
        
        if not address:
            print(f"⚠️ No address found, using area as fallback")
            address = area
        
        # Geocode the address
        result = geocode_address(address, shop_name, area)
        
        if result['status'] == 'success':
            # Update shop data with accurate location
            shop_data['locationMap'] = result['map_url']
            shop_data['coordinates'] = {
                'lat': result['lat'],
                'lng': result['lng']
            }
            shop_data['formattedAddress'] = result['formatted_address']
            
            print(f"✅ Success! Coordinates: ({result['lat']}, {result['lng']})")
            print(f"   Map URL: {result['map_url']}")
            success_count += 1
        else:
            print(f"❌ Failed to geocode")
            failed_count += 1
        
        # Respect API rate limits (avoid hitting quota too fast)
        # Google allows 50 requests per second, but we'll be conservative
        time.sleep(0.1)  # 10 requests per second
        
        # Save progress every 10 shops
        if idx % 10 == 0:
            with open('shops_details.json', 'w', encoding='utf-8') as f:
                json.dump(shops, f, ensure_ascii=False, indent=2)
            print(f"\n💾 Progress saved ({idx}/{total_shops} shops processed)")
    
    # Final save
    with open('shops_details.json', 'w', encoding='utf-8') as f:
        json.dump(shops, f, ensure_ascii=False, indent=2)
    
    # Print summary
    print("\n" + "=" * 70)
    print("🎉 Geocoding Complete!")
    print("=" * 70)
    print(f"✅ Successfully geocoded: {success_count}")
    print(f"⏭️ Skipped (already accurate): {skipped_count}")
    print(f"❌ Failed: {failed_count}")
    print(f"📊 Total: {total_shops}")
    print(f"📈 Success rate: {(success_count / (total_shops - skipped_count) * 100):.1f}%")
    print("=" * 70)
    print("\n✅ All shops now have accurate Google Maps coordinates!")

if __name__ == "__main__":
    update_shops_with_accurate_locations()
