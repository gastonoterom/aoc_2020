from typing import List, Tuple


def parse_file(path: str) -> List[int]:
    with open(path) as input_file:
        return [int(i) for i in input_file.read().split("\n")]


def is_valid(number: int, preambles: List[int]) -> bool:
    for i in range(len(preambles) - 1):
        for j in range(i + 1, len(preambles)):
            if preambles[i] + preambles[j] == number:
                return True

    return False


def check_preambles(num_list: List[int], preamble_number: int) -> int:
    for i in range(preamble_number, len(num_list)+1):
        if not is_valid(num_list[i], num_list[i-preamble_number:i]):
            return num_list[i]

    return -1


def find_weakness(num_list: List[int], preamble_number: int, weakness: int) -> int:

    for i in range(0,  len(num_list)-1):
        for j in range(i+1, len(num_list)):
            sub_set = num_list[i:j]
            if sum(sub_set) == weakness:
                return min(sub_set) + max(sub_set)

    return -1


numbers = parse_file("./challenge_9/data.txt")
weakness = check_preambles(numbers, 25)
print(find_weakness(numbers, 25, weakness))
