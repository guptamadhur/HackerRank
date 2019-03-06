/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank 10 Days of Javascript
*/

function reverseString(s) {
    try{
        s = s.split("").reverse().join("");
    }
    catch(e){
        console.log(e.message);
    }
    finally{
        console.log(s);
    }
}