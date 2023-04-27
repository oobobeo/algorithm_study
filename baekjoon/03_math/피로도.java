package baekjoon;

import java.util.Scanner;

public class 피로도 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int m = sc.nextInt();
		int stress = 0;
		int ans = 0;
		int time = 0;
		for (int i = 1; i <= 24; i++) {
			if (stress + a <= m) {
				stress += a;
				ans += b;
			}
			else {
				stress -= c;
				stress = Math.max(0, stress);
			}
		}
		System.out.println(ans);
	}
}
