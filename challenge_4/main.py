from typing import Callable, List
from functools import reduce

def validate_height(height:str) -> bool:
    unit = height[len(height)-2:]
    try:
        amount = int(height[:len(height)-2])
    except:
        return False

    if(unit not in ["cm", "in"]):
        return False

    if(unit == "cm"):
        return 150<=amount<=193
    
    return 59<=amount<=76

def get_validator(field_name: str) -> Callable:
    validators = {
        "byr": lambda x: len(x) == 4 and 1920<=int(x)<=2002,
        "iyr": lambda x: len(x) == 4 and 2010<=int(x)<=2020,
        "eyr": lambda x: len(x) == 4 and 2020<=int(x)<=2030,
        "hgt": validate_height,
        "hcl": lambda x: 
            x[0] == "#" and 
            len(x[1:]) == 6 and
            x[1:].isalnum(),
        "ecl": lambda x: x in "amb blu brn gry grn hzl oth".split(),
        "pid": lambda x: len(x) == 9 and x.isdecimal(),
        "cid": lambda _: True,
    }
    return validators[field_name]


def validate_field(field_name: str, field_value: str) -> bool:
    return get_validator(field_name)(field_value)


def check_passport(passport: List[str]) -> bool:
    passport_fields = {
        "byr": False, "iyr": False, "eyr": False, "hgt": False,
        "hcl": False, "ecl": False, "pid": False, "cid": True
    }

    for field in passport:
        field_name, field_value = field.split(":")
        passport_fields[field_name] = validate_field(field_name, field_value)

    return reduce(lambda a,b: (a and b), passport_fields.values())


def check_passports(passports: List[List[str]]) -> List[bool]:
    return [check_passport(passport) for passport in passports]


def valid_passports(passports: List[List[str]]) -> int:
    return len(list(filter(lambda a: a, check_passports(passports))))


def main() -> None:
    with open("passports.txt") as passports_file:
        passports = [ passport.replace("\n", " ").split() for passport in passports_file.read().split("\n\n")]

    print(valid_passports(passports))


if __name__ == "__main__":
    main()