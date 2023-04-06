package baekjoon;

import java.util.ArrayList;
import java.util.Scanner;
// 물이 모두 흘러가므로 자식 노드 갯수 구하면 됨 
public class 나무위의빗물 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int water = sc.nextInt();
		int cnt = 0;
		ArrayList<ArrayList<Integer>> list = new ArrayList<>();
		for (int i = 0; i < n+1; i++) list.add(new ArrayList<>());
		for (int i = 0; i < n-1; i++) {
			int first = sc.nextInt();
			int last = sc.nextInt();
			list.get(first).add(last);
			list.get(last).add(first);
		}
		for (int i = 0; i < n+1; i++) System.out.println(list);
		for (int i = 0; i < n+1; i++) {
			if (list.get(i).size() == 1) cnt++;
		}
		System.out.println((double) water / cnt);
	}

}
