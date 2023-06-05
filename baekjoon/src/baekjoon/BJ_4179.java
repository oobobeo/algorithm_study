package algorithm;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;



public class BJ_4179{
	public static class Point {
		int x, y, type, count;

		public Point(int x, int y, int type, int count) {
			this.x = x;
			this.y = y;
			this.type = type;
			this.count = count;
		}
	}
	static int n, m;
	static char[][] maze;
	static boolean[][] visit;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static Point point;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		Queue<Point> q = new LinkedList<>();
		maze = new char[n][m];
		visit = new boolean[n][m];
		for (int i = 0; i < n; i++) {
			String s = sc.next();
			for (int j = 0; j < m; j++) {
				maze[i][j] = s.charAt(j);
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (maze[i][j] == 'J') {
					if (isEdge(i, j)) {
						System.out.println(1);
						return;
					}
					maze[i][j] = '.';
					point = new Point(i, j, 0, 0);
				}
				else if (maze[i][j] == 'F') q.add(new Point(i, j, 1, 0));
			}
		}
		bfs(q);
		
	}
	static void bfs(Queue<Point> q) {
		int x;
		int y; 
		int count;
		q.add(point);
		visit[point.x][point.y] = true;
		while (!q.isEmpty()) {
			Point p = q.poll();
			x = p.x;
			y = p.y;
			count = p.count;
			if (isEdge(x, y) && p.type == 0) {
				System.out.println(count + 1);
				return;
			}
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				if (!isRange(nx, ny) || maze[nx][ny] == '#' || maze[nx][ny] == 'F') continue;
				if (p.type == 0 && !visit[nx][ny]) {
					q.add(new Point(nx, ny, p.type, count+1));
					visit[nx][ny] = true;
					
				}
				else if (p.type == 1 && !visit[nx][ny]) {
					q.add(new Point(nx, ny, p.type, count+1));
					maze[nx][ny] = 'F';
				}
			}
		}
        System.out.println("IMPOSSIBLE");

	}
	static boolean isRange(int x, int y) {
		if (x >= 0 && y >= 0 && x < n && y < m) return true;
		return false;
	}
	
	static boolean isEdge(int x, int y) {
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dx[i];
			if (!isRange(nx, ny)) return true;
		}
		return false;
	}
	
	
}