#!/usr/bin/env node

/**
 * PR #467 Verification Test Suite
 * Tests the Smart Inspection Planning Tool implementation
 * WITHOUT area/shop management features
 */

const fs = require('fs');
const path = require('path');

// Test results
let passed = 0;
let failed = 0;

function test(name, condition) {
    if (condition) {
        console.log(`✅ PASS: ${name}`);
        passed++;
    } else {
        console.log(`❌ FAIL: ${name}`);
        failed++;
    }
}

console.log('\n🧪 PR #467 Verification Test Suite\n');
console.log('Testing Smart Inspection Planning Tool');
console.log('Expected: Inspection planning WITHOUT area/shop management\n');

// Test 1: smart-planner.html should exist
const smartPlannerPath = path.join(__dirname, 'smart-planner.html');
test('smart-planner.html exists', fs.existsSync(smartPlannerPath));

if (fs.existsSync(smartPlannerPath)) {
    const smartPlannerContent = fs.readFileSync(smartPlannerPath, 'utf8');
    
    // Test 2: Should have login functionality
    test('Has login functionality', 
        smartPlannerContent.includes('GitHub Token') && 
        smartPlannerContent.includes('loginDeveloper'));
    
    // Test 3: Should have inspector selection
    test('Has inspector selection', 
        smartPlannerContent.includes('المفتش') || 
        smartPlannerContent.includes('inspector'));
    
    // Test 4: Should have date selection
    test('Has date selection', 
        smartPlannerContent.includes('التاريخ') || 
        smartPlannerContent.includes('date'));
    
    // Test 5: Should have shift selection
    test('Has shift selection', 
        smartPlannerContent.includes('المناوبة') || 
        smartPlannerContent.includes('shift'));
    
    // Test 6: Should have area selection
    test('Has area selection', 
        smartPlannerContent.includes('المنطقة') || 
        smartPlannerContent.includes('area'));
    
    // Test 7: Should have shop filtering
    test('Has shop filtering', 
        smartPlannerContent.includes('filterSmartShops') || 
        smartPlannerContent.includes('filter'));
    
    // Test 8: Should have shop selection
    test('Has shop selection', 
        smartPlannerContent.includes('المحلات المختارة') || 
        smartPlannerContent.includes('selected'));
    
    // Test 9: Should have save functionality
    test('Has save functionality', 
        smartPlannerContent.includes('saveInspection') && 
        smartPlannerContent.includes('savePlanDataToGitHub'));
    
    // Test 10: Should have preview functionality
    test('Has preview functionality', 
        smartPlannerContent.includes('معاينة') || 
        smartPlannerContent.includes('preview'));
    
    // Test 11: Should NOT have shop management (addShop, editShop, deleteShop)
    test('Does NOT have addShop function', 
        !smartPlannerContent.includes('function addShop') && 
        !smartPlannerContent.includes('function showAddShopModal'));
    
    // Test 12: Should NOT have area management (addArea, editArea, deleteArea)
    test('Does NOT have addArea function', 
        !smartPlannerContent.includes('function addArea') && 
        !smartPlannerContent.includes('function showAddAreaModal'));
    
    // Test 13: Should NOT have shop edit functionality
    test('Does NOT have editShop function', 
        !smartPlannerContent.includes('function editShop'));
    
    // Test 14: Should NOT have shop delete functionality
    test('Does NOT have deleteShop function', 
        !smartPlannerContent.includes('function deleteShop'));
}

// Test 15: smart-panel.html should NOT exist (removed)
const smartPanelPath = path.join(__dirname, 'smart-panel.html');
test('smart-panel.html does NOT exist', !fs.existsSync(smartPanelPath));

// Test 16: SMART_PANEL_GUIDE.md should NOT exist (removed)
const smartPanelGuidePath = path.join(__dirname, 'SMART_PANEL_GUIDE.md');
test('SMART_PANEL_GUIDE.md does NOT exist', !fs.existsSync(smartPanelGuidePath));

// Test 17: SMART_PANEL_README.md should NOT exist (removed)
const smartPanelReadmePath = path.join(__dirname, 'SMART_PANEL_README.md');
test('SMART_PANEL_README.md does NOT exist', !fs.existsSync(smartPanelReadmePath));

// Test 18: test_smart_panel.html should NOT exist (removed)
const testSmartPanelPath = path.join(__dirname, 'test_smart_panel.html');
test('test_smart_panel.html does NOT exist', !fs.existsSync(testSmartPanelPath));

// Test 19: admin-dashboard.html should NOT link to smart-panel
const adminDashboardPath = path.join(__dirname, 'admin-dashboard.html');
if (fs.existsSync(adminDashboardPath)) {
    const adminDashboardContent = fs.readFileSync(adminDashboardPath, 'utf8');
    test('admin-dashboard.html does NOT link to smart-panel', 
        !adminDashboardContent.includes('smart-panel.html'));
}

// Test 20: smart-planner.html should NOT link to smart-panel
if (fs.existsSync(smartPlannerPath)) {
    const smartPlannerContent = fs.readFileSync(smartPlannerPath, 'utf8');
    test('smart-planner.html does NOT link to smart-panel', 
        !smartPlannerContent.includes('smart-panel.html'));
}

// Test 21: SMART_PLANNER_DEMO.md should exist (documentation)
const demoPath = path.join(__dirname, 'SMART_PLANNER_DEMO.md');
test('SMART_PLANNER_DEMO.md exists', fs.existsSync(demoPath));

if (fs.existsSync(demoPath)) {
    const demoContent = fs.readFileSync(demoPath, 'utf8');
    
    // Test 22: Demo should describe inspection planning
    test('Demo describes inspection planning', 
        demoContent.includes('أداة التخطيط الذكية') && 
        demoContent.includes('تسجيل الدخول') && 
        demoContent.includes('اختيار المحلات'));
}

// Test 23: Data files should exist
const shopsDetailsPath = path.join(__dirname, 'shops_details.json');
test('shops_details.json exists', fs.existsSync(shopsDetailsPath));

const planDataPath = path.join(__dirname, 'plan-data.json');
test('plan-data.json exists', fs.existsSync(planDataPath));

// Print summary
console.log('\n' + '='.repeat(50));
console.log(`\n📊 Test Results Summary:`);
console.log(`   ✅ Passed: ${passed}`);
console.log(`   ❌ Failed: ${failed}`);
console.log(`   📈 Success Rate: ${((passed / (passed + failed)) * 100).toFixed(1)}%\n`);

if (failed === 0) {
    console.log('🎉 All tests passed! PR #467 is correctly implemented.');
    console.log('   The Smart Inspection Planning Tool is ready without area/shop management.\n');
    process.exit(0);
} else {
    console.log('⚠️  Some tests failed. Please review the implementation.\n');
    process.exit(1);
}
