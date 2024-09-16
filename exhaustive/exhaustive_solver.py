import more_itertools

BAD_LOCATIONS = [
    # Horizontal
    [0, 1, 2],
    [1, 2, 3],
    [4, 5, 6],
    [5, 6, 7],
    [8, 9, 10],
    [9, 10, 11],
    [12, 13, 14],
    [13, 14, 15],
    # Vertical
    [0, 4, 8],
    [4, 8, 12],
    [1, 5, 9],
    [5, 9, 13],
    [2, 6, 10],
    [6, 10, 14],
    [3, 7, 11],
    [7, 11, 15],
    # Diagonal
    [0, 5, 10],
    [5, 10, 15],
    [1, 6, 11],
    [4, 9, 14],
    [3, 6, 9],
    [6, 9, 12],
    [7, 10, 13],
    [2, 5, 8],
    # Horizontal backwards
    [2, 1, 0],
    [3, 2, 1],
    [6, 5, 4],
    [7, 6, 5],
    [10, 9, 8],
    [11, 10, 9],
    [14, 13, 12],
    [15, 14, 13],
    # Vertical backwards
    [2, 4, 0],
    [6, 8, 4],
    [3, 5, 1],
    [7, 9, 5],
    [10, 6, 2],
    [14, 10, 6],
    [11, 7, 3],
    [15, 11, 7],
    # Diagonal backwards
    [10, 5, 0],
    [15, 10, 5],
    [11, 6, 1],
    [14, 9, 4],
    [9, 6, 3],
    [12, 9, 6],
    [13, 10, 7],
    [8, 5, 2],
]

def game_loss(grid: list[str]) -> bool:
    for location in BAD_LOCATIONS:
        if grid[location[0]] == "f" and grid[location[1]] == "o" and grid[location[2]] == "x":
            return True
    return False

def main():
    patterns = ["f"] * 5 + ["o"] * 6 + ["x"] * 5
    all_perms = list(more_itertools.distinct_permutations(patterns))
    
    wins = 0
    loses = 0

    for grid in all_perms:
        if game_loss(grid):
            loses += 1
        else:
            wins += 1

    print(f"Wins: {wins:,}")
    print(f"Loses: {loses:,}")
    print(f"Win Percentage: {wins / (wins + loses) * 100:,} %")
    
if __name__ == "__main__":
    main()