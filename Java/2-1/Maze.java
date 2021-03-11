/* $File: Maze.java, $Timestamp: Wed Mar 10 03:52:19 2021 */
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

public class Maze {
  private static FastScanner scan;

  private static Maze solver;

  private int N;

  private int M;

  private char[][] maze;

  private int[][] cost;

  private Coord S;

  private Coord G;

  public static void main(String[] args) {
    try {
      scan   = new FastScanner(new FileInputStream(new File(args[0])));
      solver = new Maze(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public Maze(FastScanner scan) {
    this.N = Integer.parseInt(scan.nextLine());
    this.M = Integer.parseInt(scan.nextLine());
    this.maze = new char[this.N][this.M];
    this.cost = new int[this.N][this.M];
    for (int i = 0; i < this.N; i++) {
      scan.nextLine().getChars(0, this.M, this.maze[i], 0);
      for (int j = 0; j < this.M; j++) {
	if (this.maze[i][j] == 'S') this.S = new Coord(i, j);
	if (this.maze[i][j] == 'G') this.G = new Coord(i, j);
	if (this.maze[i][j] == '#') {
	  this.cost[i][j] = -1;
	} else {
	  this.cost[i][j] = Integer.MAX_VALUE;
	}
      }
    }
  }

  private void solve() {
    Queue<Coord> que = new LinkedList<Coord>();
    que.add(this.S);
    this.cost[this.S.x][this.S.y] = 0;
    while (!que.isEmpty()) {
      Coord cur = que.poll();
      for (Dirs d : Dirs.values()) {
	int x = cur.x + d.x;
	int y = cur.y + d.y;
	if (x >= 0 && x < this.N && y >= 0 && y < this.M && this.maze[x][y] != '#') {
	  this.maze[x][y] = '#';
	  this.cost[x][y] = this.cost[cur.x][cur.y] + 1;
	  que.add(new Coord(x, y));
	}
      }
    }
    System.out.println(this.cost[this.G.x][this.G.y]);
  }

  private enum Dirs {
    LEFT(-1, 0),
    RIGHT(1, 0),
    UP(0, 1),
    DOWN(0, -1);

    public int x;

    public int y;

    private Dirs(int x, int y) {
      this.x = x;
      this.y = y;
    }
  }

  private class Coord {
    public int x;

    public int y;

    public Coord(int x, int y) {
      this.x = x;
      this.y = y;
    }

    @Override
    public boolean equals(Object that) {
      if (!(that instanceof Coord)) {
	return false;
      } else {
	Coord coord = (Coord) that;
	return (this.x == coord.x && this.y == coord.y);
      }
    }

    @Override
    public int hashCode() {
      return Objects.hash(this.getSigFields());
    }

    private Object[] getSigFields() {
      Object[] ret = { this.x, this.y };
      return ret;
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
