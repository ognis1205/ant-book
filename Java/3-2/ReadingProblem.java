/* $File: ReadingProblem, $Timestamp: Thu Aug 12 23:55:33 2021 */
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


public class ReadingProblem {
  static Scanner scan;

  static ReadingProblem solver;

  int P;

  int[] a;

  Set<Integer> contents;

  Set<Integer> sofar;

  Queue<Integer> que;

  public static void main(String[] args) {
    try {
      scan   = new Scanner(new FileInputStream(new File(args[0])));
      solver = new ReadingProblem(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  ReadingProblem(Scanner scan) {
    P = Integer.parseInt(scan.nextLine());
    a = new int[P];
    contents = new HashSet<>();
    sofar = new HashSet<>();
    que = new ArrayDeque<>();
    String[] line = scan.nextLine().split("\\s+");
    for (int i = 0; i < P; i++) {
      a[i] = Integer.parseInt(line[i]);
      contents.add(a[i]);
    }
  }

  void solve() {
    int min = Integer.MAX_VALUE;
    for (int i = 0; i < P; i++) {
      que.add(i);
      sofar.add(a[i]);
      if (sofar.size() == contents.size()) {
	while (a[que.peek()] == a[i]) que.remove();
	min = Math.min(min, i - que.peek() + 1);
      }
    }
    System.out.println(min);
  }
}
