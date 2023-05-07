package baekjoon;

import java.util.Scanner;

public class 가장큰증가하는부분수열 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		int[] dp = new int[n];
		for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
		for (int i = 0; i < n; i++) dp[i] = arr[i];
		for (int i = 0; i < n; i++)	{
			

			for (int j = 0; j < i; j++) {
				if (arr[j] < arr[i] ) dp[i] = Math.max(dp[j] + arr[i], dp[i]);
				
			}
			
		}
		int max = 0;
		for (int x : dp) {
			//System.out.println("arr" + x);
			max = Math.max(max, x);
		}
		System.out.println(max);
			
	}

}
