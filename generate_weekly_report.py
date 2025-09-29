#!/usr/bin/env python3
"""
مولد التقرير الأسبوعي التفاعلي - Interactive Weekly Report Generator
يسمح للمستخدم بإدخال التواريخ والبيانات لإنشاء التقرير الأسبوعي

Interactive Weekly Report Generator
Allows users to input dates and data to create weekly reports
"""

import sys
import argparse
from datetime import datetime, timedelta
from weekly_report_generator import WeeklyReportGenerator

def parse_date(date_string):
    """تحويل النص إلى تاريخ"""
    try:
        return datetime.strptime(date_string, "%d/%m/%Y")
    except ValueError:
        try:
            return datetime.strptime(date_string, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"تنسيق التاريخ غير صحيح: {date_string}. استخدم DD/MM/YYYY أو YYYY-MM-DD")

def calculate_week_from_dates(start_date, end_date):
    """حساب رقم الأسبوع من التواريخ المعطاة"""
    if (end_date - start_date).days != 6:
        raise ValueError("يجب أن تكون فترة التقرير 7 أيام بالضبط (من الاثنين إلى الأحد)")
    
    if start_date.weekday() != 0:  # 0 = Monday
        raise ValueError("يجب أن يبدأ التقرير بيوم الاثنين")
    
    if end_date.weekday() != 6:  # 6 = Sunday
        raise ValueError("يجب أن ينتهي التقرير بيوم الأحد")
    
    # حساب رقم الأسبوع في السنة
    year = start_date.year
    jan_1 = datetime(year, 1, 1)
    days_to_monday = (7 - jan_1.weekday()) % 7
    if jan_1.weekday() == 0:
        days_to_monday = 0
    else:
        days_to_monday = 7 - jan_1.weekday()
    
    first_monday = jan_1 + timedelta(days=days_to_monday)
    week_number = ((start_date - first_monday).days // 7) + 1
    
    return week_number

class InteractiveWeeklyReportGenerator(WeeklyReportGenerator):
    """مولد التقرير الأسبوعي التفاعلي"""
    
    def generate_custom_template(self, start_date, end_date, week_number=None):
        """إنشاء قالب مخصص بتواريخ محددة"""
        if week_number is None:
            week_number = calculate_week_from_dates(start_date, end_date)
        
        submission_date = end_date + timedelta(days=2)  # الثلاثاء التالي
        
        print(f"🚀 بدء إنشاء التقرير الأسبوعي المخصص")
        print(f"📅 فترة التقرير: من {start_date.strftime('%d/%m/%Y')} إلى {end_date.strftime('%d/%m/%Y')}")
        print(f"📤 تاريخ التسليم: {submission_date.strftime('%d/%m/%Y')}")
        
        # إضافة الشرائح
        print("📄 إضافة شريحة العنوان...")
        self.add_title_slide(week_number, start_date, end_date, submission_date)
        
        print("📋 إضافة شرائح الأقسام...")
        for i, section in enumerate(self.report_sections, 1):
            print(f"   {i}/7 - {section['title']}")
            self.add_section_slide(section)
        
        print("📊 إضافة شريحة الملخص...")
        self.add_summary_slide()
        
        # حفظ الملف
        filename = f"التقرير_الأسبوعي_رقم_{week_number}_{start_date.year}_مخصص.pptx"
        self.presentation.save(filename)
        
        print(f"✅ تم إنشاء القالب بنجاح: {filename}")
        print(f"📈 إجمالي الشرائح: {len(self.presentation.slides)}")
        
        return filename

def interactive_mode():
    """وضع التفاعل مع المستخدم"""
    print("=== مولد التقرير الأسبوعي التفاعلي ===")
    print("Interactive Weekly Report Generator")
    print()
    
    try:
        print("📝 إدخال تواريخ التقرير:")
        print("   تنسيق التاريخ: DD/MM/YYYY (مثال: 22/09/2025)")
        print()
        
        # إدخال تاريخ البداية
        while True:
            start_input = input("🗓️  تاريخ بداية التقرير (الاثنين): ").strip()
            if not start_input:
                print("❌ يرجى إدخال تاريخ البداية")
                continue
            try:
                start_date = parse_date(start_input)
                if start_date.weekday() != 0:
                    print("❌ يجب أن يكون تاريخ البداية يوم الاثنين")
                    continue
                break
            except ValueError as e:
                print(f"❌ {e}")
        
        # حساب تاريخ النهاية تلقائياً
        end_date = start_date + timedelta(days=6)
        print(f"📅 تاريخ نهاية التقرير (الأحد): {end_date.strftime('%d/%m/%Y')}")
        
        # إدخال رقم الأسبوع (اختياري)
        week_number_input = input(f"🔢 رقم الأسبوع (اتركه فارغ للحساب التلقائي): ").strip()
        week_number = None
        if week_number_input:
            try:
                week_number = int(week_number_input)
            except ValueError:
                print("❌ رقم الأسبوع يجب أن يكون رقماً صحيحاً")
                return False
        
        # إنشاء التقرير
        generator = InteractiveWeeklyReportGenerator()
        filename = generator.generate_custom_template(start_date, end_date, week_number)
        
        print()
        print("🎉 تم إنشاء التقرير بنجاح!")
        print(f"📁 اسم الملف: {filename}")
        
        return True
        
    except KeyboardInterrupt:
        print("\n⚠️ تم إلغاء العملية بواسطة المستخدم")
        return False
    except Exception as e:
        print(f"❌ خطأ في إنشاء التقرير: {e}")
        return False

def main():
    """الدالة الرئيسية"""
    parser = argparse.ArgumentParser(
        description="مولد التقرير الأسبوعي - Weekly Report Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة على الاستخدام:
Examples:

# وضع تفاعلي
python3 generate_weekly_report.py

# إنشاء تقرير بتواريخ محددة
python3 generate_weekly_report.py --start 22/09/2025 --end 28/09/2025

# إنشاء تقرير بتواريخ ورقم أسبوع محدد
python3 generate_weekly_report.py --start 22/09/2025 --end 28/09/2025 --week 1
        """
    )
    
    parser.add_argument(
        '--start', '-s',
        help='تاريخ بداية التقرير (الاثنين) - تنسيق: DD/MM/YYYY'
    )
    
    parser.add_argument(
        '--end', '-e',
        help='تاريخ نهاية التقرير (الأحد) - تنسيق: DD/MM/YYYY'
    )
    
    parser.add_argument(
        '--week', '-w',
        type=int,
        help='رقم الأسبوع (اختياري - سيتم حسابه تلقائياً إذا لم يُحدد)'
    )
    
    args = parser.parse_args()
    
    # إذا لم يتم تحديد المعاملات، استخدم الوضع التفاعلي
    if not args.start and not args.end:
        return interactive_mode()
    
    # التحقق من المعاملات
    if not args.start or not args.end:
        print("❌ يجب تحديد تاريخ البداية والنهاية معاً")
        return False
    
    try:
        start_date = parse_date(args.start)
        end_date = parse_date(args.end)
        
        # إنشاء التقرير
        generator = InteractiveWeeklyReportGenerator()
        filename = generator.generate_custom_template(start_date, end_date, args.week)
        
        print()
        print("🎉 تم إنشاء التقرير بنجاح!")
        print(f"📁 اسم الملف: {filename}")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في إنشاء التقرير: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)