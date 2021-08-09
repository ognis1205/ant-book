/* $File: Knapsack2, $Timestamp: Tue Aug 10 02:25:50 2021 */
import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

public class Knapsack2 {
  private static FastScanner scan;

  private static Knapsack2 solver;

  private static int MAX_VALUE = 1_000;

  private static long MAX_WEIGHT = 100_000_000_000L;

  private int N;

  private int W;

  private int[] w;

  private int[] v;

  private long[][] dp;

  public static void main(String[] args) {
    try {
      scan   = new FastScanner(new FileInputStream(new File(args[0])));
      solver = new Knapsack2(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public Knapsack2(FastScanner scan) {
    String[] header = scan.nextLine().split("\\s+");
    N = Integer.parseInt(header[0]);
    W = Integer.parseInt(header[1]);
    w = new int[N + 1];
    v = new int[N + 1];
    w[0] = v[0] = 0;
    for (int i = 1; i <= N; i++) {
      String[] entry = scan.nextLine().split("\\s+");
      w[i] = Integer.parseInt(entry[0]);
      v[i] = Integer.parseInt(entry[1]);
    }
    dp = new long[N + 1][MAX_VALUE * N + 1];
    for (int i = 0; i < N + 1; i++)
      for (int j = 0; j < MAX_VALUE * N + 1; j++)
	dp[i][j] = MAX_WEIGHT;
    for (int i = 0; i < N + 1; i++)
      dp[i][0] = 0;
  }

  private void solve() {
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= MAX_VALUE * N; j++) {
	if (v[i] > j) dp[i][j] = dp[i - 1][j];
	else dp[i][j] = Math.min(dp[i - 1][j - v[i]] + w[i], dp[i - 1][j]);
      }
    }
    int res = 0;
    for (int i = 1; i <= MAX_VALUE * N; i++)
      if (dp[N][i] <= W) res = i;
    System.out.println(res);
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
