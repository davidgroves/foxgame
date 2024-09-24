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
    list(reversed([0, 1, 2])),
    list(reversed([1, 2, 3])),
    list(reversed([4, 5, 6])),
    list(reversed([5, 6, 7])),
    list(reversed([8, 9, 10])),
    list(reversed([9, 10, 11])),
    list(reversed([12, 13, 14])),
    list(reversed([13, 14, 15])),
    # Vertical backwards
    list(reversed([0, 4, 8])),
    list(reversed([4, 8, 12])),
    list(reversed([1, 5, 9])),
    list(reversed([5, 9, 13])),
    list(reversed([2, 6, 10])),
    list(reversed([6, 10, 14])),
    list(reversed([3, 7, 11])),
    list(reversed([7, 11, 15])),
    # Diagonal backwards
    list(reversed([0, 5, 10])),
    list(reversed([5, 10, 15])),
    list(reversed([1, 6, 11])),
    list(reversed([4, 9, 14])),
    list(reversed([3, 6, 9])),
    list(reversed([6, 9, 12])),
    list(reversed([7, 10, 13])),
    list(reversed([2, 5, 8])),
]

def game_loss(grid: list[str]) -> bool:
    for location in BAD_LOCATIONS:
        if grid[location[0]] == "f" and grid[location[1]] == "o" and grid[location[2]] == "x":
            return True
    return False

def show_grid(grid: list[int]) -> None:
    print(BAD_LOCATIONS)
    print(grid)
    print("=========")
    print(f"|{'x' if 0 in grid else ' '}|{'x' if 1 in grid else ' '}|{'x' if 2 in grid else ' '}|{'x' if 3 in grid else ' '}|")
    print("---------")
    print(f"|{'x' if 4 in grid else ' '}|{'x' if 5 in grid else ' '}|{'x' if 6 in grid else ' '}|{'x' if 7 in grid else ' '}|")
    print("---------")
    print(f"|{'x' if 8 in grid else ' '}|{'x' if 9 in grid else ' '}|{'x' if 10 in grid else ' '}|{'x' if 11 in grid else ' '}|")
    print("---------")
    print(f"|{'x' if 12 in grid else ' '}|{'x' if 13 in grid else ' '}|{'x' if 14 in grid else ' '}|{'x' if 15 in grid else ' '}|")
    print("=========")
    

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
