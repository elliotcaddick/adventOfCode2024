"""
--- Day 7: Bridge Repair ---
"""

from itertools import product

def can_produce_target(numbers, target):
    def evaluate(index, current_value):
        if index == len(numbers):
            return current_value == target

        return (evaluate(index + 1, current_value + numbers[index]) or
                evaluate(index + 1, current_value * numbers[index]))

    return evaluate(1, numbers[0])

def part_one(filename):
    calibration_result = 0

    with open(filename) as file:
        for line in file:
            line = line.strip()
            test_value_str, numbers_str = line.split(':')
            test_value = int(test_value_str)
            numbers = [int(n) for n in numbers_str.split()]

            if can_produce_target(numbers, test_value):
                calibration_result += test_value

    return calibration_result

           
# print(f"Part 1: {part_one("day7/input/puzzle.txt")}")


def can_produce_target_2(numbers, target):
    def evaluate(index, current_value):
        if index == len(numbers):
            return current_value == target
        
        return (evaluate(index + 1, current_value + numbers[index]) or
                evaluate(index + 1, current_value * numbers[index]) or
                evaluate(index + 1, int(str(current_value) + str(numbers[index]))))

    return evaluate(1, numbers[0])

def part_two(filename):
    calibration_result = 0

    with open(filename) as file:
        for line in file:
            line = line.strip()
            test_value_str, numbers_str = line.split(':')
            test_value = int(test_value_str)
            numbers = [int(n) for n in numbers_str.split()]

            if can_produce_target_2(numbers, test_value):
                calibration_result += test_value

    return calibration_result

# print(f"Part 2: {part_two("day7/input/puzzle.txt")}")