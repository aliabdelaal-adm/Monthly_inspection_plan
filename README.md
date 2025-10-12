# 📋 خطة التفتيش الشهرية - Monthly Inspection Plan

## 🌟 نظرة عامة - Overview

**خطة التفتيش الشهرية** هو تطبيق ويب متكامل لإدارة وتنظيم خطط التفتيش الشهرية مع نظام تخزين سحابي كبير المساحة للملفات والبيانات.

**Monthly Inspection Plan** is a comprehensive web application for managing and organizing monthly inspection schedules with a large-capacity cloud storage system for files and data.

### 🎯 الميزات الرئيسية - Key Features

- ✅ **نظام تخزين سحابي** - Cloud storage system using GitHub (Unlimited storage)
- ✅ **إدارة خطط التفتيش** - Inspection plan management
- ✅ **إدارة المفتشين والمناطق** - Inspector and area management
- ✅ **رفع وتحميل الملفات** - File upload and download
- ✅ **مكتبة ملفات منظمة** - Organized file library
- ✅ **واجهة مستخدم عربية** - Arabic-first user interface
- ✅ **نظام أمان متقدم** - Advanced security system
- ✅ **وضع الصيانة** - Maintenance mode
- ✅ **التحديثات الفورية** - Instant updates
- ✅ **دعم متعدد اللغات** - Multi-language support (Arabic & English)

---

## 🚀 البدء السريع - Quick Start

### المتطلبات - Requirements

1. **متصفح ويب حديث** - Modern web browser (Chrome, Firefox, Safari, Edge)
2. **حساب GitHub** - GitHub account (for cloud storage)
3. **GitHub Personal Access Token** - For file upload functionality

### الإعداد - Setup

#### 1. استنساخ المستودع - Clone Repository

```bash
git clone https://github.com/aliabdelaal-adm/Monthly_inspection_plan.git
cd Monthly_inspection_plan
```

#### 2. فتح التطبيق - Open Application

```bash
# افتح index.html في المتصفح
# Open index.html in your browser

# أو استخدم خادم محلي
# Or use a local server
python -m http.server 8000
# ثم افتح http://localhost:8000
# Then open http://localhost:8000
```

#### 3. تكوين التوكن - Configure Token

