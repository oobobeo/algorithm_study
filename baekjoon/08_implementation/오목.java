package baekjoon;


import java.util.Scanner;

public class 오목 {

	public static void main(String[] args) {

		Scanner sc = new Scanner (System.in);
		int stone[][] = new int [19][19];
		int [][] d = {{0,1}, {1, 0}, {1, 1}, {-1, 1}};
		for (int i = 0; i < 19; i++) {
			for (int j = 0; j < 19; j++) stone[i][j] = sc.nextInt();
		}
		for (int j = 0; j < 19; j++) {
			for (int i = 0; i < 19; i++) {
				if (stone[i][j] == 1 || stone[i][j] == 2) { // 0이 아닌 경우에만 
					for (int k = 0; k < 4; k++) {
						int x = i;
						int y = j;
						int cnt = 1; // 돌 개수 카운트 
						
						while (true) {
							x += d[k][0];
							y += d[k][1];
							if (x >= 0 && x <= 18 && y >= 0 && y <= 18) {
								if (stone[x][y] == stone[i][j]) cnt++;
								else break;
							}else break;
						}
						x = i;
						y = j;
						while (true) {
							x -= d[k][0];
							y -= d[k][1];
							if (x >= 0 && x <= 18 && y >= 0 && y <= 18) {
								if (stone[i][j] == stone[x][y]) cnt++;
								else break;
							}else break;
						}
						if (cnt == 5) {
							System.out.println(stone[i][j]);
							System.out.println(i + 1 + " " + (j+1));
							System.exit(0);
						}
					}
					
				}
			}
		}
		System.out.println(0);
	}

}
