/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank Practice Java
*/

package String;

import java.util.Scanner;

public class JavaStringReverse {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        boolean ispallin = true;
        int l = A.length();
        for (int i = 0; i < l / 2; i++) {
            if (A.charAt(i) != A.charAt(l - 1 - i))
                ispallin = false;
        }
        System.out.println(ispallin ? "Yes" : "No");
    }
}



