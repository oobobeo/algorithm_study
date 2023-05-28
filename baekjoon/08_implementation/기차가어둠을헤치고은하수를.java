package baekjoon;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class 기차가어둠을헤치고은하수를 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int t = sc.nextInt();
		Train[] arr = new Train[n+1];
		for (int i = 1; i <= n; i++) arr[i] = new Train();
		for (int k = 0; k < t; k++) {
			int cmd = sc.nextInt();
			if (cmd == 1) {
				int i = sc.nextInt();
				int x = sc.nextInt();
				arr[i].seat[x] = true;
			}
			else if (cmd == 2) {
				int i = sc.nextInt();
				int x = sc.nextInt();
				arr[i].seat[x] = false;
			}
			else if (cmd == 3) {
				int i = sc.nextInt();
				for (int j = 19; j >= 1; j--) arr[i].seat[j+1] = arr[i].seat[j];
				arr[i].seat[1] = false;
			}
			else {
				int i = sc.nextInt();
				for (int j = 1; j <= 19; j++) arr[i].seat[j] = arr[i].seat[j+1];
				arr[i].seat[20] = false;
			}
		}
		HashSet<String> set = new HashSet<>();
		for (int i = 1; i <= n; i++) {
			set.add(Arrays.toString(arr[i].seat));
		}
		//System.out.println(set);
		System.out.println(set.size());
	}

	 static class Train {
		boolean[] seat = new boolean[21];
	}
}

