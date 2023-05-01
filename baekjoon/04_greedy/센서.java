package baekjoon;

import java.util.Arrays;
import java.util.Scanner;
import java.util.TreeSet;

public class 센서 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int[] sens = new int[n];
		int sum = 0;
		for (int i = 0; i < n; i++) sens[i] = sc.nextInt();
		//Arrays.sort(sens);
		TreeSet <Integer> set = new TreeSet<>();
		for (int i = 0; i < n; i++) set.add(sens[i]);
		int[] ans = new int[set.size()];
		//System.out.println(set);
		int l = 0; 
		for (int x : set) ans[l++] = x;
		int[] sol = new int[ans.length-1];
		for (int i = 0; i < ans.length-1; i++) sol[i] = ans[i + 1] - ans[i];
		Arrays.sort(sol);
		for (int i = 0; i < ans.length - k; i++) sum += sol[i];
		System.out.println(sum);
	}

}
