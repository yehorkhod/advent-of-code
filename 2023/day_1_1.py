input_path: str = 'input/input_1.txt'
digits: str = '0123456789'


def day_1_1(input_path: str) -> int:
    result: int = 0

    with open(input_path, 'r') as input:
        lines: list[str] = input.readlines()

    for line in lines:
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
    result: int = day_1_1(input_path)
    print(result)
