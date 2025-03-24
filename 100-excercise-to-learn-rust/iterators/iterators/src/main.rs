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
    println!("{:?} and {:?}", doubled, numbers); 

    let evens: Vec<i32> = numbers.into_iter().filter(|&x| x % 2 == 0).collect();
    println!("{:?}", evens); // Prints: [2, 4]


    let v = vec![-1, 1, 2, 3, 4, 5];

    // Use filter to keep only even numbers
    let evens: Vec<_> = v.iter().filter(|x| *x % 2 == 0).collect();

    println!("{:?}, {:?}", evens, v); 

    // Benchmarking loops with iterators

    use criterion::{black_box, criterion_group, criterion_main, Criterion};

// Function to benchmark traditional for loop
fn sum_with_loop(vec: &[i32]) -> i32 {
    let mut sum = 0;
    for &num in vec {
        sum += num;
    }
    sum
}

// Function to benchmark iterator
fn sum_with_iterator(vec: &[i32]) -> i32 {
    vec.iter().sum()
}

fn criterion_benchmark(c: &mut Criterion) {
    // Create a test vector with 1 million elements
    let test_vec: Vec<i32> = (0..1_000_000).collect();

    // Benchmark traditional for loop
    c.bench_function("sum with loop", |b| {
        b.iter(|| sum_with_loop(black_box(&test_vec)))
    });

    // Benchmark iterator
    c.bench_function("sum with iterator", |b| {
        b.iter(|| sum_with_iterator(black_box(&test_vec)))
    });
}

    criterion_group!(benches, criterion_benchmark);
    criterion_main!(benches);
}
