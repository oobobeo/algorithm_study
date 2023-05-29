package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class DFS와BFS {

	static boolean[] visit;
	static int[][] map;
	static StringBuilder sb = new StringBuilder();
	static int N,M,V;
	static Queue<Integer> q = new LinkedList<>();
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		 N = Integer.parseInt(st.nextToken());
		 M = Integer.parseInt(st.nextToken());
		 V = Integer.parseInt(st.nextToken());
		visit = new boolean[N+1];
		map = new int[N+1][N+1];
		for (int i = 1; i <= M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			map[a][b] = map[b][a] = 1;
		}
		DFS(V);
		sb.append("\n");
		visit = new boolean[N+1];

		BFS(V);
		System.out.println(sb);
	}
	public static void DFS(int n) {
		visit[n] = true;
		sb.append(n + " ");
		for (int i = 1; i <= N; i++) {
			if (!visit[i] && map[n][i] == 1) DFS(i);
		}
	}
	public static void BFS(int n) {
		q.add(n);
		visit[n] = true;
		while(!q.isEmpty()) {
			n = q.poll();
			sb.append(n + " ");
			for (int i = 1; i <= N; i++) {
				if (map[n][i] == 1 && !visit[i]) {
					q.add(i);
					visit[i] = true;
				}
			}
		}
		//sb.append(q.poll());
	}

}
