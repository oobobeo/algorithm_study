package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class ABCDE {

	private static int ans = 0;
	private static ArrayList<Integer>[] list;
	private static boolean[] visit;
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		list = new ArrayList[n];
		for (int i = 0; i < n; i++) list[i] = new ArrayList<>();
		for (int i = 1; i <= m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			list[a].add(b);
			list[b].add(a);
		}
		for (int i = 0; i < n; i++) {
			visit = new boolean[n];
			dfs(i, 0);
		}
		System.out.println(0);
		
		
	}
	public static void dfs(int x, int len) {
		if (len == 4) {
			System.out.println(1);
			System.exit(0);
		}
		visit[x] = true;
		for (int i = 0; i < list[x].size(); i++) {
			int temp = list[x].get(i);
			if (visit[temp] == false) {
				visit[temp] = true;
				dfs(temp, len + 1);
				visit[temp] = false;
			}
		}
	}

}
