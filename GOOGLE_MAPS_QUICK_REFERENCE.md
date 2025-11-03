# 🗺️ Google Maps - Quick Reference Card
# 🗺️ خرائط جوجل - بطاقة مرجعية سريعة

---

## ⚡ Quick Setup (5 Minutes)
## ⚡ إعداد سريع (5 دقائق)

### Step 1: Get API Key
1. Go to: https://console.cloud.google.com/
2. Create project → Enable billing
3. Enable: Maps JavaScript API, Places API, Geocoding API
4. Create API key → Copy it

### Step 2: Configure
1. Open `google-maps-config.js`
2. Replace `YOUR_GOOGLE_MAPS_API_KEY_HERE` with your key
3. Save file

### Step 3: Test
1. Open `test_google_maps_api_key.html`
2. All green = ✅ Working!

---

## 🎯 Usage in Smart Planner
## 🎯 الاستخدام في المخطط الذكي

1. **Load Data** → Wait for "✅ خرائط جوجل جاهزة"
2. **Click Button** → "إضافة تفتيش من الخريطة"
3. **Select Shops** → Click markers on map
4. **Add to Plan** → Click "إضافة المحلات المختارة"

---

## 🔍 Status Indicators
## 🔍 مؤشرات الحالة

| Icon | Status | Meaning |
|------|--------|---------|
| ⏳ | Loading | Please wait... |
| ✅ | Ready | You can use maps! |
| ❌ | Error | Click for help |

---

## 🐛 Quick Fixes
## 🐛 إصلاحات سريعة

### Map won't load?
1. Check internet connection
2. Verify API key in `google-maps-config.js`
3. Enable billing in Google Cloud
4. Clear browser cache (Ctrl+Shift+Delete)

### "This page can't load Google Maps"?
→ Billing not enabled. Go to Google Cloud Console → Billing

### "RefererNotAllowedMapError"?
→ Add your domain to API key restrictions

### Still not working?
→ Open Console (F12) and check errors

---

## 💰 Pricing (Don't Worry!)
## 💰 التسعير (لا تقلق!)

- **$200 FREE per month** from Google
- Covers ~28,000 map loads
- Most apps stay in free tier
- Set billing alerts for safety

---

## 🔒 Security Checklist
## 🔒 قائمة الأمان

- [ ] API key is set in config file
- [ ] Billing is enabled
- [ ] Required APIs are enabled (3 APIs)
- [ ] Domain restrictions are set
- [ ] Billing alerts are configured

---

## 📞 Need Help?
## 📞 تحتاج مساعدة؟

1. **Read:** [GOOGLE_MAPS_API_SETUP_GUIDE.md](GOOGLE_MAPS_API_SETUP_GUIDE.md)
2. **Test:** Open `test_google_maps_api_key.html`
3. **Debug:** Press F12 → Check Console tab
4. **Ask:** Contact developer with screenshots + console errors

---

## 🎁 Cool Features
## 🎁 ميزات رائعة

✨ **Auto-retry:** Tries 5 times if loading fails
✨ **Smart errors:** Shows why it failed + how to fix
✨ **Visual feedback:** Always know what's happening
✨ **Nearby shops:** Find shops within 2km radius
✨ **Priority filter:** One-click high-priority selection

---

## 📁 Important Files
## 📁 ملفات مهمة

```
📄 google-maps-config.js          → Put API key here!
📄 google-maps-loader.js          → Handles loading
📄 smart-planner.html             → Main app
📄 test_google_maps_api_key.html  → Test your key
📖 GOOGLE_MAPS_API_SETUP_GUIDE.md → Full guide
```

---

## 🚦 Status Messages
## 🚦 رسائل الحالة

| Arabic | English | Action |
|--------|---------|--------|
| جاري تحميل خرائط جوجل | Loading Google Maps | Wait |
| خرائط جوجل جاهزة | Google Maps Ready | Ready! |
| فشل تحميل الخرائط | Failed to load maps | Click for help |
| محاولة 1/5 | Retry 1/5 | System retrying |

---

## ⚡ Performance Tips
## ⚡ نصائح للأداء

1. **Wait for ready indicator** before using maps
2. **Select nearby shops** for efficient routes
3. **Use area filters** to reduce map clutter
4. **Save coordinates** in shops_details.json

---

## 🎯 Common Tasks
## 🎯 المهام الشائعة

### Add inspection from map:
1. Click map button
2. Select shops on map
3. Click "إضافة المحلات المختارة"

### Find nearby shops:
1. Select one shop first
2. Click "اختيار المحلات المتقاربة"
3. Auto-selects shops within 2km

### Filter by priority:
1. Click "اختيار الأولوية العالية"
2. All high-priority shops selected

---

## 🔧 Configuration Quick Ref
## 🔧 مرجع سريع للتكوين

```javascript
// In google-maps-config.js:

apiKey: 'YOUR_KEY_HERE',          // ← Put your key here!
language: 'ar',                   // Arabic
region: 'AE',                     // UAE
nearbyRadius: 2000,               // 2km for nearby shops
maxRetryAttempts: 5,              // Retry 5 times
retryDelay: 2000,                 // 2 seconds between retries
```

---

## ✅ Success Checklist
## ✅ قائمة النجاح

After setup, verify:
- [ ] Green "✅ خرائط جوجل جاهزة" indicator
- [ ] Can click "إضافة تفتيش من الخريطة" button
- [ ] Map opens in modal
- [ ] Can see Abu Dhabi on map
- [ ] Markers appear for shops
- [ ] Can click markers for details
- [ ] Can select shops
- [ ] No console errors (F12)

---

## 🎓 Learn More
## 🎓 تعلم المزيد

- Full Setup: [GOOGLE_MAPS_API_SETUP_GUIDE.md](GOOGLE_MAPS_API_SETUP_GUIDE.md)
- Integration Details: [GOOGLE_MAPS_INTEGRATION_README.md](GOOGLE_MAPS_INTEGRATION_README.md)
- Google Docs: https://developers.google.com/maps

---

**Version:** 1.0.0
**Updated:** November 3, 2025

**Remember:** If you see ✅ green status, everything works! 🎉
**تذكر:** إذا رأيت حالة خضراء ✅، كل شيء يعمل! 🎉
