package baekjoon;

import java.util.Scanner;

public class 홀수홀릭호석 {

	private static int max = Integer.MIN_VALUE;
	private static int min = Integer.MAX_VALUE;
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		cut(n, 0);
		System.out.println(min + " " + max);
	}

	private static void cut(int n, int cnt) {
		cnt += countOdd(n);
		if (n / 10 == 0) {
			min = Integer.min(min, cnt);
			max = Integer.max(max, cnt);
		}
		else if (n / 100 == 0) {
			int next = n / 10;
			next += n % 10;
			cut(next, cnt);
		}
		else {
			String s = String.valueOf(n);
			for (int i = 0; i < s.length() - 2; i++) {
				for (int j = i + 1; j < s.length() - 1; j++) {
					int next = Integer.parseInt(s.substring(0, i+1));
					next += Integer.parseInt(s.substring(i+1, j+1));
					next += Integer.parseInt(s.substring(j+1));
					cut(next, cnt);

				}
			}
		}
	}
	private static int countOdd(int n) {
		int cnt = 0;
		while (n > 0) {
			int tmp = n % 10;
			if (tmp % 2 == 1) cnt++;
			n /= 10;
		}
		return cnt;
	}
}
