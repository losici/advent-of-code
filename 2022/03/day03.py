import logging
import os
import time
import re
import string

# Setup paths
SCRIPT_DIR = os.path.dirname(__file__)
# INPUT_FILE = "input\sample_input.txt"
INPUT_FILE = "input\input.txt"

# Setup logging
logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s", 
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# define an alphabet
alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# dict alphabet and priorities
rdict = dict([ (frozenset(x[1]),x[0]+1) for x in enumerate(alfabet) ])


def main():
    input_file = os.path.join(SCRIPT_DIR,INPUT_FILE)
    logger.debug("Input file path = %s", input_file)
    with open(input_file, mode = 'rt') as f:
        lines = f.read().split('\n')
        lines_len = len(lines)
        # Part 1
        priorities_sum = 0
        for line in lines:
            line_dim = len(line)
            compartment1 = frozenset(line[0:int(line_dim/2)])
            compartment2 = frozenset(line[int(line_dim/2):line_dim])
            common_item = (compartment1 & compartment2)
            common_item_priority = rdict[common_item]
            priorities_sum += common_item_priority
        logger.info("Result Part 1 = %d", priorities_sum)
        
        # Part 2
        counter = 0
        priorities_sum_badge = 0
        while(counter < lines_len):
            rucksack1 = frozenset(lines[counter])
            counter += 1
            rucksack2 = frozenset(lines[counter])
            counter += 1
            rucksack3 = frozenset(lines[counter])
            counter += 1
            badge = rucksack1 & rucksack2 & rucksack3
            badge_priority = rdict[badge]
            priorities_sum_badge += badge_priority
        logger.info("Result Part 2 = %d", priorities_sum_badge)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    execution_time = t2-t1
    logger.info("Execution time: %0.4f seconds", execution_time)