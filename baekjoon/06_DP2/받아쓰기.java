package baekjoon;

import java.util.Scanner;

public class 받아쓰기 {

	static long n;
	static long m;
	static long[][] dp;
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		n = sc.nextLong();
		m = sc.nextLong();
		dp = new long[(int) (n+1)][(int) (m+1)];
		String given = sc.next();
		String ans = sc.next();
		System.out.println(writeDown(given, ans));
	}
	public static long writeDown(String given, String ans) {
		for (int i = 1; i <= given.length(); i++) dp[i][0] = i;
		for (int i = 1; i <= ans.length(); i++) dp[0][i] = i;
		for (int i = 1; i <= given.length(); i++) {
			for (int j = 1; j <= ans.length(); j++) {
				if (isRight(given.charAt(i-1), ans.charAt(j-1))) dp[i][j] = dp[i-1][j-1];
				else dp[i][j] = Math.min(dp[i-1][j-1] + 1, Math.min(dp[i][j-1] + 1, dp[i-1][j] + 1)); // 삭제, 수정, 추가 
			}
		}
		return dp[(int) n][(int) m];
	}

	public static boolean isRight(char a, char b) {
		if (a == b) return true;
		if (a == 'i' && (b == 'j' || b == 'l')) return true;
		if (a == 'v' && b == 'w') return true;
		return false;
	}
}
