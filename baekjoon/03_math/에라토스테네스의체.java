package baekjoon;

import java.util.Scanner;

public class 에라토스테네스의체 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
    	int n = sc.nextInt();
    	int k = sc.nextInt();
    	boolean[] check = new boolean[n+1];
    	
    	int cnt = 0;
    	for(int i = 2; i<=n; i++) {
    		for(int j = i; j<=n; j+=i) {
    			if(check[j] == false) {
        			cnt++;
        			check[j] = true;
    			}

    			if(cnt == k) {
    				System.out.println(j);
    				System.exit(0);
    			}
    		}
    	}
	}

}
