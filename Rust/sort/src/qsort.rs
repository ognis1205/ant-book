use std::cmp;
use std::io;
use std::str;

macro_rules! parse {
    ($it: expr) => {
        $it.next().unwrap().parse().unwrap()
    };
    ($it: expr, $t: ty) => {
        $it.next().unwrap().parse::<$t>().unwrap()
    };
}

fn read_line() -> Result<String, io::Error> {
    let mut line = String::new();
    let _ = match io::stdin().read_line(&mut line) {
        Ok(byte) => byte,
        Err(e) => return Err(e),
    };
    Ok(line)
}

fn tokenize<'a>(line: &'a mut String) -> str::SplitWhitespace<'a> {
    line.split_whitespace()
}

fn partition<T: cmp::PartialOrd + Copy>(arr: &mut Vec<T>, lo: usize, hi: usize) -> usize {
    let mut i = lo;
    let pivot = arr[hi];
    for j in lo..hi {
        if arr[j] <= pivot {
            arr.swap(i, j);
            i += 1;
        }
    }
    arr.swap(i, hi);
    i
}

fn qsort<T: cmp::PartialOrd + Copy>(arr: &mut Vec<T>, lo: usize, hi: usize) -> () {
    if lo >= hi {
        return;
    }
    let p = partition(arr, lo, hi);
    qsort(arr, lo, p.saturating_sub(1));
    qsort(arr, p + 1, hi);
}

fn main() {
    let mut line = read_line().expect("n: the number of integers");
    let mut toks = tokenize(&mut line);
    let n: i32 = parse!(toks);
    println!("n: {}", n);

    let mut line = read_line().expect("a: the array to be sorted");
    let mut toks = tokenize(&mut line);
    let mut a: Vec<i32> = (0..n).map(|_| parse!(toks)).collect();
    println!("a: {:?}", a);

    let lo = 0;
    let hi = a.len() - 1;
    qsort(&mut a, lo, hi);
    println!("a: {:?}", a);
}
