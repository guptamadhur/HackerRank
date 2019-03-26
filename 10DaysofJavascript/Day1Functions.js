/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank 10 Days of Javascript
*/

function factorial(num){
    if(num==1){
        return 1;
    }
    else{
        var fact= 1;
        for(var i=num; i>1; i--){
            fact= fact*i;
        }
        return fact;
    }
}