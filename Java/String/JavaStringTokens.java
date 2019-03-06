/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank Practice Java
*/

package String;

import java.util.Scanner;

public class JavaStringTokens {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        scan.close();

        s = s.trim(); // so that .split() works properly

        /* Check special cases */
        if (s.length() == 0) {
            System.out.println(0);
            return;
        }

        /* Split on all non-alphabetic characters */
        String[] words = s.split("[^a-zA-Z]+");

        /* Print output */
        System.out.println(words.length);
        for (String word : words) {
            System.out.println(word);
        }
    }
}