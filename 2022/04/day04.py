import logging
import os
import time

# Setup paths
SCRIPT_DIR = os.path.dirname(__file__)
# INPUT_FILE = "input\samkple_input.txt"
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
        lines_raw = f.readlines()
        lines = [item.strip() for item in lines_raw]

    
        fully_contained_counter = 0
        overlap_counter = 0
        for line in lines:
            pairs = line.split(",")
            interval_0_string = (pairs[0].split("-"))
            interval_0_int = [int(x) for x in interval_0_string]
            interval_0_range = list(range(interval_0_int[0],interval_0_int[1]+1))
            interval_1_string = (pairs[1].split("-"))
            interval_1_int = [int(x) for x in interval_1_string]
            interval_1_range = list(range(interval_1_int[0],interval_1_int[1]+1))
            # Part 1
            if set(interval_0_range).issubset(interval_1_range) or set(interval_1_range).issubset(interval_0_range):
                fully_contained_counter += 1
            # Part 2
            if any(item in interval_0_range for item in interval_1_range) or any(item in interval_1_range for item in interval_0_range):
                overlap_counter += 1
        logger.info("Result Part 1 = %d", fully_contained_counter)
        logger.info("Result Part 2 = %d", overlap_counter)



        


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    execution_time = t2-t1
    logger.info("Execution time: %0.4f seconds", execution_time)