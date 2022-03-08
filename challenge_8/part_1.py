from typing import List, Tuple


def parse_instruction(i: int, operation: str, position: str) -> Tuple:
    return (i, operation, int(position))


def parse_data(path: str) -> List[Tuple]:
    with open(path) as input_file:
        return [parse_instruction(i, *line.split()) for i, line in enumerate(input_file.read().split("\n"))]


def process_instruction(operation, amount, pointer, accumulator) -> Tuple:

    if operation == 'nop':
        return accumulator, pointer + 1
    elif operation == 'acc':
        return accumulator + amount, pointer + 1
    else:
        return accumulator, pointer + amount


def process_instructions(instructions: List[Tuple]) -> int:
    processed_instructions: List[int] = []
    instruction_id, operation, amount = instructions[0]
    pointer = 0
    accumulator = 0

    while instruction_id not in processed_instructions:

        processed_instructions.append(instruction_id)

        accumulator, pointer = process_instruction(
            operation, amount, pointer, accumulator)

        instruction_id, operation, amount = instructions[pointer]

    return accumulator


instructions = parse_data("./challenge_8/data.txt")

print(process_instructions(instructions))
