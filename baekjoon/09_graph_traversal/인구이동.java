package baekjoon;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class 인구이동 {

	static int n, l, r;
	static int[][] board;
	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { 1, 0, -1, 0 }; // 동 남 서 북
	static boolean [][]  visit;
	static ArrayList<int[]> list;
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		 n = sc.nextInt();
		 l = sc.nextInt();
		 r = sc.nextInt();
		board = new int[n+1][n+1];
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				board[i][j] =sc.nextInt();
			}
		}
		System.out.println(move());
	}
	
	public static int move() {

		int result = 0;
		while (true) {
			visit = new boolean[n+1][n+1];
			boolean flag = false;
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					if (!visit[i][j]) {
						int sum = bfs(i, j);
						if (list.size() > 1) {
							changePop(sum);
							flag = true;
						}
					}
				}
			}
			if (!flag) return result;
			result++;
		}
	}

	public static int bfs(int a, int b) {
		int sum = board[a][b];
		Queue<int[]> q = new LinkedList<>();
		list = new ArrayList<>();
		q.add(new int[] {a, b});
		list.add(new int[] {a, b});
		visit[a][b] = true;
		while (!q.isEmpty()) {
			int[] tmp = q.poll();
			for (int i = 0; i < 4; i++) {
				int x = tmp[0] + dx[i];
				int y = tmp[1] + dy[i];
				if (x >= 1 && y >= 1 && x <= n && y <= n) {
				if (!visit[x][y]) {
					int diff = Math.abs(board[x][y] - board[tmp[0]][tmp[1]]);
					if (diff >= l && diff <= r) {
						visit[x][y] = true;
						q.add(new int[] {x, y});
						list.add(new int[] {x, y});
						sum += board[x][y];
					}
				}
			}
			}
		}
		return sum;
	}
	public static void changePop(int sum) {
		int avg = sum / list.size();
		for (int i = 0; i < list.size(); i++) {
			int x = list.get(i)[0];
			int y = list.get(i)[1];
			board[x][y] = avg;
		}
	}
}
