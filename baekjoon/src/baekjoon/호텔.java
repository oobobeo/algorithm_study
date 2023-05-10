package baekjoon;

import java.util.Scanner;

public class 호텔 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int c = sc.nextInt();
		int n = sc.nextInt();
		
		int[][] arr = new int[n][2];
		for (int i = 0 ; i < n; i++) {
			for (int j = 0; j < 2; j++) arr[i][j] = sc.nextInt();
		}
		
		
	}

}
