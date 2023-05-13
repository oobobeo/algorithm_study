package baekjoon;

import java.util.Scanner;

public class 가장큰정사각형 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[][] arr = new int[n + 1][m + 1];
		for (int i = 1; i <= n; i++) {
			String s = sc.next();
			for (int j = 1; j <=m; j++) arr[i][j] = Character.getNumericValue(s.charAt(j-1));
			
		}
		
		int [][] dp = new int[n+1][m+1];
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j];
			}
		}
		int ans = 0;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (arr[i][j] == 1) {
					int res = 1;
					int idx = 1;
					while(i + idx <= n && j + idx <= m) {
						int space = dp[i+idx][j+idx] - dp[i+idx][j-1] - dp[i-1][j+idx] + dp[i-1][j-1];
						idx++;
						if (space != idx * idx) break;
						res = idx * idx;
					}
						ans = Math.max(ans, res);
					
				}
			}
		}
		System.out.println(ans);
	}

}
