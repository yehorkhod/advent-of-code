input_path: str = 'input/input_1.txt'

digits_text: list[str] = ['zero', 'one', 'two', 'three','four', 'five', 'six', 'seven', 'eight', 'nine']
digits: list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
hash: dict[str, str] = dict(zip(digits_text, digits))

special_digits: list[str] = ['zerone', 'oneight', 'twone', 'threeight', 'fiveight', 'sevenine', 'eightwo', 'eighthree']
special_values: list[str] = ['01', '18', '21', '38', '58', '79', '82', '83']
special_hash: dict[str, str] = dict(zip(special_digits, special_values))


def day_1_2(input_path: str) -> int:
    result: int = 0

    with open(input_path, 'r') as input:
        lines: list[str] = input.readlines()

    for line in lines:
        for special_digit in special_digits:
            line = special_hash[special_digit].join(line.split(special_digit))

        for digit_text in digits_text:
            line = hash[digit_text].join(line.split(digit_text))

        for i in line:
            if i in digits:
                result += int(i) * 10
                break

        for j in line[::-1]:
            if j in digits:
                result += int(j)
                break

    return result


if __name__ == "__main__":
    result: int = day_1_2(input_path)
    print(result)
