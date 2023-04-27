package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 다음소수 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int t = Integer.parseInt(br.readLine());
		for (int i = 0; i < t; i++) {
			long n = Long.parseLong(br.readLine());
			while (true) {
				if (isPrime(n)) {
					sb.append(n).append("\n");
					break;
				}
				n++;
			}
			System.out.println(sb.toString());
		}
	}
	public static boolean isPrime(long x) {
		if (x == 1 || x == 0) return false;
		for (int i = 2; i * i <= x; i++) {
			if (x % i == 0) return false;
		}
		return true;
	}

}
