package baekjoon;

import java.util.Scanner;

public class Coin {

	public static void main(String[] args) {


		        Scanner scanner = new Scanner(System.in);
		        int N = scanner.nextInt();
		        int K = scanner.nextInt();
		        int[][] wv = new int[N][2];
		        for (int i = 0; i < N; i++) {
		            wv[i][0] = scanner.nextInt();
		            wv[i][1] = scanner.nextInt();
		        }

		        int[] dp = new int[K + 1];
		        for (int i = 0; i <= K; i++) {
		            dp[i] = Integer.MIN_VALUE;
		        }
		        dp[0] = 0;

		        for (int i = 0; i < N; i++) {
		            int w = wv[i][0];
		            int v = wv[i][1];

		            for (int j = w; j <= K; j++) {
		                dp[j] = Math.max(dp[j], dp[j - w] + v);
		            }
		        }

		        int max = Integer.MIN_VALUE;
		        for (int i = 0; i <= K; i++) {
		            max = Math.max(max, dp[i]);
		        }

		        System.out.println(max);
		    }
}
