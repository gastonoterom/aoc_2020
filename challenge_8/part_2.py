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


def process_instructions(instructions: List[Tuple]) -> Tuple:
    processed_instructions: List[int] = []
    instruction_id, operation, amount = instructions[0]
    pointer = 0
    accumulator = 0

    while True:
        if instruction_id in processed_instructions:
            return False, accumulator

        processed_instructions.append(instruction_id)

        accumulator, pointer = process_instruction(
            operation, amount, pointer, accumulator)

        if pointer == len(instructions):
            return True, accumulator

        instruction_id, operation, amount = instructions[pointer]


def fix_instructions(instructions, instruction_id, operation, amount):
    new_instructions = instructions.copy()
    new_instructions[instruction_id] = (
        instruction_id, 'jmp' if operation == 'nop' else 'nop', amount)

    return new_instructions


def process_and_fix_instructions(instructions: List[Tuple], pointer: int = 0) -> int:

    instruction_id, operation, amount = instructions[pointer]

    if operation not in ('jmp', 'nop'):
        return process_and_fix_instructions(instructions, pointer+1)

    fixed_instructions = fix_instructions(
        instructions, instruction_id, operation, amount)

    good_run, count = process_instructions(fixed_instructions)

    if not good_run:
        return process_and_fix_instructions(instructions, pointer+1)

    return count


instructions = parse_data("./challenge_8/data.txt")

print(process_and_fix_instructions(instructions))
