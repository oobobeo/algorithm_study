package baekjoon;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 연구소 {

	static int n, m;
	static boolean[][] visit;
	static int[][] map;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	static int[][] result;
	static int ans = Integer.MIN_VALUE;

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		 n = sc.nextInt();
		 m = sc.nextInt();
		 map = new int[n][m];
		 result = new int[n][m];
		visit = new boolean[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) map[i][j] = sc.nextInt();
		}
		result = map;
		dfs(0);
		System.out.println(ans);
	}

	public static void bfs() {
		int cnt = 0;
		Queue<int[]> q = new LinkedList<>();
		int [][] virus = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) virus[i][j] = map[i][j];
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (virus[i][j] == 2) q.add(new int[] {i, j});
			}
		}
		while (!q.isEmpty()) {
			int[] tmp = q.poll();
			for (int i = 0; i < 4; i++) {
				int x = tmp[0] + dx[i];
				int y = tmp[1] + dy[i];
				
				if (x >= 0 && y >= 0 && x < n && y < m) {
					if (virus[x][y] == 0) {
						virus[x][y] = 2;
						q.add(new int[] {x, y});
					}
				}
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (virus[i][j] == 0) cnt++;
			}
		}
		ans = Math.max(cnt, ans);
	}
	public static void dfs(int wall) {
		if (wall == 3) {
			bfs();
			return;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 0) {
					map[i][j] = 1;
					dfs(wall + 1);
					map[i][j] = 0;
				}
			}
		}
	}
	
}
