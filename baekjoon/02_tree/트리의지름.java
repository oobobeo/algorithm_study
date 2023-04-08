package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
//처음에 배열로 선언했다가 시간초과남 -> arraylist 활용 
public class 트리의지름 {
	static ArrayList<ArrayList<Tree>> list;
	static boolean[] visit;
	static int length;
	public static class Tree {
		int idx;
		int weight;
		public Tree(int idx, int weight) {
			this.idx = idx;
			this.weight = weight;
		}
		
	}
	public static void main(String[] args) throws IOException {
		//Scanner sc = new Scanner(System.in);
		
		
		//int n = sc.nextInt();
		//visit = new boolean[n+1];
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(in.readLine());
		list = new ArrayList<>();
		for (int i = 0; i < n+1; i++) list.add(new ArrayList<>());
		for (int i = 0; i < n-1; i++) {
			StringTokenizer st = new StringTokenizer(in.readLine());
			int r = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			list.get(r).add(new Tree(c, w));
			list.get(c).add(new Tree(r, w));
		}
		length = 0;
		for (int i = 1; i <= n; i++) {
			visit = new boolean[n+1];
			visit[i] = true;
			dfs(i, 0);
		}
		System.out.println(length);
	}
	
	private static void dfs(int num, int len) {
		
		for (Tree tree : list.get(num)) {
			if (!visit[tree.idx]) {
				visit[tree.idx] = true;
				dfs(tree.idx, len + tree.weight);
			}
		}
		length = (length < len)? len : length;
	}

}
