# نظام التقرير الأسبوعي - Weekly Report System

## نظرة عامة | Overview

نظام شامل لإنشاء قوالب التقارير الأسبوعية الاحترافية لإدارة التفتيش البيطري. يقوم النظام بإنشاء قوالب PowerPoint ذكية ومنظمة حسب المعايير المهنية.

A comprehensive system for creating professional weekly report templates for veterinary inspection management. The system generates smart and organized PowerPoint templates according to professional standards.

## المميزات الرئيسية | Key Features

### 🎯 المحاور الرئيسية | Main Sections
1. **التفتيش والرقابة البيطرية** - Veterinary Inspection and Monitoring
2. **الشكاوى والبلاغات** - Complaints and Reports  
3. **التوعية والتثقيف** - Awareness and Education
4. **خدمات الضبط والسيطرة** - Control and Monitoring Services
5. **الزيارات والمتابعة** - Visits and Follow-up
6. **العقود والمتابعة** - Contracts and Follow-up
7. **التطوير والجودة** - Development and Quality

### 📊 المميزات التقنية | Technical Features
- ✅ حساب التواريخ تلقائياً (الاثنين إلى الأحد)
- ✅ أماكن مخصصة للصور والرسوم البيانية
- ✅ مناطق للتحاليل الإحصائية
- ✅ تصميم احترافي مع الألوان المؤسسية
- ✅ دعم النص العربي (RTL) والإنجليزي
- ✅ واجهة تفاعلية وسطر أوامر

## المتطلبات | Requirements

### البرمجيات المطلوبة | Required Software
```bash
# Python 3.7 أو أحدث
python3 --version

# تثبيت المكتبة المطلوبة
pip install python-pptx
```

### الملفات الأساسية | Core Files
- `weekly_report_generator.py` - الملف الأساسي لإنشاء القوالب
- `generate_weekly_report.py` - الواجهة التفاعلية وسطر الأوامر
- `WEEKLY_REPORT_SYSTEM.md` - هذا الملف (التوثيق)

## طرق الاستخدام | Usage Methods

### 1. الوضع التفاعلي | Interactive Mode
```bash
python3 generate_weekly_report.py
```

سيطلب منك النظام إدخال:
- تاريخ البداية (الاثنين)
- رقم الأسبوع (اختياري)

### 2. سطر الأوامر | Command Line
```bash
# إنشاء تقرير بتواريخ محددة
python3 generate_weekly_report.py --start 22/09/2025 --end 28/09/2025

# مع تحديد رقم الأسبوع
python3 generate_weekly_report.py --start 22/09/2025 --end 28/09/2025 --week 1
```

### 3. إنشاء قوالب متعددة | Multiple Templates
```bash
# تشغيل النظام الأساسي لإنشاء 3 قوالب كأمثلة
python3 weekly_report_generator.py
```

## هيكل التقرير | Report Structure

### شريحة العنوان | Title Slide
- رقم التقرير الأسبوعي
- فترة التقرير (من الاثنين إلى الأحد)
- تاريخ التسليم (الثلاثاء)
- شعار الجهة

### شرائح الأقسام (7 شرائح) | Section Slides (7 slides)
كل شريحة تحتوي على:
- العنوان الرئيسي والفرعي
- النقاط الأساسية للقسم
- منطقة للصور والرسوم البيانية
- منطقة للتحاليل الإحصائية

### شريحة الملخص | Summary Slide
- النقاط الرئيسية للأسبوع
- الإحصائيات الإجمالية
- الخلاصة والتوصيات

## تفاصيل الأقسام | Section Details

### 1. التفتيش والرقابة البيطرية
- عدد التفتيشات الميدانية المنجزة
- نسبة انجاز الخطة (%)
- عدد المحلات/المنشآت التي تمت زيارتها
- مخرجات التفتيش (تعديل فوري، إنذارات، مخالفات)
- التحديات الميدانية

### 2. الشكاوى والبلاغات
- عدد الشكاوى والبلاغات المستلمة
- عدد الشكاوى المغلقة في الوقت المحدد
- عدد الشكاوى العالقة وأسبابها

### 3. التوعية والتثقيف
- عدد الفعاليات التوعوية المنفذة
- توعية المحلات (زيارات - برامج)
- حملات مرتبطة بالشكاوى والبلاغات

### 4. خدمات الضبط والسيطرة
- عدد الحيوانات التي تم التعامل معها
- نسبة إغلاق الحالات في الوقت المحدد
- أنواع الحيوانات (قطط، كلاب، حيوانات أخرى)
- مخرجات الضبط (إيواء، تعقيم، تبني...)

### 5. الزيارات والمتابعة
- عدد الزيارات على الملاجئ ودور الإيواء
- الملاحظات أو التحديات خلال الزيارات

### 6. العقود والمتابعة
- متابعة عقود التشغيل (الاجتماعات الأسبوعية ومخرجاتها)
- أي ملاحظات أو تحديثات من المقاولين/المشغلين

