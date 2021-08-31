import java.io.*;
import java.util.*;


class BubbleSort2 {
  public static void main(String[] args) {
    try {
      Scanner scan = new Scanner(new FileInputStream(new File(args[0])));

      int n = Integer.parseInt(scan.nextLine());
      List<Integer> list = new ArrayList<>();
      String[] items = scan.nextLine().split("\\s+");
      for (String item : items)
	list.add(Integer.valueOf(item));

      Lists.sort(list);
      list.stream().forEach(i -> System.out.println(i));
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public static class Lists {
    public static <T extends Comparable<? super T>> void sort(List<T> list) {
      boolean swapped = true;
      while (swapped) {
	swapped = false;
	for (int i = 0; i < list.size() - 1; i++) {
	  if (list.get(i).compareTo(list.get(i + 1)) > 0) {
	    swap(list, i, i + 1);
	    swapped = true;
	  }
	}
      }
    }

    private static <T> void swap(List<T> list, int lhs, int rhs) {
      T l = list.get(lhs);
      T r = list.get(rhs);
      list.set(lhs, r);
      list.set(rhs, l);
    }
  }
}
