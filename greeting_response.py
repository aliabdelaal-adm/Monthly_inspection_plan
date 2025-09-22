#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نظام الرد على التحيات والاستفسارات العامة
Greeting Response System for Arabic Monthly Inspection Plan

الرد على التحيات مثل "ازيك" و "إزيك" و "كيف حالك"
Responds to greetings like "ازيك" (How are you?) and provides system status
"""

import json
import sys
import io
from datetime import datetime

# ضمان الطباعة بترميز UTF-8 حتى على ويندوز
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def load_plan_data():
    """تحميل بيانات خطة التفتيش"""
    try:
        with open("plan-data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def get_system_status():
    """الحصول على حالة النظام الحالية"""
    data = load_plan_data()
    if not data:
        return "❌ لا يمكن قراءة بيانات النظام"
    
    # إحصائيات سريعة
    inspectors_count = len(data.get('inspectors', []))
    areas_count = len(data.get('areas', []))
    total_shops = sum(len(shops) for shops in data.get('shopsByArea', {}).values())
    distribution_count = len(data.get('distribution', []))
    
    return f"""✅ النظام يعمل بشكل طبيعي
📋 عدد المفتشين: {inspectors_count}
🏪 إجمالي المحلات: {total_shops}
📍 عدد المناطق: {areas_count}
📅 المهام المجدولة: {distribution_count}"""

def respond_to_greeting(message):
    """الرد على التحيات"""
    message = message.strip().lower()
    
    # التحيات المختلفة
    greetings = [
        "ازيك", "إزيك", "ازايك", "إزايك",
        "كيف حالك", "كيف الحال", "شلونك",
        "أهلا", "مرحبا", "السلام عليكم"
    ]
    
    # فحص إذا كانت الرسالة تحية
    is_greeting = any(greeting in message for greeting in greetings)
    
    if is_greeting:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        response = f"""🌟 أهلاً وسهلاً! 
الحمد لله بخير، شكراً لسؤالك! 💙

⏰ الوقت الحالي: {current_time}

حالة نظام خطة التفتيش الشهرية:
{get_system_status()}

💡 يمكنك استخدام النظام لإدارة خطط التفتيش الشهرية بسهولة.
"""
        return response
    else:
        return f"مرحباً! لم أفهم رسالتك '{message}'. يمكنك قول 'ازيك' أو 'كيف حالك' للتحية."

def main():
    """الدالة الرئيسية"""
    if len(sys.argv) > 1:
        # إذا تم تمرير رسالة كمعامل
        message = " ".join(sys.argv[1:])
        print(respond_to_greeting(message))
    else:
        # تشغيل تفاعلي
        print("🎯 نظام الرد على التحيات - اكتب تحيتك:")
        print("(اكتب 'خروج' للإنهاء)")
        
        while True:
            try:
                user_input = input("\n> ")
                if user_input.lower().strip() in ['خروج', 'exit', 'quit']:
                    print("مع السلامة! 👋")
                    break
                    
                response = respond_to_greeting(user_input)
                print(f"\n{response}")
                
            except KeyboardInterrupt:
                print("\n\nمع السلامة! 👋")
                break
            except EOFError:
                print("\n\nمع السلامة! 👋")
                break

if __name__ == "__main__":
    main()