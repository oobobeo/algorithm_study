package baekjoon;

import java.util.Scanner;
import java.util.TreeMap;

public class 최소최대 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int n = sc.nextInt();
			int max = Integer.MIN_VALUE;
			int min = Integer.MAX_VALUE;
			for (int j = 0; j < n; j++) {
				int k = sc.nextInt();
				if (k > max)
					max = k;
				if (k < min)
					min = k;
			}
			System.out.println(min + " " + max);
		}
	}

}
