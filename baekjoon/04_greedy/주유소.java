package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class 주유소 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[] dis = new long [n-1];
		long[] oil = new long [n];
		for (int i = 0; i < n - 1; i++) dis [i] = sc.nextInt();
		for (int i = 0; i < n; i++) oil[i] = sc.nextInt();
		long sum = 0;
		long min = oil[0];
		for (int i = 0; i < n - 1; i++) {
			if (min > oil[i]) min = oil[i];
			sum += dis[i] * min;
		}
		System.out.println(sum);
	}

}
