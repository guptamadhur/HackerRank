/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank 10 Days of Javascript
*/

class Polygon {
    constructor(lengths) {
        this.lengths = lengths;
    }
    perimeter() {
        let sum = 0;
        this.lengths.forEach(function (len) {
            sum += len;
        });
        return sum;
    }
}