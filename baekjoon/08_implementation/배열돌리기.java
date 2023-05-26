package baekjoon;

import java.util.Scanner;

public class 배열돌리기 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int r = sc.nextInt();
		int [][] arr = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) arr[i][j] = sc.nextInt();
		}
		int cnt = Math.min(m,n)/2;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < cnt; j++) {
				int tmp = arr[j][j];
				for (int k = j+1; k < m-j; k++) arr[j][k-1] = arr[j][k];
				for (int k = j+1; k < n-j; k++) arr[k-1][m-1-j] = arr[k][m-1-j];
				for (int k = m-2-j; k >= j; k--) arr[n-1-j][k+1] = arr[n-1-j][k];
				for (int k = n-2-j; k>= j; k--) arr[k+1][j] = arr[k][j];
				arr[j+1][j] = tmp;
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) System.out.print(arr[i][j] + " ");
			System.out.println();
		}
	}

}
