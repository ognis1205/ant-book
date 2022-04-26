use std::io;
use std::str;

macro_rules! parse {
    ($it: expr) => {
        $it.next().unwrap().parse().unwrap()
    };
    ($it: expr, $T: ty) => {
        $it.next().unwrap().parse::<$T>().unwrap()
    };
}

fn read_line() -> Result<String, io::Error> {
    let mut buf = String::new();
    let _ = match io::stdin().read_line(&mut buf) {
        Ok(byte) => byte,
        Err(e) => return Err(e),
    };
    Ok(buf)
}

fn tokenize<'a>(line: &'a mut String) -> str::SplitWhitespace<'a> {
    line.split_whitespace()
}

fn main() {
    let mut line = read_line().expect("n: the number of ants");
    let mut toks = tokenize(&mut line);
    let n: i32 = parse!(toks);
    println!("n: {}", n);

    let mut line = read_line().expect("a: the ants");
    let mut toks = tokenize(&mut line);
    let mut a: Vec<i32> = (0..n).map(|_| parse!(toks)).collect();
    println!("a: {:?}", a);

    let mut result = 0;
    a.sort_by(|a, b| a.cmp(b));
    let _ = a
        .windows(3)
        .inspect(|w| -> () {
            if w[2] < w[1] + w[0] {
                result = w.iter().sum();
            }
        })
        .collect::<Vec<_>>();
    println!("result: {}", result);
}
