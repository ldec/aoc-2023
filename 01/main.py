import re
from typing import List

from rich import print

from utils.readers import OneColumnFileReader

test_reader = OneColumnFileReader("input-test.txt")
test_data = test_reader.read()

reader = OneColumnFileReader("input.txt")
prod_data = reader.read()

data_sources = (
    ("Test data", test_data),
    ("Prod data", prod_data),
)

LETTER_REGEX = re.compile(r"[a-z]")

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_calibration_values(data: List[str]) -> List[int]:
    values = []
    for line in data:
        line = LETTER_REGEX.sub("", line)
        values.append(int(f"{line[0]}{line[-1]}"))

    return values


def find_digits(value: str):
    found = []
    for i, digit in enumerate(DIGITS.keys()):
        if digit in value:
            found.append((digit, value.index(digit)))

    return sorted(found, key=lambda x: x[1])


def get_calibration_values_2(data: List[str]) -> List[int]:
    values = []
    for line in data:
        found = find_digits(line)
        while found:
            num = found[0][0]
            index = found[0][1]

            line = line[:index] + str(DIGITS[num]) + line[index + 1 :]
            found = find_digits(line)

        line = LETTER_REGEX.sub("", line)
        values.append(int(f"{line[0]}{line[-1]}"))

    return values


for data_source_name, data_source in data_sources:
    # print(
    #     f"Day 1 - Result 1 - {data_source_name}: {sum(get_calibration_values(data_source))}"
    # )
    print(
        f"Day 1 - Result 2 - {data_source_name}: {sum(get_calibration_values_2(data_source))}"
    )
