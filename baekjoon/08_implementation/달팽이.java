package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 달팽이 {
	
	static int[][] arr;
	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));	
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		int target = Integer.parseInt(br.readLine());
		arr = new int[n][n];
		snail(0, n, n);
		int ansi =0;
		int ansj =0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (arr[i][j] == target) {
					ansi = i;
					ansj = j;
					//System.out.println(j + "j");
				}
				sb.append(arr[i][j] + " ");
			}
			sb.append("\n");
			
		}
		System.out.print(sb.toString());
		System.out.println(ansi+1 + " " + (ansj+1));
		
	}
	static void snail(int s, int n, int tmp) {
		for (int i = s; i < tmp-s; i++) {
				for (int j = s; j < tmp-s; j++) {
					if (j == s) {
						arr[i][j] = n*n-(i-s);
					}
					if (j == tmp-s-1) {
						arr[i][j] = n*n-(6*(n/2)) + (i-s);
					}
					
			}
			if (i == s) {
				for (int j = 1; j <= n-2; j++) arr[i][j+s] = (n-2)*(n-2)+j;
			}
			if (i == tmp-s-1) {
				for (int j = 1; j <= n-2; j++) arr[i][j+s] = n*n-n-j+1;
			}
		}
		if (n == 1) return;

		snail(s+1, n-2, tmp);

	}

}
