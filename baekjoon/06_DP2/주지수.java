package baekjoon;

import java.util.Scanner;

public class 주지수 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in); 
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[][] land = new int[n+1][m+1];
		int[][] dp = new int[n + 1][m + 1];

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) land[i][j] = sc.nextInt();
		}
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + land[i][j];
		}
		int k = sc.nextInt();
		for (int i = 0; i < k; i++) {
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();
			System.out.println(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]);
		}
	}

}
