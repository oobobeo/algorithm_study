package baekjoon;

import java.util.Scanner;

public class 민겸수 {
	static String s;
	static char[] arr;
	static String max;
	static String min;
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		s = sc.next();
		
		System.out.println(makeMax());
		System.out.println(makeMin());
	}
	public static String makeMin() {
		arr = s.toCharArray();
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] == 'K') arr[i] = '5';
		}
		int cnt = 0;
		if (s.charAt(0) == 'M') arr[0] = '1';
		for (int i = 1; i < s.length(); i++) {
			if (s.charAt(i) == 'M' && s.charAt(i - 1) != 'M') arr[i] = '1';
			else if (s.charAt(i) == 'M' && s.charAt(i - 1) == 'M') arr[i] = '0';
		}
		String tmp = "";
		for (int i = 0; i < arr.length; i++) tmp += arr[i];
		return tmp;
	}
	
	public static String makeMax() {
		arr = s.toCharArray();
		String tmp = "";
		int cnt = 0;
		int k = 0;
		boolean flag = false;
		for (int i = 0; i < arr.length; i++) {
			if (!flag && arr[i] == 'K') arr[i] = '5';
			if (arr[i] == 'M') {
				k++;
				arr[i] = '1';
				if (!flag) {
					cnt = i;
					flag = true;
				}
			}
			if (flag && arr[i] == 'K') {
				k = 0;
				for (int j = cnt + 1; j <= i; j++) arr[j] = '0';
				//arr[i] = '0';
				arr[cnt] = '5';
				flag = false;
			}
//			if (flag) {
//				for (int j = cnt; j <= k; j++) arr[j] = '1';
//			}
			//if (arr[i] == 'K' && arr[i - 1] == 'M') arr[cnt] = '5';
		}
		for (int i = 0; i < arr.length; i++) tmp += arr[i];

		return tmp;
	}

}
