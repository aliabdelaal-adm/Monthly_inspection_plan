// Simple Node.js test for smart panel
const fs = require('fs');
const path = require('path');

console.log('🧪 Running Smart Panel Tests...\n');

// Test 1: Check if smart-panel.html exists
console.log('Test 1: File Existence');
const smartPanelPath = path.join(__dirname, 'smart-panel.html');
if (fs.existsSync(smartPanelPath)) {
    console.log('✅ smart-panel.html exists');
    const stats = fs.statSync(smartPanelPath);
    console.log(`   File size: ${stats.size} bytes`);
} else {
    console.log('❌ smart-panel.html not found');
}

// Test 2: Check if shops_details.json exists
console.log('\nTest 2: Data Files');
const shopsPath = path.join(__dirname, 'shops_details.json');
if (fs.existsSync(shopsPath)) {
    console.log('✅ shops_details.json exists');
    try {
        const shopsData = JSON.parse(fs.readFileSync(shopsPath, 'utf8'));
        const shopCount = Object.keys(shopsData).length;
        console.log(`   Found ${shopCount} shops`);
    } catch (error) {
        console.log(`❌ Error parsing shops_details.json: ${error.message}`);
    }
} else {
    console.log('❌ shops_details.json not found');
}

// Test 3: Check plan-data.json
const planPath = path.join(__dirname, 'plan-data.json');
if (fs.existsSync(planPath)) {
    console.log('✅ plan-data.json exists');
    try {
        const planData = JSON.parse(fs.readFileSync(planPath, 'utf8'));
        if (planData.inspectionData) {
            console.log(`   Found ${planData.inspectionData.length} inspections`);
        }
    } catch (error) {
        console.log(`❌ Error parsing plan-data.json: ${error.message}`);
    }
} else {
    console.log('❌ plan-data.json not found');
}

// Test 4: Check smart-panel.html content
console.log('\nTest 3: HTML Content Validation');
const htmlContent = fs.readFileSync(smartPanelPath, 'utf8');

const requiredElements = [
    { name: 'Overview Tab', pattern: 'id="overview"' },
    { name: 'Shops Tab', pattern: 'id="shops"' },
    { name: 'Areas Tab', pattern: 'id="areas"' },
    { name: 'Mapping Tab', pattern: 'id="mapping"' },
    { name: 'Save Shop Function', pattern: 'function saveShop()' },
    { name: 'Delete Shop Function', pattern: 'function deleteShop(' },
    { name: 'Filter Function', pattern: 'function filterShopsTable()' },
    { name: 'GitHub Save Function', pattern: 'saveShopsData()' },
];

requiredElements.forEach(element => {
    if (htmlContent.includes(element.pattern)) {
        console.log(`✅ ${element.name} found`);
    } else {
        console.log(`❌ ${element.name} missing`);
    }
});

// Test 5: Check documentation
console.log('\nTest 4: Documentation');
const guidePath = path.join(__dirname, 'SMART_PANEL_GUIDE.md');
if (fs.existsSync(guidePath)) {
    console.log('✅ SMART_PANEL_GUIDE.md exists');
    const guideSize = fs.statSync(guidePath).size;
    console.log(`   Documentation size: ${guideSize} bytes`);
} else {
    console.log('❌ SMART_PANEL_GUIDE.md not found');
}

// Test 6: Check integration in other files
console.log('\nTest 5: Integration Links');
const adminDashPath = path.join(__dirname, 'admin-dashboard.html');
if (fs.existsSync(adminDashPath)) {
    const adminContent = fs.readFileSync(adminDashPath, 'utf8');
    if (adminContent.includes('smart-panel.html')) {
        console.log('✅ Smart panel link found in admin-dashboard.html');
    } else {
        console.log('❌ Smart panel link not found in admin-dashboard.html');
    }
}

const smartPlannerPath = path.join(__dirname, 'smart-planner.html');
if (fs.existsSync(smartPlannerPath)) {
    const plannerContent = fs.readFileSync(smartPlannerPath, 'utf8');
    if (plannerContent.includes('smart-panel.html')) {
        console.log('✅ Smart panel link found in smart-planner.html');
    } else {
        console.log('❌ Smart panel link not found in smart-planner.html');
    }
}

console.log('\n✨ Tests completed!\n');
