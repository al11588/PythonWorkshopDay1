/* 
* @Author: alvinlawson
* @Date:   2015-05-11 00:20:16
* @Last Modified by:   alvinlawson
* @Last Modified time: 2015-05-11 00:20:49
*/
import java.util.Scanner;

public class java {
    public static void main(String[] args) {
Scanner input = new Scanner(System.in);
 
        	 
        	System.out.print("Enter 6 Numbers to Sort: ");
        	int num;
        	int[] num_in_array = new int[6];
 
        	for(int enter_num=0; enter_num<6; enter_num++)
        	{
    		num_in_array[enter_num] = input.nextInt();
    		 
    		for(int sort_num=0; sort_num<6; sort_num++)
    		{
        	        	if(num_in_array[enter_num] < num_in_array[sort_num])
        	        	{
            	    	int swap = num_in_array[enter_num];
            	    	num_in_array[enter_num] = num_in_array[sort_num];
            	    	num_in_array[sort_num] = swap;
        	        	}
  	  	 
    		}
        	}
 
        	System.out.println("The Sorted Numbers are: ");
 
        	for(int print = 0; print<6; print++)
        	{
    	        	System.out.print(num_in_array[print]+ " ");
        	}
        	System.out.println();

    }
}