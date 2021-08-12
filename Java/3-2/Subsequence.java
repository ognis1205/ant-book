/* $File: Subsequence, $Timestamp: Thu Aug 12 23:06:47 2021 */
import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


public class Subsequence {
  static Scanner scan;

  static Subsequence solver;

  int n;

  int s;

  int[] a;

  TwoPointers tp;

  public static void main(String[] args) {
    try {
      scan   = new Scanner(new FileInputStream(new File(args[0])));
      solver = new Subsequence(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  Subsequence(Scanner scan) {
    n = Integer.parseInt(scan.nextLine());
    s = Integer.parseInt(scan.nextLine());
    a = new int[n];
    String[] entries = scan.nextLine().split("\\s+");
    for (int i = 0; i < n; i++) {
      a[i] = Integer.parseInt(entries[i]);
    }
    tp = new TwoPointers(s);
  }

  void solve() {
    int res = Integer.MAX_VALUE;
    for (int i = 0; i < n; i++) {
      tp.add(i, a[i]);
      while (tp.isSatisfied()) {
	res = Math.min(res, tp.length());
	tp.remove();
      }
    }
    System.out.println(res);
  }

  class TwoPointers {
    int target;
    Queue<WithIndex> que;

    TwoPointers(int target) {
      this.target = target;
      this.que = new ArrayDeque<>();
    }

    void add(int index, int value) {
      this.que.add(new WithIndex(index, value));
    }

    void remove() {
      this.que.remove();
    }

    int length() {
      return this.que.size();
    }

    boolean isSatisfied() {
      return this.target <= this.que
	.stream()
	.map(x -> x.value)
	.reduce(0, Integer::sum);
    }
  }

  class WithIndex {
    int index;
    int value;

    WithIndex(int index, int value) {
      this.index = index;
      this.value = value;
    }
  }
}
