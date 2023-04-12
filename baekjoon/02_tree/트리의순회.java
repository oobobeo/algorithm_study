package baekjoon;

import java.util.Scanner;

public class 트리의순회 {

	static int[] in;
	static int[] post;
	static int[] pre;
	static int[] parent;
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		in = new int[n];
		post = new int[n];
		parent = new int[100001];
		for (int i = 0; i < n; i++) in[i] = sc.nextInt();
		for (int i = 0; i < n; i++) post[i] = sc.nextInt();
		for (int i = 0; i < n; i++) parent[in[i]] = i;
		solve(0, n-1, 0, n-1);
	}
	

	static void solve(int instart, int inend, int poststart, int postend) {
		if (instart > inend || poststart > postend) return;
		int root = post[postend];
		System.out.print(root + " ");

		int rootidx = parent[root];
		int leftcnt = rootidx - instart;
		solve(instart, rootidx - 1, poststart, poststart + leftcnt - 1);
		solve(rootidx + 1, inend, poststart + leftcnt, postend - 1);
	}
}
