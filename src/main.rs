use clap::Parser;
use clap_derive::Parser;
use num_format::{SystemLocale, ToFormattedString};
use num_cpus;
use rand::{seq::SliceRandom, thread_rng};
use rayon::prelude::*;

#[derive(Parser)]
#[command(author="David Groves", version="0.1", about="Solves the Fox game", long_about = None)]
struct Args {
    #[arg(short, long, default_value_t = 10000000)]
    attempts: u64
}



fn main() {
    let grid = vec![0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2];
    let args = Args::parse();

    let bad_locations = [
        // Horizontal
        [0, 1, 2],
        [1, 2, 3],
        [4, 5, 6],
        [5, 6, 7],
        [8, 9, 10],
        [9, 10, 11],
        [12, 13, 14],
        [13, 14, 15],
        // Vertical
        [0, 4, 8],
        [4, 8, 12],
        [1, 5, 9],
        [5, 9, 13],
        [2, 6, 10],
        [6, 10, 14],
        [3, 7, 11],
        [7, 11, 15],
        // Diagonal
        [0, 5, 10],
        [5, 10, 15],
        [1, 6, 11],
        [4, 9, 14],
        [3, 6, 9],
        [6, 9, 12],
        [7, 10, 13],
        [2, 5, 8],
        // Horizontal backwards
        [2, 1, 0],
        [3, 2, 1],
        [6, 5, 4],
        [7, 6, 5],
        [10, 9, 8],
        [11, 10, 9],
        [14, 13, 12],
        [15, 14, 13],
        // Vertical backwards
        [2, 4, 0],
        [6, 8, 4],
        [3, 5, 1],
        [7, 9, 5],
        [10, 6, 2],
        [14, 10, 6],
        [11, 7, 3],
        [15, 11, 7],
        // Diagonal backwards
        [10, 5, 0],
        [15, 10, 5],
        [11, 6, 1],
        [14, 9, 4],
        [9, 6, 3],
        [12, 9, 6],
        [13, 10, 7],
        [8, 5, 2],
    ];

    let num_threads = num_cpus::get();
    rayon::ThreadPoolBuilder::new()
        .num_threads(num_threads)
        .build_global()
        .unwrap();

    let loses: u64 = (0..args.attempts)
        .into_par_iter()
        .map(|_| {
            let mut local_grid = grid.clone();
            let mut rng = thread_rng();
            local_grid.shuffle(&mut rng);
            for g in &bad_locations {
                if local_grid[g[0]] == 0 && local_grid[g[1]] == 1 && local_grid[g[2]] == 2 {
                    return 1;
                }
            }
            0
        })
        .sum();

    let locale = SystemLocale::default().unwrap();
    println!("Wins: {}", (args.attempts - loses).to_formatted_string(&locale));
    println!("Loses: {}", loses.to_formatted_string(&locale));
    println!("Win Percentage: {:.4}%", ((args.attempts as f64 - loses as f64) / args.attempts as f64 * 100.0));
}
