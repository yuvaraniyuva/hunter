import java.util.*;
import java.lang.*;
import java.io.*;
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		String s,reverse="";
		Scanner sc=new Scanner(System.in);

		s=sc.nextLine();
		String[] array=s.split(" ");
		for(String w:array)
		{
			StringBuilder sb=new StringBuilder(w);
			sb.reverse();
			reverse+=sb.toString()+" ";
		}
		System.out.println(reverse);

	}
	
}
