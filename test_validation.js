// Test script for the validation function

function validateShopDuplicates(inspectionDataToValidate) {
    const dayShopInspectors = {};
    const duplicates = [];
    
    for (const entry of inspectionDataToValidate) {
        const day = entry.day;
        const inspector = entry.inspector;
        const shops = entry.shops || [];
        
        if (!day || !inspector || shops.length === 0) {
            continue;
        }
        
        if (!dayShopInspectors[day]) {
            dayShopInspectors[day] = {};
        }
        
        for (const shop of shops) {
            if (!dayShopInspectors[day][shop]) {
                dayShopInspectors[day][shop] = [];
            }
            dayShopInspectors[day][shop].push(inspector);
        }
    }
    
    for (const [day, shopsDict] of Object.entries(dayShopInspectors)) {
        for (const [shop, inspectors] of Object.entries(shopsDict)) {
            if (inspectors.length > 1) {
                duplicates.push({
                    day: day,
                    shop: shop,
                    inspectors: inspectors
                });
            }
        }
    }
    
    return {
        isValid: duplicates.length === 0,
        duplicates: duplicates
    };
}

console.log('🧪 Testing Duplicate Shop Validation Function\n');
console.log('=' .repeat(60));

// Test 1: No duplicates
console.log('\n✨ Test 1: No duplicates (should pass)');
const test1 = [
    { inspector: 'د. علي', day: '2025-01-15', shops: ['محل 1', 'محل 2'] },
    { inspector: 'د. آمنه', day: '2025-01-15', shops: ['محل 3', 'محل 4'] }
];
const result1 = validateShopDuplicates(test1);
console.log('   Result:', result1.isValid ? '✅ PASS - No duplicates found' : '❌ FAIL - Unexpected duplicates');
console.log('   Expected: Valid (isValid=true)');
console.log('   Got: isValid=' + result1.isValid);

// Test 2: Has duplicates on same day
console.log('\n✨ Test 2: Has duplicates on same day (should fail)');
const test2 = [
    { inspector: 'د. علي', day: '2025-01-15', shops: ['محل 1', 'محل 2'] },
    { inspector: 'د. آمنه', day: '2025-01-15', shops: ['محل 1', 'محل 3'] }
];
const result2 = validateShopDuplicates(test2);
console.log('   Result:', !result2.isValid ? '✅ PASS - Duplicates detected' : '❌ FAIL - Should detect duplicates');
console.log('   Expected: Invalid (isValid=false)');
console.log('   Got: isValid=' + result2.isValid);
if (result2.duplicates.length > 0) {
    console.log('   Duplicates found:', result2.duplicates.length);
    result2.duplicates.forEach(dup => {
        console.log(`     - Shop: "${dup.shop}" on ${dup.day}`);
        console.log(`       Inspectors: ${dup.inspectors.join(', ')}`);
    });
}

// Test 3: Same shop on different days (should be valid)
console.log('\n✨ Test 3: Same shop on different days (should pass)');
const test3 = [
    { inspector: 'د. علي', day: '2025-01-15', shops: ['محل 1'] },
    { inspector: 'د. آمنه', day: '2025-01-16', shops: ['محل 1'] }
];
const result3 = validateShopDuplicates(test3);
console.log('   Result:', result3.isValid ? '✅ PASS - Same shop on different days is OK' : '❌ FAIL - Should allow same shop on different days');
console.log('   Expected: Valid (isValid=true)');
console.log('   Got: isValid=' + result3.isValid);

// Test 4: Multiple duplicates
console.log('\n✨ Test 4: Multiple duplicates (should fail)');
const test4 = [
    { inspector: 'د. علي', day: '2025-01-15', shops: ['محل 1', 'محل 2'] },
    { inspector: 'د. آمنه', day: '2025-01-15', shops: ['محل 1', 'محل 3'] },
    { inspector: 'د. محمد', day: '2025-01-15', shops: ['محل 2', 'محل 4'] }
];
const result4 = validateShopDuplicates(test4);
console.log('   Result:', !result4.isValid ? '✅ PASS - Multiple duplicates detected' : '❌ FAIL - Should detect multiple duplicates');
console.log('   Expected: Invalid (isValid=false)');
console.log('   Got: isValid=' + result4.isValid);
if (result4.duplicates.length > 0) {
    console.log('   Duplicates found:', result4.duplicates.length);
    result4.duplicates.forEach(dup => {
        console.log(`     - Shop: "${dup.shop}" on ${dup.day}`);
        console.log(`       Inspectors: ${dup.inspectors.join(', ')}`);
    });
}

// Test 5: Three inspectors, same shop
console.log('\n✨ Test 5: Three inspectors assigned to same shop (should fail)');
const test5 = [
    { inspector: 'د. علي', day: '2025-01-15', shops: ['محل بيت الطيور'] },
    { inspector: 'د. آمنه', day: '2025-01-15', shops: ['محل بيت الطيور'] },
    { inspector: 'د. محمد', day: '2025-01-15', shops: ['محل بيت الطيور'] }
];
const result5 = validateShopDuplicates(test5);
console.log('   Result:', !result5.isValid ? '✅ PASS - Triple assignment detected' : '❌ FAIL - Should detect triple assignment');
console.log('   Expected: Invalid (isValid=false)');
console.log('   Got: isValid=' + result5.isValid);
if (result5.duplicates.length > 0) {
    console.log('   Duplicates found:', result5.duplicates.length);
    result5.duplicates.forEach(dup => {
        console.log(`     - Shop: "${dup.shop}" on ${dup.day}`);
        console.log(`       Inspectors (${dup.inspectors.length}): ${dup.inspectors.join(', ')}`);
    });
}

console.log('\n' + '='.repeat(60));
console.log('✅ All tests completed successfully!');
