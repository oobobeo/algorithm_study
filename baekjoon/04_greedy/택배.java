package baekjoon;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class 택배 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int carry = sc.nextInt();
		int t = sc.nextInt();
		Item[] truck = new Item[t];
		for (int i = 0; i < t; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			truck[i] = new Item(a, b, c);
		}
		Arrays.sort(truck, new Comparator<Item>() {

			@Override
			public int compare(Item o1, Item o2) {
				if (o1.b == o2.b) return o1.a - o2.a;
				return o1.b - o2.b;
			}
			
		});
		int sum = 0;
		int pos = 0;
		int max = 0;
		int[] box = new int[t+1];
		for (int i = 0; i < t; i++) {
			int a = truck[i].a;
			int b = truck[i].b;
			int c = truck[i].c;
			max = 0;
			//if (truck[i].a != truck[i+1].a) sum += cnt;
			for (int j = a; j < b; j++) {
				max = Math.max(max, box[j]);
//				if (truck[j].b == truck[i].a) {
//					
//					cnt -= truck[j].c;
//					if (cnt <= 0) {
//						cnt = 0;
//						break;
//					}
//				}
			}
			pos = Math.min(c, carry-max);
			sum += pos;
			for (int j = a; j < b; j++) box[j] += pos;
			//cnt += truck[i].c;
			//if (cnt > carry) cnt = carry;
			
			//sum+=cnt;
			//System.out.println("sum" + sum);
		}
		System.out.println(sum + box[t]);
	}

	public static class Item {
		int a;
		int b;
		int c;
		public Item(int a, int b, int c) {
			super();
			this.a = a;
			this.b = b;
			this.c = c;
		}
		
	}
}
