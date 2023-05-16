package baekjoon;

import java.util.Scanner;

public class 구간나누기 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int [] arr = new int[n+1];
		for (int i = 1; i <= n; i++) arr[i] = sc.nextInt();
		int [] sum = new int[n+1];
		for (int i = 1; i <= n ; i++) sum[i] = sum[i-1] + arr[i];
		int [][] dp = new int[n+1][m+1];
		for (int i = 0; i <= n; i++) {
			for (int j = 1; j <= m; j++) dp[i][j] = Integer.MIN_VALUE / 2;
		}
		dp[1][1] = arr[1];
		for (int i = 2; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				dp[i][j] = dp[i-1][j];
				int min = 0;
				if (j == 1) min = -1;
				for (int k = i-2; k >= min; k--) {
					if (k < 0) dp[i][j] = Math.max(dp[i][j], sum[i]);
					else dp[i][j] = Math.max(dp[i][j], dp[k][j-1] + sum[i] - sum[k+1]);
				}
			}
		}
		System.out.println(dp[n][m]);
	}

}
