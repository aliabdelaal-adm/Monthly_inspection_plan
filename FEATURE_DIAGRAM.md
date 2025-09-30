# مخطط ميزة رفع الملفات - File Upload Feature Diagram

## نظرة عامة على سير العمل - Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                          BEFORE - قبل                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  User clicks "رفع ملف"  →  File dialog opens  →  User selects file │
│           ↓                                                          │
│     File selected  →  Shows file name  →  ❌ NOTHING HAPPENS        │
│                                                                      │
│  Problem: File only selected locally, not uploaded to GitHub!       │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                          AFTER - بعد                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  User clicks "رفع ملف"  →  File dialog opens  →  User selects file │
│           ↓                                                          │
│     Developer check  →  ✅ Permission granted                       │
│           ↓                                                          │
│     Show loading: "⏳ جاري رفع الملف..."                            │
│           ↓                                                          │
│     Convert file to base64  →  Upload to GitHub API                │
│           ↓                                                          │
│     Update files.json  →  Process file locally                      │
│           ↓                                                          │
│     ✅ "تم رفع الملف بنجاح!"  →  File available to all users      │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## معمارية النظام - System Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE - واجهة المستخدم                │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐    │
│  │  جدول المناوبات  │  │  تتبع الإجازات  │  │  قائمة المحلات  │    │
│  │   📅 رفع ملف    │  │   🏖️ رفع ملف    │  │   🏪 رفع ملف    │    │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘    │
│           │                     │                     │               │
│           └─────────────────────┴─────────────────────┘               │
│                                 ↓                                     │
└─────────────────────────────────┼─────────────────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │  PERMISSION CHECK         │
                    │  فحص الصلاحيات            │
                    │  isDev || window.isDev?   │
                    └─────────────┬─────────────┘
                                  │
                        YES ✅    │    ❌ NO
                    ┌─────────────┴─────────────┐
                    │                           │
         ┌──────────▼──────────┐    ┌──────────▼──────────┐
         │  UPLOAD FUNCTION    │    │  ERROR MESSAGE      │
         │  uploadFileToGitHub │    │  "عذراً، للمطور     │
         │                     │    │   فقط"              │
         └──────────┬──────────┘    └─────────────────────┘
                    │
         ┌──────────┴──────────┐
         │  FILE VALIDATION    │
         │  • Size check       │
         │  • Token check      │
         │  • Type check       │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │  LOADING INDICATOR  │
         │  ⏳ جاري رفع...     │
         │  filename.xlsx      │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │  BASE64 CONVERSION  │
         │  FileReader.        │
         │  readAsDataURL()    │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │  GITHUB API         │
         │  PUT /repos/.../    │
         │  contents/files/... │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │  UPDATE REGISTRY    │
         │  files.json         │
         │  • Add file entry   │
         │  • Update timestamp │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │  LOCAL PROCESSING   │
         │  • Parse JSON       │
         │  • Read Excel       │
         │  • Extract PDF      │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │  SUCCESS MESSAGE    │
         │  ✅ تم الرفع!       │
         │  متاح للجميع        │
         └──────────┬──────────┘
                    │
                    ▼
         ┌─────────────────────┐
         │  PUBLIC ACCESS      │
         │  مكتبة الملفات       │
         │  • Download         │
         │  • Preview          │
         └─────────────────────┘
```

---

## مثال تفصيلي - Detailed Example

### سيناريو: رفع ملف Excel لجدول المناوبات
### Scenario: Uploading Excel file for shifts schedule

```
STEP 1: User Action
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 User: Clicks "📁 رفع ملف" button
📍 Location: System Services → Shifts Schedule

STEP 2: File Selection
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💻 System: Opens file selection dialog
📄 User: Selects "جدول_المناوبات_يناير_2025.xlsx"
📊 File Details:
   - Size: 1.2 MB (< 25 MB ✅)
   - Type: Excel (.xlsx)
   - Name: جدول_المناوبات_يناير_2025.xlsx

STEP 3: Permission Check
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔐 System: Checks if (isDev || window.isDev)
✅ Result: User is developer
🎫 Token: Retrieved from localStorage

STEP 4: Validation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ File size: 1.2 MB < 25 MB
✅ Token exists: ghp_xxxxxxxxxxxx
✅ Category: schedules

