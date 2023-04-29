package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class ATM {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int [] arr = new int[n];
		for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
		Arrays.sort(arr);
		int sum = 0;
		int ans = 0;
		for (int i = 0; i < n; i++) {
			sum += arr[i];
			ans += sum;
		}
		System.out.println(ans);
	}

}
