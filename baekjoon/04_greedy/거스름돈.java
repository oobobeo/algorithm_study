package baekjoon;

import java.util.Scanner;

public class 거스름돈 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int ans = 0;
		int tmp = 0;
		if (n == 1 || n == 3) {
			System.out.println(-1);
			return;
		}
		while (true) {
			tmp = n % 5;
			if (tmp % 2 == 0) {
				ans = n / 5 + tmp / 2;
				break;
			}
			else {
				ans = n / 5 - 1 + (tmp + 5) / 2;
				break;
			}
		}
		System.out.println(ans);
	}

}
