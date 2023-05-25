package baekjoon;

import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.TreeMap;

public class 파일정리 {

	public static void main(String[] args) {
		StringBuilder sb = new StringBuilder();
		Scanner sc = new Scanner(System.in);
		TreeMap<String, Integer> map = new TreeMap<>();
		int n = sc.nextInt();
		for (int i = 0; i < n; i++) {
			String s = sc.next();
			String[] tmp = s.split("[.]");
			map.put(tmp[1], map.getOrDefault(tmp[1], 0)+1);
		}
		for (Entry<String, Integer> ans : map.entrySet()) {
			sb.append(ans.getKey() + " " + ans.getValue()).append("\n");
		}
		System.out.println(sb.toString());
	}

}
