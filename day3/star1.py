def first_puzzle():
    with open("input.txt") as puzzle:
        first = puzzle.readline()
        counter = [int(char) for char in first[:-1]]
        for it, line in enumerate(puzzle, start=1):
            tmp = [int(char) for char in line[:-1]]
            counter = [c+t for c,t in zip(counter, tmp)]

        half = it//2 +1
        gamma = [x > half for x in counter]
        epsilon = [x < half for x in counter]

        def bool_2_bin(lst):
            return ''.join(['1' if x else '0' for x in lst])
        gamma_string, epsilon_string = bool_2_bin(gamma), bool_2_bin(epsilon)
        return int(gamma_string, base=2) * int(epsilon_string, base=2)


if __name__ == "__main__":
    print(first_puzzle())



