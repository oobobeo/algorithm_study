package baekjoon;

import java.util.Collections;
import java.util.Map.Entry;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.TreeMap;

public class 최대공약수와최소공배수 {

	public static void main(String[] args) {
		PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		TreeMap<Integer, Integer> map = new TreeMap<>();
		for (int i = 1; i <= n; i++) {
			if (n % i == 0) map.put(i, map.getOrDefault(i, 0) + 1);
		}
		for (int i = 1; i <= m; i++) {
			if (m % i == 0) map.put(i, map.getOrDefault(i, 0) + 1);
		}
		for (Entry<Integer, Integer> entry : map.entrySet()) {
			if (entry.getValue() == 2) q.add(entry.getKey());
		}
		System.out.println(q.peek());
		System.out.println(n*m/q.peek());
	}
}
