/* Author: Madhur Gupta
   Github: github.com/guptamadhur
   Project: Hacker Rank Practice Java
*/
package Introduction;

import java.util.Scanner;

public class JavaStdinandStdoutII {
    public static void main(String[] args) {
        /* Read input */
        Scanner scan = new Scanner(System.in);
        int i    = scan.nextInt();
        double d = scan.nextDouble();
        scan.nextLine();              // gets rid of the pesky newline
        String s = scan.nextLine();
        scan.close();
        
        /* Print output */
        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}