from aocd import numbers


def count_increments(arr):
    deltas = [second - first for first,
              second in zip(arr[:-1], arr[1:])]
    lesser = [s for s in deltas if s > 0]
    return len(lesser)


def solve_first_puzzle():
    return count_increments(numbers)


def solve_second_puzzle():
    sums = [x+y+z for x, y, z in zip(numbers[:-2], numbers[1:-1], numbers[2:])]
    return count_increments(sums)


if __name__ == "__main__":
    print(f"First puzzle: {solve_first_puzzle()}")
    print(f"Second puzzle: {solve_second_puzzle()}")
