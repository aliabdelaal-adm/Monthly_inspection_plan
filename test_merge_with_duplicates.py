#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test merge validation with duplicates.
This script tests that the merge function correctly rejects plans with duplicate shops.
"""

import json
import sys
from merge_plan_data import validate_shop_duplicates, merge_inspection_data

def test_merge_validation():
    """Test that merge creates duplicates and validation catches them."""
    print("=" * 80)
    print("🧪 Testing Merge Validation with Duplicate Detection")
    print("=" * 80)
    print()
    
    # Main data with one inspector
    main_data = {
        "inspectionData": [
            {
                "inspector": "د. آمنه",
                "day": "2025-11-01",
                "shift": "صباحية",
                "area": "المنطقة أ",
                "shops": ["محل 1", "محل 2"]
            }
        ]
    }
    
    # Source data with another inspector on same day with overlapping shop
    source_data = {
        "inspectionData": [
            {
                "inspector": "د. أحمد",
                "day": "2025-11-01",
                "shift": "مسائية",
                "area": "المنطقة ب",
                "shops": ["محل 2", "محل 3"]  # محل 2 is duplicate!
            }
        ]
    }
    
    print("📋 Main data:")
    print(f"   Inspector: {main_data['inspectionData'][0]['inspector']}")
    print(f"   Day: {main_data['inspectionData'][0]['day']}")
    print(f"   Shops: {main_data['inspectionData'][0]['shops']}")
    print()
    
    print("📋 Source data to merge:")
    print(f"   Inspector: {source_data['inspectionData'][0]['inspector']}")
    print(f"   Day: {source_data['inspectionData'][0]['day']}")
    print(f"   Shops: {source_data['inspectionData'][0]['shops']}")
    print()
    
    # Merge the data
    print("🔄 Merging data...")
    merged_inspections, _ = merge_inspection_data(main_data, source_data)
    print(f"✅ Merged: {len(merged_inspections)} total entries")
    print()
    
    # Validate merged data
    print("🔍 Validating for duplicates...")
    is_valid, duplicates = validate_shop_duplicates(merged_inspections)
    
    if not is_valid:
        print("❌ Validation FAILED - Duplicates detected (as expected):")
        for dup in duplicates:
            print(f"   Day: {dup['day']}")
            print(f"   Shop: {dup['shop']}")
            print(f"   Inspectors: {', '.join(dup['inspectors'])}")
        print()
        print("✅ TEST PASSED: Merge validation correctly detected duplicates")
        return True
    else:
        print("❌ TEST FAILED: Validation did not detect duplicates!")
        return False

if __name__ == "__main__":
    success = test_merge_validation()
    sys.exit(0 if success else 1)
