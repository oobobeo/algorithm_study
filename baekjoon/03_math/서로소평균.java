package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

public class 서로소평균 {
	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());

		int x = Integer.parseInt(br.readLine());
		long sum = 0;
		int cnt = 0;
		for (int i = 0; i < t; i++) {
			int num = Integer.parseInt(st.nextToken());
			if (GCD(x, num) == 1) {
				sum += num;
				cnt++;
			}
		}
		System.out.println((double)sum / cnt);
	}
	public static int GCD(int n1, int n2) {
		if (n2 == 0) return n1;
		else return GCD(n2, n1 % n2);
	}
}
