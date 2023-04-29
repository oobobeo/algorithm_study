package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class 에너지드링크 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
		Arrays.sort(arr);
		double ans = arr[n-1];
		for (int i = n-2; i >= 0; i--) {
			ans += (arr[i] / 2.0);
		}
		
		System.out.println(ans);
	}

}
