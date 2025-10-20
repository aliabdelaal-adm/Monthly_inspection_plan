#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Location Tracking Data Structure
Tests the location tracking JSON file and validates data integrity
"""

import json
import sys
import io
from datetime import datetime, timedelta

# Ensure UTF-8 encoding for output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_location_tracking_structure():
    """Test location tracking JSON structure"""
    print("🧪 Testing Location Tracking Data Structure...")
    print("=" * 60)
    
    try:
        # Load location tracking data
        with open("location-tracking.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        print("✅ Successfully loaded location-tracking.json")
        
        # Validate structure
        assert "locationTracking" in data, "Missing locationTracking array"
        assert "privacyConsent" in data, "Missing privacyConsent object"
        assert "trackingSettings" in data, "Missing trackingSettings object"
        
        print("✅ All required top-level keys present")
        
        # Validate settings
        settings = data["trackingSettings"]
        assert "enabled" in settings, "Missing enabled in settings"
        assert "updateInterval" in settings, "Missing updateInterval in settings"
        assert "accuracyThreshold" in settings, "Missing accuracyThreshold in settings"
        
        print("✅ Tracking settings structure is valid")
        print(f"   - Enabled: {settings['enabled']}")
        print(f"   - Update Interval: {settings['updateInterval']}ms ({settings['updateInterval']/1000/60} minutes)")
        print(f"   - Accuracy Threshold: {settings['accuracyThreshold']}m")
        
        print("\n✅ All tests passed!")
        return True
        
    except FileNotFoundError:
        print("❌ Error: location-tracking.json not found")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format - {e}")
        return False
    except AssertionError as e:
        print(f"❌ Error: Validation failed - {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def create_sample_location_data():
    """Create sample location tracking data for testing"""
    print("\n📝 Creating Sample Location Data...")
    print("=" * 60)
    
    sample_locations = []
    base_time = datetime.now()
    
    # Create sample data for 3 inspectors over the last 5 hours
    inspectors = [
        {"name": "د. آمنه بن صرم", "area": "سوق الميناء"},
        {"name": "د. آيه سلامة", "area": "الحصن"},
        {"name": "د. حسينة العامري", "area": "سوق الميناء"}
    ]
    
    # Base coordinates (Abu Dhabi area)
    base_coords = [
        {"lat": 24.4539, "lng": 54.3773},  # Abu Dhabi
        {"lat": 24.4764, "lng": 54.3705},  # Al Hosn
        {"lat": 24.5100, "lng": 54.3787}   # Mina area
    ]
    
    for i, inspector in enumerate(inspectors):
        # Generate 6 location points (every 5 minutes for 30 minutes)
        for j in range(6):
            time_offset = timedelta(minutes=-30 + (j * 5))
            timestamp = (base_time + time_offset).isoformat()
            
            # Slight variation in coordinates to simulate movement
            lat_variation = (j * 0.0001) - 0.0003
            lng_variation = (j * 0.0001) - 0.0002
            
            location = {
                "timestamp": timestamp,
                "latitude": base_coords[i]["lat"] + lat_variation,
                "longitude": base_coords[i]["lng"] + lng_variation,
                "accuracy": 10 + (j * 2),  # Accuracy varies 10-20m
                "inspector": inspector["name"],
                "day": base_time.strftime("%Y-%m-%d"),
                "shift": "صباحية" if base_time.hour < 14 else "مسائية",
                "area": inspector["area"]
            }
            sample_locations.append(location)
    
    # Save sample data
    try:
        with open("location-tracking.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        data["locationTracking"] = sample_locations
        
        with open("location-tracking-sample.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Created sample data with {len(sample_locations)} location points")
        print(f"   Saved to: location-tracking-sample.json")
        print(f"\n📊 Sample data includes:")
        print(f"   - {len(inspectors)} inspectors")
        print(f"   - {len(sample_locations)} total location records")
        print(f"   - Time span: Last 30 minutes")
        
        return True
    except Exception as e:
        print(f"❌ Error creating sample data: {e}")
        return False

def validate_location_point(location):
    """Validate a single location point"""
    required_fields = [
        "timestamp", "latitude", "longitude", "accuracy",
        "inspector", "day", "shift", "area"
    ]
    
    for field in required_fields:
        if field not in location:
            return False, f"Missing field: {field}"
    
    # Validate data types
    if not isinstance(location["latitude"], (int, float)):
        return False, "latitude must be a number"
    if not isinstance(location["longitude"], (int, float)):
        return False, "longitude must be a number"
    if not isinstance(location["accuracy"], (int, float)):
        return False, "accuracy must be a number"
    
    # Validate ranges
    if not (-90 <= location["latitude"] <= 90):
        return False, "latitude must be between -90 and 90"
    if not (-180 <= location["longitude"] <= 180):
        return False, "longitude must be between -180 and 180"
    if location["accuracy"] < 0:
        return False, "accuracy must be non-negative"
    
    return True, "Valid"

def test_sample_data():
    """Test the sample location data"""
    print("\n🧪 Testing Sample Location Data...")
    print("=" * 60)
    
    try:
        with open("location-tracking-sample.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        locations = data["locationTracking"]
        print(f"📊 Testing {len(locations)} location records...")
        
        invalid_count = 0
        for i, location in enumerate(locations):
            is_valid, message = validate_location_point(location)
            if not is_valid:
                print(f"❌ Location {i+1}: {message}")
                invalid_count += 1
        
        if invalid_count == 0:
            print(f"✅ All {len(locations)} location records are valid!")
            
            # Print summary
            inspectors = set(loc["inspector"] for loc in locations)
            areas = set(loc["area"] for loc in locations)
            
            print(f"\n📈 Summary:")
            print(f"   - Total locations: {len(locations)}")
            print(f"   - Unique inspectors: {len(inspectors)}")
            print(f"   - Unique areas: {len(areas)}")
            print(f"   - Inspectors: {', '.join(inspectors)}")
            
            return True
        else:
            print(f"❌ Found {invalid_count} invalid location records")
            return False
            
    except FileNotFoundError:
        print("❌ Sample data file not found. Run create_sample_location_data() first.")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🌍 Location Tracking Data Structure Test Suite")
    print("=" * 60)
    print()
    
    # Run tests
    test1 = test_location_tracking_structure()
    test2 = create_sample_location_data()
    test3 = test_sample_data()
    
    print("\n" + "=" * 60)
    if test1 and test2 and test3:
        print("✅ ALL TESTS PASSED!")
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED")
        sys.exit(1)
