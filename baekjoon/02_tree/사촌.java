package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class 사촌 {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			
				StringTokenizer st = new StringTokenizer(br.readLine());

				int n = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				if (n == 0 && c == 0) break;

				int sol = 0;
				int [] arr = new int[n+1];
				int [] parent = new int[n+1];
				
				int idx = -1;
				arr[0] = -1;
				parent[0] = -1;
				st = new StringTokenizer(br.readLine());
				for (int i = 1; i <= n; i++) {
					arr[i] = Integer.parseInt(st.nextToken());
					if (arr[i] == c) sol = i; // sol은 c의 index
					if (arr[i] != arr[i-1]+1) idx++; // 1씩 증가하지 않음 -> 부모가 다름 
					parent[i] = idx;
				}
				int answer = 0;
				for (int i = 1; i <= n; i++) {
					if (parent[i] != parent[sol] && parent[parent[i]] == parent[parent[sol]]) answer++;
					// 직계 부모가 다르면서 최종 부모는 같음 
				}
				sb.append(answer).append("\n");
			
		}
		System.out.print(sb.toString());

	}

}
