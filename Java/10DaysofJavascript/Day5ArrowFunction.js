/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank 10 Days of Javascript
*/

function modifyArray(nums) {
    nums = nums.map((num) => (num%2==1? 3:2) * num);
    return nums;
}