package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 숨바꼭질3 {

	static int su;
	static int bro;
	static boolean[] visit;
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		 su = Integer.parseInt(st.nextToken());
		 bro = Integer.parseInt(st.nextToken());
		visit = new boolean[100000+1];
		System.out.println(bfs(su));
	}

	public static int bfs(int n) {
		int min = Integer.MAX_VALUE;
		Queue<Node> q = new LinkedList<>();
		visit[n] = true;
		q.add(new Node(n, 0));
		while(!q.isEmpty()) {
			Node node = q.poll();
			if (node.x == bro) min = Math.min(node.time, min);
			if (node.x*2 <= 100000 && !visit[node.x * 2]) {
				q.add(new Node(node.x * 2, node.time));
				visit[node.x*2] = true;
			}
			if (node.x - 1>=0 && !visit[node.x-1]) {
				q.add(new Node(node.x-1, node.time+1));
				visit[node.x-1] = true;
			}
			if (node.x + 1 <= 100000 && !visit[node.x+1]) {
				q.add(new Node(node.x+1, node.time+1));
				visit[node.x+1] = true;
			}
		}
		return min;
		
	}
	public static class Node {
		int x, time;

		public Node(int x, int time) {
			super();
			this.x = x;
			this.time = time;
		}
		
	}
}
