/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank 10 Days of Javascript
*/

function getGrade(score) {
    let grade;
    if(score>25 && score<=30){
        grade= 'A';
    }
    else if(score>20 && score<=25){
        grade= 'B';
    }
    else if(score>15 && score<=20){
        grade= 'C';
    }
    else if(score>10 && score<=15){
        grade= 'D';
    }
    else if(score>5 && score<=10){
        grade= 'E';
    }
    else{
        grade= 'F';
    }
    return grade;
}