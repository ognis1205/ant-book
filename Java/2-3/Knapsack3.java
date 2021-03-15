/* $File: Knapsack3.java, $Timestamp: Mon Mar 15 03:10:20 2021 */
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

public class Knapsack3 {
  private static FastScanner scan;

  private static Knapsack3 solver;

  private int n;

  private int max_v;

  private int[] v;

  private int[] w;

  private int W;

  private int[][] dp;

  public static void main(String[] args) {
    try {
      scan   = new FastScanner(new FileInputStream(new File(args[0])));
      solver = new Knapsack3(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public Knapsack3(FastScanner scan) {
    this.n = Integer.parseInt(scan.nextLine());
    this.v = new int[this.n];
    this.w = new int[this.n];
    this.max_v = 0;
    for (int i = 0; i < this.n; i++) {
      String[] tokens = scan.nextLine().split("\\s+");
      this.w[i] = Integer.parseInt(tokens[0]);
      this.v[i] = Integer.parseInt(tokens[1]);
      this.max_v = Math.max(this.max_v, this.v[i]);
    }
    this.W = Integer.parseInt(scan.nextLine());
    this.dp = new int[this.n + 1][this.n * max_v];
    for (int i = 0; i < this.n * this.max_v; i++) this.dp[0][i] = 1000000000;
    this.dp[0][0] = 0;
  }

  private void solve() {
    for (int i = 0; i < this.n; i++) {
      for (int j = 0; j < this.n * this.max_v; j++) {
	if (j >= this.v[i]) {
	  this.dp[i + 1][j] = Math.min(this.dp[i][j - this.v[i]] + this.w[i], this.dp[i][j]);
	} else {
	  this.dp[i + 1][j] = this.dp[i][j];
	}
      }
    }
    int res = 0;
    for (int j = 0; j < this.n * this.max_v; j++) {
      System.out.println(this.dp[this.n][j]);
      if (this.dp[this.n][j] <= this.W) res = j;
    }
    System.out.println(res);
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
