package baekjoon;

import java.util.Scanner;

public class 징검다리건너기 {

	static int n;
	static int k;
	static int[] arr;
	static boolean[] visit;
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		k = sc.nextInt();
		arr = new int[n];
		visit = new boolean[n];
		for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
		visit[0] = true;
		find(0);
		System.out.println("NO");
		
	}
	static void find(int idx) {
		if (visit[n-1]) {
			System.out.println("YES");
			System.exit(0);
		}
		for (int i = n-1; i>=idx; i--) {
			if (!visit[i]) {
				int tmp = (i - idx) * (1 + Math.abs(arr[idx] - arr[i]));
				if (tmp <= k) {
					visit[i] = true;
					find(i);
				}
			}
		}
	}

}
