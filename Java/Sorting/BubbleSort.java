import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.text.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

public class BubbleSort {
  private static Scanner scan;

  private static List<Integer> list;

  public static void main(String[] args) {
    try {
      scan = new Scanner(new FileInputStream(new File(args[0])));
      list = new ArrayList<Integer>();
      String[] entries = scan.nextLine().split("\\s+");
      for (String entry : entries)
	list.add(Integer.valueOf(entry));
      sort(list);
      list.stream().forEach(s -> System.out.println(s));
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
  
  private static <T extends Comparable<? super T>> void sort(List<T> list) {
    boolean swapped = true;
    while (swapped) {
      swapped = false;
      for (int i = 0; i < list.size() - 1; i++) {
	if (list.get(i).compareTo(list.get(i + 1)) > 0) {
	  swapped = true;
	  Collections.swap(list, i, i + 1);
	}
      }
    }
  }
}
