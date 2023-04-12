package baekjoon;

import java.util.Scanner;

public class 트리 {

	public static class Tree{
		int root;
		Tree left;
		Tree  right;
		public Tree(int root, Tree left, Tree right) {
			super();
			this.root = root;
			this.left = left;
			this.right = right;
		}
		
		
	}
	static int n;
	static int[] pre;
	static int[] in;
	static StringBuilder sb;
	public static void main(String[] args) {
		sb = new StringBuilder();
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			n = sc.nextInt();
			pre = new int[n];
			in = new int[n];
			for (int j = 0; j < n; j++) pre[j] = sc.nextInt();
			for (int j = 0; j < n; j++) in[j] = sc.nextInt();
			findOrder(0, 0, n-1);
			sb.append("\n");
		}
		System.out.println(sb);
	}
	private static void findOrder(int root, int begin, int last) {
		if (root >= n) return;
		int rootval = pre[root];
		for (int i = begin; i <= last; i++) {
			if (in[i] == rootval) {
				findOrder(root + 1, begin, i);
				findOrder(root + i + 1 - begin, i + 1, last);
				sb.append(rootval + " ");
				return;
			}
		}
	}

}