STEP 5: Loading Display
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💫 Modal appears in center of screen:
   ┌─────────────────────────────────┐
   │            ⏳                    │
   │      جاري رفع الملف...          │
   │  جدول_المناوبات_يناير_2025.xlsx │
   │      الرجاء الانتظار...         │
   └─────────────────────────────────┘

STEP 6: File Conversion
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔄 FileReader.readAsDataURL()
📝 Convert to base64
📦 Result: UEsDBBQABgAIAAAAIQBi7p1o... (truncated)

STEP 7: GitHub Upload
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 API Call:
   PUT https://api.github.com/repos/
       aliabdelaal-adm/Monthly_inspection_plan/
       contents/files/schedules/جدول_المناوبات_يناير_2025.xlsx

📤 Request Body:
   {
     "message": "رفع ملف جديد: جدول_المناوبات_يناير_2025.xlsx",
     "content": "UEsDBBQABgAIAAAAIQBi7p1o..."
   }

📥 Response:
   Status: 201 Created ✅

STEP 8: Update Registry
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 Load files.json
➕ Add new entry:
   {
     "id": "1735920000000",
     "name": "جدول_المناوبات_يناير_2025.xlsx",
     "path": "files/schedules/جدول_المناوبات_يناير_2025.xlsx",
     "category": "schedules",
     "type": "xlsx",
     "size": 1258291,
     "uploadDate": "2025-01-03T10:00:00.000Z",
     "description": "جدول المناوبات - جدول_المناوبات_يناير_2025.xlsx",
     "uploader": "د. علي عبدالعال",
     "visible": true
   }
💾 Save updated files.json

STEP 9: Local Processing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 XLSX.read() - Parse Excel file
📈 Extract data: 156 rows found
💾 Store in inspectionData
🔄 Update schedule table

STEP 10: Success Notification
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ Remove loading modal
✅ Show success alert:
   ┌─────────────────────────────────────────┐
   │  ✅ تم رفع ملف جدول المناوبات بنجاح!   │
   │                                         │
   │  الملف: جدول_المناوبات_يناير_2025.xlsx │
   │  الآن متاح للجميع في مكتبة الملفات     │
   └─────────────────────────────────────────┘

STEP 11: Public Accessibility
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 File appears in:
   - Public Files Library → Schedules section
   - GitHub Repository → files/schedules/
   - files.json registry

👥 All users can now:
   - 👁️ View file info
   - 📥 Download file
   - 🔍 Search and filter
```

---

## تدفق البيانات - Data Flow

```
┌─────────────┐
│   Browser   │  User Interface
│   المتصفح   │
└──────┬──────┘
       │ 1. User selects file
       ↓
┌──────────────────────────────────┐
│  JavaScript Upload Function      │
│  uploadFileToGitHub()            │
│  ┌──────────────────────────┐   │
│  │ • Check permissions      │   │
│  │ • Validate file          │   │
│  │ • Show loading           │   │
│  │ • Convert to base64      │   │
│  └──────────────────────────┘   │
└──────┬───────────────────────────┘
       │ 2. Upload request
       ↓
┌──────────────────────────────────┐
│  GitHub API                      │
│  api.github.com                  │
│  ┌──────────────────────────┐   │
│  │ PUT /repos/.../contents  │   │
│  │ Authorization: token xxx │   │
│  └──────────────────────────┘   │
└──────┬───────────────────────────┘
       │ 3. Store file
       ↓
┌──────────────────────────────────┐
│  GitHub Repository               │
│  files/schedules/ or            │
│  files/documents/                │
│  ┌──────────────────────────┐   │
│  │ • Store file content     │   │
│  │ • Create commit          │   │
│  │ • Update tree            │   │
│  └──────────────────────────┘   │
└──────┬───────────────────────────┘
       │ 4. Update registry
       ↓
┌──────────────────────────────────┐
│  files.json                      │
│  File Registry                   │
│  ┌──────────────────────────┐   │
│  │ • Add new file entry     │   │
│  │ • Update metadata        │   │
│  │ • Update timestamp       │   │
│  └──────────────────────────┘   │
└──────┬───────────────────────────┘
       │ 5. Process locally (optional)
       ↓
┌──────────────────────────────────┐
│  Local Processing                │
│  Browser Memory                  │
│  ┌──────────────────────────┐   │
│  │ • Parse JSON             │   │
│  │ • Read Excel data        │   │
│  │ • Extract PDF text       │   │
│  │ • Update UI              │   │
│  └──────────────────────────┘   │
└──────┬───────────────────────────┘
       │ 6. Show result
       ↓
