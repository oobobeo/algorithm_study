package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class 행복유치원 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int p = sc.nextInt();
		int [] arr = new int[n];
		for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
		int sum = 0;
		int [] ans = new int[n-1];
		for (int i = 0; i < n-1; i++) ans[i] = arr[i+1] - arr[i];
		Arrays.sort(ans);
		for (int i = 0; i < n-p; i++) sum += ans[i];
		System.out.println(sum);
	}

}
