fn main() {
    let v = vec![1, 2, 3, 4, 5];

    // Create an iterator from the vector
    let mut iter = v.iter();

    // Use the iterator
    while let Some(num) = iter.next() {
        println!("{}", num);
    }

    let numbers = vec![1, 2, 3, 4];
    let doubled: Vec<i32> = numbers.iter().map(|x| x * 2).collect();
    println!("{:?} and {:?}", doubled, numbers); // Prints: [2, 4, 6, 8]

    let evens: Vec<i32> = numbers.into_iter().filter(|&x| x % 2 == 0).collect();
    println!("{:?}", evens); // Prints: [2, 4]


    let v = vec![-1, 1, 2, 3, 4, 5];

    // Use filter to keep only even numbers
    let evens: Vec<_> = v.iter().filter(|x| *x % 2 == 0).collect();

    println!("{:?}", evens); // Output: [2, 4]
}
