/* $File: TopologicalSort, $Timestamp: Tue Aug 10 21:40:53 2021 */
import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

public class TopologicalSort {
  static class Graph<V, E> {
    public static class Vertex<V> {
      public V data;

      public Vertex(V data) {
	this.data = data;
      }
    }

    public static class Edge<E> {
      public final Integer to;

      public E data;

      public Edge(Integer to) {
	this(to, null);
      }

      public Edge(Integer to, E data) {
	this.to   = to;
	this.data = data;
      }

      @Override
      public int hashCode() {
	return Objects.hash(to);
      }
    }

    private Map<Integer, Vertex<V>> vertex;

    private Map<Integer, List<Edge<E>>> adjacency;

    public Graph() {
      this.vertex    = new HashMap<>();
      this.adjacency = new HashMap<>();
    }

    public void addV(Integer id, V data) {
      vertex.putIfAbsent(id, new Vertex<>(data));
      adjacency.putIfAbsent(id, new ArrayList<>());
    }

    public void removeV(Integer id) {
      Edge<E> e = new Edge<>(id);
      vertex.remove(id);
      adjacency.values().stream().forEach(es -> es.remove(e));
      adjacency.remove(id);
    }

    public void addE(Integer lhs, Integer rhs, E data) {
      adjacency.get(lhs).add(new Edge<>(rhs, data));
    }

    public void removeE(Integer lhs, Integer rhs) {
      List<Edge<E>> es = adjacency.get(lhs);
      if (es != null) es.remove(new Edge<>(rhs));
    }

    public Stack<Vertex<V>> sort() {
      Stack<Vertex<V>> stack = new Stack<>();
      Map<Integer, Boolean> visited = new HashMap<>();
      Set<Integer> keys = vertex.keySet();
      for (Integer id : keys) 
	visited.put(id, false);
      for (Integer id : keys)
	if (!visited.getOrDefault(id, true))
	  sort(id, visited, stack);
      return stack;
    }

    private void sort(Integer id, Map<Integer, Boolean> visited, Stack<Vertex<V>> stack) {
      visited.put(id, true);
      List<Edge<E>> es = adjacency.get(id);
      for (Edge<E> e : es)
	if (!visited.get(e.to)) sort(e.to, visited, stack);
      stack.push(vertex.get(id));
    }
  }

  private static FastScanner scan;

  private static TopologicalSort solver;

