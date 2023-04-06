package baekjoon;

import java.util.Scanner;
//이진검색트리 후위탐색 중위탐색 전위턈색 순서 기억 
public class 이진검색트리 {

	static Node node;
	static class Node{
		int num;
		Node left, right;
		
		
		public Node(int num) {
			super();
			this.num = num;
		}
		public Node(int num, Node left, Node right) {
			super();
			this.num = num;
			this.left = left;
			this.right = right;
		}
		void insert(int n) {
			if (n < this.num) {
				if (this.left == null) this.left = new Node(n);
				else this.left.insert(n);
			}else {
				if (this.right == null) this.right = new Node(n);
				else this.right.insert(n);
			}
		}
	}
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		node = new Node(n);
		while (sc.hasNext()) {
			try {
				n = sc.nextInt();
				node.insert(n);
			}catch(Exception e) {
				break;
			}
		}
		postOrder(node);
	}

	static void postOrder(Node node) {
		if (node == null) return;
		postOrder(node.left);
		postOrder(node.right);
		System.out.println(node.num);
	}
}
