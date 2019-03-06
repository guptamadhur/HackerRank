/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank Practice Java
*/

package String;

import java.util.Scanner;

public class JavaSubstring {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        int start = in.nextInt();
        int end = in.nextInt();
        System.out.println(S.substring(start, end));
    }
}
