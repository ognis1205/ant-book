/* $File: Layout, $Timestamp: Wed Aug 11 23:56:40 2021 */
import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


public class Layout {
  static Scanner scan;

  static Layout solver;

  int N;

  int ML;

  int MD;

  Graph G;

  static int INF = 1_000_000;

  public static void main(String[] args) {
    try {
      scan   = new Scanner(new FileInputStream(new File(args[0])));
      solver = new Layout(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  Layout(Scanner scan) {
    N  = Integer.parseInt(scan.nextLine());
    ML = Integer.parseInt(scan.nextLine());
    MD = Integer.parseInt(scan.nextLine());
    G  = new Graph(N);
    for (int i = 0; i < ML; i++) {
      String[] entry = scan.nextLine().split("\\s+");
      G.addE(Integer.parseInt(entry[0]) - 1, Integer.parseInt(entry[1]) - 1, Integer.parseInt(entry[2]));
    }
    for (int i = 0; i < MD; i++) {
      String[] entry = scan.nextLine().split("\\s+");
      G.addE(Integer.parseInt(entry[1]) - 1, Integer.parseInt(entry[0]) - 1, -1 * Integer.parseInt(entry[2]));
    }
    for (int i = 1; i < N; i++) {
      G.addE(i, i - 1, 0);
    }
  }

  void solve() {
    bellmanFord();
    System.out.println(G.V[N - 1]);
  }

  void bellmanFord() {
    G.V[0] = 0;
    for (int i = 0; i < G.V.length; i++) {
      for (Edge e : G.E)
	if (G.V[e.u] != INF && G.V[e.v] > G.V[e.u] + e.w)
	  G.V[e.v] = G.V[e.u] + e.w;
    }
  }

  class Edge {
    int u;
    int v;
    int w;

    Edge(int u, int v, int w) {
      this.u = u;
      this.v = v;
      this.w = w;
    }
  }

  class Graph {
    int[] V;
    List<Edge> E;
    
    Graph(int size) {
      this.V = new int[size];
      this.E = new ArrayList<>();
      for (int i = 0; i < size; i++) V[i] = INF;
    }

    void addE(int u, int v, int w) {
      this.E.add(new Edge(u, v, w));
    }
  }
}
