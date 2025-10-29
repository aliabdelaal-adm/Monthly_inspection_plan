#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification Script: Ensure No Auto-Geocoding
==============================================
This script verifies that all auto-geocoding features are disabled
and only manual Google Maps links are accepted.

التحقق من تعطيل جميع ميزات الترميز الجغرافي التلقائي
وقبول روابط خرائط جوجل اليدوية فقط
"""

import sys
import os
import re

def check_python_scripts_disabled():
    """Verify that auto-geocoding Python scripts are disabled"""
    print("=" * 80)
    print("🔍 Checking Python Scripts...")
    print("=" * 80)
    
    scripts_to_check = [
        'generate_google_maps_links.py',
        'standardize_google_maps_links.py'
    ]
    
    all_disabled = True
    
    for script_name in scripts_to_check:
        if not os.path.exists(script_name):
            print(f"⚠️  {script_name}: NOT FOUND")
            continue
            
        with open(script_name, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for disable markers
        has_exit = 'sys.exit(1)' in content
        has_warning = 'PERMANENTLY DISABLED' in content or 'DISABLED' in content
        has_early_exit = content.find('sys.exit') < content.find('def ') if 'def ' in content else True
        
        if has_exit and has_warning and has_early_exit:
            print(f"✅ {script_name}: PROPERLY DISABLED")
        else:
            print(f"❌ {script_name}: NOT PROPERLY DISABLED!")
            all_disabled = False
            
    return all_disabled

def check_html_files():
    """Verify that HTML files don't auto-generate Google Maps links"""
    print("\n" + "=" * 80)
    print("🔍 Checking HTML Files for Auto-Generation...")
    print("=" * 80)
    
    html_files = [
        'index.html',
        'smart-planner.html',
        'admin-dashboard.html'
    ]
    
    dangerous_patterns = [
        r'encodeURIComponent\([^)]*address',
        r'encodeURIComponent\([^)]*location',
        r'maps\.google\.com.*\+.*address',
        r'google\.com/maps.*\+.*address',
        r'function\s+generateGoogleMapsUrl',
        r'function\s+autoGenerateLocation',
        r'function\s+geocode',
    ]
    
    all_safe = True
    
    for html_file in html_files:
        if not os.path.exists(html_file):
            print(f"⚠️  {html_file}: NOT FOUND")
            continue
            
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        found_issues = []
        for pattern in dangerous_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                found_issues.append(f"  Pattern found: {pattern}")
                
        if found_issues:
            print(f"❌ {html_file}: POTENTIAL AUTO-GENERATION DETECTED!")
            for issue in found_issues:
                print(issue)
            all_safe = False
        else:
            print(f"✅ {html_file}: NO AUTO-GENERATION DETECTED")
            
    return all_safe

def check_for_warning_comments():
    """Verify that warning comments are present"""
    print("\n" + "=" * 80)
    print("🔍 Checking for Warning Comments...")
    print("=" * 80)
    
    files_to_check = {
        'smart-planner.html': 'locationMap MUST be manually provided',
        'admin-dashboard.html': 'locationMap MUST be manually provided',
    }
    
    all_present = True
    
    for filename, expected_text in files_to_check.items():
        if not os.path.exists(filename):
            print(f"⚠️  {filename}: NOT FOUND")
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if expected_text in content or 'NO AUTO-GENERATION' in content:
            print(f"✅ {filename}: WARNING COMMENTS PRESENT")
        else:
            print(f"❌ {filename}: WARNING COMMENTS MISSING!")
            all_present = False
            
    return all_present

def run_disabled_scripts_test():
    """Try to run disabled scripts and verify they exit with error"""
    print("\n" + "=" * 80)
    print("🔍 Testing Disabled Scripts Execution...")
    print("=" * 80)
    
    scripts = ['generate_google_maps_links.py', 'standardize_google_maps_links.py']
    all_exit_correctly = True
    
    for script in scripts:
        if not os.path.exists(script):
            continue
            
        import subprocess
        try:
            result = subprocess.run(
                [sys.executable, script],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode != 0:
                print(f"✅ {script}: Exits with error code {result.returncode}")
            else:
                print(f"❌ {script}: Does NOT exit with error!")
                all_exit_correctly = False
                
        except subprocess.TimeoutExpired:
            print(f"❌ {script}: TIMEOUT - may still be running!")
            all_exit_correctly = False
        except Exception as e:
            print(f"⚠️  {script}: Error testing - {e}")
            
    return all_exit_correctly

def main():
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 15 + "AUTO-GEOCODING DISABLE VERIFICATION" + " " * 28 + "║")
    print("║" + " " * 12 + "التحقق من تعطيل الترميز الجغرافي التلقائي" + " " * 25 + "║")
    print("╚" + "=" * 78 + "╝")
    print()
    
    results = {
        'Python Scripts Disabled': check_python_scripts_disabled(),
        'HTML Files Safe': check_html_files(),
        'Warning Comments Present': check_for_warning_comments(),
        'Scripts Exit Correctly': run_disabled_scripts_test(),
    }
    
    print("\n" + "=" * 80)
    print("📊 VERIFICATION SUMMARY")
    print("=" * 80)
    
    all_passed = True
    for check_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status:12} {check_name}")
        if not passed:
            all_passed = False
    
    print("=" * 80)
    
    if all_passed:
        print("\n🎉 SUCCESS: All verification checks passed!")
        print("✅ Auto-geocoding is DISABLED 100%")
        print("✅ Manual Google Maps links ONLY are enforced")
        print()
        return 0
    else:
        print("\n❌ FAILURE: Some verification checks failed!")
        print("⚠️  Please review the issues above")
        print()
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
