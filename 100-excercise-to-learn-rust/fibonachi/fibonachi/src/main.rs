fn main() {

    // Writing a fibonachi using recursion
    fn fibonachi(n: u32) -> u32 {
        if n == 0 || n == 1 {
            return 1;
        } else {
            return fibonachi(n - 1) + fibonachi(n - 2);
        }
    }

    // Printing the fibonachi sequence
    for i in 0..10 {
        println!("Fibonachi of {} is {}", i, fibonachi(i));
    }


    // Writing a fibonachi using iteration
    fn fibonachi_iter(n: u32) -> u32 {
        let mut n1 = 1;
        let mut n2 = 1;
        let mut result = 1;
        for i in 1..n {
            result = n1 + n2;
            n1 = n2;
            n2 = result;
        }
        return result;
    }

    // Printing the fibonachi sequence
    for i in 0..10 {
        println!("Fibonachi of {} is {}", i, fibonachi_iter(i));
    }
}