┌──────────────────────────────────┐
│  User Interface                  │
│  Success/Error Message           │
│  ┌──────────────────────────┐   │
│  │ ✅ File uploaded!        │   │
│  │ 📚 Available to all      │   │
│  └──────────────────────────┘   │
└──────────────────────────────────┘
```

---

## مقارنة: قبل وبعد - Comparison: Before vs After

```
┌─────────────────────────────────────────────────────────────────┐
│                 BEFORE - قبل التحديث                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ❌ Files only selected, not uploaded                           │
│  ❌ No GitHub integration                                       │
│  ❌ Files not accessible to other users                         │
│  ❌ No central storage                                          │
│  ❌ Each user had to upload separately                          │
│  ❌ No version control                                          │
│  ❌ No file registry                                            │
│  ⚠️  Only local processing (temporary)                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                 AFTER - بعد التحديث                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ✅ Files uploaded to GitHub repository                         │
│  ✅ Full GitHub API integration                                 │
│  ✅ Files accessible to ALL users                               │
│  ✅ Central storage in /files/ directory                        │
│  ✅ Upload once, available for everyone                         │
│  ✅ Version control via Git                                     │
│  ✅ Automatic file registry (files.json)                        │
│  ✅ Both remote storage AND local processing                    │
│  ✅ Organized by categories                                     │
│  ✅ Searchable and filterable                                   │
│  ✅ Download and preview capabilities                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## الأقسام الثلاثة - Three Sections

```
┌────────────────────────────────────────────────────────────────┐
│  1. SHIFTS SCHEDULE - جدول المناوبات                           │
├────────────────────────────────────────────────────────────────┤
│  📅 Purpose: Upload work shift schedules                       │
│  📁 Storage: files/schedules/                                  │
│  📝 Types: JSON, Excel, PDF, CSV, TXT, DOC                     │
│  🎯 Use Case: Share monthly shift rotations                    │
│                                                                 │
│  Example Files:                                                 │
│  • جدول_المناوبات_يناير.xlsx                                   │
│  • schedule_february_2025.pdf                                   │
│  • shifts_data.json                                             │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│  2. VACATION TRACKING - تتبع الإجازات                          │
├────────────────────────────────────────────────────────────────┤
│  🏖️ Purpose: Upload vacation schedules and tracking data      │
│  📁 Storage: files/schedules/                                  │
│  📝 Types: JSON, Excel, PDF, CSV, TXT, DOC                     │
│  🎯 Use Case: Track inspector vacations and availability       │
│                                                                 │
│  Example Files:                                                 │
│  • الإجازات_السنوية_2025.xlsx                                  │
│  • vacation_calendar.pdf                                        │
│  • leave_requests.csv                                           │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│  3. SHOPS MANAGEMENT - قائمة المحلات                           │
├────────────────────────────────────────────────────────────────┤
│  🏪 Purpose: Upload shops lists and databases                  │
│  📁 Storage: files/documents/                                  │
│  📝 Types: JSON, Excel, CSV, PDF, TXT, DOC                     │
│  🎯 Use Case: Maintain centralized shops database              │
│                                                                 │
│  Example Files:                                                 │
│  • قائمة_المحلات_المحدثة.xlsx                                  │
│  • shops_database.csv                                           │
│  • stores_info.json                                             │
└────────────────────────────────────────────────────────────────┘
```

---

## الخلاصة - Summary

```
═══════════════════════════════════════════════════════════════════
   FILE UPLOAD FEATURE - ميزة رفع الملفات
═══════════════════════════════════════════════════════════════════

   PROBLEM SOLVED:
   ✅ Files now actually upload to GitHub
   ✅ Available to all users instantly
   ✅ Organized and searchable
   ✅ With proper security and permissions

   SECTIONS ENABLED:
   ✅ Shifts Schedule (جدول المناوبات)
   ✅ Vacation Tracking (تتبع الإجازات)
   ✅ Shops Management (قائمة المحلات)

   KEY FEATURES:
   ✅ Developer-only upload
   ✅ Automatic file registry
   ✅ Loading indicators
   ✅ Success/error messages
   ✅ Local + remote processing

═══════════════════════════════════════════════════════════════════
```
