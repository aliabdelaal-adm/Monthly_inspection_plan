#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate plan-data.json for duplicate shop assignments.
This script checks if any shop is assigned to multiple inspectors on the same day.
"""

import json
import sys
import io
from datetime import datetime

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def validate_shop_duplicates(inspection_data):
    """Validate that no shop is assigned to multiple inspectors on the same day.
    
    Returns:
        tuple: (is_valid, duplicate_info_list)
        - is_valid: True if no duplicates found, False otherwise
        - duplicate_info_list: List of dictionaries with duplicate information
    """
    # Track shop assignments by day: {day: {shop: [inspector1, inspector2, ...]}}
    day_shop_inspectors = {}
    duplicates = []
    
    for entry in inspection_data:
        day = entry.get('day')
        inspector = entry.get('inspector')
        shops = entry.get('shops', [])
        
        if not day or not inspector or not shops:
            continue
            
        if day not in day_shop_inspectors:
            day_shop_inspectors[day] = {}
        
        for shop in shops:
            if shop not in day_shop_inspectors[day]:
                day_shop_inspectors[day][shop] = []
            day_shop_inspectors[day][shop].append(inspector)
    
    # Find duplicates
    for day, shops_dict in day_shop_inspectors.items():
        for shop, inspectors in shops_dict.items():
            if len(inspectors) > 1:
                duplicates.append({
                    'day': day,
                    'shop': shop,
                    'inspectors': inspectors
                })
    
    is_valid = len(duplicates) == 0
    return is_valid, duplicates

def main():
    print("=" * 80)
    print("🔍 Validation Tool for Inspection Plan Data")
    print("=" * 80)
    print()
    
    # Load plan-data.json
    try:
        with open('plan-data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("✅ Successfully loaded plan-data.json")
    except Exception as e:
        print(f"❌ Error loading plan-data.json: {e}")
        return False
    
    inspection_data = data.get('inspectionData', [])
    print(f"📊 Total inspection entries: {len(inspection_data)}")
    print()
    
    # Validate for duplicates
    print("🔍 Checking for duplicate shop assignments...")
    is_valid, duplicates = validate_shop_duplicates(inspection_data)
    
    if is_valid:
        print()
        print("✅ ممتاز! لا يوجد تكرارات")
        print("✅ Excellent! No duplicate shop assignments found")
        print("✅ All inspectors have unique shops assigned on each day")
        return True
    else:
        print()
        print("❌" + "=" * 78 + "❌")
        print("❌ خطأ: تم اكتشاف تكرار محلات لعدة مفتشين في نفس اليوم!")
        print("❌ Error: Duplicate shop assignments detected!")
        print("❌" + "=" * 78 + "❌")
        print()
        print(f"🔔 عدد التكرارات / Number of duplicates: {len(duplicates)}")
        print()
        print("📋 تفاصيل التكرارات / Duplicate Details:")
        print("=" * 80)
        
        for i, dup in enumerate(duplicates, 1):
            print(f"\n{i}. 📅 التاريخ / Date: {dup['day']}")
            print(f"   🏪 المحل / Shop: {dup['shop']}")
            print(f"   👥 المفتشين / Inspectors ({len(dup['inspectors'])}):")
            for inspector in dup['inspectors']:
                print(f"      - {inspector}")
        
        print()
        print("=" * 80)
        print("⚠️  توصيات / Recommendations:")
        print("   1. يرجى مراجعة الخطة وتعديل توزيع المحلات")
        print("   1. Please review the plan and modify shop assignments")
        print("   2. تأكد من أن كل محل مخصص لمفتش واحد فقط في اليوم الواحد")
        print("   2. Ensure each shop is assigned to only one inspector per day")
        print("   3. يمكن تخصيص نفس المحل لمفتشين مختلفين في أيام مختلفة")
        print("   3. The same shop can be assigned to different inspectors on different days")
        print("=" * 80)
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
