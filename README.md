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

## Method 1: Monte Carlo Simulation.

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

```shell
$ time cargo run --release -- --attempts 500000000
   Compiling fox_game v0.1.0 (/home/dwg/CODE/fox_game)
    Finished `release` profile [optimized] target(s) in 0.36s
     Running `target/release/fox_game --attempts 500000000`
Wins: 64,477,198
Loses: 435,522,802
Win Percentage: 12.8954%

real    0m4.020s
user    1m54.730s
sys     0m0.234s
```

----

## Method 2: Exhaustive Search

Then I realised the number of possible games isn't actually that large.

We can caluclate it using the [binomial coefficient](https://en.wikipedia.org/wiki/Binomial_coefficient).

First we count the number of ways we can arrage the 6 'o' characters.

```latex
$\displaystyle \frac{(16!) }{ (10!) \cdot (6!) } = 8008$
```

Then, we have 10 remaining empty spaces, and we want to arrange the 5 'f' characters into them.

```latex
$\displaystyle \frac{(10!) }{ (5!) \cdot (5!) } = 252$
```

And the remaining 5 'x' characters can only go in the empty spaces.

This means the total number of possible games of fox is `8008 * 252 = 2018016`.

## Search all games in Python.

Then I wrote a python program to calculate all these possible games. As I only have a relatively small and finite
number of games to check, I didn't feel the need to use a more performant language, and so wrote this in a language
that I am more familiar with.

Usefully the [more-itertools](https://more-itertools.readthedocs.io/en/stable/) library has a function to calculate
all the unique permutations of a list in a sufficiently performant way.

Running that Python script we get.

```shell
$ time python exhaustive_solver.py 
Wins: 260,253
Loses: 1,757,763
Win Percentage: 12.896478521478521

real    0m1.441s
user    0m1.326s
sys     0m0.107s
```

And obviously, this is exhaustive, so will always give the same results, and the fully correct answer.

We can check the total number of games `260253 + 1757763 = 2018016` matches our mathematical result
using the binomial coefficient from earlier, which it does.
