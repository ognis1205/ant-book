/* $File: LakeCounting.java, $Timestamp: Mon Mar  8 23:15:17 2021 */
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

public class LakeCounting {
  private static FastScanner scan;
  private static LakeCounting solver;
  private int N;
  private int M;
  private char[][] lake;

  public static void main(String[] args) {
    try {
      scan   = new FastScanner(new FileInputStream(new File(args[0])));
      solver = new LakeCounting(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public LakeCounting(FastScanner scan) {
    this.N = Integer.parseInt(scan.nextLine());
    this.M = Integer.parseInt(scan.nextLine());
    this.lake = new char[N][M];
    for (int i = 0; i < this.N; i++) {
      scan.nextLine().getChars(0, this.M, this.lake[i], 0);
    }
  }

  private void solve() {
    int count = 0;
    for (int i = 0; i < this.N; i++) {
      for (int j = 0; j < this.M; j++) {
	if (this.lake[i][j] == 'W') {
	  count++;
	  this.dfs(i, j);
	}
      }
    }
    System.out.println(count);
  }

  private void dfs(int x, int y) {
    for (int i = -1; i < 2; i++) {
      for (int j = -1; j < 2; j++) {
	if (x + i >= 0 && x + i < this.N && y + j >= 0 && y + j < this.M && this.lake[x + i][y + j] == 'W') {
	  this.lake[x + i][y + j] = '.';
	  this.dfs(x + i, y + j);
	}
      }
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
