#!/bin/bash

# Google Maps API Setup Verification Script
# سكريبت التحقق من إعداد Google Maps API

echo "======================================================================"
echo "  Google Maps API Setup Verification"
echo "  التحقق من إعداد Google Maps API"
echo "======================================================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if google-maps-config.local.js exists
echo -e "${BLUE}[1/5]${NC} Checking if google-maps-config.local.js exists..."
echo -e "${BLUE}[1/5]${NC} التحقق من وجود ملف google-maps-config.local.js..."

if [ ! -f "google-maps-config.local.js" ]; then
    echo -e "${RED}❌ File not found! / الملف غير موجود!${NC}"
    echo ""
    echo "Please create google-maps-config.local.js first."
    echo "الرجاء إنشاء ملف google-maps-config.local.js أولاً."
    exit 1
else
    echo -e "${GREEN}✅ File exists / الملف موجود${NC}"
fi

echo ""

# Check if API key is set
echo -e "${BLUE}[2/5]${NC} Checking API key configuration..."
echo -e "${BLUE}[2/5]${NC} التحقق من إعدادات مفتاح API..."

API_KEY=$(grep "GOOGLE_MAPS_API_KEY = " google-maps-config.local.js | head -1 | sed "s/.*= '\(.*\)';/\1/")

if [ -z "$API_KEY" ]; then
    echo -e "${RED}❌ API key not found! / مفتاح API غير موجود!${NC}"
    exit 1
elif [ "$API_KEY" = "YOUR_NEW_API_KEY_FROM_GOOGLE_CLOUD" ]; then
    echo -e "${RED}❌ API key is still placeholder! / مفتاح API ما زال قيمة افتراضية!${NC}"
    echo ""
    echo "You need to replace the placeholder with your actual API key."
    echo "تحتاج إلى استبدال القيمة الافتراضية بمفتاح API الفعلي."
    echo ""
    echo "Steps / الخطوات:"
    echo "1. Open setup-google-maps-api.html in browser"
    echo "   افتح setup-google-maps-api.html في المتصفح"
    echo "2. Follow the instructions to get your API key"
    echo "   اتبع التعليمات للحصول على مفتاح API"
    echo "3. Update google-maps-config.local.js"
    echo "   حدّث ملف google-maps-config.local.js"
    exit 1
elif [[ ! "$API_KEY" =~ ^AIza ]]; then
    echo -e "${RED}❌ API key format invalid! / تنسيق مفتاح API غير صالح!${NC}"
    echo ""
    echo "Google Maps API keys should start with 'AIza'"
    echo "مفاتيح Google Maps API يجب أن تبدأ بـ 'AIza'"
    exit 1
elif [ ${#API_KEY} -lt 30 ]; then
    echo -e "${RED}❌ API key too short! / مفتاح API قصير جداً!${NC}"
    exit 1
else
    echo -e "${GREEN}✅ API key format looks valid / تنسيق مفتاح API يبدو صالحاً${NC}"
    echo "   Key: ${API_KEY:0:20}..."
fi

echo ""

# Check if both occurrences are the same
echo -e "${BLUE}[3/5]${NC} Checking API key consistency..."
echo -e "${BLUE}[3/5]${NC} التحقق من اتساق مفتاح API..."

API_KEY_WINDOW=$(grep "window.GOOGLE_MAPS_API_KEY = " google-maps-config.local.js | sed "s/.*= '\(.*\)';/\1/")

if [ "$API_KEY" != "$API_KEY_WINDOW" ]; then
    echo -e "${YELLOW}⚠️  Warning: API keys don't match! / تحذير: مفاتيح API غير متطابقة!${NC}"
    echo "   Line ~81: $API_KEY"
    echo "   Line ~87: $API_KEY_WINDOW"
    echo ""
    echo "Please make sure both occurrences use the same API key."
    echo "الرجاء التأكد من أن كلا الموضعين يستخدمان نفس مفتاح API."
else
    echo -e "${GREEN}✅ API keys match / مفاتيح API متطابقة${NC}"
fi

echo ""

# Check if required files exist
echo -e "${BLUE}[4/5]${NC} Checking required files..."
echo -e "${BLUE}[4/5]${NC} التحقق من الملفات المطلوبة..."

REQUIRED_FILES=("google-maps-config.js" "google-maps-loader.js" "smart-planner.html")
ALL_FILES_EXIST=true

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "   ${GREEN}✅${NC} $file"
    else
        echo -e "   ${RED}❌${NC} $file (missing / مفقود)"
        ALL_FILES_EXIST=false
    fi
done

if [ "$ALL_FILES_EXIST" = false ]; then
    echo -e "${RED}❌ Some required files are missing! / بعض الملفات المطلوبة مفقودة!${NC}"
    exit 1
fi

echo ""

# Check project configuration
echo -e "${BLUE}[5/5]${NC} Checking project configuration..."
echo -e "${BLUE}[5/5]${NC} التحقق من إعدادات المشروع..."

if grep -q "monthly-insection-plan" google-maps-config.js; then
    echo -e "${GREEN}✅ Project configuration found / إعدادات المشروع موجودة${NC}"
else
    echo -e "${YELLOW}⚠️  Project configuration not found in comments / إعدادات المشروع غير موجودة في التعليقات${NC}"
fi

echo ""
echo "======================================================================"
echo -e "${GREEN}✅ Setup verification complete! / اكتمل التحقق من الإعداد!${NC}"
echo "======================================================================"
echo ""
echo "Next steps / الخطوات التالية:"
echo ""
echo "1. Open smart-planner.html in your browser"
echo "   افتح smart-planner.html في المتصفح"
echo ""
echo "2. Press Ctrl+Shift+R (hard reload) to clear cache"
echo "   اضغط Ctrl+Shift+R (إعادة تحميل كاملة) لمسح الذاكرة المؤقتة"
echo ""
echo "3. Open Developer Tools (F12) and check Console"
echo "   افتح أدوات المطور (F12) وتحقق من Console"
echo ""
echo "4. You should see: ✅ Google Maps API loaded successfully"
echo "   يجب أن ترى: ✅ تم تحميل Google Maps API بنجاح"
echo ""
echo "======================================================================"
echo ""
echo "For complete setup instructions, see:"
echo "للحصول على تعليمات الإعداد الكاملة، انظر:"
echo "  • GOOGLE_MAPS_SETUP_GUIDE_AR.md"
echo "  • setup-google-maps-api.html"
echo ""
echo "======================================================================"
