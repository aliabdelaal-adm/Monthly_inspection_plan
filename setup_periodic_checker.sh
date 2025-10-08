#!/bin/bash
# Setup script for Periodic Error Checker
# سكريبت إعداد مدقق الأخطاء الدوري

echo "============================================================"
echo "🕐 Periodic Error Checker Setup"
echo "إعداد مدقق الأخطاء الدوري"
echo "============================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Get the absolute path of the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHECKER_SCRIPT="$SCRIPT_DIR/periodic_error_checker.py"

# Check if Python is installed
print_status "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    print_success "Python found: $PYTHON_VERSION"
else
    print_error "Python 3 is not installed. Please install Python 3.6 or higher."
    exit 1
fi

# Check if the checker script exists
print_status "Checking periodic_error_checker.py script..."
if [ -f "$CHECKER_SCRIPT" ]; then
    print_success "periodic_error_checker.py script found"
    
    # Make it executable
    chmod +x "$CHECKER_SCRIPT"
    print_success "Made script executable"
else
    print_error "periodic_error_checker.py script not found"
    exit 1
fi

# Create logs directory
print_status "Creating logs directory..."
mkdir -p "$SCRIPT_DIR/logs/error_checker"
print_success "Logs directory created at: $SCRIPT_DIR/logs/error_checker"

# Test the script
print_status "Testing the error checker script..."
if cd "$SCRIPT_DIR" && python3 "$CHECKER_SCRIPT"; then
    print_success "Error checker script test passed"
else
    print_warning "Error checker script test found issues (this is normal if there are errors in the data)"
fi

echo ""
echo "============================================================"
echo "📋 Schedule Setup Options / خيارات جدولة التشغيل"
echo "============================================================"
echo ""
echo "Choose your preferred scheduling method:"
echo "اختر طريقة الجدولة المفضلة:"
echo ""
echo "1. Cron (Linux/Mac) - للينكس/ماك"
echo "2. Systemd Timer (Linux) - للينكس"
echo "3. Manual/Skip - يدوي/تخطي"
echo ""
read -p "Enter your choice (1-3): " CHOICE

case $CHOICE in
    1)
        print_status "Setting up Cron job..."
        
        # Create cron job entry
        CRON_ENTRY="0 1 * * * cd $SCRIPT_DIR && /usr/bin/python3 $CHECKER_SCRIPT >> $SCRIPT_DIR/logs/error_checker/cron.log 2>&1"
        
        # Check if cron job already exists
        if crontab -l 2>/dev/null | grep -q "periodic_error_checker.py"; then
            print_warning "Cron job already exists. Updating..."
            (crontab -l 2>/dev/null | grep -v "periodic_error_checker.py"; echo "$CRON_ENTRY") | crontab -
        else
            (crontab -l 2>/dev/null; echo "$CRON_ENTRY") | crontab -
        fi
        
        print_success "Cron job added successfully!"
        echo ""
        echo "📋 Cron job details:"
        echo "   - Runs daily at 1:00 AM"
        echo "   - يعمل يومياً في الساعة 1:00 صباحاً"
        echo ""
        echo "To view your cron jobs: crontab -l"
        echo "To remove the cron job: crontab -e (then delete the line)"
        ;;
    
    2)
        print_status "Setting up Systemd Timer..."
        
        # Create systemd service file
        SERVICE_FILE="/etc/systemd/system/periodic-error-checker.service"
        TIMER_FILE="/etc/systemd/system/periodic-error-checker.timer"
        
        print_status "Creating systemd service file..."
        sudo tee "$SERVICE_FILE" > /dev/null <<EOF
[Unit]
Description=Periodic Error Checker for Inspection Plan
After=network.target

[Service]
Type=oneshot
WorkingDirectory=$SCRIPT_DIR
ExecStart=/usr/bin/python3 $CHECKER_SCRIPT
StandardOutput=append:$SCRIPT_DIR/logs/error_checker/systemd.log
StandardError=append:$SCRIPT_DIR/logs/error_checker/systemd.log

[Install]
WantedBy=multi-user.target
EOF
        
        print_status "Creating systemd timer file..."
        sudo tee "$TIMER_FILE" > /dev/null <<EOF
[Unit]
Description=Timer for Periodic Error Checker
Requires=periodic-error-checker.service

[Timer]
OnCalendar=*-*-* 01:00:00
Persistent=true

[Install]
WantedBy=timers.target
EOF
        
        # Enable and start the timer
        print_status "Enabling and starting the timer..."
        sudo systemctl daemon-reload
        sudo systemctl enable periodic-error-checker.timer
        sudo systemctl start periodic-error-checker.timer
        
        print_success "Systemd timer configured successfully!"
        echo ""
        echo "📋 Timer details:"
        echo "   - Runs daily at 1:00 AM"
        echo "   - يعمل يومياً في الساعة 1:00 صباحاً"
        echo ""
        echo "Useful commands:"
        echo "   Check timer status: sudo systemctl status periodic-error-checker.timer"
        echo "   View logs: sudo journalctl -u periodic-error-checker.service"
        echo "   Stop timer: sudo systemctl stop periodic-error-checker.timer"
        echo "   Disable timer: sudo systemctl disable periodic-error-checker.timer"
        ;;
    
    3)
        print_status "Skipping automatic scheduling"
        echo ""
        echo "📋 Manual execution:"
        echo "   To run the checker manually:"
        echo "   cd $SCRIPT_DIR && python3 $CHECKER_SCRIPT"
        echo ""
        echo "   لتشغيل المدقق يدوياً:"
        echo "   cd $SCRIPT_DIR && python3 $CHECKER_SCRIPT"
        ;;
    
    *)
        print_error "Invalid choice. Skipping scheduling."
        ;;
esac

echo ""
echo "============================================================"
print_success "Setup completed!"
echo "============================================================"
echo ""
echo "📁 Log files location: $SCRIPT_DIR/logs/error_checker/"
echo "📁 موقع ملفات السجلات: $SCRIPT_DIR/logs/error_checker/"
echo ""
echo "🔍 The error checker will:"
echo "   - Validate shop duplicate assignments"
echo "   - Check data completeness"
echo "   - Generate detailed logs"
echo "   - Run automatically at 1:00 AM daily"
echo ""
echo "🔍 مدقق الأخطاء سيقوم بـ:"
echo "   - التحقق من تكرارات المحلات"
echo "   - فحص اكتمال البيانات"
echo "   - إنشاء سجلات مفصلة"
echo "   - التشغيل التلقائي يومياً في الساعة 1:00 صباحاً"
echo ""
