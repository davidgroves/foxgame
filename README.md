# Fox Game

I was asked to calculate the probability of winning the "fox" game, based
on the youtube shorts by [AlexCheddarUK](https://www.youtube.com/@AlexCheddarUK), such as
[Attempt 7](https://www.youtube.com/shorts/5CARrKOvtFI).

This is a very quick and dirty program to get answers.

## Rules

- The game is played on a 4x4 grid of squares.
- You have 5 'f' characters, 5 'x' characters and 6 'o' characters.
- You place them RANDOMLY on the grid.
- You win if nowhere on the grid spells the word 'fox'.
- This uses "wordsearch rules, so the word can be vertical, horizontal, or diagonal.
- It can also be backwards, so if the first three characters were 'fox' you would lose, but so would 'xof'

## Method

- Use numbers to represent the characters. 0 = f, 1 = o, 2 = x.
- The grid is a 16 long vector of numnbers. Position 0 is the top left, and position 15 is the bottom right.

So the grid has positions.

```
[0 , 1 , 2 , 3]
[4 , 5 , 6 , 7]
[8 , 9 , 10, 11]
[12, 13, 14, 15]
```

- Generate a random grid by "shuffling" a vector of characters.
- Check if the word 'fox' is in the grid, but looking at subsets of the positions.
- The subsets are precalculated for speed, there is no logic, just a list of 3 positions to check for 0,1,2 in.

## Notes

This is a Rust program, and uses the [rayon](https://github.com/rayon-rs/rayon) library to parallelize the work.
It will run your machine at near 100% CPU use while it computes the results.

## Examples

```
$ time cargo run --release -- --attempts 500000000
    Finished `release` profile [optimized] target(s) in 0.01s
     Running `target/release/fox_game --attempts 500000000`
Wins: 64477441
Loses: 435522559
Win Percentage: 0.128954882

real    0m3.634s
user    1m52.034s
sys     0m0.201s
```