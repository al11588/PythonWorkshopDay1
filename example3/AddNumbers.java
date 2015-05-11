/* 
* @Author: alvinlawson
* @Date:   2015-05-11 00:07:32
* @Last Modified by:   alvinlawson
* @Last Modified time: 2015-05-11 00:10:34
*/
import java.util.Scanner;

public class AddNumbers {
    public static void main(String[] args) {
	int x, y, z;
      System.out.println("Enter two integers to calculate their sum ");
        	Scanner in = new Scanner(System.in);
        	x = in.nextInt();
        	y = in.nextInt();
        	z = x + y;
      System.out.println("Sum of entered integers = "+z);

    }
}