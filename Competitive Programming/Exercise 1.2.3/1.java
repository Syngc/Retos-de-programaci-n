/*
Using Java, read in a double
(e.g. 1.4732, 15.324547327, etc.)
echo it, but with a minimum field width of 7 and 3 digits after the decimal point
(e.g. ss1.473 (where ‘s’ denotes a space), s15.325, etc.)
*/

import java.util.Scanner;

class Main{

  public static void main(String[] args) {
    Scanner scn = new Scanner(System.in);
    double y = 3,192
    double d = scn.nextDouble();
    System.out.print(String.format("%7.3f", d));
  }

}
