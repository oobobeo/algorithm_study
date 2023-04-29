package baekjoon;

import java.util.Scanner;

public class 동전 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int[] arr = new int[n+1];
		int cnt = 0;
		for(int i = 1; i < n+1; i++) arr[i] = sc.nextInt();
		for (int i = arr.length - 1; i >= 0; i--) {
			if (k / arr[i] > 0) {
				cnt += k / arr[i];
				if (k % arr[i] == 0) break;
				k %= arr[i];
			}
		}
		
		System.out.println(cnt);
	}

}
