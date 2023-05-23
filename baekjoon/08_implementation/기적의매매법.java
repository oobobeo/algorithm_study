package baekjoon;

import java.util.Scanner;

public class 기적의매매법 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int money = sc.nextInt();
		int jun = money;
		int junStock = 0;
		int sung = money;
		int sungStock = 0;
		int[] stock = new int[15];
		for (int i = 1; i <= 14; i++) stock[i] = sc.nextInt();
		for (int i = 1; i <= 14; i++){
			if (jun >= stock[i]) {
				junStock += jun / stock[i];
				jun %= stock[i];
				
			}
		}
		jun += stock[14] * junStock;
		int buycnt = 0;
		int sellcnt = 0;
		for (int i = 1; i <= 14; i++) {
			if (stock[i] < stock[i-1]) {
				buycnt++;
				sellcnt = 0;
			}
			if (stock[i] > stock[i-1]) {
				sellcnt++;
				buycnt = 0;
			}
			if (sellcnt == 3) {
				sung += stock[i] * sungStock;
				if (i > 11) break;
				sungStock = 0;
				sellcnt = 0;
				buycnt = 0;

			}
			if (buycnt >= 3 && sung > stock[i]) {
				sungStock += sung / stock[i];
				sung %= stock[i];
				sellcnt = 0;
				//buycnt = 0;

			}
			if (i == 14) sung += stock[i] * sungStock;
		}
//		System.out.println(jun);
//		System.out.println(sung);
		
		if (sung > jun) System.out.println("TIMING");
		else if (sung < jun) System.out.println("BNP");
		else System.out.println("SAMESAME");
	}

}
