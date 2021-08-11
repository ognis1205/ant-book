/* $File: Prim, $Timestamp: Wed Aug 11 12:28:30 2021 */
import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


public class Prim {
  static Scanner scan;

  static Prim solver;

  int N;

  int M;

  boolean[] V;

  Map<Integer, List<Edge>> E;

  PriorityQueue<Edge> que;

  public static void main(String[] args) {
    try {
      scan   = new Scanner(new FileInputStream(new File(args[0])));
      solver = new Prim(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  Prim(Scanner scan) {
    N = Integer.parseInt(scan.nextLine());
    M = Integer.parseInt(scan.nextLine());
    V = new boolean[N];
    E = new HashMap<>();
    for (int i = 0; i < N; i++) {
      V[i] = false;
      E.putIfAbsent(i, new ArrayList<>());
    }
    for (int i = 0; i < M; i++) {
      String[] edge = scan.nextLine().split("\\s+");
      int from = Integer.parseInt(edge[0]);
      int to   = Integer.parseInt(edge[1]);
      int cost = Integer.parseInt(edge[2]);
      E.get(from).add(new Edge(to, cost));
      E.get(to).add(new Edge(from, cost));
    }
    que = new PriorityQueue<>(new Comparator<>() {
	@Override
	public int compare(Edge lhs, Edge rhs) {
	  return lhs.cost - rhs.cost;
	}
      });
  }

  void solve() {
    System.out.println(MST(0));
  }

  int MST(int v) {
    int cost = 0;
    que.add(new Edge(v, 0));
    while (!que.isEmpty()) {
      Edge curr = que.remove();
      if (!V[curr.to]) {
	cost += curr.cost;
	V[curr.to] = true;
	for (Edge e : E.get(curr.to))
	  if (!V[e.to]) que.add(e);
      }
    }
    return cost;
  }

  class Edge {
    int to;
    int cost;
    Edge(int to, int cost) {
      this.to   = to;
      this.cost = cost;
    }
  }
}
