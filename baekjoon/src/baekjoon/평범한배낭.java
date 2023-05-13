package baekjoon;

import java.util.Scanner;

public class 평범한배낭 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int [][] bag = new int[n+1][2];
		for (int i = 1; i <= n; i++) {
			bag[i][0] = sc.nextInt(); //무게 
			bag[i][1] = sc.nextInt(); //가치 
		}
		int [][] dp = new int[n+1][k+1];
		for (int i = 1; i <= k; i++) {
			for (int j = 1; j <= n; j++) {
				dp[j][i] = dp[j-1][i];
				if (i - bag[j][0] >= 0) dp[j][i] = Math.max(dp[j-1][i], bag[j][1] + dp[j-1][i-bag[j][0]]);
			}
		}
		System.out.println(dp[n][k]);
	}

}
