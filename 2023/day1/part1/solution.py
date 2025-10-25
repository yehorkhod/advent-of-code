from string import digits

FILE_PATH: str = 'input.txt'
with open(FILE_PATH, 'r') as input:
    lines: list[str] = input.readlines()

result: int = 0
for line in lines:
    match [char for char in line if char in digits]:
        case [a]:
            result += int(a + a)
        case [a, *_, b]:
            result += int(a + b)

print(result)
