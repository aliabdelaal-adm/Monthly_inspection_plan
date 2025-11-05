# 🔐 Google Service Account Security Guide
# دليل أمان حسابات خدمة Google

## ⚠️ CRITICAL SECURITY WARNING / تحذير أمني حرج

**NEVER commit service account credentials to Git repositories!**  
**لا تقم أبداً بإضافة بيانات اعتماد حسابات الخدمة إلى مستودعات Git!**

Service account JSON files contain sensitive private keys that grant access to your Google Cloud resources. If exposed, they can be used by attackers to:
- Access your data
- Incur charges on your billing account
- Compromise your infrastructure

ملفات JSON لحسابات الخدمة تحتوي على مفاتيح خاصة حساسة تمنح الوصول إلى موارد Google Cloud الخاصة بك. إذا تم كشفها، يمكن استخدامها من قبل المهاجمين من أجل:
- الوصول إلى بياناتك
- فرض رسوم على حساب الفوترة الخاص بك
- اختراق البنية التحتية الخاصة بك

---

## 📋 Quick Setup / الإعداد السريع

### 1. Create Service Account / إنشاء حساب خدمة

**English:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project or create a new one
3. Navigate to "IAM & Admin" → "Service Accounts"
4. Click "Create Service Account"
5. Fill in the details:
   - Name: `monthly-inspection-plan-service`
   - Description: `Service account for Monthly Inspection Plan app`
6. Grant necessary roles (e.g., Storage Admin, Cloud Functions Invoker)
7. Click "Done"

