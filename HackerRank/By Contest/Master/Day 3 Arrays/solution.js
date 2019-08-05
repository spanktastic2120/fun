

/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    let largest = 0
    let second = 0
    for (let n of nums) {
        if (n > largest) {
            second = largest
            largest = n
        }
        else if (n > second && n < largest) {
            second = n
        }
    }
    return second
}

