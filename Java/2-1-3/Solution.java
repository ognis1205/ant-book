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
    private static char[][] maze;
    private static int[][] dist;
    private static char START = 's';
    private static char GOAL  = 'g';
    private static char WALL  = '#';
    private static Coordinate s;
    private static Coordinate g;
    private static Deque<Coordinate> queue;

    public static void main(String[] args) {
        solver = new Solution();
        scanner = new Scanner(System.in);

        n = scanner.nextInt();
        m = scanner.nextInt();
        scanner.nextLine();

        maze = new char[n][m];
        for (int i = 0; i < n; i++) {
            String line = scanner.nextLine();
            for (int j = 0; j < m; j++) {
                char c = line.charAt(j);
                maze[i][j] = c;
                if (c == START) s = solver.new Coordinate(i, j);
                if (c == GOAL) g = solver.new Coordinate(i, j);
            }
        }

        dist = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                dist[i][j] = Integer.MAX_VALUE;
            }
        }

        queue = new ArrayDeque<Coordinate>();

        try {
            solver.solve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void solve() {
        bfs();
        System.out.println(dist[g.x][g.y]);
    }

    private void bfs() {
        dist[s.x][s.y] = 0;
        queue.add(new Coordinate(s.x, s.y));
        while (!queue.isEmpty()) {
            Coordinate cur = queue.poll();
            for (Direction d : Direction.values()) {
                int nx = cur.x + d.x;
                int ny = cur.y + d.y;
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && maze[nx][ny] != WALL && dist[nx][ny] == Integer.MAX_VALUE) {
                    queue.add(new Coordinate(nx, ny));
                    dist[nx][ny] = dist[cur.x][cur.y] + 1;
                    if (nx == g.x && ny == g.y) break;
                }
            }
        }
    }

    private enum Direction {
        UP(0, 1),
        LEFT(-1, 0),
        RIGHT(1, 0),
        DOWN(0, -1);
        public int x, y;
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
