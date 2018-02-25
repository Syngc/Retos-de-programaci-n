/*
Given an integer n (n ≤ 15), print π to n digits after the decimal point (rounded).
(e.g. for n = 2, print 3.14; for n = 4, print 3.1416; for n = 5, prints 3.14159.)
*/
import java.util.Scanner;
import java.lang.Math;

class Main{
  public static void main(String[] args) {
    Scanner scn = new Scanner(System.in);
    int i = scn.nextInt();
    String f = "%." + i + "f";
    System.out.print(String.format(f,Math.PI));

  }
}
