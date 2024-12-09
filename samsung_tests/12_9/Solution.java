import java.util.*;
import java.io.FileInputStream;

class Solution {
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
            return Long.compare(this.cost, target.cost);
        }
    }

    public static void main(String args[]) throws Exception {
        // Uncomment the following line for testing with an input file.
        // System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            // Read input
            N = sc.nextInt(); 
            M = sc.nextInt();

            // Initialize graph and auxiliary data structures
            initializeGraph();

            for (int i = 0; i < M; i++) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                long cost = sc.nextLong();
                adList.get(u).add(new Node(v, cost));
                adList.get(v).add(new Node(u, cost));
            }

            // Perform Dijkstra's algorithm and calculate the result
            answer = 0;
            pq = new PriorityQueue<>();
            visited = new boolean[N + 1];
            dist = new long[N + 1];
            trace = new int[N + 1];
            Arrays.fill(dist, INF);
            Arrays.fill(trace, UNVISITED);

            dijkstra(1);

            // Free up memory
            visited = null;
            dist = null;
            trace = null;
            adList = null;
            System.gc();

            // Print the result for the test case
            System.out.println("#" + test_case + " " + answer);
        }
    }

    private static void initializeGraph() {
        adList = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            adList.add(new ArrayList<>());
        }
    }

    private static void dijkstra(int start) {
        dist[start] = 0;
        trace[start] = start;
        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            if (visited[current.ID]) continue;
            visited[current.ID] = true;

            for (Node next : adList.get(current.ID)) {
                if (dist[next.ID] >= dist[current.ID] + next.cost) {
                    dist[next.ID] = dist[current.ID] + next.cost;
                    if (trace[next.ID] == UNVISITED) {
                        trace[next.ID] = current.ID;
                    } else {
                        Node A = findEdge(current.ID, next.ID);
                        Node B = findEdge(trace[next.ID], next.ID);
                        if (A.cost < B.cost) trace[next.ID] = current.ID;
                    }
                    pq.add(new Node(next.ID, dist[next.ID]));
                }
            }
        }

        tracert(start);
    }

    private static void tracert(int start) {
        for (int v = 1; v <= N; v++) {
            if (v == start) continue;

            for (int prev = v; prev != start; prev = trace[prev]) {
                int A = prev;
                int B = trace[prev];

                Node edge = findEdge(A, B);
                if (edge.checked) break;

                answer += edge.cost;
                edge.checked = true;

                Node converseEdge = findEdge(B, A);
                converseEdge.checked = true;
            }
        }
    }

    private static Node findEdge(int A, int B) {
        for (Node edge : adList.get(A)) {
            if (edge.ID == B) {
                return edge;
            }
        }
        return null;
    }
}