**العربية:**
1. اذهب إلى [Google Cloud Console](https://console.cloud.google.com/)
2. اختر مشروعك أو أنشئ مشروعاً جديداً
3. انتقل إلى "IAM والإدارة" → "حسابات الخدمة"
4. انقر على "إنشاء حساب خدمة"
5. املأ التفاصيل:
   - الاسم: `monthly-inspection-plan-service`
   - الوصف: `حساب خدمة لتطبيق خطة التفتيش الشهرية`
6. امنح الأدوار الضرورية (مثل مدير التخزين، مستدعي Cloud Functions)
7. انقر "تم"

### 2. Create and Download Key / إنشاء وتحميل المفتاح

**English:**
1. In the Service Accounts list, click on your newly created account
2. Go to the "Keys" tab
3. Click "Add Key" → "Create new key"
4. Select "JSON" format
5. Click "Create"
6. **The JSON file will download automatically - KEEP IT SECURE!**

**العربية:**
1. في قائمة حسابات الخدمة، انقر على الحساب الذي أنشأته
2. اذهب إلى تبويب "المفاتيح"
3. انقر "إضافة مفتاح" → "إنشاء مفتاح جديد"
4. اختر تنسيق "JSON"
5. انقر "إنشاء"
6. **سيتم تحميل ملف JSON تلقائياً - احتفظ به آمناً!**

### 3. Secure the Credentials File / تأمين ملف بيانات الاعتماد

**English:**

**OPTION A: Local File (Recommended for Development)**

1. Rename the downloaded file to `service-account-key.json`
2. Place it in your project root directory
3. **VERIFY** it's listed in `.gitignore` (it should be automatically ignored)
4. Test that Git ignores it: `git status` (should not show the file)

**OPTION B: Environment Variables (Recommended for Production)**

Instead of using a file, store credentials as environment variables:

```bash
# Linux/Mac
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"

# Windows (Command Prompt)
set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\service-account-key.json

# Windows (PowerShell)
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\service-account-key.json"
```

**العربية:**

**الخيار أ: ملف محلي (موصى به للتطوير)**

1. أعد تسمية الملف المحمل إلى `service-account-key.json`
2. ضعه في المجلد الجذري للمشروع
3. **تحقق** من أنه مدرج في `.gitignore` (يجب تجاهله تلقائياً)
4. اختبر أن Git يتجاهله: `git status` (يجب ألا يظهر الملف)

**الخيار ب: متغيرات البيئة (موصى به للإنتاج)**

بدلاً من استخدام ملف، قم بتخزين بيانات الاعتماد كمتغيرات بيئة:

```bash
# Linux/Mac
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"

# Windows (موجه الأوامر)
set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\service-account-key.json

# Windows (PowerShell)
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\service-account-key.json"
```

---

## 🛡️ Security Best Practices / أفضل الممارسات الأمنية

### ✅ DO / افعل

- ✅ Store service account files locally and add them to `.gitignore`
- ✅ Use environment variables for production deployments
- ✅ Rotate service account keys regularly (every 90 days recommended)
- ✅ Use the principle of least privilege (grant minimum necessary permissions)
- ✅ Monitor service account usage in Cloud Console
- ✅ Delete unused service accounts and keys
- ✅ Use separate service accounts for different environments (dev, staging, prod)

- ✅ احفظ ملفات حسابات الخدمة محلياً وأضفها إلى `.gitignore`
- ✅ استخدم متغيرات البيئة للنشر في الإنتاج
- ✅ قم بتدوير مفاتيح حسابات الخدمة بانتظام (يُنصح كل 90 يوماً)
- ✅ استخدم مبدأ الامتياز الأدنى (امنح الحد الأدنى من الأذونات الضرورية)
- ✅ راقب استخدام حساب الخدمة في Cloud Console
- ✅ احذف حسابات الخدمة والمفاتيح غير المستخدمة
- ✅ استخدم حسابات خدمة منفصلة لبيئات مختلفة (التطوير، التجهيز، الإنتاج)

### ❌ DON'T / لا تفعل

- ❌ **NEVER commit service account JSON files to Git**
- ❌ **NEVER share service account keys via email, chat, or messaging apps**
- ❌ **NEVER hardcode credentials in source code**
- ❌ Don't grant overly broad permissions
- ❌ Don't use the same service account across all environments
- ❌ Don't forget to delete old/unused keys

- ❌ **لا تقم أبداً بإضافة ملفات JSON لحسابات الخدمة إلى Git**
- ❌ **لا تشارك مفاتيح حسابات الخدمة عبر البريد الإلكتروني أو الدردشة أو تطبيقات المراسلة**
- ❌ **لا تضع بيانات الاعتماد مباشرة في الكود المصدري**
- ❌ لا تمنح أذونات واسعة جداً
- ❌ لا تستخدم نفس حساب الخدمة عبر جميع البيئات
- ❌ لا تنس حذف المفاتيح القديمة/غير المستخدمة

---

## 🚨 If Credentials Are Compromised / إذا تم اختراق بيانات الاعتماد

**IMMEDIATE ACTIONS / إجراءات فورية:**

1. **Delete the compromised key immediately:**
   - Go to [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
   - Find your service account
   - Go to "Keys" tab
   - Delete the compromised key

2. **Create a new key:**
   - Follow the steps in "Create and Download Key" section above
   - Update your application with the new credentials

3. **Review access logs:**
   - Check [Cloud Logging](https://console.cloud.google.com/logs) for suspicious activity
   - Look for unusual API calls or access patterns

4. **If committed to Git:**
   - The key is permanently in Git history
   - You MUST delete the key from Google Cloud Console
   - Create a new key
   - Consider the repository compromised

**إجراءات فورية:**

1. **احذف المفتاح المخترق فوراً:**
   - اذهب إلى [حسابات الخدمة](https://console.cloud.google.com/iam-admin/serviceaccounts)
   - ابحث عن حساب الخدمة الخاص بك
   - اذهب إلى تبويب "المفاتيح"
   - احذف المفتاح المخترق

2. **أنشئ مفتاحاً جديداً:**
   - اتبع الخطوات في قسم "إنشاء وتحميل المفتاح" أعلاه
   - حدّث تطبيقك ببيانات الاعتماد الجديدة

3. **راجع سجلات الوصول:**
   - تحقق من [Cloud Logging](https://console.cloud.google.com/logs) لنشاط مشبوه
   - ابحث عن استدعاءات API غير عادية أو أنماط وصول مشبوهة

4. **إذا تم الالتزام بـ Git:**
   - المفتاح موجود بشكل دائم في تاريخ Git
   - يجب عليك حذف المفتاح من Google Cloud Console
   - أنشئ مفتاحاً جديداً
   - اعتبر المستودع مخترقاً

---

## 📝 Template File / ملف النموذج

This repository includes `service-account-template.json` as a reference.  
**DO NOT put real credentials in this template!**

هذا المستودع يتضمن `service-account-template.json` كمرجع.  
**لا تضع بيانات اعتماد حقيقية في هذا النموذج!**

To use it:
1. Copy the template: `cp service-account-template.json service-account-key.json`
2. Replace all placeholder values with your actual credentials
3. Verify the file is gitignored: `git status` (should not appear)

لاستخدامه:
1. انسخ النموذج: `cp service-account-template.json service-account-key.json`
2. استبدل جميع القيم النائبة ببيانات الاعتماد الفعلية الخاصة بك
3. تحقق من أن الملف مُتجاهل: `git status` (يجب ألا يظهر)

---

## 🔍 Verification / التحقق

Before committing any changes, always verify:

```bash
# Check what files will be committed
git status

# Make sure service account files are NOT listed
# If you see any *-account*.json files, STOP and investigate

# Verify .gitignore is working
git check-ignore service-account-key.json
# Should output: service-account-key.json
```

قبل إرسال أي تغييرات، تحقق دائماً:

```bash
# تحقق من الملفات التي سيتم إرسالها
git status

# تأكد من عدم إدراج ملفات حسابات الخدمة
# إذا رأيت أي ملفات *-account*.json، توقف وتحقق

# تحقق من أن .gitignore يعمل
git check-ignore service-account-key.json
# يجب أن يخرج: service-account-key.json
```

---

## 📚 Additional Resources / مصادر إضافية

- [Google Cloud Service Accounts Best Practices](https://cloud.google.com/iam/docs/best-practices-service-accounts)
- [Google Cloud Security Best Practices](https://cloud.google.com/security/best-practices)
- [Managing Service Account Keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

---

## 💡 Need Help? / هل تحتاج مساعدة؟

If you're unsure about service account security:
1. Review the official Google Cloud documentation
2. Consult with your team's security expert
3. When in doubt, DON'T commit - ask first!

إذا كنت غير متأكد بشأن أمان حساب الخدمة:
1. راجع وثائق Google Cloud الرسمية
2. استشر خبير الأمن في فريقك
3. عند الشك، لا ترسل - اسأل أولاً!

---

**Remember: Security is everyone's responsibility!**  
**تذكر: الأمن مسؤولية الجميع!**
