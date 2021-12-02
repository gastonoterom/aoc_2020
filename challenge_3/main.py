from typing import List
from functools import reduce

def get_trees(map: List[str], xi: int = 3, yi: int = 1) -> int:
    current_col, current_row, trees = xi, yi, 0

    while current_row < len(map):
        if map[current_row][current_col] == "#":
            trees += 1

        current_col = (current_col + xi) % len(map[current_row])
        current_row = current_row + yi

    return trees


def main() -> None:
    with open("map.txt") as map_file:
        map = [line.strip() for line in map_file.readlines()]

    # Part 1
    trees = get_trees(map)
    print(trees)

    # Part 2
    starting_locations = [
        [1, 1], [3, 1], [5, 1], [7, 1], [1, 2]
    ]

    trees = reduce(
        lambda a, b: a*b,
        [get_trees(map, x, y) for x,y in starting_locations]
    )

    print(trees)


if __name__ == "__main__":
    main()
