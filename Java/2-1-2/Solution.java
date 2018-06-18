import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    private static Scanner scanner;
    private static Solution solver;

    private static int n;
    private static int m;
    private static char[][] map;
    private static char LAKE = 'w';
    private static Deque<Coordinate> queue;

    public static void main(String[] args) {
        solver = new Solution();
        scanner = new Scanner(System.in);

        n = scanner.nextInt();
        m = scanner.nextInt();
        scanner.nextLine();

        map = new char[n][m];
        for (int i = 0; i < n; i++) {
            String line = scanner.next();
            for (int j = 0; j < m; j++) {
                map[i][j] = line.charAt(j);
            }
        }

        queue = new ArrayDeque<Coordinate>();

        try {
            System.out.println(String.format("%d lake(s).", solver.solve()));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private int solve() {
        int acc = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == LAKE) {
                    acc++;
                    dfs(i, j);
                }
            }
        }
        return acc;
    }

    private void dfs(int i, int j) {
        queue.add(new Coordinate(i, j));
        while (!queue.isEmpty()) {
            Coordinate cur = queue.poll();
            map[cur.x][cur.y] = '.';
            for (Direction d : Direction.values()) {
                int nx = cur.x + d.x;
                int ny = cur.y + d.y;
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] == LAKE) queue.add(new Coordinate(nx, ny));
            }
        }
    }

    private enum Direction {
        UPLEFT(-1, 1),
        UP(0, 1),
        UPRIGHT(1, 1),
        LEFT(-1, 0),
        RIGHT(1, 0),
        DOWNLEFT(-1, -1),
        DOWN(0, -1),
        DOWNRIGHT(1, -1);

        public final int x, y;

        private Direction(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private class Coordinate {
        public int x, y;
        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
