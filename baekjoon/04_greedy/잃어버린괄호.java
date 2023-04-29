package baekjoon;

import java.util.Scanner;

public class 잃어버린괄호 {

	static long sum;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		if (!s.contains("-")) {
			sum = 0;
			String[] plus = s.split("\\+");
			for (int i = 0; i < plus.length; i++) sum += Integer.parseInt(plus[i]);
			System.out.println(sum);
			return;
		}
		String[] sub = s.split("\\-");
		sum = 0;
		if (!sub[0].contains("+")) {
		sum = Integer.parseInt(sub[0]);
		sub(sub);
		}
		else {
			String[] s1 = sub[0].split("\\+");
			for (int i = 0; i < s1.length; i++) sum += Integer.parseInt(s1[i]);
			sub(sub);
		}
		System.out.println(sum);
		
	}
	public static void sub(String[] sub) {
		for (int i = 1; i < sub.length; i++) {
			if (!sub[i].contains("+")) sum -= Integer.parseInt(sub[i]);
			else {
				String[] plus = sub[i].split("\\+");
				int p = 0;
				for (int j = 0; j < plus.length; j++) {
					p += Integer.parseInt(plus[j]);
				}
				sum -= p;
			}
		}
	}
	
}
