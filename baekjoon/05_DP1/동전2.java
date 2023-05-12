package baekjoon;

import java.util.Scanner;

public class 동전2 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int cnt = 0;
		int [] coin = new int[n];
		for (int i = 0; i < n; i++) coin[i] = sc.nextInt();
		int[] dp = new int[k+1];
		for (int i = 1; i <= k; i++) dp[i] = 100000;
		//dp[0] = 0;
		for (int i = 0; i < n; i++) {
			for (int j = coin[i]; j <= k; j++) {
				dp[j] = Math.min(dp[j], dp[j-coin[i]]+1);
			}
		}
		if (dp[k] == 100000) {
			System.out.println(-1);
			System.exit(0);
		}
		System.out.println(dp[k]);
	}

}
