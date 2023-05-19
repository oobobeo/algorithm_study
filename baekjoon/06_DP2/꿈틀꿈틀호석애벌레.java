package baekjoon;

import java.util.Scanner;

public class 꿈틀꿈틀호석애벌레 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
		long[] dp = new long[n+1];
		int left = 0; 
		int right = 1;
		int sum = arr[left];
		while (right <= n) {
			if (sum >= k) {
				while (sum >= k) {
					dp[right] = Math.max(dp[right], dp[left] + sum - k);
					sum -= arr[left];
					left++;
				}
			}
			else {
				dp[right] = Math.max(dp[right], dp[right-1]);
				if (right == n) break;
				sum += arr[right];
				right++;
			}
		}
		System.out.println(dp[n]);
	}

}
