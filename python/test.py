# pylint: disable=line-too-long
"""
Test Suite for Project Euler Solutions

This script runs tests for the Project Euler solutions, comparing their outputs against the expected results.
Since each solution module has a standard entry point `if __name__ == "__main__"`, we can't simply run the modules directly or call the functions 
due to their need for variable arguments. Instead, this script uses `subprocess.run()` to execute each module and capture its output, 
which is then compared to the expected output for each problem.
"""

import os
import fnmatch
import re
import subprocess
import time
from typing import Dict


def find_file(pattern: str, path: str) -> str:
	"""
	Searches for a file in the given directory that matches the provided pattern.

	This function walks through the specified directory recursively and returns 
	the first file whose name matches the given pattern.

	Args:
		pattern (str): The pattern to match the filenames.
		path (str): The directory path to search for files.

	Returns:
		str: The filename that matches the pattern, or an empty string if no match is found.
	"""
	for _, _, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				return name
	return ""



def run_tests() -> None:
    """
    Executes the test suite for all Project Euler solutions and compares the results 
    to the expected answers. The function uses `subprocess.run()` to run each solution 
    and compares the output with pre-defined expected answers.

    The results are displayed in the format:
    - Problem number
    - Execution time in milliseconds
    - Pass/Fail status for each problem

    Finally, it displays the total time taken and the number of tests that passed/failed.
    """
    total_time: float = 0.0 # Total execution time in seconds
    num_passed: int = 0 # Counter for passed tests
    num_failed: int = 0 # Counter for failed tests

    # Iterate over all problems and their expected answers
    for problem_number, expected_answer in sorted(ANSWERS.items()):
        start_time: float = time.time()

        # Find the file corresponding to the current problem (dayXXX.py format)
        solution_file = find_file(f'p{problem_number:03}.py', os.getcwd())

        # Run the solution file as a subprocess and capture the output
        result = subprocess.run(
            f'python3 {solution_file}', check=False, capture_output=True, text=True
        )

        # Parse the output for the problem's answer
        output_lines = re.findall(r'Problem .+:.+\n', result.stdout)
        actual_answer = output_lines[0].split(":")[1].strip()

        elapsed_time: float = time.time() - start_time
        total_time += elapsed_time

        # Check if the answer matches the expected answer
        if actual_answer == expected_answer:
            fail_message: str = ""
            num_passed += 1
        else:
            fail_message = "    *** FAIL ***"
            num_failed += 1

        # Print the results for the current problem
        print(f"\r{' '*70}\r", end="") # Clear the line to print on the same line
        print(f"Problem {problem_number:03}: {int(round(elapsed_time * 1000)):7} ms{fail_message}")

    # Print the overall test results
    print(f"Elapsed = {int(total_time)} s, Passed = {num_passed}, Failed = {num_failed}")


ANSWERS: Dict[int, str] = {
	1: "233168",
	2: "4613732",
	3: "6857",
	4: "906609",
	5: "232792560",
	6: "25164150",
	7: "104743",
	8: "23514624000",
	9: "31875000",
	10: "142913828922",
	11: "70600674",
	12: "76576500",
	13: "5537376230",
	14: "837799",
	15: "137846528820",
	16: "1366",
	17: "21124",
	18: "1074",
	19: "171",
	20: "648",
	21: "31626",
	22: "871198282",
	23: "4179871",
	24: "2783915460",
	25: "4782",
	26: "983",
	27: "-59231",
	28: "669171001",
	29: "9183",
	30: "443839",
	31: "73682",
	32: "45228",
	33: "100",
	34: "40730",
	35: "55",
	36: "872187",
	37: "748317",
	38: "932718654",
	39: "840",
	40: "210",
	41: "7652413",
	42: "162",
	43: "16695334890",
	44: "5482660",
	45: "1533776805",
	46: "5777",
	47: "134043",
	48: "9110846700",
	49: "296962999629",
	50: "997651",
	51: "121313",
	52: "142857",
	53: "4075",
	54: "376",
	55: "249",
	56: "972",
	57: "153",
	58: "26241",
	59: "129448",
	60: "26033",
	61: "28684",
	62: "127035954683",
	63: "49",
	64: "1322",
	65: "272",
	66: "661",
	67: "7273",
	68: "6531031914842725",
	69: "510510",
	70: "8319823",
	71: "428570",
	72: "303963552391",
	73: "7295372",
	74: "402",
	75: "161667",
	76: "190569291",
	77: "71",
	78: "55374",
	79: "73162890",
	80: "40886",
	81: "427337",
	82: "260324",
	83: "425185",
	84: "101524",
	85: "2772",
	86: "1818",
	87: "1097343",
	88: "7587457",
	89: "743",
	90: "1217",
	91: "14234",
	92: "8581146",
	93: "1258",
	94: "518408346",
	95: "14316",
	96: "24702",
	97: "8739992577",
	98: "18769",
	99: "709",
	100: "756872327473",
	104: "329468",
	109: "38182",
	112: "1587000",
	206: "1389019170"
}


if __name__ == "__main__":
	run_tests()
