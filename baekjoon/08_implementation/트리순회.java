package baekjoon;

import java.util.ArrayList;
import java.util.Scanner;

public class 트리순회 {
	static int cnt = 0;
	static ArrayList<Integer> inOrder;
	static ArrayList<Tree>[] arr;
	 static class Tree{
		int left;
		int right;
		public Tree(int left, int right) {
			this.left = left;
			this.right = right;
		}
		
	}
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		arr = new ArrayList[n+1];
		int ans = 0;
		for (int i = 0; i <= n; i++) arr[i] = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			int h = sc.nextInt();
			int l = sc.nextInt();
			int r = sc.nextInt();
			arr[h].add(new Tree(l, r));
		}
		inOrder = new ArrayList<>();
		dfs(1, 0, true);
		dfs(1, 0, false);
	}
	static void dfs(int now, int next, boolean x) {
		for (Tree tree : arr[now]) {
			if (tree.left != -1) {
				dfs(tree.left, now, x);
				if (!x) cnt++;
			}
			if (x) inOrder.add(now);
			else {
				if (inOrder.get(inOrder.size()-1) == now) {
					System.out.println(cnt);
					return;
				}
				cnt++;
			}
			if (tree.right != -1) {
				dfs(tree.right, now, x);
				if (!x) cnt++;
			}
		}
	}

}
