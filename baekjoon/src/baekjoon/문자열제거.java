package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


	class erase{
	    String s;
	    int cost;
	 
	    public erase(String s, int cost) {
	        this.s = s;
	        this.cost = cost;
	    }
	}
	public class 문자열제거 {
	    public static void main(String[] args) throws IOException {
	        BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
	 
	        String s = br.readLine();
	        int length = s.length();
	        int m = Integer.parseInt(br.readLine());
	        List<erase> list = new ArrayList<>();
	        for (int i=0 ; i < m; i++){
	            String[] s1 = br.readLine().split(" ");
	            String a = s1[0];
	            int cost = Integer.parseInt(s1[1]);
	            list.add(new erase(a,cost));
	        
	    }
	        int [] dp = new int[length+1];
	        for (int i = 0; i < s.length(); i++){
	            dp[i + 1] = Math.max(dp[i+1], dp[i] + 1);
	            for (int j = 0; j < m; j++){
	                erase now = list.get(j);
	                if (s.startsWith(now.s, i)){
	                    dp[i +now.s.length()] = Math.max(dp[i + now.s.length()], dp[i]+now.cost );
	                }
	            }
	        }
	        System.out.println(dp[s.length()]);
	    }
}
	
