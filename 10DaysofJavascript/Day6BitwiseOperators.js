/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank 10 Days of Javascript
*/
function getMaxLessThanK(n, k) {
    var mx = -1;
    for(var i=1; i<=n; i++){
        for(var j=i+1; j<=n; j++){
            var res = i & j;
            if(res > mx && res < k){
                mx = res;
            }
        }
    }
    return mx;
}