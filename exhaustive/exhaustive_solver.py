import more_itertools

BAD_LOCATIONS_FORWARDS = [
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
]

BAD_LOCATIONS_BACKWARDS = [
    list(reversed(location)) for location in BAD_LOCATIONS_FORWARDS
]
BAD_LOCATIONS = BAD_LOCATIONS_FORWARDS + BAD_LOCATIONS_BACKWARDS


def game_loss(grid: list[str]) -> bool:
    for location in BAD_LOCATIONS:
        if (
            grid[location[0]] == "f"
            and grid[location[1]] == "o"
            and grid[location[2]] == "x"
        ):
            return True
    return False


def show_grid(grid: list[int]) -> None:
    print(BAD_LOCATIONS)
    print(grid)
    print("=========")
    print(
        f"|{'x' if 0 in grid else ' '}|{'x' if 1 in grid else ' '}|{'x' if 2 in grid else ' '}|{'x' if 3 in grid else ' '}|"
    )
    print("---------")
    print(
        f"|{'x' if 4 in grid else ' '}|{'x' if 5 in grid else ' '}|{'x' if 6 in grid else ' '}|{'x' if 7 in grid else ' '}|"
    )
    print("---------")
    print(
        f"|{'x' if 8 in grid else ' '}|{'x' if 9 in grid else ' '}|{'x' if 10 in grid else ' '}|{'x' if 11 in grid else ' '}|"
    )
    print("---------")
    print(
        f"|{'x' if 12 in grid else ' '}|{'x' if 13 in grid else ' '}|{'x' if 14 in grid else ' '}|{'x' if 15 in grid else ' '}|"
    )
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
