# test_aoc_template.py

import pathlib
import pytest
import aoc_202201 as aoc
import os

PUZZLE_DIR = pathlib.Path(__file__).parent
print(aoc.INPUT_FILE)
print(PUZZLE_DIR)

@pytest.fixture
def example1():
    # puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    puzzle_input = (PUZZLE_DIR / aoc.INPUT_FILE).read_text().strip()

    # input_file = os.path.join(aoc.SCRIPT_DIR,aoc.INPUT_FILE)
    # puzzle_input = (input_file).read_text().strip()
    print(puzzle_input)
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.mark.skip(reason = "Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == ...


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 24000

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == ...