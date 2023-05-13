package baekjoon;

import java.util.Scanner;

public class 로또 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			long [][] dp = new long[n+1][m+1];
			for (int j = 0; j <= m; j++) dp[0][j] = 1;
			for (int j = 1; j <= n; j++) {
				for (int k = 1; k <= m; k++) dp[j][k] = dp[j-1][k/2] + dp[j][k-1]; //n번째로 m을 택한경우 , m을 택하지 않은 경우 
			}
			System.out.println(dp[n][m]);
		}
	}

}
