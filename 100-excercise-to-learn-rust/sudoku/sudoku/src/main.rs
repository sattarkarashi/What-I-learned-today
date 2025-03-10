use std::env;

fn main() {
    // Sudoku solver
    let args: Vec<String> = env::args().collect();
    let mut board = vec![
        vec![0, 0, 0, 0, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 0, 0],
    ];
    let mut row = 0;
    let mut col = 0;
    for i in 1..10 {
        for j in 1..10 {
            let index = (i - 1) * 9 + j - 1;
            board[i - 1][j - 1] = args[index].parse::<i32>().unwrap();
            if args[index].parse::<i32>().unwrap() == 0 {
                row = i - 1;
                col = j - 1;
            }
        }
    }
    if solve(&mut board, row, col) {
        for i in 0..9 {
            for j in 0..9 {
                print!("{} ", board[i][j]);
            }
            println!();
        }
    } else {
        println!("No solution exists");
    }
    

}
