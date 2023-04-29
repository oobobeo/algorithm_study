package baekjoon;

import java.util.Scanner;

public class 블로그2 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String s = sc.next();
		int cnt = 0;
		char first = s.charAt(0);
		for (int i = 0; i < s.length()-1; i++) {
			if (s.charAt(i) == first && s.charAt(i + 1) != first) cnt++;
		}
		System.out.println(cnt + 1);
	}

}

