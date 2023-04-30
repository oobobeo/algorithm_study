package baekjoon;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class AB {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		long a = sc.nextLong();
		long b = sc.nextLong();
		Queue<Long> q=  new LinkedList<>();
		q.add(a * 2);
		q.add(a * 10 + 1);
		int ans = 0;
		while (!q.isEmpty()) {
			ans++;
			int size = q.size();
			for (int i = 0; i < size; i++) {
			long now = q.poll();
			if (now > b) continue;
			if (now == b) {
				System.out.println(ans + 1);
				return;
			}
			q.add(now * 2);
			q.add(now * 10 + 1);
			}
		}
		System.out.println(-1);
	}

}
