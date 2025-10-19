#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Priority Logic for Very High Priority Shops from 15th of Month
Tests the new priority calculation logic that assigns "very high" priority
to shops from the 15th of each month onwards.
"""

import json
import sys
import io
from datetime import datetime, timedelta

# Ensure UTF-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def calculate_shop_priority_python(last_inspection_date, current_date, has_special_activity=False):
    """
    Python implementation of the JavaScript calculateShopPriority function
    for testing purposes.
    
    Args:
        last_inspection_date: Date string of last inspection (YYYY-MM-DD) or None
        current_date: Current date string (YYYY-MM-DD)
        has_special_activity: Boolean indicating if shop has special activity requiring registration
        
    Returns:
        dict with 'level', 'score', and 'reason'
    """
    score = 0
    reasons = []
    
    if last_inspection_date is None:
        score += 100
        reasons.append('لم يتم تفتيشه من قبل')
    else:
        target_date = datetime.strptime(current_date, '%Y-%m-%d')
        last_date = datetime.strptime(last_inspection_date, '%Y-%m-%d')
        days_since = (target_date - last_date).days
        
        if days_since > 30:
            score += 80
            reasons.append(f'آخر تفتيش قبل {days_since} يوم')
        elif days_since > 21:
            score += 60
            reasons.append(f'آخر تفتيش قبل {days_since} يوم')
        elif days_since > 14:
            score += 40
            reasons.append(f'آخر تفتيش قبل {days_since} يوم')
        else:
            score += 20
            reasons.append(f'آخر تفتيش قبل {days_since} يوم')
    
    if has_special_activity:
        score += 30
        reasons.append('نشاط يتطلب التسجيل')
    
    # Check if we're in the second half of the month (from 15th onwards)
    target_date = datetime.strptime(current_date, '%Y-%m-%d')
    day_of_month = target_date.day
    
    if day_of_month >= 15:
        # From the 15th onwards, boost high priority shops to "very high"
        if score >= 80:
            score += 50  # Boost very high priority shops even more
            reasons.append('أولوية النصف الثاني من الشهر')
        elif score >= 50:
            score += 20  # Moderate boost for medium priority
    
    # Determine priority level
    level = 'low'
    if score >= 130:
        level = 'very-high'  # Very high priority (from 15th onwards)
    elif score >= 80:
        level = 'high'
    elif score >= 50:
        level = 'medium'
    
    return {
        'level': level,
        'score': score,
        'reason': ' - '.join(reasons)
    }


def test_priority_before_15th():
    """Test priority calculation before the 15th of the month"""
    print("\n=== Testing Priority Before 15th ===")
    
    # Test 1: Never inspected shop on 10th of month
    result = calculate_shop_priority_python(None, '2025-10-10', False)
    assert result['level'] == 'high', f"Expected 'high', got '{result['level']}'"
    assert result['score'] == 100, f"Expected score 100, got {result['score']}"
    print(f"✅ Test 1 Passed: Never inspected on 10th = {result['level']} (score: {result['score']})")
    
    # Test 2: Shop inspected 35 days ago on 10th of month
    last_date = (datetime.strptime('2025-10-10', '%Y-%m-%d') - timedelta(days=35)).strftime('%Y-%m-%d')
    result = calculate_shop_priority_python(last_date, '2025-10-10', False)
    assert result['level'] == 'high', f"Expected 'high', got '{result['level']}'"
    assert result['score'] == 80, f"Expected score 80, got {result['score']}"
    print(f"✅ Test 2 Passed: 35 days ago on 10th = {result['level']} (score: {result['score']})")
    
    # Test 3: Shop inspected 25 days ago on 10th of month
    last_date = (datetime.strptime('2025-10-10', '%Y-%m-%d') - timedelta(days=25)).strftime('%Y-%m-%d')
    result = calculate_shop_priority_python(last_date, '2025-10-10', False)
    assert result['level'] == 'medium', f"Expected 'medium', got '{result['level']}'"
    assert result['score'] == 60, f"Expected score 60, got {result['score']}"
    print(f"✅ Test 3 Passed: 25 days ago on 10th = {result['level']} (score: {result['score']})")


def test_priority_after_15th():
    """Test priority calculation from 15th onwards"""
    print("\n=== Testing Priority From 15th Onwards ===")
    
    # Test 1: Never inspected shop on 15th of month - should be VERY HIGH
    result = calculate_shop_priority_python(None, '2025-10-15', False)
    assert result['level'] == 'very-high', f"Expected 'very-high', got '{result['level']}'"
    assert result['score'] == 150, f"Expected score 150, got {result['score']}"
    assert 'أولوية النصف الثاني من الشهر' in result['reason'], "Expected second half of month reason"
    print(f"✅ Test 1 Passed: Never inspected on 15th = {result['level']} (score: {result['score']})")
    
    # Test 2: Shop inspected 35 days ago on 20th of month - should be VERY HIGH
    last_date = (datetime.strptime('2025-10-20', '%Y-%m-%d') - timedelta(days=35)).strftime('%Y-%m-%d')
    result = calculate_shop_priority_python(last_date, '2025-10-20', False)
    assert result['level'] == 'very-high', f"Expected 'very-high', got '{result['level']}'"
    assert result['score'] == 130, f"Expected score 130, got {result['score']}"
    print(f"✅ Test 2 Passed: 35 days ago on 20th = {result['level']} (score: {result['score']})")
    
    # Test 3: Shop inspected 25 days ago on 25th of month - should be HIGH (boosted from medium)
    last_date = (datetime.strptime('2025-10-25', '%Y-%m-%d') - timedelta(days=25)).strftime('%Y-%m-%d')
    result = calculate_shop_priority_python(last_date, '2025-10-25', False)
    assert result['level'] == 'high', f"Expected 'high', got '{result['level']}'"
    assert result['score'] == 80, f"Expected score 80, got {result['score']}"
    print(f"✅ Test 3 Passed: 25 days ago on 25th = {result['level']} (score: {result['score']})")
    
    # Test 4: Never inspected with special activity on 28th - should be VERY HIGH
    result = calculate_shop_priority_python(None, '2025-10-28', True)
    assert result['level'] == 'very-high', f"Expected 'very-high', got '{result['level']}'"
    assert result['score'] == 180, f"Expected score 180, got {result['score']}"
    print(f"✅ Test 4 Passed: Never inspected + special activity on 28th = {result['level']} (score: {result['score']})")


def test_priority_edge_cases():
    """Test edge cases around the 15th boundary"""
    print("\n=== Testing Edge Cases ===")
    
    # Test 1: On 14th (last day before boost)
    result = calculate_shop_priority_python(None, '2025-10-14', False)
    assert result['level'] == 'high', f"Expected 'high', got '{result['level']}'"
    assert result['score'] == 100, f"Expected score 100, got {result['score']}"
    assert 'أولوية النصف الثاني من الشهر' not in result['reason'], "Should not have second half boost on 14th"
    print(f"✅ Test 1 Passed: 14th of month (no boost) = {result['level']} (score: {result['score']})")
    
    # Test 2: On 15th (first day with boost)
    result = calculate_shop_priority_python(None, '2025-10-15', False)
    assert result['level'] == 'very-high', f"Expected 'very-high', got '{result['level']}'"
    assert result['score'] == 150, f"Expected score 150, got {result['score']}"
    assert 'أولوية النصف الثاني من الشهر' in result['reason'], "Should have second half boost on 15th"
    print(f"✅ Test 2 Passed: 15th of month (with boost) = {result['level']} (score: {result['score']})")
    
    # Test 3: End of month (31st)
    result = calculate_shop_priority_python(None, '2025-10-31', False)
    assert result['level'] == 'very-high', f"Expected 'very-high', got '{result['level']}'"
    assert result['score'] == 150, f"Expected score 150, got {result['score']}"
    print(f"✅ Test 3 Passed: 31st of month (with boost) = {result['level']} (score: {result['score']})")


def test_month_rotation():
    """Test that priority resets at the beginning of next month"""
    print("\n=== Testing Month Rotation ===")
    
    # Test 1: Last day of month (31st)
    result = calculate_shop_priority_python(None, '2025-10-31', False)
    assert result['level'] == 'very-high', f"Expected 'very-high', got '{result['level']}'"
    print(f"✅ Test 1 Passed: Last day of month = {result['level']} (score: {result['score']})")
    
    # Test 2: First day of next month (1st) - should reset to normal priority
    result = calculate_shop_priority_python(None, '2025-11-01', False)
    assert result['level'] == 'high', f"Expected 'high', got '{result['level']}'"
    assert result['score'] == 100, f"Expected score 100, got {result['score']}"
    assert 'أولوية النصف الثاني من الشهر' not in result['reason'], "Should not have second half boost on 1st of new month"
    print(f"✅ Test 2 Passed: First day of new month = {result['level']} (score: {result['score']}) - rotation complete")


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("Testing Very High Priority Logic from 15th of Month")
    print("=" * 60)
    
    try:
        test_priority_before_15th()
        test_priority_after_15th()
        test_priority_edge_cases()
        test_month_rotation()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nSummary:")
        print("- Priority system works correctly before 15th")
        print("- Very high priority is assigned from 15th onwards")
        print("- Edge cases around 15th are handled correctly")
        print("- Month rotation works correctly (resets on 1st)")
        return True
        
    except AssertionError as e:
        print("\n" + "=" * 60)
        print(f"❌ TEST FAILED: {e}")
        print("=" * 60)
        return False
    except Exception as e:
        print("\n" + "=" * 60)
        print(f"❌ ERROR: {e}")
        print("=" * 60)
        return False


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
