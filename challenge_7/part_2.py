from functools import reduce
from re import M
from typing import Dict, List, Any


def remove_bag_bags(text: str) -> str:
    """Removes ' bag' or ' bags' from some str"""

    text = text.replace(" bag", "").replace(" bags", "").replace('.', "")

    if text[len(text)-1] == 's':
        return text[:len(text)-1]

    return text


def parse_bags(unparsed_bags: List[str]) -> List[dict]:
    return [parse_bag(bag) for bag in unparsed_bags]


def parse_bag(unparsed_bag: str) -> dict:

    # handle empty bags
    if "contain no other bags" in unparsed_bag:
        return {
            unparsed_bag.split(" bags contain no other bags.")[0]: {}
        }

    main_bag, unparsed_children = unparsed_bag.split(" bags contain ")
    children = [remove_bag_bags(child)
                for child in unparsed_children.split(", ")]

    return {
        main_bag: {
            c[2:]: int(c[:1])
            for c in children
        }
    }


def read_document(path: str) -> List[str]:
    with open(path) as input_file:
        return input_file.read().split("\n")


def count_sub_bags(all_bags: dict, bag: str) -> int:

    if all_bags[bag] == {}:
        return 0

    return reduce(lambda acc, sub_bag: acc +
                  all_bags[bag][sub_bag] +
                  all_bags[bag][sub_bag] * (count_sub_bags(all_bags, sub_bag)),
                  all_bags[bag],
                  0)


unparsed_bags = read_document("./challenge_7/bags.txt")
bags: dict = reduce(lambda a, b: a | b, parse_bags(unparsed_bags), {})
sub_bags_amount = count_sub_bags(bags, 'shiny gold')

print(sub_bags_amount)
