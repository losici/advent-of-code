import logging
import os
import time

# Setup paths
SCRIPT_DIR = os.path.dirname(__file__)
# INPUT_FILE = "input\sample_input.txt"
INPUT_FILE = "input\input.txt"

# Setup logging
logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s", 
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main():
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

        #Part 2
        calories_x_elf.sort(reverse = True)
        max_calories_3_elves = sum(calories_x_elf[0:3])
        
        logger.info("Result Part 2 = %d", max_calories_3_elves)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    execution_time = t2-t1
    logger.info("Execution time: %0.4f seconds", execution_time)