/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank 10 Days of Javascript
*/

function getSecondLargest(nums) {
    var max = Math.max.apply(null, nums);
    var maxI = nums.indexOf(max);
    nums[maxI] = -Infinity;
    // getting the second maximum value (if the maximum is duplicated)
    while (max == Math.max.apply(null, nums)) {
        var max = Math.max.apply(null, nums);
        var maxI = nums.indexOf(max);
        nums[maxI] = -Infinity;
    }
    // returning the second maximum value
    return Math.max.apply(null, nums);
}