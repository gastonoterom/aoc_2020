from typing import List, Set
from functools import reduce

def main() -> None:
    with open("input.txt") as input_file:
        answers_by_group = [answer.replace("\n", "") for answer in input_file.read().split("\n\n")]

    groups = len(answers_by_group)
    answer_sets: List[Set] = [set() for _ in range(groups)]

    for i in range(groups):
        for answer in answers_by_group[i]:
            answer_sets[i].add(answer)

    questions_answered = sum( len(i) for i in answer_sets)
    print(questions_answered)

if __name__ == "__main__":
    main()