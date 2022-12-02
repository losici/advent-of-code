import logging
import os
import time
import numpy as np

# Setup paths
SCRIPT_DIR = os.path.dirname(__file__)
# INPUT_FILE = "input\sample_input.txt"
INPUT_FILE = "input\input.txt"

# Setup logging
logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s", 
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

marks = {   "Rock"      : 1,
            "Paper"     : 2,
            "Scissors"  : 3
}

opponent = {    "A" : "Rock",
                "B" : "Paper",
                "C" : "Scissors"
}

elf_part1 = {   "X" : "Rock",
                "Y" : "Paper",
                "Z" : "Scissors"
}

elf_part2 = {   "X" : "lose",
                "Y" : "draw",
                "Z" : "win"
}

# Rock & Paper vittoria = paper + 6
# Rock & Scissor perso = 3 + 0
# Paper & Rock perso = 1 + 0
# Paper & Scissor vittoria = scissor + 6
# Scissor & Paper perso = paper + 0
# Scissor & Rock vittoria = rock + 6

def compute_score(l_opponent, l_elf):
    l_score = 0
    if l_opponent == l_elf:
        l_score =  marks[l_elf] + 3
    else:
        if  (l_opponent == "Rock" and l_elf == "Paper") or \
            (l_opponent == "Paper" and l_elf == "Scissors") or \
            (l_opponent == "Scissors" and l_elf == "Rock"):
            l_score = marks[l_elf] + 6
        else:
            l_score = marks[l_elf]
    return l_score

def solve_part1(l_opponent, l_elf):
    choice_opponent = opponent[l_opponent]
    choice_elf = elf_part1[l_elf]
    l_score = compute_score(choice_opponent, choice_elf)
    return l_score

def compute_choice_with_round_end(l_opponent, l_round):
    l_choice_opponent = opponent[l_opponent]
    l_round_end = elf_part2[l_round]
    l_choice_elf = "None"
    if l_round_end == "draw":
        l_choice_elf = l_choice_opponent
    elif l_round_end == "lose":
        if l_choice_opponent == "Rock":
            l_choice_elf = "Scissors"
        elif l_choice_opponent == "Paper":
            l_choice_elf = "Rock"
        else:
            l_choice_elf = "Paper"
    else:
        if l_choice_opponent == "Rock":
            l_choice_elf = "Paper"
        elif l_choice_opponent == "Paper":
            l_choice_elf = "Scissors"
        else:
            l_choice_elf = "Rock"
    return [l_choice_opponent, l_choice_elf]

def solve_part2(l_opponent, l_round):
    [choice_opponent, choice_elf] = compute_choice_with_round_end(l_opponent, l_round)
    l_score = compute_score(choice_opponent, choice_elf)
    return l_score

def main():
    input_file = os.path.join(SCRIPT_DIR,INPUT_FILE)
    logger.debug("Input file path = %s", input_file)
    file_data = np.loadtxt(input_file, dtype='str')
    num_col = file_data.shape[1]
    num_row = file_data.shape[0]
   
    # part 1
    score_count = 0
    for i in range(num_row):
        opponent_temp = file_data[i,0]
        elf_temp = file_data[i,1]
        score = solve_part1(opponent_temp,elf_temp)
        score_count += score
    logger.info("Result Part 1: %d", score_count)

    # part 2
    score_count = 0
    for i in range(num_row):
        opponent_temp = file_data[i,0]
        elf_temp = file_data[i,1]
        score = solve_part2(opponent_temp,elf_temp)
        score_count += score
    logger.info("Result Part 2: %d", score_count)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    execution_time = t2-t1
    logger.info("Execution time: %0.4f seconds", execution_time)