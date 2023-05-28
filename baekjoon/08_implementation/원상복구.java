package baekjoon;

import java.util.Scanner;

public class 원상복구 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int t = sc.nextInt();
		int s[] = new int[n + 1];
		int p[] = new int[n + 1];
		int d[] = new int[n + 1]; // i를 d[i] 번째로 : s -> p
		for (int i = 1; i <= n; i++)
			s[i] = sc.nextInt();
		for (int i = 1; i <= n; i++)
			d[i] = sc.nextInt();
		for (int j = 0; j < t; j++) {
			for (int i = 1; i <= n; i++) {
				p[d[i]] = s[i];
			}
			for (int i = 1; i <= n; i++) s[i] = p[i];
		}
		for (int i = 1; i <= n; i++) System.out.print(p[i] + " ");
	}

}
