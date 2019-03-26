/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank 10 Days of Javascript
*/

function getCount(objects) {
    return objects.filter(function(o){
        return o.x == o.y;
    }).length;
}