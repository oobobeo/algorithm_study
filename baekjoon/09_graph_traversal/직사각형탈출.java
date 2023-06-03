package baekjoon;

import java.util.*;
import java.io.*;

public class 직사각형탈출 {  
	
	static int N, M;
	static int h, w, sx, sy, fx, fy;
	static int[][] map;
	
	static List<Pos> list;
	
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};
	
	static int ans;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		list = new ArrayList<>(); // 벽 위치 넣을 리스트
		map = new int[N+1][M+1];
		for(int i=1; i<=N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j=1; j<=M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if(map[i][j] == 1) {
					map[i][j] = -1; // 벽 위치의 값을 -1로 교체
					list.add(new Pos(i, j)); // 벽 위치를 리스트에 넣음
				}
			}
		}
		
		st = new StringTokenizer(br.readLine(), " ");
		h = Integer.parseInt(st.nextToken()); // 사각형 가로 길이
		w = Integer.parseInt(st.nextToken()); // 사각형 세로 길이
		sx = Integer.parseInt(st.nextToken()); // 시작 위치
		sy= Integer.parseInt(st.nextToken()); // 시작 위치
		fx = Integer.parseInt(st.nextToken()); // 목표 위치
		fy = Integer.parseInt(st.nextToken()); // 목표 위치
		
		ans = -1; // 답 ( 최소 거리 )
		bfs();
		System.out.println(ans);
	}
	
	static void bfs() {
		Queue<Pos> que = new LinkedList<>();
		boolean[][] isChecked = new boolean[N+1][M+1];
		
		que.add(new Pos(sx, sy));
		isChecked[sx][sy] = true;
		
		while(!que.isEmpty()) {
			Pos p = que.poll();
			
			int curX = p.x;
			int curY = p.y;
			
			// 목표 위치에 도달하면 탐색 종료
			if(curX == fx && curY == fy) {
				ans = map[curX][curY];
				return;
			}
			
			for(int t=0; t<4; t++) {
				int nx = curX + dx[t];
				int ny = curY + dy[t];
				
				// 탐색한 위치의 범위와 방문 여부 체크
				if(nx < 1 || ny < 1 || nx > N || ny > M || isChecked[nx][ny]) continue;				
				// 해당 사각형의 범위와 벽이 있는지 체크
				if(!isPossible(nx, ny)) continue;
				
				// 이동 가능한 위치면 Queue에 넣고 방문 체크, 거리값 삽입
				if(map[nx][ny] == 0) {
					que.add(new Pos(nx, ny));
					isChecked[nx][ny] = true;
					map[nx][ny] = map[curX][curY] + 1;
				}
			}

		}
		
	}
	
	// 사각형이 있을 수 있는지 체크하는 메소드
	static boolean isPossible(int x, int y) {
		// 사각형이 범위를 벗어나면 false 반환
		if(x+h-1 > N || y+w-1 > M) return false;
		// 벽의 위치를 차례로 꺼내서 범위 체크
		for(int i=0; i<list.size(); i++) {
			Pos p = list.get(i);
			
			int px = p.x;
			int py = p.y;
			
			if(px >= x && px <= x+h-1 && py >= y && py <= y+w-1) {
				return false;
			}
		}
		
		
		
		return true;
	}
	
	static class Pos {
		int x, y;
		
		Pos(int x, int y){
			this.x = x;
			this.y = y;
		}
	}
}  