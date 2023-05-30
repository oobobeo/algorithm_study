package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 공주님을구해라 {

	static int n, m, t;
	static boolean[][] visit;
	static int[][] map;
	static int[][] result;
	static int[] dy = {1, -1, 0, 0};
	static int[] dx = {0, 0, 1, -1};
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		 n = Integer.parseInt(st.nextToken());
		 m = Integer.parseInt(st.nextToken());
		 t = Integer.parseInt(st.nextToken());
		map = new int[n+1][m+1];
		//visit = new boolean[n+1][m+1];
		int si = 0;
		int sj = 0;
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 2) {
					si = i;
					sj = j;
				}
			}
		}
		int time  = 0;
		if (BFS(n, m, map) == 0) {
			if (sword()!=0) {
				time = sword() + (n-si) + (m-sj);
			}
			else {
				System.out.println("Fail");
				System.exit(0);
			}
		}
		else if (sword() == 0) time = BFS(n, m, map);
		else time = Math.min(BFS(n, m, map), sword() + (n-si) + (m-sj));
		if (time > t || time == 0) System.out.println("Fail");
		else System.out.println(time);
		//else System.out.println(BFS(n, m, map));
	}
	public static int BFS(int a, int b, int[][] arr) {
		visit = new boolean[a+1][b+1];
		result = new int[a+1][b+1];

		Queue<int[]> q = new LinkedList<>();
		visit[1][1] = true;
		q.add(new int[] {1, 1});
		while(!q.isEmpty()) {
			int[] tmp = q.poll();
			for (int i = 0; i < 4; i++) {
				int x = tmp[0] + dx[i];
				int y = tmp[1] + dy[i];
				if (x >= 1 && y >= 1 && x <= a && y <= b) {
					if (!visit[x][y] && arr[x][y] != 1) {
						visit[x][y] = true;
						result[x][y] = result[tmp[0]][tmp[1]] + 1;
						q.add(new int[] {x, y});
					}
				}
			}
		}
		return result[a][b];
	}

	public static int sword() {
		visit = new boolean[n+1][m+1];
		result = new int[n+1][m+1];

		Queue<int[]> q = new LinkedList<>();
		visit[1][1] = true;
		q.add(new int[] {1, 1});
		while(!q.isEmpty()) {
			int[] tmp = q.poll();
			for (int i = 0; i < 4; i++) {
				int x = tmp[0] + dx[i];
				int y = tmp[1] + dy[i];
				if (x >= 1 && y >= 1 && x <= n && y <= m) {
					if (!visit[x][y] && map[x][y] != 1) {
						visit[x][y] = true;
						result[x][y] = result[tmp[0]][tmp[1]] + 1;
						q.add(new int[] {x, y});
						if (map[x][y] == 2) return result[x][y];
					}
				}
			}
		}
		return 0;
	}
}
