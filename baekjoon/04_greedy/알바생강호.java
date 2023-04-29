package baekjoon;

import java.util.Collections;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class 알바생강호 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		PriorityQueue<Integer> arr = new PriorityQueue<>(Collections.reverseOrder());
		for (int i = 0; i < n; i++) {
			arr.add(sc.nextInt());
		}
		long sum = 0;
		for (int i = 0; i < n; i++) {
			if (arr.peek() - i > 0) sum += arr.poll() - i;
		}
		System.out.println(sum);
	}

}
