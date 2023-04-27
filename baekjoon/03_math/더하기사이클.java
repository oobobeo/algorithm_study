package baekjoon;

import java.util.Scanner;

public class 더하기사이클 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int cnt = 0;
		
		int n = sc.nextInt();
		if (n == 0) System.out.println(1);
		else {
		int a = n;
		int tmp = 0;
		while (tmp != n) {
			tmp = (a/10 + a%10) %10 + a % 10 * 10;
			a = tmp;
			cnt++;
			if (tmp == n) break;
		}
		System.out.println(cnt);
		}
	}

}
