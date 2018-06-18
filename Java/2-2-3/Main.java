import java.io.*;
import java.util.*;

public class Main {
    private static Main solver;
    private static Scanner scanner;

    private static String s;

    public static void main(String[] args) {
        solver = new Main();
        scanner = new Scanner(System.in);

        s = scanner.nextLine();

        try {
            solver.solve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void solve() {
        System.out.println(minimum(s));
    }

    private String minimum(String t) {
        if (t.length() == 0) return t;
        if (t.charAt(0) < t.charAt(t.length() - 1)) {
            return t.charAt(0) + minimum(t.substring(1, t.length()));
        } else if (t.charAt(0) > t.charAt(t.length() - 1)) {
            return t.charAt(t.length() - 1) + minimum(t.substring(0, t.length() - 1));
        } else {
            String l = minimum(t.substring(1, t.length()));
            String r = minimum(t.substring(0, t.length() - 1));
            return l.compareTo(r) < 0 ? t.charAt(0) + minimum(t.substring(1, t.length())) : t.charAt(t.length() - 1) + minimum(t.substring(0, t.length() - 1));
        }
    }
}
