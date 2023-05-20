package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class 합이0인네정수 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int [] A = new int[n];
		int [] B = new int[n];
		int [] C = new int[n];
		int [] D = new int[n];
		int [] AB = new int [n*n];
		int [] CD = new int [n*n];
		for (int i = 0; i < n; i++) {
			A[i] = sc.nextInt();
			B[i] = sc.nextInt();
			C[i] = sc.nextInt();
			D[i] = sc.nextInt();
		}
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				AB[cnt] = A[i] + B[j];
				CD[cnt] = C[i] + D[j];
				cnt++;
			}
		}
		Arrays.sort(AB);
		Arrays.sort(CD);
		int l = 0, r = CD.length-1;
		long ans = 0;
		while(l < n * n && r >= 0) {
			long lVal = AB[l];
			long rVal = CD[r];
			long lCnt = 0;
			long rCnt = 0;
			
			if (lVal + rVal == 0) {
				while (l < AB.length && AB[l] == lVal) {
					lCnt++;
					l++;
				}
				while (r >= 0 && CD[r] == rVal) {
					rCnt++;
					r--;
				}
				ans += rCnt *  lCnt;
			}
			else if (lVal + rVal < 0) l++;
			else r--;
		}
		System.out.println(ans);
		
	}

}
