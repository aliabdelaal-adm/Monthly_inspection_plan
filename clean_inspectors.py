#!/usr/bin/env python3
"""
Clean inspectors list in plan-data.json by removing fake and duplicate inspectors.
Keep only the 9 real inspectors as specified.
"""

import json
import sys
import io
from datetime import datetime
import shutil

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def backup_file(filename):
    """Create a backup of the file."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"{filename}.backup_{timestamp}"
    shutil.copy2(filename, backup_name)
    print(f"✅ Backup created: {backup_name}")
    return backup_name

def clean_inspectors():
    """Remove fake and duplicate inspectors, keeping only the 9 real ones."""
    
    filename = 'plan-data.json'
    
    # Create backup
    print("📦 Creating backup...")
    backup_file(filename)
    
    # Load data
    print(f"\n📖 Loading {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # The 9 real inspectors as per the requirement
    real_inspectors = [
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
    
    print(f"\n📊 Before cleanup:")
    print(f"   Total inspectors: {len(data['inspectors'])}")
    
    # Find the inspector records to keep (keep first occurrence of each real inspector)
    inspectors_to_keep = []
    seen_names = set()
    removed_count = 0
    
    print(f"\n🔍 Processing inspectors...")
    for inspector in data['inspectors']:
        name = inspector['name']
        # Normalize the name (handle both علي and على variants)
        normalized_name = name.replace('على', 'علي')
        
        if (normalized_name in real_inspectors or name in real_inspectors) and name not in seen_names:
            inspectors_to_keep.append(inspector)
            seen_names.add(name)
            print(f"   ✅ Keep: {name}")
        else:
            if name in seen_names:
                print(f"   ❌ Remove duplicate: {name} (ID: {inspector['id']})")
            else:
                print(f"   ❌ Remove fake: {name} (ID: {inspector['id']})")
            removed_count += 1
    
    # Update data
    data['inspectors'] = inspectors_to_keep
    
    # Update lastUpdate timestamp
    data['lastUpdate'] = datetime.now().isoformat()
    
    # Save cleaned data
    print(f"\n💾 Saving cleaned data...")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Cleanup complete!")
    print(f"\n📊 After cleanup:")
    print(f"   Total inspectors: {len(data['inspectors'])}")
    print(f"   Removed: {removed_count} fake/duplicate inspectors")
    
    # Verify all inspection data still references valid inspectors
    print(f"\n🔍 Verifying inspection data...")
    inspectors_in_use = set()
    for entry in data['inspectionData']:
        inspectors_in_use.add(entry['inspector'])
    
    all_valid = all(name in seen_names for name in inspectors_in_use)
    
    if all_valid:
        print(f"   ✅ All {len(inspectors_in_use)} inspectors in inspection data are valid")
    else:
        print(f"   ⚠️  Warning: Some inspectors in inspection data not found in inspectors list")
        invalid = [name for name in inspectors_in_use if name not in seen_names]
        for name in invalid:
            print(f"      - {name}")
    
    return True

if __name__ == '__main__':
    try:
        success = clean_inspectors()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Error: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
