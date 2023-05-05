package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class 피보나치수2 {
	static long n;
	static long[] arr;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		 n = Integer.parseInt(in.readLine());
		 arr = new long[(int) (n+1)];
		 arr[0] = 0;
		 arr[1] = 1;
		 for (int i = 2; i <= n; i++) arr[i] = arr[i-1] + arr[i-2];
		 System.out.println(arr[(int) n]);
	}
//	public static int Fibo(int n) {
//		arr = new int[n+1];
//		arr[0] = 0;
//		arr[1] = 1;
//		if (n > 1) arr[n] = Fibo(n-1) + Fibo(n-2); 
//		for (int x : arr) System.out.println(x);
//		return arr[n];
//	}
}
