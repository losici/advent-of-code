# aoc_template.py

import pathlib
import sys
import logging
import os

# Setup paths
SCRIPT_DIR = os.path.dirname(__file__)
#INPUT_FILE = "input/input.txt"
INPUT_FILE = "input/sample_input.txt"
print(SCRIPT_DIR)
print(INPUT_FILE)

# Setup logging
logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s", 
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# print some stuff
logger.debug("We'll see this.")
logger.info("And this.")


def parse(puzzle_input):
    """Parse input"""

def part1(data):
    """Solve part 1"""
    input_file = os.path.join(SCRIPT_DIR,INPUT_FILE)
    logger.debug("Input file path = %s", input_file)
    with open(input_file, mode = 'rt') as f:
        num_elves =f.read().split('\n\n')

        # Part 1
        calories_x_elf = []
        for elf in num_elves:
            calories = elf.split('\n')
            calories = [int(i) for i in calories]
            calories_x_elf.append(sum(calories))
        max_calories_x_elf = max(calories_x_elf)
        logger.info("Result Part 1 = %d", max_calories_x_elf)
    return max_calories_x_elf
    
def part2(data):
    """Solve part 2"""

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))