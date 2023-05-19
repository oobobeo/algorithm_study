package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 가장긴짝수연속한부분수열 {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] line = br.readLine().split(" ");
		int n = Integer.parseInt(line[0]);
		int k = Integer.parseInt(line[1]);
		boolean[] arr = new boolean[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(st.nextToken());
			arr[i] = num % 2 == 0; // 짝수 
		}
		int len = 0;
		int l = 0, r = 0, ct = 0; // l : 부분수열 시작, r : 부분수열 현재 
		while (r < n) {
			if (ct < k) { // 홀수 제거 기회남은 경우 
				if (!arr[r]) ct++;
				r++;
				len = Math.max(r - l - ct, len); // 제거된 ct까지 빼줘야함 
			}
			else if (arr[r]) { // 짝수인경우 
				r++;
				len = Math.max(r - l - ct, len);
			}
			else { // 홀수인 경우 -> 연속이 안되므로 ct값 줄여줘야함 
				if (!arr[l]) ct--;
				l++;
			}
		}
		System.out.println(len);
	}

}
