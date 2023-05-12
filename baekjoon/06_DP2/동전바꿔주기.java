package baekjoon;

import java.util.Scanner;

public class 동전바꿔주기 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt(); // 지폐의 금액 
		int k = sc.nextInt(); // 동전의 가지 수 
		int [][] coin = new int [k + 1][2]; // coin[i][0] -> 동전의 종류
											// coin[i][1] -> 동전의 개수
		int [] dp = new int[T+1];
		dp[0] = 1;
 		for (int i = 1; i <= k; i++) {
			coin[i][0] = sc.nextInt();
			coin[i][1] = sc.nextInt();
		}
 		for (int a = 1; a <= k; a++) { // 동전의 가지 수 
 			int x = coin[a][0];
 			for (int b = T; b >= x; b--) { // 목표금액부터 top -> bottom 
 				for (int c = 1; c <= coin[a][1]; c++) { // 각 종류별 동전의 개수 
 					if (b < x * c) break;
 					dp[b] += dp[b - x * c];
 				}
 			}
 		}
 		
		System.out.println(dp[T]);
	}

}
