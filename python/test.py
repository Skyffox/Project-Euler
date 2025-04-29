# pylint: disable=line-too-long
"""
Test suite for the AoC solutions for 2024 (for now). 
Since all our modules contain the standard entry point of if __name__ == "__main__" we can not simply run 
the module to get our output. We also can not run the individual functions because they require variable arguments.
So instead I will use the subprocess.run() function to read the stdout of each file in this directory and 
compare that with the answers given by the AoC website.
"""

import re
import subprocess
import time
import os
import fnmatch


def find_file(pattern: str, path: str) -> str:
	"""Walk the directory for the path variable and return the file that matches the pattern"""
	for _, _, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				return name
	return ""


def run_tests() -> None:
	"""aa"""
	total_time: float = 0.0 # In seconds
	num_pass: int = 0
	num_fail: int = 0

	for (prob, expect_answers) in sorted(ANSWERS.items()):
		start_time: float = time.time()

		# Find file in the current directory that has the following format: dayXX.py
		module = find_file(f'p{prob:03}.py', os.getcwd())

		# Run the entire file as a subprocces and pipe the output to stdout
		output: str = subprocess.run(f'python3 {module}', check=False, capture_output=True, text=True).stdout

		# Answer are always in the form: Problem X: XXXXX
		output = re.findall(r'Problem .+:.+\n', output)

		ans = output[0].split(":")[1].strip()

		elapsed_time: float = time.time() - start_time
		total_time += elapsed_time

		if ans == expect_answers:
			failstr: str = ""
			num_pass += 1
		else:
			failstr = "    *** FAIL ***"
			num_fail += 1

		print(f"\r{' '*70}\r", end="")
		print(f"Problem {prob:03}: {int(round(elapsed_time * 1000)):7} ms{failstr}")

	print(f"Elapsed = {int(total_time)} s, Passed = {num_pass}, Failed = {num_fail}")


ANSWERS: dict[int,str] = {
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
	206: "1389019170",
}


if __name__ == "__main__":
	run_tests()
