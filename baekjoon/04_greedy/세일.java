package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class 세일 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int [] arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		int ans = 0;
		Arrays.sort(arr);
		for (int i = n-1; i >= 0; i--) {
			if (i % 3 == n % 3) continue;
			ans += arr[i];
		}
		System.out.println(ans);
	}

}
