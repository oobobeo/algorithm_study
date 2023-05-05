package baekjoon;

import java.util.Scanner;

public class 타일링2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] tile = new int[n+2];
		tile[1] = 1;
		tile[2] = 3;
		for (int i = 3; i <= n; i++) tile[i] = (tile[i-1] + 2 * tile[i-2]) % 10007;
		System.out.println(tile[n] % 10007);
	}

}
