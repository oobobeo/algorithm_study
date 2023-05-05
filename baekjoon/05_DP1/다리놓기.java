package baekjoon;

import java.util.Scanner;

public class 다리놓기 {

	public static void main(String[] args) {

		int [][] arr = new int[30][30];
		Scanner sc = new Scanner(System.in);
		
		for (int i = 0; i < 30; i++) {
			arr[i][i] = 1;
			arr[0][i] = 1;
			arr[i][0] = 1;
		}
		for (int i = 2; i < 30; i++) {
			for (int j = 1; j < 30; j++) {
				arr[i][j] = arr[i-1][j-1] + arr[i-1][j];
			}
		}
//		for (int i= 0 ;i < 30; i++) {
//			for (int j = 0; j < 30; j++) {
//				System.out.println(arr[i][j]);
//			}
//		}
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int west = sc.nextInt();
			int east = sc.nextInt();
			System.out.println(arr[east][west]);
		}
	}

}
