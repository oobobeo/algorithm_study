package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 바이러스 {
static boolean visit[];
static int cnt = 0;
static int c, n;
	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		 c = Integer.parseInt(br.readLine());
		 n = Integer.parseInt(br.readLine());
		 int [][] tree = new int[c+1][c+1];
		visit = new boolean[c+1];
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			tree[a][b] = tree[b][a] = 1;
		}
		DFS(1, tree);
		System.out.println(cnt);
	}

	public static int DFS(int x, int[][] tree) {
		visit[x] = true;
		for (int j = 1; j <= c; j++) {
			if (visit[j] == false && tree[x][j] == 1) {
				cnt++;
				DFS(j, tree);
			}
		}
		return cnt;
	}
}