### 7. التطوير والجودة
- مقترحات تحسين اللوائح والسياسات
- متابعات الجودة والمخاطر
- أي برامج تدريبية أو خطط تصحيحية مقترحة

## نظام التواريخ | Date System

### قواعد التواريخ | Date Rules
- التقرير يبدأ دائماً يوم **الاثنين**
- التقرير ينتهي دائماً يوم **الأحد**
- مدة التقرير: **7 أيام بالضبط**
- تاريخ التسليم: **الثلاثاء** التالي لنهاية الأسبوع

### أمثلة على التواريخ | Date Examples
```
التقرير الأسبوعي رقم 1:
- من: الاثنين 06/01/2025
- إلى: الأحد 12/01/2025  
- التسليم: الثلاثاء 14/01/2025

التقرير الأسبوعي رقم 2:
- من: الاثنين 13/01/2025
- إلى: الأحد 19/01/2025
- التسليم: الثلاثاء 21/01/2025
```

## التخصيص والتعديل | Customization

### الألوان | Colors
```python
primary_color = RGBColor(35, 54, 160)      # الأزرق الأساسي
secondary_color = RGBColor(41, 128, 185)   # الأزرق الثانوي  
accent_color = RGBColor(231, 76, 60)       # الأحمر للتأكيد
text_color = RGBColor(44, 62, 80)          # لون النص
light_gray = RGBColor(236, 240, 241)       # الرمادي الفاتح
```

### إضافة أقسام جديدة | Adding New Sections
لإضافة قسم جديد، عدل قائمة `report_sections` في `weekly_report_generator.py`:

```python
{
    'title': '8. القسم الجديد',
    'subtitle': 'New Section',
    'items': [
        'النقطة الأولى',
        'النقطة الثانية',
        'النقطة الثالثة'
    ]
}
```

## استكشاف الأخطاء | Troubleshooting

### مشاكل شائعة | Common Issues

#### خطأ في تثبيت python-pptx
```bash
# على Windows
pip install --user python-pptx

# على Linux/Mac
pip3 install python-pptx
```

#### خطأ في تنسيق التاريخ
- استخدم تنسيق `DD/MM/YYYY` (مثال: 22/09/2025)
- أو تنسيق `YYYY-MM-DD` (مثال: 2025-09-22)
- تأكد من أن التاريخ يوم اثنين

#### خطأ في ترميز النص العربي
- تأكد من حفظ الملفات بترميز UTF-8
- استخدم محرر نصوص يدعم UTF-8

## الملفات المُولدة | Generated Files

### أسماء الملفات | File Names
```
التقرير_الأسبوعي_رقم_1_2025.pptx
التقرير_الأسبوعي_رقم_2_2025.pptx
التقرير_الأسبوعي_رقم_1_2025_مخصص.pptx
```

### خصائص الملفات | File Properties
- تنسيق: PowerPoint 2007+ (.pptx)
- نسبة العرض: 16:9
- عدد الشرائح: 9 (عنوان + 7 أقسام + ملخص)
- دعم النص العربي: كامل

## أمثلة عملية | Practical Examples

### مثال 1: إنشاء تقرير أسبوعي عادي
```bash
python3 generate_weekly_report.py --start 22/09/2025 --end 28/09/2025
```

### مثال 2: إنشاء تقرير مع رقم أسبوع محدد
```bash
python3 generate_weekly_report.py --start 06/10/2025 --end 12/10/2025 --week 3
```

### مثال 3: استخدام الوضع التفاعلي
```bash
python3 generate_weekly_report.py
# ثم اتبع التعليمات على الشاشة
```

## التطوير المستقبلي | Future Development

### مميزات مقترحة | Proposed Features
- [ ] دمج البيانات من ملف plan-data.json
- [ ] إنشاء رسوم بيانية تلقائية
- [ ] واجهة ويب لإنشاء التقارير
- [ ] تصدير لصيغ أخرى (PDF, Word)
- [ ] قوالب تقارير شهرية وسنوية

### المساهمة | Contributing
لتحسين النظام أو إضافة مميزات جديدة:
1. إنشاء fork للمشروع
2. إنشاء branch جديد للميزة
3. إجراء التعديلات
4. إرسال pull request

## الدعم والمساعدة | Support

### التواصل | Contact
للاستفسارات أو المساعدة الفنية، يرجى:
- فتح issue في GitHub
- مراجعة هذا الملف للحلول
- التحقق من الأمثلة المتوفرة

### الموارد المفيدة | Useful Resources
- [python-pptx Documentation](https://python-pptx.readthedocs.io/)
- [Python datetime Documentation](https://docs.python.org/3/library/datetime.html)
- [Arabic Text Handling in Python](https://docs.python.org/3/howto/unicode.html)

---

**نظام التقرير الأسبوعي - إصدار 1.0**  
**Weekly Report System - Version 1.0**

تم التطوير بواسطة: علي عبدالعال | Developed by: Ali Abdelaal  
تاريخ الإنشاء: سبتمبر 2024 | Created: September 2024