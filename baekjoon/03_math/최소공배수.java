package baekjoon;

import java.util.Collections;
import java.util.Map.Entry;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.TreeMap;

public class 최소공배수 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for (int i = 0; i < n; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			TreeMap<Integer, Integer> map = new TreeMap<>();
			PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());

			for (int j = 1; j <= a; j++) {
				if (a % j == 0) map.put(j, map.getOrDefault(j, 0) + 1);
			}
			for (int j = 1; j <= b; j++) {
				if (b % j == 0) map.put(j, map.getOrDefault(j, 0) + 1);
			}
			for (Entry<Integer, Integer> entry : map.entrySet()) {
				if (entry.getValue() == 2) q.add(entry.getKey());
			}
			System.out.println(a*b/q.peek());
		}
	}

}