1. اذهب إلى: [GitHub Settings → Tokens](https://github.com/settings/tokens)
2. أنشئ توكن جديد مع صلاحيات `repo`
3. في التطبيق، انقر على "تحديث التوكن" وأدخل التوكن
4. احفظ التوكن - سيتم استخدامه لرفع الملفات

---

## 💾 نظام التخزين السحابي - Cloud Storage System

### البنية التحتية - Infrastructure

التطبيق يستخدم **GitHub** كمخزن سحابي بمساحة غير محدودة:

- **المساحة**: غير محدودة (Unlimited storage)
- **حجم الملف الواحد**: حتى 25 MB per file
- **أنواع الملفات المدعومة**: PDF, Excel, Word, CSV, JSON, TXT, Images
- **الأمان**: مشفر ومحمي بتوكن GitHub
- **النسخ الاحتياطي**: تلقائي عبر Git version control
- **الوصول**: من أي مكان في العالم

### المجلدات - Directories

```
files/
├── documents/      # الوثائق العامة - General documents
├── schedules/      # الجداول والخطط - Schedules and plans
├── reports/        # التقارير - Reports
└── resources/      # الموارد والمراجع - Resources
```

### أنواع الملفات المدعومة - Supported File Types

| النوع | الامتداد | الحجم الأقصى |
|------|---------|------------|
| PDF | .pdf | 25 MB |
| Excel | .xlsx, .xls | 25 MB |
| Word | .docx, .doc | 25 MB |
| CSV | .csv | 25 MB |
| JSON | .json | 25 MB |
| Text | .txt | 25 MB |
| Images | .jpg, .png, .gif | 25 MB |

---

## 📚 الاستخدام - Usage

### للمطورين - For Developers

1. **تسجيل الدخول**: استخدم كلمة المرور المطورة
2. **رفع الملفات**: من إدارة خدمات النظام
3. **إدارة البيانات**: تحرير خطط التفتيش والمحلات
4. **الصيانة**: تفعيل وضع الصيانة عند الحاجة

### للمفتشين - For Inspectors

1. **عرض الخطة**: مشاهدة خطة التفتيش الشهرية
2. **تحميل الملفات**: الوصول إلى مكتبة الملفات
3. **بحث**: البحث في البيانات والملفات
4. **تصدير**: تصدير البيانات إلى Excel أو PDF

---

## 🔐 الأمان - Security

### الحماية - Protection

- 🔒 **كلمة مرور المطور**: حماية الوظائف الإدارية
- 🔑 **GitHub Token**: تشفير عمليات الرفع
- 🛡️ **Session Management**: إدارة جلسات آمنة
- 🚫 **Firewall Protection**: حماية من الهجمات
- ✅ **Data Validation**: التحقق من صحة البيانات

### أفضل الممارسات - Best Practices

1. **لا تشارك كلمة المرور المطورة** - Don't share developer password
2. **احفظ التوكن بشكل آمن** - Store token securely
3. **حدّث التوكن دورياً** - Update token regularly
4. **راقب سجلات النشاط** - Monitor activity logs
5. **استخدم HTTPS فقط** - Use HTTPS only

---

## 📦 نشر التطبيق - Deployment

### GitHub Pages (مجاني - Free)

التطبيق منشور على: https://aliabdelaal-adm.github.io/Monthly_inspection_plan/

#### خطوات النشر - Deployment Steps

1. **Fork المستودع** - Fork the repository
2. **تفعيل GitHub Pages**:
   - Settings → Pages
   - Source: main branch
   - Save
3. **الوصول للتطبيق**: `https://USERNAME.github.io/Monthly_inspection_plan/`

### استضافة مخصصة - Custom Hosting

يمكن نشر التطبيق على أي خادم ويب:

```bash
# نسخ الملفات إلى الخادم
rsync -av ./ user@server:/var/www/html/

# أو استخدام FTP
# Or use FTP to upload files
```

---

## 📖 التوثيق - Documentation

### الأدلة المتوفرة - Available Guides

| الملف | الوصف |
|------|-------|
| [FILE_UPLOAD_GUIDE.md](FILE_UPLOAD_GUIDE.md) | دليل رفع الملفات |
| [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) | دليل النشر الكامل |
| [CLOUD_STORAGE_GUIDE.md](CLOUD_STORAGE_GUIDE.md) | شرح نظام التخزين السحابي |
| [FEATURE_DIAGRAM.md](FEATURE_DIAGRAM.md) | مخطط الميزات |
| [FILE_UPLOAD_TROUBLESHOOTING.md](FILE_UPLOAD_TROUBLESHOOTING.md) | حل المشاكل |

---

## 🛠️ التطوير - Development

### البنية التقنية - Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with RTL support
- **Storage**: GitHub API for cloud storage
- **Libraries**: 
  - xlsx.js (Excel processing)
  - jsPDF (PDF generation)
  - html2canvas (Screenshots)
  - PDF.js (PDF viewing)

### المساهمة - Contributing

1. Fork المشروع
2. أنشئ فرع للميزة (`git checkout -b feature/AmazingFeature`)
3. Commit التغييرات (`git commit -m 'Add AmazingFeature'`)
4. Push للفرع (`git push origin feature/AmazingFeature`)
5. افتح Pull Request

---

## 🎓 الدعم - Support

### الحصول على المساعدة - Getting Help

- 📧 **البريد الإلكتروني**: عبر GitHub Issues
- 📝 **التوثيق**: راجع ملفات MD في المستودع
- 🐛 **الأخطاء**: أبلغ عنها في GitHub Issues
- 💡 **اقتراحات**: استخدم GitHub Discussions

---

## 📊 الإحصائيات - Statistics

- **حجم المشروع**: ~500 KB
- **الملفات**: 200+ files
- **التوثيق**: 100+ documentation files
- **اللغات**: عربي + English
- **المتصفحات المدعومة**: All modern browsers
- **Mobile Support**: ✅ Full responsive design

---

## 📜 الترخيص - License

هذا المشروع مخصص للاستخدام الداخلي.
This project is for internal use only.

---

## 👨‍💻 المطور - Developer

**د. علي عبدالعال - Dr. Ali Abdelaal**

- GitHub: [@aliabdelaal-adm](https://github.com/aliabdelaal-adm)
- Repository: [Monthly_inspection_plan](https://github.com/aliabdelaal-adm/Monthly_inspection_plan)

---

## 🎯 الحالة - Status

✅ **جاهز للإنتاج** - Production Ready  
✅ **مستقر** - Stable  
✅ **تحديثات مستمرة** - Active Maintenance  
✅ **موثق بالكامل** - Fully Documented

---

## 📅 آخر تحديث - Last Update

**التاريخ**: 2025-01-15  
**الإصدار**: 2.0.0  
**الحالة**: Active Development

---

<div align="center">

**صُنع بـ ❤️ في الإمارات - Made with ❤️ in UAE**

[🌟 النجوم](https://github.com/aliabdelaal-adm/Monthly_inspection_plan/stargazers) | 
[🐛 المشاكل](https://github.com/aliabdelaal-adm/Monthly_inspection_plan/issues) | 
[📖 Wiki](https://github.com/aliabdelaal-adm/Monthly_inspection_plan/wiki)

</div>
