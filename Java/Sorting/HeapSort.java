import java.io.*;
import java.util.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


public class HeapSort {
  private static Scanner scan;

  private static int n;

  private static List<Integer> list;

  public static void main(String[] args) {
    try {
      scan = new Scanner(new FileInputStream(new File(args[0])));
      n = Integer.parseInt(scan.nextLine());
      list = new ArrayList<>();
      String[] items = scan.nextLine().split("\\s+");
      for (int i = 0; i < n; i++)
	list.add(Integer.parseInt(items[i]));
      HeapTree<Integer> heap = HeapTree.of(list);
      while (!heap.isEmpty()) {
	System.out.println(heap.pop());
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  static class HeapTree<T extends Comparable<? super T>> {
    private List<T> elements = new ArrayList<>();

    public static <T extends Comparable<? super T>> HeapTree<T> of(Iterable<T> elements) {
      HeapTree<T> heap = new HeapTree<>();
      for (T e : elements)
	heap.push(e);
      return heap;
    }

    public void push(T element) {
      elements.add(element);
      int curr = elements.size() - 1;
      while (!isRoot(curr) && !isOrderedChild(curr)) {
	int p = parentOf(curr);
	swap(curr, p);
	curr = p;
      }
    }

    public T pop() {
      if (isEmpty())
	throw new IllegalStateException();
      T ret = elementAt(0);
      int last = elements.size() - 1;
      swap(0, last);
      elements.remove(last);
      int curr = 0;
      while (hasChild(curr) && !isOrderedParent(curr)) {
	int c = smallerChildOf(curr);
	swap(curr, c);
	curr = c;
      }
      return ret;
    }

    public boolean isEmpty() {
      return elements.isEmpty();
    }

    private int parentOf(int i) {
      return (i - 1) / 2;
    }

    private int leftOf(int i) {
      return 2 * i + 1;
    }

    private int rightOf(int i) {
      return 2 * i + 2;
    }

    private boolean isRoot(int i) {
      return i == 0;
    }

    private T elementAt(int i) {
      return elements.get(i);
    }

    private void swap(int lhs, int rhs) {
      T l = elementAt(lhs);
      T r = elementAt(rhs);
      elements.set(lhs, r);
      elements.set(rhs, l);
    }

    private boolean isOrderedChild(int i) {
      if (isRoot(i))
	return true;
      return elementAt(parentOf(i)).compareTo(elementAt(i)) <= 0;
    }

    private boolean isOrderedParent(int i) {
      if (!hasChild(i))
	return true;
      if (rightOf(i) >= elements.size())
	return elementAt(leftOf(i)).compareTo(elementAt(i)) >= 0;
      return elementAt(leftOf(i)).compareTo(elementAt(i)) >= 0 
	&& elementAt(rightOf(i)).compareTo(elementAt(i)) >= 0;
    }

    private int smallerChildOf(int i) {
      int l = leftOf(i);
      int r = rightOf(i);
      if (r >= elements.size())
	return l;
      return elementAt(l).compareTo(elementAt(r)) <= 0 ? l : r;
    }

    private boolean hasChild(int i) {
      return 2 * i + 1 < elements.size();
    }
  }
}
