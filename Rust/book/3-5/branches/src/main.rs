use std::io;

fn main() {
    println!("Please enter a number.");

    let mut line = String::new();

    io::stdin()
        .read_line(&mut line)
        .expect("Failed to read line");

    let number: i32 = line.trim().parse().expect("The input is not a number");

    if number < 5 {
        println!("The condition was true.");
    } else {
        println!("The condition was false.");
    }

    let mut count = 0;

    'counting: loop {
        println!("count = {}", count);
        let mut remaining = 10;

        loop {
            println!("remaining = {}", remaining);
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting;
            }
            remaining -= 1;
        }
        count += 1;
    }
    println!("End count = {}", count);
}
