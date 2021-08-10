/* $File: FoodChain, $Timestamp: Tue Aug 10 18:24:54 2021 */
import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

public class FoodChain {
  private static class UnionFind<T> {
    private Map<T, T> parent;

    private Map<T, Integer> rank;

    public UnionFind() {
      parent = new HashMap<>();
      rank   = new HashMap<>();
    }

    public void add(T entry) {
      parent.put(entry, entry);
      rank.put(entry, 0);
    }

    public boolean contains(T entry) {
      return parent.containsKey(entry);
    }

    public T find(T entry) {
      T p = parent.get(entry);
      if (entry.equals(p)) {
	return p;
      } else {
	p = find(p);
	parent.put(entry, p);
	return p;
      }
    }

    public boolean isDisjoint(T lhs, T rhs) {
      return !(find(lhs).equals(find(rhs)));
    }

    public void union(T lhs, T rhs) {
      T l = find(lhs);
      T r = find(rhs);
      if (l.equals(r)) {
	return;
      } else if (rank.get(l) < rank.get(r)) {
	parent.put(l, r);
      } else if (rank.get(l) > rank.get(r)) {
	parent.put(r, l);
      } else {
	parent.put(l, r);
	rank.put(l, rank.get(l) + 1);
      }
    }
  }

  private static class Info {
    public final int type;
    public final int x;
    public final int y;

    public Info(int type, int x, int y) {
      this.type = type;
      this.x = x;
      this.y = y;
    }

    @Override
    public boolean equals(Object that) {
      if (!(that instanceof Info)) return false;
      Info info = (Info) that;
      return this.type == info.type && this.x == info.x && this.y == info.y;
    }

    @Override
    public int hashCode() {
      return Objects.hash(type, x, y);
    }
  }

  private static FastScanner scan;

  private static FoodChain solver;

  private int N;

  private int K;

  private Info[] I;

  private UnionFind<Integer> uf;

  public static void main(String[] args) {
    try {
      scan   = new FastScanner(new FileInputStream(new File(args[0])));
      solver = new FoodChain(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public FoodChain(FastScanner scan) {
    N = Integer.parseInt(scan.nextLine());
    K = Integer.parseInt(scan.nextLine());
    I = new Info[K];
    for (int i = 0; i < K; i++) {
      String[] info = scan.nextLine().split("\\s+");
      I[i] = new Info(Integer.parseInt(info[0]), Integer.parseInt(info[1]), Integer.parseInt(info[2]));
    }
    uf = new UnionFind<>();
    for (int i = 0; i < N; i++) {
      uf.add(A(i));
      uf.add(B(i));
      uf.add(C(i));
    }
  }

  private void solve() {
    int res = 0;
    for (Info info : I) {
      if (!validate(info)) {
	res++;
	continue;
      } else if (info.type == 1) {
	if (isSame(info.x, info.y) || doesEat(info.y, info.x)) {
	  res++;
	  continue;
	} else {
	  eat(info.x, info.y);
	}
      } else {
	if (doesEat(info.x, info.y) || doesEat(info.y, info.x)) {
	  res++;
	  continue;
	} else {
	  same(info.x, info.y);
	}
      }
    }
    System.out.println(res);
  }

  private void eat(int sbj, int obj) {
    uf.union(A(sbj), B(obj));
    uf.union(B(sbj), C(obj));
    uf.union(C(sbj), A(obj));
  }

  private void same(int sbj, int obj) {
    uf.union(A(sbj), A(obj));
    uf.union(B(sbj), B(obj));
    uf.union(C(sbj), C(obj));
  }

  private boolean doesEat(int sbj, int obj) {
    return !uf.isDisjoint(A(sbj), B(obj));
  }

  private boolean isSame(int sbj, int obj) {
    return !uf.isDisjoint(A(sbj), A(obj));
  }

  private int A(int x) {
    return x;
  }

  private int B(int x) {
    return x + N;
  }

  private int C(int x) {
    return x + 2 * N;
  }

  private boolean validate(Info info) {
    return info.x >= 1 && info.x <= N && info.y >= 1 && info.y <= N;
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
