#!/usr/bin/env python3
"""
Verification script to ensure all shops from shops_details.json 
are present in plan-data.json for الوثبة جنوب area.
"""
import json

def load_json(filename):
    """Load JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("=" * 60)
    print("Verification: الوثبة جنوب shops in smart planner")
    print("=" * 60)
    
    # Load both files
    plan_data = load_json('plan-data.json')
    shops_details = load_json('shops_details.json')
    
    area_name = "الوثبة جنوب"
    
    # Get shops from both sources
    shops_in_plan = {s['name'] for s in plan_data['shops'] if s.get('area') == area_name}
    shops_in_details = {name for name, details in shops_details.items() if details.get('area') == area_name}
    
    print(f"\n📊 Statistics:")
    print(f"  • Shops in plan-data.json: {len(shops_in_plan)}")
    print(f"  • Shops in shops_details.json: {len(shops_in_details)}")
    
    # Check for missing shops
    missing_in_plan = shops_in_details - shops_in_plan
    extra_in_plan = shops_in_plan - shops_in_details
    
    if not missing_in_plan and not extra_in_plan:
        print(f"\n✅ SUCCESS! All shops match perfectly!")
        print(f"\n✅ All {len(shops_in_plan)} shops from shops_details.json are in plan-data.json")
        print(f"✅ Smart planner will display all shops when filtering by '{area_name}'")
        return True
    
    if missing_in_plan:
        print(f"\n❌ Missing shops in plan-data.json ({len(missing_in_plan)}):")
        for shop in sorted(missing_in_plan):
            print(f"  - {shop}")
    
    if extra_in_plan:
        print(f"\n⚠️  Extra shops in plan-data.json not in shops_details.json ({len(extra_in_plan)}):")
        for shop in sorted(extra_in_plan):
            print(f"  - {shop}")
    
    return False

if __name__ == '__main__':
    success = main()
    print("\n" + "=" * 60)
    exit(0 if success else 1)
