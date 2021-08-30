import java.io.*;
import java.util.*;


class QuickSort2 {
  private static Scanner scan;

  private static List<Integer> list;

  public static void main(String[] args) {
    try {
      scan = new Scanner(new FileInputStream(new File(args[0])));
      int n = Integer.parseInt(scan.nextLine());
      list = new ArrayList<>();
      String[] entries = scan.nextLine().split("\\s+");
      for (String entry : entries)
	list.add(Integer.valueOf(entry));
      Lists.sort(list);
      list.stream().forEach(i -> System.out.println(i));
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  private static class Lists {
    public static <T extends Comparable<? super T>> void sort(List<T> list) {
      Lists.sort(list, 0, list.size() - 1);
    }

    private static <T extends Comparable<? super T>> void sort(List<T> list, int lo, int hi) {
      if (lo < hi) {
	int p = partition(list, lo, hi);
	sort(list, lo, p - 1);
	sort(list, p + 1, hi);
      }
    }

    private static <T extends Comparable<? super T>> int partition(List<T> list, int lo, int hi) {
      T p = list.get(hi);
      int i = lo;
      for (int j = lo; j <= hi; j++)
	if (list.get(j).compareTo(p) < 0)
	  swap(list, i++, j);
      swap(list, i, hi);
      return i;
    }

    private static <T> void swap(List<T> list, int lhs, int rhs) {
      T l = list.get(lhs);
      T r = list.get(rhs);
      list.set(lhs, r);
      list.set(rhs, l);
    }
  }
}

