#!/usr/bin/env python3
"""
Link inspectors from PR #269 to all inspection plans.
Ensures all plan-data files only contain the 9 official inspectors.
"""

import json
import sys
import io
from datetime import datetime
import os

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# The 9 official inspectors from PR #269
OFFICIAL_INSPECTORS = [
    'د. آمنه بن صرم',
    'د. آيه سلامة',
    'د. حسينة العامري',
    'د. حصة العلي',
    'د. هاجر الغافري',
    'د. علي عبدالعال',
    'د. محمد إسماعيل',
    'د. محمد سعيد',
    'د. فايز المسالمة'
]

def clean_inspectors_list(data):
    """Remove duplicate/fake inspectors, keep only the 9 official ones."""
    if 'inspectors' not in data:
        return data, 0
    
    # Keep only inspectors whose names are in the official list
    # For duplicates, keep the first occurrence
    seen_names = set()
    cleaned_inspectors = []
    removed_count = 0
    
    for inspector in data['inspectors']:
        name = inspector.get('name', '')
        
        if name in OFFICIAL_INSPECTORS and name not in seen_names:
            cleaned_inspectors.append(inspector)
            seen_names.add(name)
        else:
            removed_count += 1
            if name in seen_names:
                print(f"  ⚠️  Removed duplicate: {name} (ID: {inspector.get('id')})")
            elif name not in OFFICIAL_INSPECTORS:
                print(f"  ⚠️  Removed non-official inspector: {name} (ID: {inspector.get('id')})")
    
    data['inspectors'] = cleaned_inspectors
    return data, removed_count

def verify_inspection_data(data):
    """Verify that all inspection data uses only official inspectors."""
    if 'inspectionData' not in data:
        return True, []
    
    invalid_inspectors = set()
    
    for entry in data['inspectionData']:
        inspector = entry.get('inspector', '')
        if inspector not in OFFICIAL_INSPECTORS:
            invalid_inspectors.add(inspector)
    
    return len(invalid_inspectors) == 0, list(invalid_inspectors)

def process_file(filename):
    """Process a single plan-data file."""
    print(f"\n{'='*60}")
    print(f"Processing: {filename}")
    print('='*60)
    
    # Check if file exists
    if not os.path.exists(filename):
        print(f"  ⚠️  File not found, skipping")
        return False
    
    # Load data
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"  ❌ JSON error: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Error loading file: {e}")
        return False
    
    # Show initial state
    original_inspector_count = len(data.get('inspectors', []))
    print(f"  📊 Original inspectors: {original_inspector_count}")
    print(f"  📊 Inspection entries: {len(data.get('inspectionData', []))}")
    
    # Verify inspection data integrity
    is_valid, invalid = verify_inspection_data(data)
    if not is_valid:
        print(f"  ❌ Found {len(invalid)} invalid inspector(s) in inspection data:")
        for inspector in invalid:
            print(f"     - {inspector}")
        return False
    else:
        print(f"  ✅ All inspection data uses official inspectors")
    
    # Clean inspectors list
    data, removed_count = clean_inspectors_list(data)
    
    if removed_count > 0:
        print(f"  🔧 Removed {removed_count} duplicate/invalid inspector(s)")
        print(f"  📊 Final inspectors: {len(data.get('inspectors', []))}")
        
        # Create backup
        backup_file = f"{filename}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  💾 Backup created: {backup_file}")
        
        # Save cleaned data
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  ✅ File updated successfully")
        return True
    else:
        print(f"  ✅ No changes needed - file is already clean")
        return True

def main():
    """Process all plan-data files."""
    print("="*60)
    print("Link Inspectors from PR #269 to All Inspection Plans")
    print("="*60)
    print("\nOfficial inspectors:")
    for i, inspector in enumerate(OFFICIAL_INSPECTORS, 1):
        print(f"  {i}. {inspector}")
    
    # List of files to process
    files = [
        'plan-data.json',
        'plan-data10.json',
        'plan-data11.json',
        'plan-data13.json',
        'plan-data15.json',
        'plan-data65.json',
        'plan-data91.json'
    ]
    
    results = {}
    for filename in files:
        success = process_file(filename)
        results[filename] = success
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    success_count = sum(1 for v in results.values() if v)
    total_count = len(results)
    
    for filename, success in results.items():
        status = "✅" if success else "❌"
        print(f"  {status} {filename}")
    
    print(f"\n  Total: {success_count}/{total_count} files processed successfully")
    
    if success_count == total_count:
        print("\n🎉 All files have been successfully linked to PR #269 inspectors!")
        return True
    else:
        print(f"\n⚠️  {total_count - success_count} file(s) had issues")
        return False

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
