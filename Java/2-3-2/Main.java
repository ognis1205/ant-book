import java.io.*;
import java.util.*;

public class Main {
    private static Main solver;
    private static Scanner scanner;

    private static String s;
    private static String t;
    private static int[][] dp;

    public static void main(String[] args) {
        solver = new Main();
        scanner = new Scanner(System.in);

        s = scanner.nextLine();
        t = scanner.nextLine();

        dp = new int[s.length()][t.length()];
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < t.length(); j++) {
                dp[i][j] = -1;
            }
        }

        try {
            solver.solve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void solve() {
        System.out.println(rec(0, 0));
    }

    private int rec(int i, int j) {
        if (i >= s.length() || j >= t.length()) return 0;
        if (dp[i][j] >= 0) return dp[i][j];
        if (s.charAt(i) == t.charAt(j)) return dp[i][j] = Math.max(1 + rec(i + 1, j + 1), Math.max(rec(i + 1, j), rec(i, j + 1)));
        return dp[i][j] = Math.max(rec(i + 1, j), rec(i, j + 1));
    }
}
