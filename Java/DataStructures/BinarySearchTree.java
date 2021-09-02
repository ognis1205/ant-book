import java.io.*;
import java.util.*;


public class BinarySearchTree<T extends Comparable<? super T>> {
  Node<T> root;

  public BinarySearchTree() {
    this.root = null;
  }

  public void delete(T data) {
    this.root = this.deleteRecursively(this.root, data);
  }

  public void insert(T data) {
    this.root = this.insertRecursively(this.root, data);
  }

  public boolean search(T data) {
    Node<T> node = this.searchRecursively(this.root, data);
    return node == null ? false : true;
  }

  public void inorder() { 
    inorderRecursively(this.root); 
  } 
   
  private Node<T> deleteRecursively(Node<T> node, T data) {
    if (node == null)
      return node;
    if (data.compareTo(node.data) < 0) {
      node.left = deleteRecursively(node.left, data);
    } else if (data.compareTo(node.data) > 0) {
      node.right = deleteRecursively(node.right, data);
    } else {
      if (node.left == null) 
	return node.right; 
      else if (node.right == null) 
	return node.left; 
      node.data = minOf(node.right); 
      root.right = deleteRecursively(node.right, node.data);
    }
    return node;
  }

  private Node<T> insertRecursively(Node<T> node, T data) {
    if (node == null)
      return new Node<T>(data);
    if (data.compareTo(node.data) < 0) {
      node.left = insertRecursively(node.left, data);
    } else if (data.compareTo(node.data) >= 0) {
      node.right = insertRecursively(node.right, data);
    }
    return node;
  }

  private Node<T> searchRecursively(Node<T> node, T data) {
    if (node == null)
      return null;
    if (data.compareTo(node.data) < 0) {
      return searchRecursively(node.left, data);
    } else if (data.compareTo(node.data) > 0) {
      return searchRecursively(node.right, data);
    } else {
      return node;
    }
  }

  private void inorderRecursively(Node<T> node) { 
    if (node != null) { 
      inorderRecursively(node.left); 
      System.out.println(node.data); 
      inorderRecursively(node.right); 
    } 
  }

  private T minOf(Node<T> node) {
    if (node == null)
      throw new IllegalStateException();
    while (node.left != null)
      node = node.left;
    return node.data;
  }

  class Node<T> {
    T data;
    Node<T> left;
    Node<T> right;
    public Node(T data) {
      this.data = data;
      this.left = null;
      this.right = null;
    }
  }

  public static void main(String[] args) {
    BinarySearchTree<Integer> tree = new BinarySearchTree<>();
    /* BST tree example
       45 
       /     \ 
       10      90 
       /  \    /   
       7   12  50   */
    tree.insert(45); 
    tree.insert(10); 
    tree.insert(7); 
    tree.insert(12); 
    tree.insert(90); 
    tree.insert(50); 
    tree.inorder(); 

    tree.delete(50);
    boolean ret = tree.search (50);
    System.out.println("\nKey 50 found in BST:" + ret);
    ret = tree.search(12);
    System.out.println("\nKey 12 found in BST:" + ret);
  }
}
