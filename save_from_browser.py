#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Save Plan Data from Browser Script
==================================

This script reads the latest plan data from browser's localStorage
and saves it directly to plan-data.json file.

Usage:
1. Run this script: python save_from_browser.py
2. The script will prompt you to paste the JSON data
3. It will save the data to plan-data.json

Alternative automated usage:
- The browser will create this data in localStorage
- This script can read and save it automatically
"""

import json
import sys
import os
from datetime import datetime

def save_plan_data_from_input():
    """Save plan data by prompting user to paste JSON"""
    print("=== Save Plan Data to plan-data.json ===")
    print("Please paste the JSON data from the browser (Ctrl+V, then press Enter twice):")
    print()
    
    lines = []
    empty_lines = 0
    
    try:
        while True:
            line = input()
            if line.strip() == "":
                empty_lines += 1
                if empty_lines >= 2:  # Two empty lines means done
                    break
            else:
                empty_lines = 0
                lines.append(line)
        
        json_str = '\n'.join(lines)
        
        if not json_str.strip():
            print("❌ No data provided!")
            return False
            
        # Parse JSON to validate
        data = json.loads(json_str)
        
        # Add timestamp if not present
        if 'lastUpdate' not in data:
            data['lastUpdate'] = datetime.now().isoformat()
        
        # Save to plan-data.json
        with open('plan-data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Successfully saved data to plan-data.json!")
        print(f"📊 Saved {len(data.get('inspectionData', []))} inspection records")
        print(f"👥 Saved {len(data.get('inspectors', []))} inspectors")
        print(f"🏘️ Saved {len(data.get('areas', []))} areas")
        print(f"🏪 Saved {len(data.get('shops', []))} shops")
        print(f"🕒 Last update: {data.get('lastUpdate', 'Not set')}")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON format: {e}")
        return False
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False

def save_plan_data_from_file(input_file='plan-data-new.json'):
    """Save plan data from a file (alternative method)"""
    try:
        if not os.path.exists(input_file):
            print(f"❌ Input file {input_file} not found!")
            return False
            
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Add timestamp if not present
        if 'lastUpdate' not in data:
            data['lastUpdate'] = datetime.now().isoformat()
        
        # Save to plan-data.json
        with open('plan-data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Successfully copied {input_file} to plan-data.json!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == '__main__':
    print("Plan Data Save Helper")
    print("====================")
    
    if len(sys.argv) > 1:
        # File mode
        input_file = sys.argv[1]
        save_plan_data_from_file(input_file)
    else:
        # Interactive mode
        save_plan_data_from_input()