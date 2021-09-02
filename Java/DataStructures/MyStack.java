import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.stream.*;


public class MyStack<E> {
  private int size;

  private int minCap;

  private Object[] elements;

  public MyStack(int minCap) {
    this.size = 0;
    this.minCap = minCap;
    this.elements = new Object[minCap];
  }

  @SuppressWarnings("unchecked")
  public E pop() {
    this.check();
    E ret = (E) this.elements[--this.size];
    this.elements = Arrays.copyOfRange(this.elements, 0, this.size);
    return ret;
  }

  public void push(E element) {
    this.grow(this.size);
    this.elements[this.size++] = element;
  }

  public boolean isEmpty() {
    return this.size <= 0;
  }

  private void check() {
    if (this.isEmpty()) throw new IllegalStateException();
  }

  private void grow(int index) {
    if (index >= this.elements.length) {
      int cap = this.elements.length + (this.elements.length >> 1);
      while (index >= cap)
	cap = cap + (cap >> 1);
      if (cap - this.minCap < 0)
	cap = this.minCap;
      this.elements = Arrays.copyOf(this.elements, cap);
    }
  }

  public static void main(String[] args) {
    List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
    MyStack<Integer> stack = new MyStack<>(10);
    for (Integer i : list)
      stack.push(i);
    while (!stack.isEmpty())
      System.out.println(stack.pop());
  }
}
