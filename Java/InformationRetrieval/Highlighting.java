/* $File: Highlighting, $Timestamp: Thu Aug 12 11:18:42 2021 */
import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


public class Highlighting {
  static Scanner scan;

  static Highlighting solver;

  public static void main(String[] args) {
    try {
      scan   = new Scanner(new FileInputStream(new File(args[0])));
      solver = new Highlighting(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  Highlighting(Scanner scan) {
    // Placeholder.
  }

  void solve() {
    List<String> document =
      Arrays.asList("apple banana apple apple dog cat apple dog banana apple cat dog".split("\\s+"));
    List<String> query =
      Arrays.asList("banana cat".split("\\s+"));
    Map.Entry<Integer, Integer> result = highlight(document, query);
    System.out.println(result.getKey());
    System.out.println(result.getValue());
  }

  Map.Entry<Integer, Integer> highlight(Collection<String> document, Collection<String> query) {
    Queue<WithIndex> que = new ArrayDeque<>(query.size());
    Set<String> bow = new HashSet<>();
    Set<String> sofar = new HashSet<>();
    query.stream().forEach(bow::add);

    AtomicInteger indexer = new AtomicInteger();
    Interval interval = new Interval(0, Integer.MAX_VALUE - 1);

    document.stream()
      .map(w -> new WithIndex(indexer.getAndIncrement(), w))
      .filter(key -> bow.contains(key.word))
      .forEach(rhs -> {
	  que.add(rhs);
	  sofar.add(rhs.word);
	  normalize(que);
	  WithIndex lhs = que.peek();
	  int diff = rhs.index - lhs.index;
	  if (sofar.size() == bow.size() && diff < interval.length()) {
	    interval.left = lhs.index;
	    interval.right = rhs.index;
	  }
	});

    return new AbstractMap.SimpleImmutableEntry<>(interval.left, interval.right);
  }

  private <T> void normalize(Queue<T> que) {
    while (que.stream().filter(e -> e.equals(que.peek())).count() > 1)
      que.remove();
  }

  class WithIndex {
    Integer index;
    String word;

    WithIndex(Integer index, String word) {
      this.index = index;
      this.word  = word;
    }

    @Override
    public boolean equals(Object obj) {
      if (!(obj instanceof WithIndex)) return false;
      WithIndex that = (WithIndex) obj;
      return this.word.equals(that.word);
    }
  }

  class Interval {
    Integer left;
    Integer right;

    Interval(Integer left, Integer right) {
      this.left  = left;
      this.right = right;
    }

    Integer length() {
      return this.right - this.left + 1;
    }
  }
}
