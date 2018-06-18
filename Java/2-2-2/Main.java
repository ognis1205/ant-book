import java.io.*;
import java.util.*;

public class Main {
    private static Main solver;
    private static Scanner scanner;

    private static int n;
    private static int[] s;
    private static int[] e;
    private static Schedule[] x;

    public static void main(String[] args) {
        solver = new Main();
        scanner = new Scanner(System.in);

        n = scanner.nextInt();
        scanner.nextLine();

        s = new int[n];
        for (int i = 0; i < n; i++) {
            s[i] = scanner.nextInt();
        }

        e = new int[n];
        for (int i = 0; i < n; i++) {
            e[i] = scanner.nextInt();
        }

        x = new Schedule[n];
        for (int i = 0; i < n; i++) {
            x[i] = solver.new Schedule(s[i], e[i]);
        }
        Arrays.sort(x, solver.new ScheduleComparator());

        try {
            System.out.println(solver.solve());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private int solve() {
        int acc = 0;
        for (int i = 0; i < n;) {
            acc++;
            Schedule cur = x[i];
            do {
                i++;
            } while (i < n && cur.end > x[i].start);
        }
        return acc;
    }

    private class Schedule {
        public int start;
        public int end;
        public Schedule(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    private class ScheduleComparator implements Comparator<Schedule> {
        @Override
        public int compare(Schedule l, Schedule r) {
            return l.end - r.end;
        }
    }
}
