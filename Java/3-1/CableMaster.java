/* $File: CableMaster, $Timestamp: Thu Aug 12 15:44:56 2021 */
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


public class CableMaster {
  static Scanner scan;

  static CableMaster solver;

  int N;

  int K;

  double[] L;

  public static void main(String[] args) {
    try {
      scan   = new Scanner(new FileInputStream(new File(args[0])));
      solver = new CableMaster(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  CableMaster(Scanner scan) {
    N = Integer.parseInt(scan.nextLine());
    K = Integer.parseInt(scan.nextLine());
    L = new double[N];
    String[] entries = scan.nextLine().split("\\s+");
    for (int i = 0; i < N; i++) {
      L[i] = Double.parseDouble(entries[i]);
    }
  }

  void solve() {
    double lb = 0.0;
    double ub = 100;
    for (int i = 0; i < 100; i++) {
      double m = (lb + ub) / 2;
      if (!C(m)) {
	ub = m;
      } else {
	lb = m;
      }
    }
    System.out.println(lb);
  }

  boolean C(double x) {
    int total = 0;
    for (int i = 0; i < N; i++)
      total += (int) (L[i] / x);
    return total >= K;
  }
}
