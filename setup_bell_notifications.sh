#!/bin/bash
# Setup script for Bell Notifications Auto-Push System
# نصية إعداد نظام رفع إشعارات الجرس التلقائي

echo "============================================================"
echo "🔔 Bell Notifications Auto-Push Setup"
echo "إعداد نظام رفع إشعارات الجرس التلقائي"
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

# Check if Python is installed
print_status "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    print_success "Python found: $PYTHON_VERSION"
else
    print_error "Python 3 is not installed. Please install Python 3.6 or higher."
    exit 1
fi

# Check if pip is installed
print_status "Checking pip installation..."
if command -v pip3 &> /dev/null || command -v pip &> /dev/null; then
    print_success "pip is available"
else
    print_error "pip is not installed. Please install pip."
    exit 1
fi

# Install watchdog library
print_status "Installing watchdog library..."
if pip3 install watchdog 2>/dev/null || pip install watchdog 2>/dev/null; then
    print_success "watchdog library installed successfully"
else
    print_warning "Failed to install watchdog globally, trying user installation..."
    if pip3 install --user watchdog 2>/dev/null || pip install --user watchdog 2>/dev/null; then
        print_success "watchdog library installed for user"
    else
        print_error "Failed to install watchdog library"
        exit 1
    fi
fi

# Test watchdog import
print_status "Testing watchdog library..."
if python3 -c "import watchdog; print('watchdog imported successfully')" 2>/dev/null; then
    print_success "watchdog library is working correctly"
else
    print_error "watchdog library is not working properly"
    exit 1
fi

# Check Git installation
print_status "Checking Git installation..."
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version 2>&1)
    print_success "Git found: $GIT_VERSION"
else
    print_error "Git is not installed. Please install Git."
    exit 1
fi

# Check if we're in a Git repository
print_status "Checking Git repository..."
if git rev-parse --git-dir > /dev/null 2>&1; then
    print_success "Current directory is a Git repository"
else
    print_error "Current directory is not a Git repository"
    exit 1
fi

# Check Git configuration
print_status "Checking Git configuration..."
if git config user.name > /dev/null 2>&1 && git config user.email > /dev/null 2>&1; then
    USER_NAME=$(git config user.name)
    USER_EMAIL=$(git config user.email)
    print_success "Git user configured: $USER_NAME <$USER_EMAIL>"
else
    print_warning "Git user not configured. Setting up default configuration..."
    git config user.name "Monthly Inspection System"
    git config user.email "monthly-inspection@system.local"
    print_success "Default Git configuration set"
fi

# Check remote origin
print_status "Checking remote repository..."
if git remote get-url origin > /dev/null 2>&1; then
    REMOTE_URL=$(git remote get-url origin)
    print_success "Remote origin configured: $REMOTE_URL"
else
    print_error "No remote origin configured"
    exit 1
fi

# Check if plan-data.json exists
print_status "Checking plan-data.json file..."
if [ -f "plan-data.json" ]; then
    print_success "plan-data.json file found"
else
    print_warning "plan-data.json file not found, but system will monitor when created"
fi

# Test auto-push script
print_status "Testing auto-push script..."
if [ -f "auto_push_on_change.py" ]; then
    print_success "auto_push_on_change.py script found"
    
    # Test script syntax
    if python3 -m py_compile auto_push_on_change.py 2>/dev/null; then
        print_success "auto_push_on_change.py script syntax is valid"
    else
        print_error "auto_push_on_change.py script has syntax errors"
        exit 1
    fi
else
    print_error "auto_push_on_change.py script not found"
    exit 1
fi

echo ""
echo "============================================================"
print_success "Setup completed successfully!"
echo "============================================================"
echo ""
echo "📋 Next steps:"
echo "1. Run the auto-push script:"
echo "   python3 auto_push_on_change.py"
echo ""
echo "2. In the background (Linux/Mac):"
echo "   nohup python3 auto_push_on_change.py &"
echo ""
echo "3. In the background (Windows):"
echo "   start python3 auto_push_on_change.py"
echo ""
echo "4. The script will automatically:"
echo "   - Monitor plan-data.json for changes"
echo "   - Detect the current Git branch"
echo "   - Commit and push changes to GitHub"
echo ""
echo "🔔 Bell notifications will now sync automatically to GitHub!"
echo "إشعارات الجرس ستتم مزامنتها تلقائياً مع GitHub!"