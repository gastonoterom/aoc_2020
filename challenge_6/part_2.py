def main() -> None:
    with open("input.txt") as input_file:
        answers_by_group = [answer.split("\n") for answer in input_file.read().split("\n\n")]

    asws = 0
    # We iterate each group
    for group in answers_by_group:

        # We check if each of the first persons answers is in each of the other peoples answers
        first_persons_answers = list(group[0])
        for answer in first_persons_answers:
            # We assume each answer is present, we have to proove the opposite
            in_all = True

            other_persons = group[1:]
            # We compare each first person answer to others
            for other_person in other_persons:
                in_person = False
                for other_answer in list(other_person):
                    # If the answer of the first person is in the other person, set in_person to true
                    if (answer == other_answer):
                        in_person = True
                # If the answer was not in this person it means that it was not in everyone so we set it to false
                if (not in_person):
                    in_all = False
            if(in_all):
                asws += 1
    print(asws)

if __name__ == "__main__":
    main()