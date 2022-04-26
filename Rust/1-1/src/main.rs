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

fn main() {
    let mut line = read_line().expect("n: the number of values");
    let mut toks = tokenize(&mut line);
    let n: usize = parse!(toks);
    println!("n: {}", n);

    let mut line = read_line().expect("m: the number of total sum");
    let mut toks = tokenize(&mut line);
    let m: i32 = parse!(toks);
    println!("m: {}", m);

    let mut line = read_line().expect("k: the numbers to be summed");
    let mut toks = tokenize(&mut line);
    let k: Vec<i32> = (0..n).map(|_| parse!(toks)).collect();
    println!("k: {:?}", k);

    let mut result = false;
    for a in 0..n {
        for b in a..n {
            for c in b..n {
                for d in c..n {
                    if k[a] + k[b] + k[c] + k[d] == m {
                        result = true;
                        break;
                    }
                }
            }
        }
    }

    let result = if result { "Yes" } else { "No" };
    println!("Result: {}", result);
}
