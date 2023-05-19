package baekjoon;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 팀빌딩 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int [] arr = new int[n];
		for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
		//Arrays.sort(arr);
		int l = 0, r = n-1;
		int sum = 0;
		while (l <= r) {

			sum = Math.max((r-l-1) * Math.min(arr[l], arr[r]), sum);

			
			if (arr[r] >= arr[l]) l++;
			else r--;
			
		}
		System.out.println(sum);
	}

}
