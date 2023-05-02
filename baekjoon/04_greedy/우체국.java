package baekjoon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class 우체국 {
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		ArrayList<Node> post = new ArrayList<>(); 
		int n = sc.nextInt();
		long cnt = 0;
		long sum = 0;
		for (int i = 0; i < n; i++) {
			long x = sc.nextLong();
			long a = sc.nextLong();
			post.add(new Node(x, a));
			cnt += post.get(i).a; 
		}
		Collections.sort(post, new Comparator<Node>() {
			@Override
			public int compare(Node o1, Node o2) {
				if (o1.x == o2.x) return (int) (o1.a - o2.a);
				return (int) (o1.x - o2.x);
			}
			
		});
		for (int i = 0; i < n; i++) {
			sum += post.get(i).a;
			if (sum >= (cnt+1)/2) { ///2가 버리기 때문에 +1해줘야함 
				System.out.println(post.get(i).x);
				return;
			}
		}
	}

	public static class Node{
		long x;
		long a;
		public Node(long x, long a) {
			super();
			this.x = x;
			this.a = a;
		}
		
	}
	
}
