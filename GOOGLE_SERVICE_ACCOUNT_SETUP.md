# 🔧 Google Cloud Service Account Setup
# إعداد حساب خدمة Google Cloud

## ⚠️ SECURITY FIRST / الأمان أولاً

**Before proceeding, read the security guide:**  
[SERVICE_ACCOUNT_SECURITY_GUIDE.md](./SERVICE_ACCOUNT_SECURITY_GUIDE.md)

**قبل المتابعة، اقرأ دليل الأمان:**  
[SERVICE_ACCOUNT_SECURITY_GUIDE.md](./SERVICE_ACCOUNT_SECURITY_GUIDE.md)

---

## 📋 Quick Start / البدء السريع

### Step 1: Create Service Account

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create or select your project
3. Navigate to **IAM & Admin** → **Service Accounts**
4. Click **Create Service Account**
5. Fill in details and assign roles

### Step 2: Download Credentials

1. Click on your service account
2. Go to **Keys** tab
3. Click **Add Key** → **Create new key**
4. Select **JSON** format
5. Click **Create** (file downloads automatically)

### Step 3: Secure the File

**IMPORTANT:** The downloaded file contains sensitive credentials!

```bash
# Rename the file
mv ~/Downloads/your-project-*.json service-account-key.json

# Move to project directory
mv service-account-key.json /path/to/Monthly_inspection_plan/

# Verify it's gitignored
cd /path/to/Monthly_inspection_plan/
git status
# service-account-key.json should NOT appear in the list
```

### Step 4: Verify Protection

```bash
# This should output the filename, confirming it's ignored
git check-ignore service-account-key.json

# Output should be:
# service-account-key.json
```

---

## 🔒 File Must Be Gitignored / يجب تجاهل الملف

The `.gitignore` file already includes these patterns:

```gitignore
*service-account*.json
*serviceaccount*.json
*credentials*.json
service-account-key.json
gcp-credentials.json
firebase-adminsdk*.json
```

**If your file doesn't match these patterns, rename it or update `.gitignore`**

---

## 🎯 Using Service Account in Code

### Option 1: Environment Variable (Recommended for Production)

```bash
# Set the environment variable
export GOOGLE_APPLICATION_CREDENTIALS="/absolute/path/to/service-account-key.json"

# Or add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
echo 'export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"' >> ~/.bashrc
```

### Option 2: Explicit Path in Code (Development Only)

```javascript
// In your JavaScript code
const serviceAccount = require('./service-account-key.json');

// Initialize with credentials
// ... your implementation
```

**⚠️ WARNING:** If using Option 2, double-check that the file is gitignored!

---

## ✅ Validation Checklist

Before committing any code:

- [ ] Service account file is named to match `.gitignore` patterns
- [ ] `git status` does NOT show the credentials file
- [ ] `git check-ignore service-account-key.json` outputs the filename
- [ ] Credentials are not hardcoded in any source files
- [ ] `.gitignore` includes service account patterns

---

## 🚨 If You Accidentally Committed Credentials

**ACT IMMEDIATELY:**

1. **Delete the key in Google Cloud Console**
   - The key is now public and must be revoked
   - Go to Service Accounts → Keys → Delete the compromised key

2. **Create a new key**
   - Follow the setup steps again with a new key

3. **Remove from Git history (Advanced)**
   ```bash
   # WARNING: This rewrites Git history
   # Coordinate with your team before running
   git filter-branch --tree-filter 'rm -f service-account-key.json' HEAD
   ```

4. **Force push (if necessary and coordinated)**
   ```bash
   # Only after team coordination
   git push --force
   ```

---

## 📚 More Information

- **Complete Security Guide:** [SERVICE_ACCOUNT_SECURITY_GUIDE.md](./SERVICE_ACCOUNT_SECURITY_GUIDE.md)
- **Main Security Policy:** [SECURITY.md](./SECURITY.md)
- **Google Cloud Docs:** [Service Account Best Practices](https://cloud.google.com/iam/docs/best-practices-service-accounts)

---

## 💡 Template File

Use `service-account-template.json` as a reference for the structure:

```bash
# Copy template to create your config
cp service-account-template.json service-account-key.json

# Edit and replace placeholder values with real credentials
# VERIFY it's gitignored before committing anything!
```

---

**Remember: Never commit service account credentials to Git!**  
**تذكر: لا تقم أبداً بإرسال بيانات اعتماد حساب الخدمة إلى Git!**
