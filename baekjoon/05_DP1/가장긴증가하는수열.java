package baekjoon;

import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class 가장긴증가하는수열 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		int[] dp = new int[n];
		for (int i = 0; i < n; i++)
			arr[i] = sc.nextInt();
		dp[0] = 1;
		for (int i = 1; i < n; i++) {
			dp[i] = 1;
			for (int j = 0; j < i; j++) {
				if (arr[j] < arr[i] && dp[i] <= dp[j]) dp[i] = dp[j] + 1;
				
			}
		}
		int max = 0;
		for (int i : dp) max = Math.max(max, i);
		System.out.println(max);

	}
}
