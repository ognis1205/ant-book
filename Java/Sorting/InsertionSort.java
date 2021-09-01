import java.util.*;
import java.io.*;


public class InsertionSort {
  public static void main(String[] args) {
    try {
      Scanner scan = new Scanner(new FileInputStream(new File(args[0])));
      List<Double> list = new ArrayList<>();
      while (scan.hasNext())
	list.add(scan.nextDouble());

      Lists.sort(list);
      list.stream().forEach(System.out::println);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public static class Lists {
    public static <T extends Comparable<? super T>> void sort(List<T> list) {
      for (int i = 1; i < list.size(); i++) {
	T pivot = list.get(i);
	int j = i - 1;
	while (j >= 0 && list.get(j).compareTo(pivot) > 0) {
	  list.set(j + 1, list.get(j));
	  j--;
	}
	list.set(j + 1, pivot);
      }
    }
  }
}
