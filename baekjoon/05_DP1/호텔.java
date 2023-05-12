package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class 호텔 {

	public static void main(String[] args) {
		// c명, n개
		// 돈, 사람 
		Scanner sc = new Scanner(System.in);
		int c = sc.nextInt();
		int n = sc.nextInt();
		
		int[][] arr = new int[n][2];
//		for (int i = 0 ; i < n; i++) {
//			for (int j = 0; j < 2; j++) arr[i][j] = sc.nextInt();
//		}
		int [] dp = new int[101 + c];
		Arrays.fill(dp, 987654321);
		dp[0] = 0;
		for (int i = 0; i < n; i++) {
			int cost = sc.nextInt();
			int human = sc.nextInt();
			for (int j = human; j < c+101; j++) {
				dp[j] = Math.min(dp[j], cost + dp[j-human]);
			}
		}
		int ans = Integer.MAX_VALUE;
		for (int i = c; i < 101 + c; i++) ans = Math.min(ans, dp[i]);
		System.out.println(ans);
		
	}

}
