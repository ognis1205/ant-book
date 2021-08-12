/* $File: MaximumAverage, $Timestamp: Thu Aug 12 22:38:42 2021 */
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


public class MaximumAverage {
  static Scanner scan;

  static MaximumAverage solver;

  int n;

  int k;

  int[] w;

  int[] v;

  public static void main(String[] args) {
    try {
      scan   = new Scanner(new FileInputStream(new File(args[0])));
      solver = new MaximumAverage(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  MaximumAverage(Scanner scan) {
    n = Integer.parseInt(scan.nextLine());
    k = Integer.parseInt(scan.nextLine());
    w = new int[n];
    v = new int[n];
    for (int i = 0; i < n; i++) {
      String[] line = scan.nextLine().split("\\s+");
      w[i] = Integer.parseInt(line[0]);
      v[i] = Integer.parseInt(line[1]);
    }
  }

  void solve() {
    System.out.println(upper());
  }

  double upper() {
    double lb = 0;
    double ub = 100;
    for (int i = 0; i < 100; i++) {
      double m = (lb + ub) / 2;
      if (C(m)) {
	lb = m;
      } else {
	ub = m;
      }
    }
    return lb;
  }

  boolean C(double mean) {
    double cond = 0;
    double[] aux = new double[n];
    for (int i = 0; i < n; i++)
      aux[i] = v[i] - mean * w[i];
    Arrays.sort(aux);
    for (int i = 0; i < k; i++)
      cond += aux[n - 1 - i];
    return cond >= 0;
  }
}
