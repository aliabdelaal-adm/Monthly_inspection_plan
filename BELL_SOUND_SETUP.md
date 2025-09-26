# تعليمات إضافة الملف الصوتي المخصص للجرس
# Custom Bell Sound Setup Instructions

## نظرة عامة / Overview
تم تحديث نظام الجرس ليستخدم ملف صوتي خارجي بدلاً من الصوت المدمج في النظام. إذا لم يوجد الملف، سيتم استخدام صوت عصافير محسن مولد تلقائياً.

The bell system has been updated to use an external audio file instead of the embedded sound. If the file is not found, an enhanced synthetic bird sound will be used as fallback.

## الخطوات المطلوبة / Required Steps

### 1. تحضير الملف الصوتي / Prepare Audio File
- احصل على ملف صوتي لأصوات العصافير بصيغة MP3 (متوفر في الرابط أدناه)
- تأكد من أن الملف بجودة جيدة وحجم مناسب (يُفضل أقل من 1 ميجابايت)
- يُفضل أن يكون طول الصوت بين 2-5 ثواني لتجربة مستخدم أفضل
- Get a bird song audio file in MP3 format (available in the link below)
- Ensure the file is good quality and reasonable size (preferably under 1MB)
- Ideally 2-5 seconds duration for better user experience

### 2. تسمية الملف / File Naming
- أعد تسمية الملف الصوتي إلى: `bell_sound.mp3`
- Rename your audio file to: `bell_sound.mp3`

### 3. رفع الملف / Upload File
- ضع الملف `bell_sound.mp3` في نفس المجلد الذي يحتوي على ملف `index.html`
- Place the `bell_sound.mp3` file in the same directory as the `index.html` file

### 4. اختبار الصوت / Test Audio
- افتح الموقع في المتصفح
- اضغط على أيقونة الجرس لاختبار الصوت
- Open the website in your browser
- Click the bell icon to test the sound

## تحميل الملف من Google Drive / Download from Google Drive

لتحميل الملف من Google Drive:
1. افتح الرابط: https://drive.google.com/file/d/1AUE1ypm81NTFsEIy4MiqCCKAopVVwqua/view?usp=drivesdk
2. اضغط على زر "تحميل" أو "Download"
3. احفظ الملف باسم `bell_sound.mp3`
4. ضع الملف في مجلد الموقع

To download from Google Drive:
1. Open the link: https://drive.google.com/file/d/1AUE1ypm81NTFsEIy4MiqCCKAopVVwqua/view?usp=drivesdk
2. Click the "Download" button
3. Save the file as `bell_sound.mp3`
4. Place the file in the website directory

## استكشاف الأخطاء / Troubleshooting

### الصوت لا يعمل / Sound Not Working
- تأكد من وجود الملف `bell_sound.mp3` في المجلد الصحيح
- تأكد من أن اسم الملف صحيح تماماً
- تحقق من أن صيغة الملف MP3
- جرب تحديث الصفحة (F5)

- Make sure `bell_sound.mp3` exists in the correct directory
- Verify the filename is exactly correct
- Check that the file format is MP3
- Try refreshing the page (F5)

### مشاكل أخرى / Other Issues
- تأكد من أن المتصفح يدعم تشغيل ملفات MP3
- تحقق من إعدادات الصوت في المتصفح
- جرب متصفح آخر للاختبار
- إذا لم يعمل الملف الخارجي، سيتم تشغيل صوت عصافير محسن تلقائياً

- Ensure your browser supports MP3 playback
- Check browser audio settings
- Try a different browser for testing
- If external file doesn't work, enhanced synthetic bird sound will play automatically

## هيكل الملفات المطلوب / Required File Structure
```
Monthly_inspection_plan/
├── index.html
├── bell_sound.mp3    ← الملف الصوتي الجديد (ملف أصوات العصافير)
├── admin.html
├── plan-data.json
└── ... (ملفات أخرى)
```

## ملاحظات مهمة / Important Notes
- حجم الملف الصوتي يؤثر على سرعة تحميل الموقع
- يُنصح بملفات أقل من 1 ميجابايت
- الصوت سيتوقف تلقائياً بعد 10 ثواني
- يمكن تشغيل الصوت مرة واحدة كل ثانية لتجنب التكرار السريع
- تم تحسين الصوت الاحتياطي ليبدو مثل أصوات العصافير الطبيعية

- Audio file size affects website loading speed
- Files under 1MB are recommended
- Sound will automatically stop after 10 seconds
- Sound can only be played once per second to prevent spam
- Fallback sound has been enhanced to sound like natural bird songs

## التحديثات الأخيرة / Recent Updates
- ✅ تم إضافة مصدر الصوت لعنصر الصوت في HTML
- ✅ تم تحسين صوت العصافير الاحتياطي بشكل كبير ليبدو طبيعياً
- ✅ تم تحسين معالجة الأخطاء والرسائل التوضيحية
- ✅ إزالة الضوضاء الخلفية من الصوت الاصطناعي

- ✅ Added audio source to HTML audio element
- ✅ Significantly enhanced fallback bird sound to sound natural
- ✅ Improved error handling and user messages
- ✅ Eliminated background noise from synthetic audio