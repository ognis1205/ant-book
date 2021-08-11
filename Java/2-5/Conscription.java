/* $File: Conscription, $Timestamp: Wed Aug 11 20:26:37 2021 */
import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


public class Conscription {
  static Scanner scan;

  static Conscription solver;

  int N;

  int M;

  int R;

  List<Relation> relation;

  UnionFind uf;

  public static void main(String[] args) {
    try {
      scan   = new Scanner(new FileInputStream(new File(args[0])));
      solver = new Conscription(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  Conscription(Scanner scan) {
    N = Integer.parseInt(scan.nextLine());
    M = Integer.parseInt(scan.nextLine());
    R = Integer.parseInt(scan.nextLine());
    relation = new ArrayList<>();
    uf = new UnionFind(N + M);
    for (int i = 0; i < R; i++) {
      String[] entry = scan.nextLine().split("\\s+");
      relation.add(new Relation(Integer.parseInt(entry[0]), 
				Integer.parseInt(entry[1]) + M, 
				-1 * Integer.parseInt(entry[2])));
    }
    Collections.sort(relation, new Comparator<Relation>() {
	@Override
	public int compare(Relation lhs, Relation rhs) {
	  return lhs.cost - rhs.cost;
	}
      });
  }

  void solve() {
    System.out.println(10000 * (N + M) + kruskal());
  }

  int kruskal() {
    int res = 0;
    for (int i = 0; i < R; i++) {
      Relation r = relation.get(i);
      if (!uf.isJoint(r.lhs, r.rhs)) {
	res += r.cost;
	uf.union(r.lhs, r.rhs);
      }
    }
    return res;
  }

  class Relation {
    int lhs;
    int rhs;
    int cost;

    Relation(int lhs, int rhs, int cost) {
      this.lhs = lhs;
      this.rhs = rhs;
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
	rank[i]   = 0;
      }
    }

    int find(int x) {
      int p = parent[x];
      if (p == x) {
	return x;
      } else {
	p = find(p);
	parent[x] = p;
	return p;
      }
    }

    boolean isJoint(int lhs, int rhs) {
      return find(lhs) == find(rhs);
    }

    void union(int lhs, int rhs) {
      int l = find(lhs);
      int r = find(rhs);
      if (l == r) {
	return;
      } else if (rank[l] < rank[r]) {
	parent[l] = r;
      } else if (rank[l] > rank[r]) {
	parent[r] = l;
      } else {
	parent[l] = r;
	rank[l]++;
      }
    }
  }
}
