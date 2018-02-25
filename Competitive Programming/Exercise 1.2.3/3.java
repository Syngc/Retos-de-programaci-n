/*
Given a date, determine the day of the week (Monday, . . . , Sunday) on that day.
(e.g. 9 August 2010—the launch date of the first edition of this book—is a Monday.)
*/
import java.util.Scanner;
import java.util.GregorianCalendar;
import java.util.Calendar;

class Main{

  public static void main(String[] args) {
    String[] dias = {"Sunday","Monday","Tuesday","Thursday","Wednesday","Friday","Saturday"};
    int[] fecha = new int[3];
    for(int i = 0; i <= 2; i++){
        fecha[i] = Integer.parseInt(args[i]);
    }
    Calendar cld = new GregorianCalendar(fecha[2],fecha[1]-1,fecha[0]);
    System.out.println(dias[cld.get(cld.DAY_OF_WEEK) - 1]);
  }
}
