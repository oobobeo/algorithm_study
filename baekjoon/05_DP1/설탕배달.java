package baekjoon;

import java.util.Scanner;

public class 설탕배달 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		if (t == 4 || t == 7) {
			System.out.println(-1);
			return;
		}
		int cnt = 0;
		int tmp = t % 5;
		int five = t / 5;
		if (tmp %3 == 0) {
			System.out.println(five + tmp / 3);
			return;
		}
		while (tmp % 3 != 0) {

			tmp += 5;
			five -= 1;
			cnt = five + tmp / 3;
			if (tmp % 3 == 0) {
				System.out.println(cnt);
				break;
			}
		}
	}

}
