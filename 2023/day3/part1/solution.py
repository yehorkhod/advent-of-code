input_path: str = 'input/input_3.txt'
digits: str = '0123456789'


# check whether there is a symbol around the digit
def check(buffer: str, index: int, row_length: int) -> bool:
    # skip if we're in the end of a row
    if index % row_length != 0:
        for shift in [-1, (row_length - 1), -(row_length + 1)]:
            try:
                if not (buffer[index + shift].isdigit() or buffer[index + shift] == '.'):
                    return True
            except IndexError:
                continue

    # skip if we're in the start of a row
    if (index + 1) % row_length != 0:
        for shift in [1, (row_length + 1), -(row_length - 1)]:
            try:
                if not (buffer[index + shift].isdigit() or buffer[index + shift] == '.'):
                    return True
            except IndexError:
                continue

    for shift in [-row_length, row_length]:
        try:
            if not (buffer[index + shift].isdigit() or buffer[index + shift] == '.'):
                return True
        except IndexError:
            continue

    return False


def day_3_1(input_path: str) -> int:
    with open(input_path, 'r') as input:
        lines: list[str] = []

        for line in input.readlines():
            lines.append(line[:-1])

    row_length: int = len(lines[0])

    buffer: str = ''.join(lines)

    sum: int = 0
    cur_num: str = ''
    valid: bool = False

    for i, char in enumerate(buffer):
        if char.isdigit():
            cur_num += char

            if check(buffer, i, row_length):
                valid = True

            # refresh if we're in the end of a row
            if (i + 1) % row_length == 0:
                if valid:
                    sum += int(cur_num)

                cur_num = ''
                valid = False

            continue

        # refresh
        if valid:
            sum += int(cur_num)

        cur_num = ''
        valid = False
        
    return sum


if __name__ == "__main__":
    result: int = day_3_1(input_path)
    print(result)
