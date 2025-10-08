#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Delete all inspections for October 15th, 2025
==============================================

This script removes all inspection entries for October 15th (2025-10-15)
from all plan-data files while preserving all other data.
"""

import json
import sys
import io
from datetime import datetime
import shutil

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Files to process
FILES_TO_PROCESS = [
    'plan-data.json',
    'plan-data12.json',
    'plan-data13.json',
    'plan-data15.json'
]

TARGET_DATE = '2025-10-15'

def backup_file(filename):
    """Create a backup of the file before modification."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"{filename}.backup_{timestamp}_before_oct15_deletion"
    shutil.copy2(filename, backup_name)
    print(f"✅ Backup created: {backup_name}")
    return backup_name

def delete_october_15_inspections(filename):
    """Delete all inspections for October 15th from the specified file."""
    print(f"\n{'='*70}")
    print(f"Processing: {filename}")
    print('='*70)
    
    # Read the file
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error in {filename}: {e}")
        return False
    
    if 'inspectionData' not in data:
        print(f"⚠️  No 'inspectionData' field found in {filename}")
        return False
    
    # Count inspections before deletion
    original_count = len(data['inspectionData'])
    print(f"📊 Original inspection count: {original_count}")
    
    # Find inspections for October 15th
    oct15_inspections = [
        entry for entry in data['inspectionData'] 
        if entry.get('day') == TARGET_DATE
    ]
    
    if not oct15_inspections:
        print(f"ℹ️  No inspections found for {TARGET_DATE}")
        return True
    
    print(f"\n🔍 Found {len(oct15_inspections)} inspection(s) for {TARGET_DATE}:")
    for i, entry in enumerate(oct15_inspections, 1):
        inspector = entry.get('inspector', 'Unknown')
        shift = entry.get('shift', 'Unknown')
        area = entry.get('area', 'Unknown')
        shop_count = len(entry.get('shops', []))
        print(f"  {i}. المفتش: {inspector}")
        print(f"     الفترة: {shift}")
        print(f"     المنطقة: {area}")
        print(f"     عدد المحلات: {shop_count}")
        print()
    
    # Create backup
    backup_name = backup_file(filename)
    
    # Filter out October 15th inspections
    data['inspectionData'] = [
        entry for entry in data['inspectionData']
        if entry.get('day') != TARGET_DATE
    ]
    
    # Update lastUpdate timestamp
    data['lastUpdate'] = datetime.now().isoformat()
    
    # Count inspections after deletion
    new_count = len(data['inspectionData'])
    deleted_count = original_count - new_count
    
    # Save the modified data
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Successfully deleted {deleted_count} inspection(s)")
    print(f"📊 New inspection count: {new_count}")
    print(f"✅ File updated: {filename}")
    
    return True

def main():
    """Main function to process all files."""
    print("="*70)
    print("حذف جميع التفتيشات ليوم 15 أكتوبر")
    print("Delete All Inspections for October 15th")
    print("="*70)
    print(f"Target date: {TARGET_DATE}")
    print(f"Files to process: {len(FILES_TO_PROCESS)}")
    print()
    
    success_count = 0
    total_files = len(FILES_TO_PROCESS)
    
    for filename in FILES_TO_PROCESS:
        try:
            if delete_october_15_inspections(filename):
                success_count += 1
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*70}")
    print("SUMMARY / الملخص")
    print('='*70)
    print(f"✅ Successfully processed: {success_count}/{total_files} files")
    print(f"✅ تمت معالجة: {success_count}/{total_files} ملف")
    
    if success_count == total_files:
        print("\n🎉 All files processed successfully!")
        print("🎉 تمت معالجة جميع الملفات بنجاح!")
        return 0
    else:
        print(f"\n⚠️  Warning: {total_files - success_count} file(s) had issues")
        print(f"⚠️  تحذير: {total_files - success_count} ملف به مشاكل")
        return 1

if __name__ == "__main__":
    sys.exit(main())
