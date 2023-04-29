package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class 로프 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		int ans = 0;
		for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
		Arrays.sort(arr);
		for (int i = n - 1; i >=0; i--) {
			 ans = Math.max(ans, arr[i] * (n-i));
		}
		System.out.println(ans);
	}
}
