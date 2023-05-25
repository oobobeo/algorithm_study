package baekjoon;

import java.util.Scanner;

public class 지뢰찾기 {

	static int n;
	static char[][] boom;
	static char[][] map;
	static int[] dx = {-1, -1, -1, 0, 1, 1, 1, 0};
	static int[] dy = {-1, 0, 1, 1, 1, 0, -1, -1};
	static boolean flag = false;
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		map = new char[n][n];
		boom = new char[n][n];
		for (int i = 0; i < n; i++) {
			String s = sc.next();
			for (int j = 0; j < n; j++) boom[i][j] = s.charAt(j);
		}
		for (int i = 0; i < n; i++) {
			String s = sc.next();
			for (int j = 0; j < n; j++) map[i][j] = s.charAt(j);
		}
		process();
		check();
		for (char[] chars : map) {
			for (char c : chars) {
				System.out.print(c);
			}
			System.out.println();
		}
	}
	private static void check() {
		if(flag) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if(boom[i][j] == '*') map[i][j] = '*';
				}
			}
		}
	}
	private static void process() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(map[i][j] == 'x'){
                    if(boom[i][j] == '*')
                        flag = true;
                    else {
                        count(i, j);
                    }
                }
                else
                    map[i][j] = '.';
            }
        }
    }
	 private static void count(int i, int j) {
	        int count = 0;

	        for (int k = 0; k < 8; k++) {
	            int x = i + dx[k];
	            int y = j + dy[k];
	            if(0 <= x && x <= n-1 && 0 <= y && y <= n-1){
	                if(boom[x][y] == '*')
	                    count++;
	            }
	        }
	        map[i][j] = (char) (count + '0');
	    }

}
