package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 쉬운최단거리 {

	static int n, m, homei, homej;
	static int[][] map;
	static boolean[][] visit;
	static int dx[] = { -1, 1, 0, 0 };
	static int dy[] = { 0, 0, -1, 1 };
	static int[][] result;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		homei = 0;
		homej = 0;
		map = new int[n + 1][m + 1];
		result = new int[n + 1][m + 1];
		visit = new boolean[n + 1][m + 1];
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 2) {
					homei = i;
					homej = j;
				} else if (map[i][j] == 0)
					visit[i][j] = true;
			}
		}

		bfs(homei, homej);
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (!visit[i][j])
					result[i][j] = -1;
				sb.append(result[i][j] + " ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

	public static void bfs(int a, int b) {
		Queue<int[]>q = new LinkedList<>();
		q.add(new int[] { a, b });
		visit[a][b] = true;
		while (!q.isEmpty()) {
			int tmp[] = q.poll();
			for (int k = 0; k < 4; k++) {
				int x = tmp[0] + dx[k];
				int y = tmp[1] + dy[k];
				if (x >= 0 && y >= 0 && x <= n && y <= m) {
					if (map[x][y] == 1 && !visit[x][y]) {
						visit[x][y] = true;
						result[x][y] = result[tmp[0]][tmp[1]] + 1;
						q.add(new int[] {x, y});
					}
				}
			}
		}
	}

}
