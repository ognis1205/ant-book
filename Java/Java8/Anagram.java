import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.stream.*;


class Anagram {
  public static void main(String[] args) {
    Path dictionary = Paths.get(args[0]);
    int minSize = 1;

    try (Stream<String> lines = Files.lines(dictionary)) {
      lines
	.collect(Collectors.groupingBy(word -> alphabetize(word)))
	.values()
	.stream()
	.filter(group -> group.size() >= minSize)
	.forEach(g -> System.out.println(g.size() + ": " + g));
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  private static String alphabetize(String str) {
    char[] arr = str.toCharArray();
    Arrays.sort(arr);
    return new String(arr);
  }
}
