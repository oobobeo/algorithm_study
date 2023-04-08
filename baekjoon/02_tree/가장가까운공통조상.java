package baekjoon;

import java.util.Scanner;

public class 가장가까운공통조상 {
	static int[] parent;
	static boolean[] visit;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int n = sc.nextInt();
			parent = new int[n+1];
			visit = new boolean[n+1];
			for (int j = 0; j < n-1; j++) {
				int p = sc.nextInt();
				int c = sc.nextInt();
				parent[c] = p; // c의 부모는 p
			}
			int x = sc.nextInt();
			int y = sc.nextInt();
			find(x, y);
		}
	}

	public static void find(int x, int y) {
		while (x > 0) {//x가 0이하면 종료 
			visit[x] = true;
			x = parent[x];
		}
		while (y > 0) {
			if (visit[y]) {
				System.out.println(y);
				break;
			}
			y = parent[y];
			
			//visit[y] = true;
		}
	}
}
