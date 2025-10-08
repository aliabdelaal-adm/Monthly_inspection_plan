#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Periodic Error Checker for Inspection Plan
===========================================

مدقق الأخطاء الدوري لخطة التفتيش
================================

هذا السكريبت يقوم بالفحص الدوري للأخطاء في خطة التفتيش
ويتم تشغيله تلقائياً يومياً في الساعة 1 صباحاً

This script performs periodic error checking for the inspection plan
and runs automatically daily at 1 AM

Features / المميزات:
- التحقق من تكرارات المحلات / Check for shop duplicates
- إنشاء سجلات مفصلة / Generate detailed logs
- إرسال تنبيهات عند وجود أخطاء / Send alerts when errors are found
- جدولة يومية تلقائية / Automatic daily scheduling
"""

import os
import sys
import json
import logging
from datetime import datetime
from pathlib import Path
import io

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# =============================================================================
# Configuration / الإعدادات
# =============================================================================

# Log directory / مجلد السجلات
LOG_DIR = Path("logs/error_checker")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Log file with date / ملف السجل مع التاريخ
LOG_FILE = LOG_DIR / f"error_check_{datetime.now().strftime('%Y%m%d')}.log"

# Setup logging / إعداد نظام السجلات
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# =============================================================================
# Validation Functions / دوال التحقق
# =============================================================================

def validate_shop_duplicates(inspection_data):
    """
    Validate that no shop is assigned to multiple inspectors on the same day.
    
    التحقق من عدم تعيين نفس المحل لعدة مفتشين في نفس اليوم
    
    Only applies validation to dates from October 7, 2024 onwards.
    يطبق التحقق فقط على التواريخ من 7 أكتوبر 2024 فصاعداً
    
    Returns:
        tuple: (is_valid, duplicate_info_list)
    """
    day_shop_inspectors = {}
    duplicates = []
    
    # Date cutoff: Only apply validation from October 7, 2024 onwards
    VALIDATION_START_DATE = datetime(2024, 10, 7)
    
    for entry in inspection_data:
        day = entry.get('day')
        inspector = entry.get('inspector')
        shops = entry.get('shops', [])
        
        if not day or not inspector or not shops:
            continue
        
        # Skip validation for dates before October 7, 2024
        try:
            entry_date = datetime.strptime(day, '%Y-%m-%d')
            if entry_date < VALIDATION_START_DATE:
                continue
        except ValueError:
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

def validate_data_completeness(inspection_data):
    """
    Check if all required fields are present in the data.
    
    التحقق من وجود جميع الحقول المطلوبة في البيانات
    
    Returns:
        tuple: (is_valid, missing_fields_list)
    """
    missing_fields = []
    
    for i, entry in enumerate(inspection_data):
        issues = []
        
        if not entry.get('day'):
            issues.append('missing day')
        if not entry.get('inspector'):
            issues.append('missing inspector')
        if not entry.get('shops') or len(entry.get('shops', [])) == 0:
            issues.append('missing or empty shops')
        
        if issues:
            missing_fields.append({
                'entry_index': i,
                'issues': issues,
                'entry': entry
            })
    
    is_valid = len(missing_fields) == 0
    return is_valid, missing_fields

# =============================================================================
# Main Error Checking Function / الدالة الرئيسية للفحص
# =============================================================================

def run_error_check():
    """
    Run comprehensive error checking on the inspection plan.
    
    تشغيل فحص شامل للأخطاء في خطة التفتيش
    
    Returns:
        bool: True if all checks passed, False otherwise
    """
    logger.info("=" * 80)
    logger.info("🔍 بدء الفحص الدوري للأخطاء / Starting Periodic Error Check")
    logger.info(f"⏰ التاريخ والوقت / Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 80)
    
    all_checks_passed = True
    
    # Check if plan-data.json exists
    plan_file = Path("plan-data.json")
    if not plan_file.exists():
        logger.error("❌ خطأ: ملف plan-data.json غير موجود")
        logger.error("❌ Error: plan-data.json file not found")
        return False
    
    # Load plan data
    try:
        with open(plan_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logger.info("✅ تم تحميل plan-data.json بنجاح")
        logger.info("✅ Successfully loaded plan-data.json")
    except Exception as e:
        logger.error(f"❌ خطأ في تحميل plan-data.json: {str(e)}")
        logger.error(f"❌ Error loading plan-data.json: {str(e)}")
        return False
    
    inspection_data = data.get('inspectionData', [])
    logger.info(f"📊 عدد السجلات / Total entries: {len(inspection_data)}")
    logger.info("")
    
    # Check 1: Data Completeness
    logger.info("🔍 الفحص 1: اكتمال البيانات / Check 1: Data Completeness")
    logger.info("-" * 80)
    is_complete, missing_fields = validate_data_completeness(inspection_data)
    
    if is_complete:
        logger.info("✅ جميع البيانات كاملة / All data is complete")
    else:
        logger.error(f"❌ وجدت {len(missing_fields)} سجلات بها بيانات ناقصة")
        logger.error(f"❌ Found {len(missing_fields)} entries with missing data")
        for issue in missing_fields[:5]:  # Show first 5 only
            logger.error(f"   - Entry {issue['entry_index']}: {', '.join(issue['issues'])}")
        if len(missing_fields) > 5:
            logger.error(f"   ... و {len(missing_fields) - 5} سجلات أخرى")
            logger.error(f"   ... and {len(missing_fields) - 5} more entries")
        all_checks_passed = False
    
    logger.info("")
    
    # Check 2: Duplicate Shop Assignments
    logger.info("🔍 الفحص 2: تكرار المحلات / Check 2: Duplicate Shop Assignments")
    logger.info("-" * 80)
    is_valid, duplicates = validate_shop_duplicates(inspection_data)
    
    if is_valid:
        logger.info("✅ لا يوجد تكرارات في المحلات")
        logger.info("✅ No duplicate shop assignments found")
    else:
        logger.error(f"❌ وجدت {len(duplicates)} حالات تكرار")
        logger.error(f"❌ Found {len(duplicates)} duplicate cases")
        logger.error("")
        logger.error("📋 تفاصيل التكرارات / Duplicate Details:")
        
        for i, dup in enumerate(duplicates[:10], 1):  # Show first 10 only
            logger.error(f"\n{i}. 📅 التاريخ / Date: {dup['day']}")
            logger.error(f"   🏪 المحل / Shop: {dup['shop']}")
            logger.error(f"   👥 المفتشين / Inspectors ({len(dup['inspectors'])}):")
            for inspector in dup['inspectors']:
                logger.error(f"      - {inspector}")
        
        if len(duplicates) > 10:
            logger.error(f"\n... و {len(duplicates) - 10} حالات تكرار أخرى")
            logger.error(f"... and {len(duplicates) - 10} more duplicate cases")
        
        all_checks_passed = False
    
    logger.info("")
    logger.info("=" * 80)
    
    # Summary
    if all_checks_passed:
        logger.info("🎉 ممتاز! جميع الفحوصات نجحت / Excellent! All checks passed")
        logger.info("✅ البيانات صحيحة وجاهزة للاستخدام / Data is valid and ready to use")
    else:
        logger.warning("⚠️  تحذير: وجدت أخطاء تحتاج إلى تصحيح")
        logger.warning("⚠️  Warning: Errors found that need correction")
        logger.warning("📧 يرجى مراجعة السجلات ومعالجة الأخطاء")
        logger.warning("📧 Please review the logs and address the errors")
    
    logger.info("=" * 80)
    logger.info(f"📁 تم حفظ السجل في / Log saved to: {LOG_FILE}")
    logger.info("=" * 80)
    
    return all_checks_passed

# =============================================================================
# Entry Point / نقطة الدخول
# =============================================================================

def main():
    """Main entry point for the periodic error checker."""
    try:
        success = run_error_check()
        sys.exit(0 if success else 1)
    except Exception as e:
        logger.error(f"❌ خطأ غير متوقع: {str(e)}")
        logger.error(f"❌ Unexpected error: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
