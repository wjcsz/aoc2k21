from dataclasses import dataclass

@dataclass
class Position:
    horizontal: int = 0
    depth: int = 0

    def encoding(self) -> int:
        return self.horizontal * self.depth

class Submarine:
    def __init__(self):
        self.position = Position(0, 0)
        self.aim = 0

    def forward(self, delta):
        self.position.horizontal += delta
        self.position.depth += self.aim * delta


    def down(self, delta):
        self.aim += delta

    def up(self, delta):
        self.aim -= delta

    def get_position(self):
        return self.position.encoding()



def first_puzzle(submarine: Submarine) -> None:
    with open("input.txt") as puzzle:
        for command in puzzle:
            match command.split():
                    case ["forward", distance]:
                        submarine.forward(int(distance))
                    case ["up", distance]:
                        submarine.up(int(distance))
                    case ["down", distance]:
                        submarine.down(int(distance))
        return submarine.get_position()



if __name__ == "__main__":
    submarine = Submarine()
    print(first_puzzle(submarine))
