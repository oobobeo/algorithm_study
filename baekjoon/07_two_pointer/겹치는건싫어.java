package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 겹치는건싫어 {

        static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        static int []arr;
        static int []cnt;
        public static void main(String[] args) throws IOException {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            arr = new int[n];
            cnt = new int[100001];
            st = new StringTokenizer(br.readLine());
            for(int i=0;i<n;i++)
                arr[i] = Integer.parseInt(st.nextToken());

            int l =0, r= 0;
            int ans = 0 ;
            while(l<=r)
            {
              if(r<=n-1 &&cnt[arr[r]] <k)
              {
                  cnt[arr[r]]++;
                  r++;

              }
              else if(cnt[arr[r]] == k)
              {
                  cnt[arr[l]]--;
                  l++;
              }

                ans = Math.max(ans, r - l);
                if(r == n)
                    break;
            }
            System.out.println(ans);
        }

    }

