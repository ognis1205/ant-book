import java.io.*;
import java.util.*;

public class Main {
    private static Main solver;
    private static Scanner scanner;

    private static int a;
    private static int[] y = {1, 5, 10, 50, 100, 500};
    private static int[] c = new int[6];

    public static void main(String[] args) {
        solver = new Main();
        scanner = new Scanner(System.in);

        a = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < 6; i++) {
            c[i] = scanner.nextInt();
        }

        try {
            solver.solve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void solve() {
        System.out.println(satisfiable(5, a, 0));
    }

    private int satisfiable(int i, int res, int acc) {
        if (res <= 0 || i < 0) return acc;
        return satisfiable(i - 1, res % y[i], acc + res / y[i]);
    }
}
