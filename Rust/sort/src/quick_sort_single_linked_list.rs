use std::io;
use std::ptr;
use std::str;

macro_rules! parse {
    ($it: expr) => {
        $it.next().unwrap().parse().unwrap()
    };
    ($it: expr, $t: ty) => {
        $it.next().unwrap().parse::<$t>().unwrap()
    };
}

macro_rules! parse_array {
    ($it: expr) => {
        $it.map(|i| i.parse().unwrap()).collect()
    };
    ($it: expr, $t: ty) => {
        $it.map(|i| i.parse::<$t>().unwrap()).collect()
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

#[derive(Debug)]
pub struct List<T: Copy, PartialOrd> {
    head: Option<Box<Node<T>>>,
}

#[derive(Debug)]
struct Node<T: Copy> {
    data: T,
    next: Option<Box<Node<T>>>,
}

impl<T: Copy> List<T> {
    fn new() -> Self {
        List { head: None }
    }

    fn append(&mut self, data: T) -> () {
        match self.head {
            Some(ref mut node) => node.append(data),
            None => {
                self.head = Some(Box::new(Node {
                    data: data,
                    next: None,
                }))
            }
        }
    }

    fn partition(&mut self, lo: Option<Node<T>>, hi: Option<Node<T>>) -> Option<Node<T>> {
        match lo.zip(hi) {
            Some((ref mut lo, ref mut hi)) => {
                if ptr::eq(lo, hi) {
                    return None;
                } else {
                    let pivot = hi.data;
                    let mut prev = None;
                    let mut curr = &lo;
                    while !ptr::eq(lo, hi) {
                        if lo.data <= pivot {
                            Node::swap(curr, lo);
                            curr = curr.next;
                        }
                        lo = lo.next;
                    }
                    Node::swap(curr, hi);
                    return prev;
                }
            }
            None => return None,
        }
    }

    fn length(&self) -> usize {
        match self.head {
            Some(ref node) => node.length(),
            None => 0,
        }
    }
}

impl<T: Copy> Node<T> {
    fn swap(lhs: &mut Node<T>, rhs: &mut Node<T>) -> () {
        let tmp = lhs.data;
        lhs.data = rhs.data;
        rhs.data = tmp;
    }

    fn append(&mut self, data: T) -> () {
        match self.next {
            Some(ref mut node) => node.append(data),
            None => {
                self.next = Some(Box::new(Node {
                    data: data,
                    next: None,
                }))
            }
        }
    }

    fn length(&self) -> usize {
        match self.next {
            Some(ref node) => 1 + node.length(),
            None => 1,
        }
    }
}

fn main() {
    let mut line = read_line().expect("a: the array to be sorted");
    let toks = tokenize(&mut line);
    let xs: Vec<i32> = parse_array!(toks);
    let mut l: List<i32> = List::new();
    for x in xs {
        l.append(x);
    }
    println!("l: {:?}", l);
    println!("len: {}", l.length());
}
