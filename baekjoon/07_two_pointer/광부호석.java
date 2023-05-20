package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class 광부호석 {

	public static int N, C;
	public static ArrayList<Index>[] list;
	
		
	public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());
	list = new ArrayList[100005];
	for (int i = 0; i < list.length; i++) list[i] = new ArrayList<>();
	for (int i = 0; i < N; i++) {
		st = new StringTokenizer(br.readLine());
		int x = Integer.parseInt(st.nextToken());
		int y = Integer.parseInt(st.nextToken());
		long value = Long.parseLong(st.nextToken());
		list[x].add(new Index(x, y, value));
	}
	long ans = 0;
	long currentV = 0L;
	PriorityQueue<Index> q = new PriorityQueue<>();
	for (int i = 0; i < list.length; i++) {
		if (list[i].isEmpty()) continue;
		for (int j = 0; j < list[i].size(); j++) {
			q.add(list[i].get(j));
			currentV += list[i].get(j).value;
		}
		int prevTop = -1;
		while (!q.isEmpty() && q.size() > C) {
			prevTop = q.peek().y;
			currentV -= q.poll().y;
			while (!q.isEmpty() && q.peek().y == prevTop) {
				currentV -= q.poll().value;
			}
		}
		ans = Math.max(ans, currentV);
	}
	System.out.println(ans);
	}

	public static class Index implements Comparable<Index>{

		int x;
		int y;
		long value;
		
		public Index(int x, int y, long value) {
			super();
			this.x = x;
			this.y = y;
			this.value = value;
		}

		@Override
		public int compareTo(Index o) {
			return o.y - this.y;
		}
		
	}
}