  public static void main(String[] args) {
    try {
      scan   = new FastScanner(new FileInputStream(new File(args[0])));
      solver = new TopologicalSort(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public TopologicalSort(FastScanner scan) {
  }

  private void solve() {
    Graph<String, String> g = new Graph<>();
    g.addV(0, "vertex0");
    g.addV(1, "vertex1");
    g.addV(2, "vertex2");
    g.addV(3, "vertex3");
    g.addV(4, "vertex4");
    g.addV(5, "vertex5");
    g.addE(5, 2, "edge0");
    g.addE(5, 0, "edge1");
    g.addE(4, 0, "edge2");
    g.addE(4, 1, "edge3");
    g.addE(2, 3, "edge4");
    g.addE(3, 1, "edge5");

    Stack<Graph.Vertex<String>> sorted = g.sort();
    while (!sorted.isEmpty()) {
      System.out.println(sorted.pop().data);
    }
  }

  private static int getLowerBound(int[] target, int key) {
    int l = 0;
    int r = target.length - 1;
    int m = (l + r) / 2;
    while (true) {
      if (target[m] == key || target[m] > key) {
        r = m - 1;
        if (r < l) return m;
      } else {
        l = m + 1;
        if (r < l) return m < target.length - 1 ? m + 1 : -1;
      }
      m = (l + r) / 2;
    }
  }

  private static int getUpperBound(int[] target, int key) {
    int l = 0;
    int r = target.length - 1;
    int m = (l + r) / 2;
    while (true) {
      if (target[m] == key || target[m] < key) {
        l = m + 1;
        if (r < l) return m < target.length - 1 ? m + 1 : -1;
      } else {
        r = m - 1;
        if (r < l) return m;
      }
      m = (l + r) / 2;
    }
  }

  private static class FastScanner implements Closeable {
    private InputStream in;
    private byte[] buffer;
    private int ptr;
    private int len;
    private boolean[] isSpace;

    public FastScanner(InputStream in) {
      this.in = in;
      this.buffer = new byte[1 << 15];
      this.ptr = 0;
      this.len = 0;
      this.isSpace = new boolean[128];
      this.isSpace[' '] = this.isSpace['\n'] = this.isSpace['\r'] = this.isSpace['\t'] = true;
    }

    public void setSpace(char... cs) {
      Arrays.fill(this.isSpace, false);
      this.isSpace['\r'] = this.isSpace['\n'] = true;
      for (char c : cs) this.isSpace[c] = true;
    }
        
    private int read() {
      if (this.len == -1) return -1;
      if (this.ptr >= this.len) {
        this.ptr = 0;
        if (this.in == null) return this.len = -1;
        try {
          this.len = this.in.read(this.buffer);
        } catch (IOException e) {
          throw new RuntimeException(e);
        }
        if (this.len <= 0) return -1;
      }
      return this.buffer[this.ptr++];
    }

    public boolean hasNext() {
      int c = this.read();
      while (c >= 0 && this.isSpace[c]) c = this.read();
      if (c == -1) return false;
      this.ptr--;
      return true;
    }

    public void skipLine() {
      if (this.ptr > 0 && this.buffer[this.ptr - 1] == '\n') {
        this.buffer[this.ptr - 1] = ' ';
        return;
      }
      int c = this.read();
      if (c < 0) return;
      while (c >= 0 && c != '\n' && c != '\r') c = this.read();
      if (c == '\r') this.read();
      if (this.ptr > 0) this.buffer[this.ptr - 1] = ' ';
    }

    public String next() {
      if (!hasNext()) throw new InputMismatchException();
      StringBuilder sb = new StringBuilder();
      int c = this.read();
      while (c >= 0 && !this.isSpace[c]) {
        sb.append((char)c);
        c = this.read();
      }
      return sb.toString();
    }
        
    public String nextLine() {
      StringBuilder sb = new StringBuilder();
      if (this.ptr > 0 && this.buffer[this.ptr - 1] == '\n') {
        this.buffer[this.ptr - 1] = ' ';
        return "";
      }
      int c = this.read();
      if (c < 0) throw new InputMismatchException();
      while (c >= 0 && c != '\n' && c != '\r') {
        sb.append((char)c);
        c = this.read();
      }
      if (c == '\r') this.read();
      if (this.ptr > 0) this.buffer[this.ptr - 1] = ' ';
      return sb.toString();
    }

    public FastScanner scanLine() {
      return new FastScanner(new ByteArrayInputStream(this.nextLine().getBytes(StandardCharsets.UTF_8)));
    }

    public int nextInt() {
      if (!hasNext()) throw new InputMismatchException();
      int c = this.read();
      int sgn = 1;
      if (c == '-') {
        sgn = -1;
        c = this.read();
      }
      int res = 0;
      do {
        if (c < '0' || c > '9') throw new InputMismatchException();
        res *= 10;
        res += c - '0';
        c = this.read();
      } while (c >= 0 && !this.isSpace[c]);
      return res * sgn;
    }

    public long nextLong() {
      if (!hasNext()) throw new InputMismatchException();
      int c = this.read();
      int sgn = 1;
      if (c == '-') {
        sgn = -1;
        c = this.read();
      }
      long res = 0;
      do {
        if (c < '0' || c > '9') throw new InputMismatchException();
        res *= 10;
        res += c - '0';
        c = this.read();
      } while (c >= 0 && !this.isSpace[c]);
      return res * sgn;
    }

    public double nextDouble() {
      return Double.parseDouble(next());
    }
        
    @Override
    public void close() {
      try {
        if (in != null) in.close();
      } catch (IOException e) {
        e.printStackTrace();
      }
    }
  }
}
