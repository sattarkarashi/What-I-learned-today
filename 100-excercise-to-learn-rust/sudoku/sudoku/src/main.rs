use std::fmt;

const SIZE: usize = 9;
const SUBGRID_SIZE: usize = 3;

#[derive(Clone)]
struct Sudoku {
    grid: [[u8; SIZE]; SIZE],
}

impl Sudoku {
    fn new(grid: [[u8; SIZE]; SIZE]) -> Self {
        Sudoku { grid }
    }

    fn is_valid(&self, row: usize, col: usize, num: u8) -> bool {
        // Check if the number is already in the row or column
        for i in 0..SIZE {
            if self.grid[row][i] == num || self.grid[i][col] == num {
                return false;
            }
        }

        // Check if the number is in the 3x3 subgrid
        let start_row = row / SUBGRID_SIZE * SUBGRID_SIZE;
        let start_col = col / SUBGRID_SIZE * SUBGRID_SIZE;
        for i in 0..SUBGRID_SIZE {
            for j in 0..SUBGRID_SIZE {
                if self.grid[start_row + i][start_col + j] == num {
                    return false;
                }
            }
        }

        true
    }

    fn solve(&mut self) -> bool {
        for row in 0..SIZE {
            for col in 0..SIZE {
                if self.grid[row][col] == 0 {
                    for num in 1..=SIZE as u8 {
                        if self.is_valid(row, col, num) {
                            self.grid[row][col] = num;

                            if self.solve() {
                                return true;
                            }

                            self.grid[row][col] = 0; // Backtrack
                        }
                    }
                    return false; // No valid number found
                }
            }
        }
        true // Puzzle solved
    }
}

impl fmt::Display for Sudoku {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for row in 0..SIZE {
            for col in 0..SIZE {
                write!(f, "{} ", self.grid[row][col])?;
            }
            writeln!(f)?;
        }
        Ok(())
    }
}

fn main() {
    let grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ];

    let mut sudoku = Sudoku::new(grid);

    println!("Sudoku Puzzle:");
    println!("{}", sudoku);

    if sudoku.solve() {
        println!("Solved Sudoku:");
        println!("{}", sudoku);
    } else {
        println!("No solution exists.");
    }
}