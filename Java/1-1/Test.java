import java.io.*;
import java.util.*;
import java.text.*;
import java.util.function.*;
import java.util.regex.*;

class Test {
  private static Test solver;
  private static Scanner scanner;

  public static void main(String[] args) {
    solver  = new Test();
    scanner = new Scanner(System.in);
    solver.solve();
  }

  private void solve() {
    System.out.println("input: ");
    int   a = Integer.parseInt(scanner.nextLine());
    System.out.println(a);
    int[] x = Arrays.stream(scanner.nextLine().split("\\s+")).mapToInt(s -> Integer.parseInt(s)).toArray();
    Arrays.stream(x).forEach(s -> System.out.println(s));
  }
}
