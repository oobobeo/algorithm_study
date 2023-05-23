package baekjoon;

import java.util.Scanner;

public class 전구 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int t = sc.nextInt();
		int[] light = new int[n+1];
		for (int i = 1; i <= n; i++) light[i] = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int cmd = sc.nextInt();
			int l = sc.nextInt();
			int r = sc.nextInt();
			if (cmd == 1) light[l] = r;
			if (cmd == 2) {
				for (int j = l; j <= r; j++) {
					if (light[j] == 0) light[j] = 1;
					else if (light[j] == 1) light[j] = 0;
				}
			}
			if (cmd == 3) {
				for (int j = l; j <= r; j++) light[j] = 0;
			}
			if (cmd == 4) {
				for (int j = l; j <= r; j++) light[j] = 1;

			}
		}
		for (int i = 1; i <= n; i++) {
			System.out.print(light[i] + " ");
		}

	}

}
