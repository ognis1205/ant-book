import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.stream.*;


public class RadixSort2 {
  public static void main(String[] args) {
    try (Stream<String[]> lines = Files.lines(Paths.get(args[0])).map(l -> l.split("\\s+"))) {
      List<Integer> list = lines
	.flatMap(x -> Arrays.asList(x).stream())
	.map(Integer::valueOf)
	.collect(Collectors.toList());
      Lists.sort(list);
      list.stream().forEach(System.out::println);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public static class Lists {
    public static void sort(List<Integer> list) {
      Optional<Integer> max = maxOf(list);
      if (max.isPresent()) {
	int m = max.get();
	for (int exp = 1; m / exp > 0; exp *= 10)
	  count(list, exp);
      }
    }

    private static Optional<Integer> maxOf(List<Integer> list) {
      return list.stream().reduce(Integer::max);
    }

    private static void count(List<Integer> list, Integer exp) {
      int size = list.size();
      Integer[] aux  = new Integer[size];
      Integer[] hist = new Integer[10];
      Arrays.fill(hist, 0);

      for (int i = 0; i < size; i++)
	hist[(list.get(i) / exp) % 10]++;

      for (int i = 1; i < 10; i++)
	hist[i] += hist[i - 1];

      for (int i = size - 1; i >= 0; i--) {
	aux[hist[(list.get(i) / exp) % 10] - 1] = list.get(i);
	hist[(list.get(i) / exp) % 10]--;
      }

      for (int i = 0; i < size; i++)
	list.set(i, aux[i]);
    }
  }
}
