import java.io.*;
import java.util.*;

public class Main {
    private static Main solver;
    private static Scanner scanner;

    private static int n;
    private static int[] x;
    private static int r;

    public static void main(String[] args) {
        solver = new Main();
        scanner = new Scanner(System.in);

        n = scanner.nextInt();
        scanner.nextLine();

        x = new int[n];
        for (int i = 0; i < n; i++) {
            x[i] = scanner.nextInt();
        }

        r = scanner.nextInt();

        try {
            System.out.println(solver.solve());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public int solve() {
        int acc = 0;
        int i = 0;
        while (i < n) {
            int s = x[i++];
            while (i < n && x[i] - s <= r) i++;
            int p = x[i-1];
            while (i < n && x[i] - p <= r) i++;
            acc++;
        }
        return acc;
    }
}
