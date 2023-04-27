package baekjoon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class 소수 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> list = new ArrayList<>();
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int sum = 0; 
		int min = 0;
		for (int i = n; i <= m; i++) {
			if (isPrime(i)) {
				sum += i;
				list.add(i);
			}
		}
		if (list.isEmpty()) System.out.println(-1);
		
		else{
			Collections.sort(list);
			min = list.get(0);
			System.out.println(sum);
			System.out.println(min);
		}
		
	}
	public static boolean isPrime(int x) {
		if (x == 1)return false;
		for (int i = 2; i*i <=x; i++) {
			if (x % i == 0) return false;
		}
		return true;
	}
}
