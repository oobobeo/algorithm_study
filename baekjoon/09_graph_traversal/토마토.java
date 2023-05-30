package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 토마토 {

	static int n, m;
	static int[][] tomato;
	//static boolean[][] visit;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
	static Queue<int[]> q = new LinkedList<>();;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		 m = Integer.parseInt(st.nextToken());
		 n = Integer.parseInt(st.nextToken());
		 tomato = new int[n+1][m+1];
		 //visit = new boolean[n+1][m+1];
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= m; j++) {
				tomato[i][j] =Integer.parseInt(st.nextToken());
				if (tomato[i][j] == 1) {
					q.add(new int[] {i, j});
				}
			}
		}
		System.out.println(bfs());
	}
	public static int bfs() {
		while (!q.isEmpty()) {
			int [] tmp = q.poll();
			int a = tmp[0];
			int b = tmp[1];
			for (int i = 0; i < 4; i++) {
				int x = a + dx[i];
				int y = b + dy[i];
				if (x > 0 && x <= n && y > 0 && y <= m) {
					if (tomato[x][y] == 0) {
						//visit[x][y] = true;
						q.add(new int[] {x, y});
						tomato[x][y] = tomato[a][b]+1;
					}
				}
			}
		}
		int cnt = Integer.MIN_VALUE;

		
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (tomato[i][j] == 0) return -1;
				cnt = Math.max(cnt, tomato[i][j]);
			}
		}
		return cnt-1;
	}
	

}
