/* $File: Roadblocks, $Timestamp: Wed Aug 11 15:39:33 2021 */
import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


public class Roadblocks {
  static Scanner scan;

  static Roadblocks solver;

  static int MAX_VALUE = 1_000_000;

  int N;

  int R;

  Graph G;

  PriorityQueue<Propagate> que;

  public static void main(String[] args) {
    try {
      scan   = new Scanner(new FileInputStream(new File(args[0])));
      solver = new Roadblocks(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  Roadblocks(Scanner scan) {
    N = Integer.parseInt(scan.nextLine());
    R = Integer.parseInt(scan.nextLine());
    G = new Graph(N);
    que = new PriorityQueue<>(new Comparator<>() {
        @Override
        public int compare(Propagate lhs, Propagate rhs) {
          return lhs.aux - rhs.aux;
        }
      });
    for (int i = 0; i < R; i++) {
      String[] entry = scan.nextLine().split("\\s+");
      G.addE(Integer.parseInt(entry[0]), Integer.parseInt(entry[1]), Integer.parseInt(entry[2]));
    }
  }

  void solve() {
    bfs(0);
    System.out.println(G.V1[N - 1]);
    System.out.println(G.V2[N - 1]);
  }

  void bfs(int s) {
    G.V1[s] = 0;
    G.V2[s] = 0;
    for (Edge e: G.E.get(s))
      que.add(new Propagate(e.to, e.cost));
    while (!que.isEmpty()) {
      Propagate p = que.remove();
      List<Edge> es = G.E.get(p.to);
      int d = p.aux;
      if (G.V1[p.to] > d) {
        int t = G.V1[p.to];
        G.V1[p.to] = d;
        d = t;
        for (Edge e: es) que.add(new Propagate(e.to, G.V1[e.from] + e.cost));
      }
      if (G.V2[p.to] > d && G.V1[p.to] < d) {
        G.V2[p.to] = d;
        for (Edge e: es) que.add(new Propagate(e.to, G.V2[e.from] + e.cost));
      }
    }
  }

  class Propagate {
    int to;
    int aux;

    Propagate(int to, int aux) {
      this.to  = to;
      this.aux = aux;
    }
  }

  class Edge {
    int from;
    int to;
    int cost;

    Edge(int from, int to, int cost) {
      this.from = from;
      this.to   = to;
      this.cost = cost;
    }
  }

  class Graph {
    int[] V1;
    int[] V2;
    Map<Integer, List<Edge>> E;

    Graph(int size) {
      V1 = new int[size];
      V2 = new int[size];
      E  = new HashMap<>();
      for (int i = 0; i < size; i++) {
        V1[i] = MAX_VALUE;
        V2[i] = MAX_VALUE;
        E.putIfAbsent(i, new ArrayList<>());
      }
    }

    void addE(int from, int to, int cost) {
      E.get(from).add(new Edge(from, to, cost));
      E.get(from).add(new Edge(from, to, cost));
    }
  }
}
