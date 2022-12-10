import logging
import os
import time
import numpy as np
import re

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
    with open(input_file) as f:
        crates_stack, instructions = (i.splitlines() for i in f.read().split("\n\n"))
        stacks = {int(digit):[] for digit in crates_stack[-1].replace(" ","")}

        indexes = [index for index, char in enumerate(crates_stack[-1]) if char != " "]
        for string in crates_stack[:-1]:
            stack_num = 1
            for index in indexes:
                if string[index] != " ":
                    stacks[stack_num].insert(0,string[index])
                stack_num += 1

        instructions_re = [[int(x) for x in (re.findall(r"[0-9]+",instruction))] for instruction in instructions]
        counter = 0
        for instruction in instructions_re:
            counter += 1
            num = instruction[0]
            from_stack= instruction[1]
            to_stack = instruction[2]
            temp = stacks[from_stack][-num:]
            if len(temp)>1:
                temp.reverse()

            for i in range(num):
                crate_removed = stacks[from_stack].pop()
                stacks[to_stack].append(crate_removed)
            # print("Instruction num %d:\n" % counter)
            # print(from_stack, stacks[from_stack])
            # print(to_stack, stacks[to_stack])



        result = [x[-1] for x in stacks.values()]
        Result = ''.join(result)
        logger.info("Result Part 1: %s" %Result)




if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    execution_time = t2-t1
    logger.info("Execution time: %0.4f seconds", execution_time)