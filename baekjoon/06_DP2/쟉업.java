package baekjoon;

import java.util.Scanner;

public class 쟉업 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int result = 0;

		int dp[] = new int[n];
		for (int i = 0; i < n; i++) {
			int time = sc.nextInt();
			dp[i] = time;
			int idx = sc.nextInt();
			for (int j = 0; j < idx; j++) {
				int tmp = sc.nextInt();
				dp[i] = Math.max(dp[i], dp[tmp-1] + time);
			}
			result = Math.max(result, dp[i]);
		}
		System.out.println(result);
	}

}
