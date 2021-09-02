import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.stream.*;


public class ExternalMergeSort {
  public static void main(String[] args) {
    Scanner scan = null;
    List<Scanner> inputs = new ArrayList<>();

    try {
      scan = new Scanner(new FileInputStream(Paths.get(args[0]).toFile()));

      while (scan.hasNextLine())
	inputs.add(new Scanner(new FileInputStream(Paths.get(scan.nextLine()).toFile())));

      Heap<Pair<Integer>> heap = new Heap<>();
      for (int i = 0; i < inputs.size(); i++) {
	Scanner input = inputs.get(i);
	if (input.hasNext())
	  heap.push(new Pair<Integer>(i, input.nextInt()));
      }

      while (!heap.isEmpty()) {
	Pair<Integer> p = heap.pop();
	System.out.println(p.value);
	Scanner input = inputs.get(p.index);
	if (input.hasNext()) {
	  p.value = input.nextInt();
	  heap.push(p);
	}
      }
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      if (scan != null)
	scan.close();
      for (Scanner s : inputs)
	s.close();
    }
  }

  public static class Pair<T extends Comparable<? super T>> implements Comparable<Pair<T>> {
    T value;

    int index;

    public Pair(int index, T value) {
      this.value = value;
      this.index = index;
    }

    @Override
    public int compareTo(Pair<T> that) {
      return this.value.compareTo(that.value);
    }
  }

  public static class Heap<T extends Comparable<? super T>> {
    private List<T> tree;

    public Heap() {
      this.tree = new ArrayList<>();
    }

    public void push(T value) {
      this.tree.add(value);
      int i = this.tree.size() - 1;
      while (!this.isRoot(i) && !this.isValidChild(i)) {
	int p = this.parentOf(i);
	this.swap(i, p);
	i = p;
      }
    }

    public T pop() {
      T ret = this.elementAt(0);
      this.swap(0, this.tree.size() - 1);
      this.removeLast();
      int i = 0;
      while (this.hasLeft(i) && !this.isValidParent(i)) {
	int c = this.smallerChildOf(i);
	this.swap(i, c);
	i = c;
      }
      return ret;
    }

    public boolean isEmpty() {
      return this.tree.size() == 0;
    }

    private T elementAt(int i) {
      return this.tree.get(i);
    }

    private void removeLast() {
      this.tree.remove(this.tree.size() - 1);
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

    private boolean hasLeft(int i) {
      return this.leftOf(i) < this.tree.size();
    }

    private boolean hasRight(int i) {
      return this.rightOf(i) < this.tree.size();
    }

    private boolean isValidChild(int i) {
      if (this.isRoot(i))
	return true;
      T p = this.elementAt(this.parentOf(i));
      return p.compareTo(this.elementAt(i)) <= 0;
    }

    private boolean isValidParent(int i) {
      if (!this.hasLeft(i))
	return true;
      T c = this.elementAt(this.smallerChildOf(i));
      return c.compareTo(this.elementAt(i)) >= 0;
    }

    private int smallerChildOf(int i) {
      if (!this.hasRight(i))
	return this.leftOf(i);
      int l = this.leftOf(i);
      int r = this.rightOf(i);
      return this.elementAt(l).compareTo(this.elementAt(r)) <= 0 ? l : r;
    }

    private void swap(int lhs, int rhs) {
      T l = this.elementAt(lhs);
      T r = this.elementAt(rhs);
      this.tree.set(lhs, r);
      this.tree.set(rhs, l);
    }
  }

  public static class Lists {
  }
}
