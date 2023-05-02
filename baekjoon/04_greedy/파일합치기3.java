package baekjoon;

import java.util.PriorityQueue;
import java.util.Scanner;

public class 파일합치기3 {
	static PriorityQueue <Long> q;
	static Long[] arr;
	static long sum;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int n = sc.nextInt();
			arr = new Long[n];
			for (int j = 0; j < n; j++) {
				arr[j] = sc.nextLong();
			}
			sol(n);
			System.out.println(sum);
		}
	}
	public static long sol (int n) {
		q = new PriorityQueue<>();
		sum = 0;
		long tmp = 0;
		int odd = 0;
		for (int i = 0; i < n; i++) q.add(arr[i]);
		while (q.size()!= 1) {
				tmp += q.poll();
				tmp += q.poll();
				sum += tmp;
				q.add(tmp);
				tmp = 0;
		}
		return sum;
	}
}
