import java.io.*;
import java.util.*;
import java.util.function.*;


class BucketSort2 {
  public static void main(String[] args) {
    try {
      Scanner scan = new Scanner(new FileInputStream(new File(args[0])));
      List<Double> list = new ArrayList<>();

      String[] items = scan.nextLine().split("\\s+");
      for (String item : items)
	list.add(Double.valueOf(item));

      Function<Double, Integer> func = (x) -> {
	Long l = Math.round(x);
	return l.intValue();
      };
      Bucket<Double> bucket = new Bucket<>(10, func);
      bucket.addAll(list);
      List<Double> result = bucket.sort();

      result.stream().forEach(System.out::println);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public static class Bucket<T extends Comparable<? super T>> {
    private List<List<T>> buckets;

    private Function<T, Integer> op;

    public Bucket(int size, Function<T, Integer> op) {
      this.buckets = new ArrayList<>();
      this.op = op;
      for (int i = 0; i < size; i++)
	this.buckets.add(new ArrayList<>());
    }

    public void addAll(List<T> list) {
      for (T item : list)
	this.buckets.get(this.op.apply(item)).add(item);
    }

    public List<T> sort() {
      List<T> ret = new ArrayList<>();
      for (List<T> bucket : this.buckets) {
	Collections.sort(bucket);
	for (T item : bucket)
	  ret.add(item);
      }
      return ret;
    }
  }
}
