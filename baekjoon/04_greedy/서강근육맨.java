package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class 서강근육맨 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[] arr = new long[n];
		for (int i = 0; i < n; i++) arr[i] = sc.nextLong();
		Arrays.sort(arr);
		long min = 0;
		if (n % 2 == 1) {
			min = arr[n-1];
			for (int i = 0; i < n/2; i++) {
				min = Math.max(min, arr[i] + arr[n-2-i]);
			}
		}
		else {
			for (int i = 0; i < n/2; i++) {
				min = Math.max(min, arr[i] + arr[n-1-i]);
			}
		}
		System.out.println(min);
	}

}
