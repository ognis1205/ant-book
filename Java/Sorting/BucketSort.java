import java.io.*;
import java.nio.*;
import java.util.*;
import java.text.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


public class BucketSort {
  private static Scanner scan;

  private static List<Float> list;

  public static void main(String[] args) {
    try {
      scan = new Scanner(new FileInputStream(new File(args[0])));
      list = new ArrayList<>();
      String[] entries = scan.nextLine().split("\\s+");
      for (String entry : entries)
	list.add(Float.valueOf(entry));
      sort(list, 10);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  private static void sort(List<Float> list, int size) {
    assert size > -1 : "size must be greater than 0.";
    List<List<Float>> buckets = new ArrayList<>();
    for (int i = 0; i < size; i++)
      buckets.add(new Vector<>());
    for (Float i : list)
      buckets.get(Math.round(i)).add(i);
    for (List<Float> bucket : buckets) 
      Collections.sort(bucket);
    int index = 0;
    for (int i = 0; i < size; i++) {
      for (int j = 0; j < buckets.get(i).size(); j++) {
	list.set(index++, buckets.get(i).get(j));
      }
    }
    list.stream().forEach(s -> System.out.println(s));
  }
}
