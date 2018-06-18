import java.io.*;
import java.util.*;

public class Main {
    private static Main solver;
    private static Scanner scanner;

    private static int n;
    private static PriorityQueue<Integer> queue;

    public static void main(String[] args) {
        solver = new Main();
        scanner = new Scanner(System.in);

        n = scanner.nextInt();
        scanner.nextLine();

        queue = new PriorityQueue<Integer>(n);
        for (int i = 0; i < n; i++) {
            queue.add(scanner.nextInt());
        }

        try {
            System.out.println(solver.solve());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static int solve() {
        int acc = 0;
        while (queue.size() > 1) {
            int c = queue.poll() + queue.poll();
            acc += c;
            queue.add(c);
        }
        return acc;
    }
}
