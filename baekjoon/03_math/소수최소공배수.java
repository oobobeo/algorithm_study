package baekjoon;

import java.math.BigInteger;
import java.util.Scanner;

public class 소수최소공배수 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long mul = 1;
		for (int i = 0; i < n; i++) {
			long num = sc.nextLong();
			if (isPrime(num)) {
				mul = lcm(mul, num);
			}
		}
		if (mul == 1) System.out.println(-1);
		else System.out.println(mul);
	}
	public static boolean isPrime(long x) {
		if (x==1) return false;
		for (int i = 2; i * i <= x; i++) {
			if (x % i == 0) return false;
		}
		return true;
	}
	public static long gcd (long a1, long a2) {
		if (a2 == 0) return a1;
		else return gcd(a2, a1 % a2);
	}
	public static long lcm(long a1, long a2) {
        return a1 / gcd(a1, a2) * a2;
    }
}
