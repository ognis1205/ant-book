import java.io.*;
import java.util.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


public class MergeSort {
  private static Scanner scan;

  private static int n;

  private static List<List<Integer>> lists;

  public static void main(String[] args) {
    try {
      scan = new Scanner(new FileInputStream(new File(args[0])));

      lists = new ArrayList<>();
      n = Integer.parseInt(scan.nextLine());
      for (int i = 0; i < n; i++) {
	lists.add(new ArrayList<>());
	String[] entries = scan.nextLine().split("\\s+");
	for (String entry : entries)
	  lists.get(i).add(Integer.parseInt(entry));
      }

      for (List<Integer> list : lists)
	Collections.sort(list);

      List<Integer> result = solve(lists);
      result.stream().forEach(e -> System.out.println(e));
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  static List<Integer> solve(List<List<Integer>> lists) {
    List<Integer> ret = new ArrayList<>();
    Queue<Pair> que = new PriorityQueue<>(new Comparator<Pair>() {
	@Override
	public int compare(Pair lhs, Pair rhs) {
	  return lhs.value - rhs.value;
	}
      });
    for (int i = 0; i < lists.size(); i++)
      que.add(new Pair(i, 0, lists.get(i).get(0)));
    while (!que.isEmpty()) {
      Pair p = que.poll();
      ret.add(p.value);
      p.position++;
      if (p.position < lists.get(p.index).size()) {
	p.value = lists.get(p.index).get(p.position);
	que.add(p);
      }
    }
    return ret;
  }

  static class Pair {
    int value;
    int index;
    int position;
    public Pair(int index, int position, int value) {
      this.index = index;
      this.position = position;
      this.value = value;
    }
  }
}
