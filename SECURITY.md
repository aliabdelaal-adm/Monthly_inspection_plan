# Security Policy / سياسة الأمان

## 🔐 Critical Security Requirements / المتطلبات الأمنية الحرجة

### ⚠️ NEVER Commit These Files / لا تقم أبداً بإرسال هذه الملفات

The following files contain sensitive credentials and **MUST NEVER** be committed to Git:

الملفات التالية تحتوي على بيانات اعتماد حساسة ويجب **ألا يتم إرسالها أبداً** إلى Git:

- ❌ `service-account-key.json` - Google Cloud service account credentials
- ❌ `*service-account*.json` - Any service account files
- ❌ `*credentials*.json` - Any credential files
- ❌ `.env` - Environment variables
- ❌ `*.local.js` - Local configuration files
- ❌ `google-maps-config.local.js` - Local API keys

### ✅ Protected by .gitignore

These file patterns are automatically excluded by `.gitignore`:

```
*service-account*.json
*serviceaccount*.json
*credentials*.json
service-account-key.json
gcp-credentials.json
firebase-adminsdk*.json
*.local.js
.env
.env.local
```

## 🛡️ Security Guidelines / إرشادات الأمان

### 1. Google Service Accounts / حسابات خدمة Google

**📖 See detailed guide:** [SERVICE_ACCOUNT_SECURITY_GUIDE.md](./SERVICE_ACCOUNT_SECURITY_GUIDE.md)

**Quick rules:**
- ✅ Store credentials locally, never in Git
- ✅ Use environment variables for production
- ✅ Rotate keys every 90 days
- ✅ Grant minimum necessary permissions
- ❌ Never commit JSON credential files
- ❌ Never share keys via email/chat

**قواعد سريعة:**
- ✅ احفظ بيانات الاعتماد محلياً، ليس في Git
- ✅ استخدم متغيرات البيئة للإنتاج
- ✅ قم بتدوير المفاتيح كل 90 يوماً
- ✅ امنح الحد الأدنى من الأذونات الضرورية
- ❌ لا تقم أبداً بإرسال ملفات بيانات اعتماد JSON
- ❌ لا تشارك المفاتيح عبر البريد الإلكتروني/الدردشة

### 2. API Keys / مفاتيح API

**Google Maps API:**
- ✅ Store in `google-maps-config.local.js` (gitignored)
- ✅ Restrict keys to specific domains in Google Cloud Console
- ✅ Monitor API usage regularly
- ❌ Don't use unrestricted API keys in production

**GitHub Personal Access Tokens:**
- ✅ Use tokens with minimum required scopes
- ✅ Store securely in browser localStorage (not in code)
- ✅ Regenerate tokens if compromised
- ❌ Never commit tokens to Git

### 3. Developer Password / كلمة مرور المطور

- ✅ Change the default developer password
- ✅ Use a strong, unique password
- ✅ Don't share the password in insecure channels
- ✅ Implement session timeout for security

## 🚨 If Credentials Are Compromised / إذا تم اختراق بيانات الاعتماد

### Immediate Actions:

1. **Service Account Keys:**
   - Delete the key immediately in [Google Cloud Console](https://console.cloud.google.com/iam-admin/serviceaccounts)
   - Create a new key
   - Review access logs for suspicious activity

2. **API Keys:**
   - Regenerate the key in Google Cloud Console
   - Update your local configuration
   - Monitor for unauthorized usage

3. **If Committed to Git:**
   - The credential is permanently in Git history
   - Delete the key from the cloud provider immediately
   - Rotate to a new key
   - Consider using tools like [git-filter-repo](https://github.com/newren/git-filter-repo) to remove from history (advanced)

## 📋 Supported Versions / الإصدارات المدعومة

| Version | Supported          |
| ------- | ------------------ |
| 2.x.x   | :white_check_mark: |
| 1.x.x   | :x:                |

## 🐛 Reporting a Vulnerability / الإبلاغ عن ثغرة أمنية

### English:

If you discover a security vulnerability:

1. **DO NOT** open a public issue
2. Send details privately to the repository owner via:
   - GitHub Security Advisories (preferred)
   - Direct message to [@aliabdelaal-adm](https://github.com/aliabdelaal-adm)
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

**Response time:**
- Initial acknowledgment: Within 48 hours
- Status update: Within 7 days
- Resolution timeline: Depends on severity

### العربية:

إذا اكتشفت ثغرة أمنية:

1. **لا تفتح** مشكلة عامة
2. أرسل التفاصيل بشكل خاص إلى مالك المستودع عبر:
   - GitHub Security Advisories (مفضل)
   - رسالة مباشرة إلى [@aliabdelaal-adm](https://github.com/aliabdelaal-adm)
3. ضمّن:
   - وصف الثغرة
   - خطوات إعادة الإنتاج
   - التأثير المحتمل
   - الإصلاح المقترح (إن وجد)

**وقت الاستجابة:**
- الإقرار الأولي: في غضون 48 ساعة
- تحديث الحالة: في غضون 7 أيام
- الجدول الزمني للحل: يعتمد على الخطورة

## 🔍 Security Checklist / قائمة التحقق الأمنية

Before deploying or committing code:

- [ ] No service account credentials in code
- [ ] No API keys hardcoded in source files
- [ ] All sensitive files are in `.gitignore`
- [ ] `git status` shows no credential files
- [ ] API keys are restricted to specific domains
- [ ] Service account permissions follow least privilege
- [ ] Developer password has been changed from default
- [ ] All dependencies are up to date
- [ ] No secrets in environment variables committed to Git

قبل النشر أو إرسال الكود:

- [ ] لا توجد بيانات اعتماد حسابات خدمة في الكود
- [ ] لا توجد مفاتيح API مشفرة في ملفات المصدر
- [ ] جميع الملفات الحساسة في `.gitignore`
- [ ] `git status` لا يظهر ملفات بيانات اعتماد
- [ ] مفاتيح API مقيدة لنطاقات محددة
- [ ] أذونات حساب الخدمة تتبع الامتياز الأدنى
- [ ] تم تغيير كلمة مرور المطور من الافتراضية
- [ ] جميع التبعيات محدثة
- [ ] لا توجد أسرار في متغيرات البيئة المُرسلة إلى Git

## 📚 Additional Resources / مصادر إضافية

- [SERVICE_ACCOUNT_SECURITY_GUIDE.md](./SERVICE_ACCOUNT_SECURITY_GUIDE.md) - Complete service account security guide
- [Google Cloud Security Best Practices](https://cloud.google.com/security/best-practices)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

---

**Remember: Security is everyone's responsibility!**  
**تذكر: الأمن مسؤولية الجميع!**
