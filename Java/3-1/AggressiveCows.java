/* $File: AggressiveCows, $Timestamp: Thu Aug 12 22:14:09 2021 */
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


public class AggressiveCows {
  static Scanner scan;

  static AggressiveCows solver;

  int N;

  int M;

  int[] x;

  public static void main(String[] args) {
    try {
      scan   = new Scanner(new FileInputStream(new File(args[0])));
      solver = new AggressiveCows(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  AggressiveCows(Scanner scan) {
    N = Integer.parseInt(scan.nextLine());
    M = Integer.parseInt(scan.nextLine());
    x = new int[N];
    String[] entries = scan.nextLine().split("\\s+");
    for (int i = 0; i < N; i++) {
      x[i] = Integer.parseInt(entries[i]);
    }
    Arrays.sort(x);
  }

  void solve() {
    System.out.println(upper());
  }

  int upper() {
    int lb = 0;
    int ub = Integer.MAX_VALUE;
    while (ub - lb > 1) {
      int m = (lb + ub) / 2;
      if (C(m)) {
	lb = m;
      } else {
	ub = m;
      }
    }
    return lb;
  }

  boolean C(int d) {
    int res  = M;
    int prev = 0;
    for (int i = 0; i < N; i++) {
      if (x[i] >= prev) {
	res--;
	prev = x[i] + d;
      }
    }
    return res <= 0;
  }
}
