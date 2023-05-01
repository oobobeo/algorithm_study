package baekjoon;

import java.util.Scanner;

public class 꿀따기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		int sum = 0;
		int min = 10000;
		int tmp = 0;
		for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
		for (int i = 1; i < n-1; i++) {
			if (arr[i] < min) {
				min = arr[i];
				tmp = i;
			}
		}
		int sub1 = 0;
		int case1 = 0;
		int sub2 = 0;
		int case2 = 0;
		int[] ca1 = new int[tmp+1];
		int[] x1 = new int[tmp+1];
		int x = 1;
		while (x <=tmp) {
		for (int i = x + 1; i < arr.length; i++) {
			sub1 += arr[i];
			ca1[x] = sub1;
			x1[x] = x;
			x++;
		}
		}
		for (int i = 1; i < arr.length; i++) case1 += arr[i];
		for (int i = tmp - 1; i >= 0; i--) sub2 += arr[i];
		for (int i = arr.length - 2; i >= 0; i--) case2 += arr[i];
		if (arr[0] <= arr[arr.length-1]) {
			for (int i = 1; i < tmp + 1; i++)
			sum = Math.max(ca1[i] + case1 - arr[x1[i]], sum);
		}
		else {
			sum = Math.max(sub2 + case2 - arr[tmp], (case2 - arr[arr.length-2]) * 2);

		}
		int mid = arr.length/2;
		int right = 0;
		int left = 0;
		for (int i = 1; i <= mid; i++) right += arr[i];
		for (int i = mid; i < arr.length-1; i++) left += arr[i];
		System.out.println(Math.max(sum, right+left));
	}
	
}
