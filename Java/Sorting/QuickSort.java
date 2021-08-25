import java.io.*;
import java.util.*;


public class QuickSort {
  private static Scanner scan;

  private static int n;

  private static List<Integer> list;

  public static void main(String[] args) {
    try {
      scan = new Scanner(new FileInputStream(new File(args[0])));
      n = Integer.parseInt(scan.nextLine());
      list = new ArrayList<>();
      String[] is = scan.nextLine().split("\\s+");
      for (int i = 0; i < n; i++)
	list.add(Integer.valueOf(is[i]));
      QSort.<Integer>sort(list, 0, list.size() - 1, new Comparator<Integer> () {
	  @Override
	  public int compare(Integer lhs, Integer rhs) {
	    return lhs.compareTo(rhs);
	  }
	});
      for (Integer i : list)
	System.out.println(i);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  static class QSort {
    private static <T> void sort(List<T> list, int l, int r, Comparator<? super T> comparator) {
      if (l < r) {
	int p = partition(list, l, r, comparator);
	sort(list, l, p - 1, comparator);
	sort(list, p + 1, r, comparator);
      }
    }

    private static <T> int partition(List<T> list, int l, int r, Comparator<? super T> comparator) {
      T p = list.get(r);
      int i = l;
      for (int j = l; j <= r; j++)
	if (comparator.compare(list.get(j), p) < 0)
	  swap(list, i++, j);
      swap(list, i, r);
      return i;
    }

    private static <T> void swap(List<T> list, int l, int r) {
      T lhs = list.get(l);
      T rhs = list.get(r);
      list.set(l, rhs);
      list.set(r, lhs);
    }
  }
}
