/* $File: BinaryTree, $Timestamp: Tue Aug 10 13:45:54 2021 */
import java.io.*;
import java.nio.*;
import java.nio.charset.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

public class BinaryTree {
  private static class Tree<T extends Comparable<? super T>> {
    private static class Node<T> {
      T value;
      Node<T> lhs;
      Node<T> rhs;
      public Node(T value) {
	this.value = value;
	this.lhs = null;
	this.rhs = null;
      }
    }

    private Node<T> root;

    public Tree() {
      this.root = null;
    }

    public void insert(T value) {
      this.root = this.insertRecursive(this.root, value);
    }

    public boolean contains(T value) {
      return this.containsRecursive(this.root, value);
    }

    public T delete(T value) {
      try {
	Node<T> node = this.deleteRecursive(this.root, value);
	return value;
      } catch (Exception e) {
	return null;
      }
    }

    private Node<T> insertRecursive(Node<T> curr, T value) {
      if (curr == null) return new Node<>(value);
      if (curr.value.compareTo(value) <= 0)
	curr.rhs = insertRecursive(curr.rhs, value);
      else
	curr.lhs = insertRecursive(curr.lhs, value);
      return curr;
    }

    private boolean containsRecursive(Node<T> curr, T value) {
      if (curr == null) return false;
      if (curr.value.compareTo(value) == 0)
	return true;
      else if (curr.value.compareTo(value) < 0)
	return containsRecursive(curr.rhs, value);
      else
	return containsRecursive(curr.lhs, value);
    }

    private Node<T> deleteRecursive(Node<T> curr, T value) throws Exception {
      if (curr == null) throw new Exception();
      if (curr.value.compareTo(value) == 0) {
	if (curr.lhs == null && curr.rhs == null) return null;
	else if (curr.lhs == null) return curr.rhs;
	else if (curr.rhs == null) return curr.lhs;
	T smallest = findSmallest(curr.rhs);
	curr.value = smallest;
	curr.rhs = deleteRecursive(curr.rhs, smallest);
	return curr;
      } else if (curr.value.compareTo(value) <= 0) {
        curr.rhs = deleteRecursive(curr.rhs, value);
	return curr;
      } else {
	curr.lhs = deleteRecursive(curr.lhs, value);
	return curr;
      }
    }

    private T findSmallest(Node<T> node) {
      if (node.lhs == null) return node.value;
      else return findSmallest(node.lhs);
    }
  }

  private static FastScanner scan;

  private static BinaryTree solver;

  private Tree<Integer> tree;

