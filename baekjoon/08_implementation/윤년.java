package baekjoon;

import java.util.Scanner;

public class 윤년 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		if ((n % 4 == 0 && n % 100 != 0) || n % 400 ==0) System.out.println(1);
		else System.out.println(0);
	}

}
