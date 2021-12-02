from typing import Callable

def recursive_find_builder(seat: str, lower_char: str) -> Callable: 
    def recursive_find(index, first_seat: int, last_seat: int) -> int:
        if first_seat == last_seat:
            return first_seat

        if seat[index] == lower_char:
            return recursive_find(index+1, first_seat, (first_seat + last_seat)//2,)
        else:
            return recursive_find(index+1, (first_seat + last_seat)//2 + 1, last_seat)

    return recursive_find

def get_row(seat: str) -> int:
    return recursive_find_builder(seat[:7], "F")(0, 0, 127)

def get_col(seat: str) -> int:
    return recursive_find_builder(seat[7:], "L")(0, 0, 7)

def get_id(seat: str) -> int:
    row = get_row(seat)
    col = get_col(seat)
    return row * 8 + col

def main() -> None:
    with open("seats.txt") as seats_file:
        max_id = max([get_id(seat.strip()) for seat in seats_file.readlines()])
    print(max_id)

if __name__ == "__main__":
    main()