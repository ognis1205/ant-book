use std::io;

fn main() {
    let arr = [1, 2, 3, 4, 5];

    println!("Please enter an array index.");

    let mut index = String::new();

    io::stdin()
        .read_line(&mut index)
        .expect("Failed to read line");

    let index: usize = index
        .trim()
        .parse()
        .expect("Indext entered was not a number");

    let element = arr[index];

    println!(
        "The value of the element at index {} is: {}",
        index, element
    );
}
