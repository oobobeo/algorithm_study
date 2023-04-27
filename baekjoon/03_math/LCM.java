package baekjoon;

import java.util.Scanner;

public class LCM {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for (int i = 0; i < n; i++) {
			long a = sc.nextInt();
			long b = sc.nextInt();
			long min = Math.min(a, b);
			long gcd = 0;
			for (int j = 1; j <= min; j++) {
				if (a % j == 0 && b % j == 0) gcd = j;
			}
			 System.out.println(a*b/gcd);
		}
	}

}
