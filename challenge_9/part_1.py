from typing import List


def parse_file(path: str) -> List[int]:
    with open(path) as input_file:
        return [int(i) for i in input_file.read().split("\n")]


def is_valid(number: int, preambles: List[int]) -> bool:
    for i in range(len(preambles) - 1):
        for j in range(i + 1, len(preambles)):
            if preambles[i] + preambles[j] == number:
                return True

    return False


def check_preambles(num_list: List[int], preamble_number) -> int:
    for i in range(preamble_number, len(num_list)+1):
        if not is_valid(num_list[i], num_list[i-preamble_number:i]):
            return num_list[i]

    return -1


numbers = parse_file("./challenge_9/data.txt")
print(check_preambles(numbers, 25))
