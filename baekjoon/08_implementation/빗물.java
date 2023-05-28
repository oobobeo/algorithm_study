package baekjoon;

import java.util.Scanner;

public class 빗물 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int rain[] = new int [m];
		int result = 0;
		for (int i = 0; i < m; i++) rain[i] = sc.nextInt();
		for (int i = 1; i < m-1; i++) {
			int left = 0;
			int right = 0;
			for (int j = 0; j < i; j++) left = Math.max(left, rain[j]);
			for (int j = i+1; j < m; j++) right = Math.max(right, rain[j]);
			if (left > rain[i] && right > rain[i]) result += Math.min(left, right) - rain[i];
		}
		System.out.println(result);
	}

}
