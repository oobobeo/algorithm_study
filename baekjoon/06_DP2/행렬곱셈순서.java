package baekjoon;

import java.util.Scanner;

public class 행렬곱셈순서 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int [] arr = new int [n + 1];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < 2; j++) arr[i+j] = sc.nextInt();
		}
		int [][] dp = new int[n+1][n+1];
		for (int i = 0; i < n; i++) {
			for (int j = 1; j < n-i; j++) {
				int k = i+j+1;
				dp[j][k] = Integer.MAX_VALUE;
				for (int l = j; l < k; l++) dp[j][k] = Math.min(dp[j][k], dp[j][l] + dp[l+1][k] + (arr[j-1] * arr[l] * arr[k]));
			}
		}
		System.out.println(dp[1][n]);
	}

}
