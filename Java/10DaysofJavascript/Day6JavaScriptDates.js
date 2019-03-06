/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank 10 Days of Javascript
*/
function getDayName(dateString) {
    let dayName;
    const dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    dayName = dayNames[new Date(dateString).getDay()];
    return dayName;
}