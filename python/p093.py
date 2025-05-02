# pylint: disable=line-too-long
"""
Project Euler Problem 93: Arithmetic Expressions

Problem description:
From a set of four distinct digits, generate expressions using +, −, *, and / to produce the longest set of consecutive 
positive integers starting from 1. The goal is to determine which set of four digits produces the longest consecutive run.

Answer: 1258
"""

import itertools
from typing import List, Tuple, Set


def evaluate_expressions(numbers: Tuple[int, int, int, int], operations: Tuple[str, str, str], parenthesis_patterns: List[str], operators: List[str]) -> Set[int]:
    """
    Generate and evaluate all valid expressions for a number tuple and operator triple using different parenthesis groupings.

    Args:
        numbers (Tuple[int, int, int, int]): The tuple of 4 digits to be used in the expression.
        operations (Tuple[str, str, str]): The tuple of 3 operators to be used in the expression.
        parenthesis_patterns (List[str]): A list of different parenthesis arrangements for the expression.
        operators (List[str]): A list of operators like '+', '-', '*', '/'.

    Returns:
        Set[int]: A set of valid integer results obtained from evaluating the expressions.
    """
    results = set()
    a, b, c, d = map(str, numbers)
    op1, op2, op3 = operations

    for pattern in parenthesis_patterns:
        expr = pattern.format(a, op1, b, op2, c, op3, d)
        try:
            value = eval(expr)
            if value > 0 and float(value).is_integer():
                results.add(int(value))
        except ZeroDivisionError:
            continue

    return results


def compute() -> str:
    """
    Finds the 4-digit combination that produces the longest run of consecutive positive integers starting from 1.

    This function tries all combinations of four digits (from 0 to 9), evaluates all possible expressions with these digits
    using three operators and various parenthesis groupings, and determines which combination produces the longest sequence 
    of consecutive integers starting from 1.

    Returns:
        str: The sorted string of the 4 digits that create the longest sequence of consecutive integers.
    """
    # Local variables for operator and parenthesis patterns
    parenthesis_patterns = [
        "(({}{}{}){}{}){}{}",   # ((a op b) op c) op d
        "({}{}({}{}{})){}{}",   # (a op (b op c)) op d
        "{}{}(({}{}{}){}{})",   # a op ((b op c) op d)
        "{}{}({}{}({}{}{}))",   # a op (b op (c op d))
        "({}{}{}){}({}{}{})",   # (a op b) op (c op d)
    ]

    operators = ["+", "-", "*", "/"]

    max_consecutive = 0
    best_quadruple = ()

    for digits in itertools.combinations(range(10), 4):
        results = set()

        # Test all digit permutations and operator combinations
        for perm in itertools.permutations(digits):
            for ops in itertools.product(operators, repeat=3):
                results.update(evaluate_expressions(perm, ops, parenthesis_patterns, operators))

        # Count how many consecutive positive integers can be made starting from 1
        n = 1
        while n in results:
            n += 1

        if n - 1 > max_consecutive:
            max_consecutive = n - 1
            best_quadruple = digits

    return ''.join(map(str, sorted(best_quadruple)))


if __name__ == "__main__":
    print(f"Problem 93: {compute()}")
