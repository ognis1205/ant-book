import java.io.*;
import java.util.*;

public class Main {
    private static Main solver;
    private static Scanner scanner;

    private static int n;
    private static int W;
    private static int[] w;
    private static int[] v;
    private static int[][] dp;

    public static void main(String[] args) {
        solver = new Main();
        scanner = new Scanner(System.in);

        n = scanner.nextInt();
        scanner.nextLine();

        w = new int[n];
        for (int i = 0; i < n; i++) {
            w[i] = scanner.nextInt();
        }

        v = new int[n];
        for (int i = 0; i < n; i++) {
            v[i] = scanner.nextInt();
        }

        W = scanner.nextInt();

        dp = new int[n][W+1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < W+1; j++) {
                dp[i][j] = -1;
            }
        }

        try {
            System.out.println(solver.solve());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private int solve() {
        return rec(0, W);
    }

    private int rec(int i, int j) {
        if (i >= n || j <= 0) return 0;
        if (dp[i][j] >= 0) return dp[i][j];
        return dp[i][j] = j - w[i] >= 0 ? Math.max(v[i] + rec(i + 1, j - w[i]), rec(i + 1, j)) : rec(i + 1, j);
    }
}
