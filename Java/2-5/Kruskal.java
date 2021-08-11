/* $File: Kruskal, $Timestamp: Wed Aug 11 14:17:35 2021 */
import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


public class Kruskal {
  static Scanner scan;

  static Kruskal solver;

  int N;

  int M;

  Graph G;

  UnionFind uf;

  PriorityQueue<Edge> que;

  public static void main(String[] args) {
    try {
      scan   = new Scanner(new FileInputStream(new File(args[0])));
      solver = new Kruskal(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  Kruskal(Scanner scan) {
    N = Integer.parseInt(scan.nextLine());
    M = Integer.parseInt(scan.nextLine());
    G   = new Graph(N);
    uf  = new UnionFind(N);
    que = new PriorityQueue<>(new Comparator<>() {
	@Override
	public int compare(Edge lhs, Edge rhs) {
	  return lhs.cost - rhs.cost;
	}
      });
    for (int i = 0; i < M; i++) {
      String[] entry = scan.nextLine().split("\\s+");
      G.addE(Integer.parseInt(entry[0]), Integer.parseInt(entry[1]), Integer.parseInt(entry[2]));
    }
  }

  void solve() {
    System.out.println(MST(0));
  }

  int MST(int s) {
    int ret = 0;
    que.add(new Edge(-1, s, 0));
    while (!que.isEmpty()) {
      Edge curr = que.remove();
      if (curr.from < 0 || !uf.isJoint(curr.from, curr.to)) {
	if (curr.from >= 0) uf.union(curr.from, curr.to);
	ret += curr.cost;
	for (Edge e :G.E.get(curr.to))
	  if (curr.from < 0 || !uf.isJoint(e.from, e.to))
	    que.add(e);
      }
    }
    return ret;
  }

  class Graph {
    boolean[] V;
    Map<Integer, List<Edge>> E;

    Graph(int size) {
      V = new boolean[size];
      E = new HashMap<>();
      for (int i = 0; i < size; i++) {
	V[i] = false;
	E.putIfAbsent(i, new ArrayList<>());
      }
    }

    void addE(int from, int to, int cost) {
      E.get(from).add(new Edge(from, to, cost));
      E.get(to).add(new Edge(to, from, cost));
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

  class UnionFind {
    int[] parent;
    int[] rank;

    UnionFind(int size) {
      parent = new int[size];
      rank   = new int[size];
      for (int i = 0; i < size; i++) {
	parent[i] = i;
	rank[i]   = 1;
      }
    }

    int find(int x) {
      int p = parent[x];
      if (p == x) {
	return p;
      } else {
	parent[x] = find(p);
	return parent[x];
      }
    }

    boolean isJoint(int x, int y) {
      return find(x) == find(y);
    }

    void union(int x, int y) {
      if (isJoint(x, y)) {
	return;
      } else if (rank[x] < rank[y]) {
	parent[x] = parent[y];
      } else if (rank[x] > rank[y]) {
	parent[y] = parent[x];
      } else {
	parent[x] = parent[y];
	rank[x]++;
      }
    }
  }
}