  public static void main(String[] args) {
    try {
      scan   = new FastScanner(new FileInputStream(new File(args[0])));
      solver = new BinaryTree(scan);
      solver.solve();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public BinaryTree(FastScanner scan) {
    tree = new Tree<>();
  }

  private void solve() {
    tree.insert(0);
    tree.insert(1);
    tree.insert(2);
    tree.insert(2);
    tree.insert(3);
    tree.insert(3);
    tree.insert(3);
    System.out.println(tree.contains(0));
    System.out.println(tree.contains(-1));
    System.out.println(tree.contains(3));
    System.out.println(tree.delete(3));
    System.out.println(tree.contains(3));
    System.out.println(tree.delete(3));
    System.out.println(tree.contains(3));
    System.out.println(tree.delete(3));
    System.out.println(tree.contains(3));
    System.out.println(tree.delete(3));
  }

  private static int getLowerBound(int[] target, int key) {
    int l = 0;
    int r = target.length - 1;
    int m = (l + r) / 2;
    while (true) {
      if (target[m] == key || target[m] > key) {
        r = m - 1;
        if (r < l) return m;
      } else {
        l = m + 1;
        if (r < l) return m < target.length - 1 ? m + 1 : -1;
      }
      m = (l + r) / 2;
    }
  }

  private static int getUpperBound(int[] target, int key) {
    int l = 0;
    int r = target.length - 1;
    int m = (l + r) / 2;
    while (true) {
      if (target[m] == key || target[m] < key) {
        l = m + 1;
        if (r < l) return m < target.length - 1 ? m + 1 : -1;
      } else {
        r = m - 1;
        if (r < l) return m;
      }
      m = (l + r) / 2;
    }
  }

  private static class FastScanner implements Closeable {
    private InputStream in;
    private byte[] buffer;
    private int ptr;
    private int len;
    private boolean[] isSpace;

    public FastScanner(InputStream in) {
      this.in = in;
      this.buffer = new byte[1 << 15];
      this.ptr = 0;
      this.len = 0;
      this.isSpace = new boolean[128];
      this.isSpace[' '] = this.isSpace['\n'] = this.isSpace['\r'] = this.isSpace['\t'] = true;
    }

    public void setSpace(char... cs) {
      Arrays.fill(this.isSpace, false);
      this.isSpace['\r'] = this.isSpace['\n'] = true;
      for (char c : cs) this.isSpace[c] = true;
    }
        
    private int read() {
      if (this.len == -1) return -1;
      if (this.ptr >= this.len) {
        this.ptr = 0;
        if (this.in == null) return this.len = -1;
        try {
          this.len = this.in.read(this.buffer);
        } catch (IOException e) {
          throw new RuntimeException(e);
        }
        if (this.len <= 0) return -1;
      }
      return this.buffer[this.ptr++];
    }

    public boolean hasNext() {
      int c = this.read();
      while (c >= 0 && this.isSpace[c]) c = this.read();
      if (c == -1) return false;
      this.ptr--;
      return true;
    }

    public void skipLine() {
      if (this.ptr > 0 && this.buffer[this.ptr - 1] == '\n') {
        this.buffer[this.ptr - 1] = ' ';
        return;
      }
      int c = this.read();
      if (c < 0) return;
      while (c >= 0 && c != '\n' && c != '\r') c = this.read();
      if (c == '\r') this.read();
      if (this.ptr > 0) this.buffer[this.ptr - 1] = ' ';
    }

    public String next() {
      if (!hasNext()) throw new InputMismatchException();
      StringBuilder sb = new StringBuilder();
      int c = this.read();
      while (c >= 0 && !this.isSpace[c]) {
        sb.append((char)c);
        c = this.read();
      }
      return sb.toString();
    }
        
    public String nextLine() {
      StringBuilder sb = new StringBuilder();
      if (this.ptr > 0 && this.buffer[this.ptr - 1] == '\n') {
        this.buffer[this.ptr - 1] = ' ';
        return "";
      }
      int c = this.read();
      if (c < 0) throw new InputMismatchException();
      while (c >= 0 && c != '\n' && c != '\r') {
        sb.append((char)c);
        c = this.read();
      }
      if (c == '\r') this.read();
      if (this.ptr > 0) this.buffer[this.ptr - 1] = ' ';
      return sb.toString();
    }

    public FastScanner scanLine() {
      return new FastScanner(new ByteArrayInputStream(this.nextLine().getBytes(StandardCharsets.UTF_8)));
    }

    public int nextInt() {
      if (!hasNext()) throw new InputMismatchException();
      int c = this.read();
      int sgn = 1;
      if (c == '-') {
        sgn = -1;
        c = this.read();
      }
      int res = 0;
      do {
        if (c < '0' || c > '9') throw new InputMismatchException();
        res *= 10;
        res += c - '0';
        c = this.read();
      } while (c >= 0 && !this.isSpace[c]);
      return res * sgn;
    }

    public long nextLong() {
      if (!hasNext()) throw new InputMismatchException();
      int c = this.read();
      int sgn = 1;
      if (c == '-') {
        sgn = -1;
        c = this.read();
      }
      long res = 0;
      do {
        if (c < '0' || c > '9') throw new InputMismatchException();
        res *= 10;
        res += c - '0';
        c = this.read();
      } while (c >= 0 && !this.isSpace[c]);
      return res * sgn;
    }

    public double nextDouble() {
      return Double.parseDouble(next());
    }
        
    @Override
    public void close() {
      try {
        if (in != null) in.close();
      } catch (IOException e) {
        e.printStackTrace();
      }
    }
  }
}
