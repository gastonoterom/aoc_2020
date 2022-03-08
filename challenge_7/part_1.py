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
            unparsed_bag.split(" bags contain no other bags.")[0]: []
        }

    main_bag, unparsed_children = unparsed_bag.split(" bags contain ")
    children = [remove_bag_bags(child)
                for child in unparsed_children.split(", ")]

    return {
        main_bag: [
            c[2:]
            for c in children
        ]
    }


def read_document(path: str) -> List[str]:
    with open(path) as input_file:
        return input_file.read().split("\n")


def can_have_shiny(all_bags: dict, bag: str) -> bool:

    if all_bags[bag] == {} or bag == 'shiny gold':
        return False

    if 'shiny gold' in all_bags[bag]:
        return True

    for sub_bag in all_bags[bag]:
        if can_have_shiny(all_bags, sub_bag):
            return True

    return False


def find_all_shiny(all_bags: dict):
    return reduce(
        lambda acc, bag: acc + can_have_shiny(all_bags, bag),
        all_bags.keys(),
        0
    )


unparsed_bags = read_document("./challenge_7/bags.txt")
bags: dict = reduce(lambda a, b: a | b, parse_bags(unparsed_bags), {})
shiny_bags = find_all_shiny(bags)

print(shiny_bags)
