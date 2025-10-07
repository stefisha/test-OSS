// problematic.js
// Issue 1: Unused variable 'temp'
// Issue 2: Logic error in condition

function checkEven(num) {
    let temp = num % 2; // Unused variable
    // Should return true if num is even, but always returns false
    if (num % 2 === 1) {
        return true;
    } else {
        return false;
    }
}