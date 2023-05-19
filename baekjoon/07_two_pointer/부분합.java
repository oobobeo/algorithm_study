package baekjoon;

import java.util.Scanner;

public class 부분합 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int s = sc.nextInt();
		int [] arr = new int [n+1];
	
		for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
		
		int min = Integer.MAX_VALUE;
		int l = 0, r = 0;
		int sum  = 0;
		while (r <= n) {
			if (sum >= s) { // l 포인터를 이동시키며 계속 비교함 
				min = Math.min(min, r-l);
				sum -= arr[l++];
			}
			else sum += arr[r++];
		}
		if (min == Integer.MAX_VALUE) {
			System.out.println(0);
			System.exit(0);
		}
		System.out.println(min);
	}

}
