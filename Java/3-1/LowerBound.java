/* $File: LowerBound, $Timestamp: Thu Aug 12 13:33:24 2021 */
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


public class LowerBound {
  static Scanner scan;

  static LowerBound solver;

  int n;

  int[] a;

  int k;

  public static void main(String[] args) {
    try {
      scan   = new Scanner(new FileInputStream(new File(args[0])));
      solver = new LowerBound(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  LowerBound(Scanner scan) {
    n = Integer.parseInt(scan.nextLine());
    a = new int[n];
    String[] entries = scan.nextLine().split("\\s+");
    for (int i = 0; i < n; i++) {
      a[i] = Integer.parseInt(entries[i]);
    }
    k = Integer.parseInt(scan.nextLine());
  }

  void solve() {
    System.out.println(lowerBound(a, n, k));
  }

  int lowerBound(int a[], int len, int target) {
    int lb = -1;
    int ub = len;
    while (ub - lb > 1) {
      int m = (lb + ub) / 2;
      if (a[m] >= target) {
	ub = m;
      } else {
	lb = m;
      }
    }
    return ub;
  }
}
