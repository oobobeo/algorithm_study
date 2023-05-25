package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
public class 별찍기 {
	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		char[][] arr = new char[8*(n-1)+1][4*(n-1)+1];
		for (int i = 0; i < 4*(n-1) + 1; i++) Arrays.fill(arr[i], ' ');
		if (n == 1) System.out.println("*");
		else {
			star(n, arr, 0);
		}
		for (int i = 0; i <  4*(n-1)+1; i++) {
			for (int j = 0; j < 4*(n-1)+1; j++) {
				System.out.print(arr[i][j]);
			}
			System.out.println();
		}
	}
public static void star(int n, char[][] arr, int s){
		
		//if (n == 1) arr[0][0] = '*';
			for (int i = s; i < 4*(n-1)+1+s; i++) {
				if (i == s || i== 4*(n-1)+s) {
					for (int j = s; j < 4*(n-1)+1+s; j++) arr[i][j] = '*';

				}

					arr[i][s] = '*';
					arr[i][4*(n-1)+s] = '*';
			}
			if (n==1) return;			
			star(n-1, arr, s+2);

		}

}
