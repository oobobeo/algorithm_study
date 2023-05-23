package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class 상어초등학교 {
	static int[][] map, like;
	static int n;
	static PriorityQueue<Student> list;
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        n = Integer.parseInt(br.readLine());
        
        like = new int[n * n][5]; //좋아하는 학생
        for (int i = 0; i < n * n; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	int x = 0;
        	while (st.hasMoreTokens())
        		like[i][x++] = Integer.parseInt(st.nextToken());
        }
        
        map = new int[n][n]; //자리
        for (int i = 0; i < n * n; i++)
        	select(i);
        
        score();
    }
    
    public static void score() { //점수 계산
    	int[] dx = {-1, 1, 0, 0}, dy = {0, 0, 1, -1};
    	
    	int sum = 0;
    	
    	for (int i = 0; i < n; i++) {
    		for (int j = 0; j < n; j++) {
    			int cnt = 0;
    			
				for (int k = 0; k < 4; k++) {//인접거리 체크
					int nx = i + dx[k], ny = j + dy[k];
					
					if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
						for (int x = 0; x < n * n; x++) {
							if (map[i][j] == like[x][0]) {
								for (int q = 1; q <= 4; q++)
									if (map[nx][ny] == like[x][q])//좋아하는 학생 수 cnt
										cnt++;
								break;
							}
						}
					}
				}
				
				switch(cnt) { //점수 계산
					case 1: 
						sum++;
						break;
					case 2:
						sum += 10;
						break;
					case 3:
						sum += 100;
						break;
					case 4:
						sum += 1000;
						break;
				}
    		}
    	}
    	
    	System.out.println(sum);
    }
    
    public static void select(int idx) { //좌석 선택
    	int[] dx = {-1, 1, 0, 0}, dy = {0, 0, 1, -1};
    	list = new PriorityQueue<>(); //비어있는 칸의 좌표, 주변의 친구, 빈자리 저장
    	
    	for (int i = 0; i < n; i++) {
    		for (int j = 0; j < n; j++) {
    			if (map[i][j] == 0) {
    				int cnt = 0, empty = 0;
    				
    				for (int k = 0; k < 4; k++) { //인접 거리 체크
    					int nx = i + dx[k], ny = j + dy[k];
    					if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
    						for (int q = 1; q <= 4; q++) { //좋아하는 학생 cnt
    							if (map[nx][ny] == like[idx][q])
    								cnt++;
    						}
    						if (map[nx][ny] == 0) //빈자리 cnt
								empty++;
    					}
    				}
    				list.add(new Student(i, j, cnt, empty));
    			}
    		}
    	}
    	
    	Student s = list.poll();
    	map[s.x][s.y] = like[idx][0]; //자리정함
    } 
}
class Student implements Comparable<Student> {// 좌표, 좋아하는 학생 수, 빈자리 수
	int x, y, cnt, empty;
	
	public Student(int x, int y, int cnt, int empty) {
		this.x = x;
		this.y = y;
		this.cnt = cnt;
		this.empty = empty;
	}

	@Override
	public int compareTo(Student o) {// 우선순위 구현
		if (o.cnt == cnt) {
			if (o.empty == empty) {
				if (o.x == x)
					return y - o.y;
				return x - o.x;
			}
			return o.empty - empty;
		}
		return o.cnt - cnt;
	}
}