import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

public class RadixSort {
  private static Scanner scan;

  private static int n;

  private static int[] arr;

  public static void main(String[] args) {
    try {
      scan = new Scanner(new FileInputStream(new File(args[0])));

      n = Integer.parseInt(scan.nextLine());
      arr = new int[n];

      String[] items = scan.nextLine().split("\\s+");
      for (int i = 0; i < n; i++)
	arr[i] = Integer.parseInt(items[i]);

      sort(arr, n);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  private static void sort(int[] arr, int size) {
    int max = maxOf(arr, size);
    for (int exp = 1; max / exp > 0; exp *= 10)
      countSort(arr, size, exp);
    for (int i : arr)
      System.out.println(i);
  }

  private static int maxOf(int[] arr, int size) {
    int max = arr[0];
    for (int i = 0; i < size; i++)
      if (arr[i] > max) max = arr[i];
    return max;
  }

  private static void countSort(int[] arr, int size, int exp) {
    int[] aux = new int[size];
    int[] counts = new int[10];
    Arrays.fill(counts, 0);

    for (int i = 0; i < size; i++)
      counts[(arr[i] / exp) % 10]++;

    for (int i = 1; i < 10; i++)
      counts[i] += counts[i - 1];

    for (int i : counts)
      System.out.println(i);
    System.out.println();
    
    for (int i = size - 1; i >= 0; i--) {
      aux[counts[(arr[i] / exp) % 10] - 1] = arr[i];
      counts[(arr[i] / exp) % 10]--;
    }

    for (int i : aux)
      System.out.println(i);
    System.out.println();

    for (int i = 0; i < size; i++)
      arr[i] = aux[i];
  }
}
