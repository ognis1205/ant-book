/* $File: Lottery.java, $Timestamp: Thu Mar  4 16:15:00 2021 */
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;

public class Lottery {
  private static FastScanner scanner;
  private static Lottery solver;

  public static void main(String[] args) {
    solver = new Lottery();
    scanner = solver.new FastScanner(args[0]);
    try {
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  private void solve() {
    int   n  = Integer.parseInt(scanner.next());
    int   m  = Integer.parseInt(scanner.next());
    int[] k  = Arrays.stream(scanner.next().split(",")).mapToInt(s -> Integer.parseInt(s)).toArray();
    int[] kk = new int[4096];

    int p = 0;
    for (int i = 0; i < n; i++) {
      for (int j = i; j < n; j++) {
	kk[p++] = k[i] + k[j];
      }
    }

    sort(kk, 0, n * (n + 1) / 2);
    for (int i = 0; i < n; i++) {
      for (int j = i; j < n; j++) {
	if (search(kk, 0, n * (n + 1) / 2, m - k[i] - k[j])) {
	  System.out.println("Yes");
	  return;
	}
      }
    }
    System.out.println("No");
  }

  private static boolean search(int[] arr, int s, int e, int t) {
    if (s     >= e) return false;
    if (s + 1 == e) return arr[s] == t;
    int m = s + (e - s) / 2;
    if (t == arr[m]) return true;
    if (t  < arr[m]) return search(arr,     s, m, t);
    if (t  > arr[m]) return search(arr, m + 1, e, t);
    return false;
  }

  private static void sort(int[] arr, int s, int e) {
    if (s != e && s + 1 != e) {
      int p = arr[s + (e - s) / 2];
      int l = partition(arr, s, e, k -> k  < p);
      int r = partition(arr, l, e, k -> k <= p);
      sort(arr, s, l);
      sort(arr, r, e);
    }
  }

  private static int partition(int[] arr, int s, int e, IntPredicate pred) {
    int ret = s;
    for (int i = s; i < e; i++) {
      if (pred.test(arr[i])) {
	if (i != ret) swap(arr, i, ret);
	ret++;
      }
    }
    return ret;
  }

  private static void swap(int[] arr, int i, int j) {
    int t  = arr[i];
    arr[i] = arr[j];
    arr[j] = t;
  }

  private interface Predicate {
    boolean call(int x);
  }
  
  private class FastScanner {
    private InputStream in;
    private byte[] buffer;
    private int ptr;
    private int len;

    public FastScanner() {
      this.in = System.in;
      this.buffer = new byte[1024];
      this.ptr = 0;
      this.len = 0;
    }

    public FastScanner(String input) {
      try {
	this.in = new FileInputStream(new File(input));
	this.buffer = new byte[1024];
	this.ptr = 0;
	this.len = 0;
      } catch (FileNotFoundException e) {
	e.printStackTrace();
      }
    }

    private boolean hasNextByte() {
      if (ptr < len) {
        return true;
      } else {
        ptr = 0;
        try {
          len = in.read(buffer);
        } catch (IOException e) {
          e.printStackTrace();
        }
        if (len <= 0) return false;
      }
      return true;
    }

    private int readByte() {
      if (hasNextByte()) return buffer[ptr++];
      else return -1;
    }

    private boolean isPrintableChar(int c) {
      return 33 <= c && c <= 126;
    }

    public boolean hasNext() {
      while (hasNextByte() && !this.isPrintableChar(buffer[ptr])) ptr++;
      return hasNextByte();
    }

    public String next() {
      if (!hasNext()) throw new NoSuchElementException();
      StringBuilder sb = new StringBuilder();
      int b = readByte();
      while (this.isPrintableChar(b)) {
        sb.appendCodePoint(b);
        b = readByte();
      }
      return sb.toString();
    }

    public long nextLong() {
      if (!hasNext()) throw new NoSuchElementException();
      long n = 0;
      boolean minus = false;
      int b = readByte();
      if (b == '-') {
        minus = true;
        b = readByte();
      }
      if (b < '0' || '9' < b) throw new NumberFormatException();
      while (true) {
        if ('0' <= b && b <= '9') {
          n *= 10;
          n += b - '0';
        } else if (b == -1 || !this.isPrintableChar(b)) {
          return minus ? -n : n;
        } else {
          throw new NumberFormatException();
        }
        b = readByte();
      }
    }
    public int nextInt() {
      long nl = nextLong();
      if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) throw new NumberFormatException();
      return (int) nl;
    }

    public double nextDouble() {
      return Double.parseDouble(next());
    }
  }
}
