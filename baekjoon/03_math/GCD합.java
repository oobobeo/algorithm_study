package baekjoon;

import java.util.ArrayList;
import java.util.Scanner;

public class GCD합 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			long ans = 0;
			ArrayList<Integer> arr = new ArrayList<>();
			int n = sc.nextInt();
			for (int j = 0; j < n; j++) arr.add(sc.nextInt());
			for (int j = 0; j < n - 1; j++) {
				for (int k = j + 1; k < n; k++) {
					ans += GCD(arr.get(j), arr.get(k));
				}
			}
			System.out.println(ans);
		}
	}
	public static int GCD(int n1, int n2) {
		if (n2 == 0) return n1;
		else return GCD(n2, n1 % n2);
	}
}
