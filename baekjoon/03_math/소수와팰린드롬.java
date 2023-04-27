package baekjoon;

import java.util.Scanner;

public class 소수와팰린드롬 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String n = sc.next();
		while (true) {
			
			if (isPrime(n)&&isPal(n)) {
				System.out.println(n);
				break;
			}
			n = String.valueOf(Integer.parseInt(n) + 1);
			
		}
		
	}
	public static boolean isPrime(String a) {
		int x = Integer.parseInt(a);
		if (x == 1) return false;
		for (int i = 2; i * i <= x; i++) {
			if (x % i == 0) return false;
		}
		return true;
	}
	public static boolean isPal(String x) {
		char[] arr = x.toCharArray();
		char[] pal = new char[x.length()];
		boolean flag = true;
		for (int i = 0; i < x.length(); i++) pal[x.length() - i - 1] = x.charAt(i);
		for (int i = 0; i < x.length() / 2; i++) {
			if (arr[i] != pal[i])flag = false;
		}
		if (flag) return true;
		return false;
	}
}
