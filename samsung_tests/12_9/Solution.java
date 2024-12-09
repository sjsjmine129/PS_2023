import java.io.*;
import java.util.*;
 
public class Solution {
    static final long INF = Long.MAX_VALUE;
    static final int UNVISITED = -1;
    static int N, M;
    static long answer;
    static long[] dist;
    static int[] trace; 
    static boolean[] visited;
    static List<List<Node>> adList;
    static PriorityQueue<Node> pq;
     
    static class Node implements Comparable<Node> {
        int ID;
        long cost;
        boolean checked;
 
        public Node(int ID, long cost) {
            this.ID = ID;
            this.cost = cost;
            this.checked = false;
        }
 
        @Override
        public int compareTo(Node target) {
            if(this.cost - target.cost < 0)
                return -1;
            return 1;
        }
    }
     
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
 
        int T = Integer.parseInt(sc.next());
        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(sc.next()); 
            M = Integer.parseInt(sc.next()); 
             
            adList = new ArrayList<>();
            adList.add(new<Node> ArrayList());
            for(int i=1; i<=N; i++) {
                adList.add(new<Node> ArrayList());
            }
             
            while(M-- > 0) {
                int u = Integer.parseInt((sc.next()));
                int v = Integer.parseInt((sc.next()));
                long cost = Long.parseLong((sc.next()));
                adList.get(u).add(new Node(v, cost));
                adList.get(v).add(new Node(u, cost));
            }
             
            answer = 0;
            pq = new PriorityQueue<>();
            visited = new boolean[N+1];
            dist = new long[N+1];
            trace = new int[N+1];
            Arrays.fill(dist, INF); Arrays.fill(trace, UNVISITED);
             
            dijkstra(1);
             
            visited = null; dist = null;
            trace = null; adList = null;
            System.gc();
             
            System.out.println("#" + tc + " " + answer);
        }
    }
     
    private static void dijkstra(int start) {
        dist[start] = 0; trace[start] = start;
        pq.add(new Node(start, 0));
         
        while(!pq.isEmpty()) {
            Node current =  pq.poll();
            if(visited[current.ID]) continue;
            visited[current.ID] = true;
             
            for(Node next : adList.get(current.ID)) {
                if(dist[next.ID] >= dist[current.ID] + next.cost) {
                    dist[next.ID] = dist[current.ID] + next.cost;
                    if(trace[next.ID] == UNVISITED) {
                        trace[next.ID] = current.ID;    
                    }
                    else {
                        Node A = findEdge(current.ID, next.ID);
                        Node B = findEdge(trace[next.ID], next.ID);
                        if(A.cost < B.cost) trace[next.ID] = current.ID;
                    }
                     
                    pq.add(new Node(next.ID, dist[next.ID]));
                }
            }
        }
         
        tracert(start);
    }
     
    // 다익스트라 경로 추적
    private static void tracert(int start) {
        for(int v = 1; v <= N; v++) {
            // 자기 자신인 경우
            if(v == start) {
                continue;
            }
            int prev;
            for(prev = v; prev != start; prev = trace[prev]) {
                int A = prev;
                int B = trace[prev];
                 
                Node edge = findEdge(A, B); 
                if(edge.checked) {
                    break;
                }
                else {
                    answer += edge.cost;
                    edge.checked = true;
                    Node converseEdge = findEdge(B, A);
                    converseEdge.checked = true;    
                }               
            }
        }
    }
     
    private static Node findEdge(int A, int B) {
        Node edge = null;
        List<Node> list = adList.get(A);
        for(int i=0; i<list.size(); i++) {
            edge = list.get(i);
 
            if(edge.ID == B) {
                break;
            }
        }
        return edge;
    }
}