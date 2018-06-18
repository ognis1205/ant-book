import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    private static Scanner scanner;
    private static Solution solver;

    private static int n;
    private static int k;
    private static int[] a;

    public static void main(String[] args) {
        solver = new Solution();
        scanner = new Scanner(System.in);

        n = scanner.nextInt();
        k = scanner.nextInt();
        scanner.nextLine();

        a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }

        try {
            solver.solve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void solve() {
        System.out.println(dfs(0, k));
    }

    private boolean dfs(int i, int res) {
        if (res <= 0 || i >= n) return res == 0;
        return dfs(i + 1, res - a[i]) || dfs(i + 1, res);
    }
}
