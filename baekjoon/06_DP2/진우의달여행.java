package baekjoon;

import java.util.Scanner;

public class 진우의달여행 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int [][] space = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) space[i][j] = sc.nextInt();
		}
		int [][][] dp = new int[n+1][m][3];
	
		for (int i = 0; i <= n; i++) {
			for (int j = 0; j < m; j++) {
				for (int k = 0; k < 3; k++) dp[i][j][k] = Integer.MAX_VALUE;
			}
		}
		
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < 3; j++) dp[0][i][j] = space[0][i];
		}
		// 0 : 왼쪽에서 내려옴, 1 : 바로 아래. 2 : 오른쪽에서 내려옴 
		for (int i = 1; i <= n; i++) { // 왼쪽에서 내려온 경우 
			for (int j = 0; j < m; j++) {
				int min = Integer.MAX_VALUE;
				if (j > 0) {
					for (int k = 0; k < 3; k++) {
						if (k != 0) min = Math.min(min, dp[i-1][j-1][k]); // 이전 값이 왼쪽에서 내려오지 않은 경우 
					}
					if (i == n) dp[i][j][0] = min;
					else dp[i][j][0] = min + space[i][j];
							
				}
				min = Integer.MAX_VALUE;
				//오른쪽에서 오는 경우 
				if (j < m-1) {
					for (int k = 0; k < 3; k++) {
						if (k != 2) min = Math.min(min, dp[i-1][j+1][k]);
					}
					if (i == n) dp[i][j][2] = min;
					else dp[i][j][2] = min + space[i][j];
				}
				min = Integer.MAX_VALUE;
				//가운데서 오는 경우
				for (int k = 0; k < 3; k++) {
					if (k != 1) min = Math.min(min, dp[i-1][j][k]);
				}
				if (i == n) dp[i][j][1] = min;
				else dp[i][j][1] = min + space[i][j];
			}
		}
		int ans = Integer.MAX_VALUE;
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < 3; j++) {
				if (dp[n][i][j] != 0) ans = Math.min(ans, dp[n][i][j]);
			}
		}
		System.out.println(ans);
	}

}
