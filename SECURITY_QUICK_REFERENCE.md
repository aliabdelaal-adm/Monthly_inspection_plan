# 🔐 Security Quick Reference Card
# بطاقة مرجع سريع للأمان

## ⚠️ DO NOT COMMIT THESE FILES
## لا تقم بإرسال هذه الملفات

```
❌ service-account-key.json
❌ *service-account*.json (except -template.json)
❌ *credentials*.json (except -template.json)
❌ gcp-credentials.json
❌ firebase-adminsdk*.json
❌ .env
❌ .env.local
❌ *.local.js
```

## ✅ Before Every Commit / قبل كل إرسال

```bash
# Check what will be committed
git status

# If you see ANY credential files, STOP!
# إذا رأيت أي ملفات بيانات اعتماد، توقف!

# Verify gitignore is working
git check-ignore service-account-key.json
# Should output: service-account-key.json
```

## 🚨 Accidentally Committed Credentials?
## قمت بإرسال بيانات اعتماد عن طريق الخطأ؟

**IMMEDIATE ACTION:**

1. **Revoke the credential immediately!**
   - Google Service Account: Delete key in [Cloud Console](https://console.cloud.google.com/iam-admin/serviceaccounts)
   - API Key: Regenerate in Google Cloud Console
   
2. **Create new credentials**

3. **Contact your team lead**

## 📚 Full Documentation / الوثائق الكاملة

- **Service Account Security:** [SERVICE_ACCOUNT_SECURITY_GUIDE.md](./SERVICE_ACCOUNT_SECURITY_GUIDE.md)
- **Setup Instructions:** [GOOGLE_SERVICE_ACCOUNT_SETUP.md](./GOOGLE_SERVICE_ACCOUNT_SETUP.md)
- **Security Policy:** [SECURITY.md](./SECURITY.md)

## 💡 Quick Tips / نصائح سريعة

1. **Use template files for examples**
   ```bash
   cp service-account-template.json service-account-key.json
   # Edit with your real credentials
   ```

2. **Verify file is gitignored**
   ```bash
   git check-ignore service-account-key.json
   ```

3. **Environment variables for production**
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/key.json"
   ```

4. **Regular security audit**
   ```bash
   # Search for potential credentials in tracked files
   git grep -i "private_key"
   git grep -i "BEGIN PRIVATE"
   ```

---

**When in doubt, DON'T commit - ASK!**  
**عند الشك، لا ترسل - اسأل!**
