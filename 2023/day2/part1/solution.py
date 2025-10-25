input_path: str = 'input/input_2.txt'
cubes: list[int] = [12, 13, 14]


def rgb(subgame: str) -> list[int]:
    result: list[int] = [0, 0, 0]
    splits: list[str] = subgame.split(', ')

    for split in splits:
        number, color = split.split(' ')
        if 'red' in color:
            result[0] += int(number)
        if 'green' in color:
            result[1] += int(number)
        if 'blue' in color:
            result[2] += int(number)

    return result


def day_2_1(input_path: str) -> int:
    games: list[tuple[int, list[list[int]]]] = []
    impossible_games: list[int] = []

    with open(input_path, 'r') as input:
        lines: list[str] = input.readlines()

    for line in lines:
        id, game = line.split(': ')

        id = int(id[5:])
        subgames: list[str] = game.split('; ')

        rgb_subgames: list[list[int]] = [rgb(subgame) for subgame in subgames]

        games.append((id, rgb_subgames))

    for id, game in games:
        for subgame in game:
            if subgame[0] > cubes[0] or subgame[1] > cubes[1] or subgame[2] > cubes[2]:
                impossible_games.append(id)
                break

    return sum([i for i in range(1, 101)]) - sum(impossible_games)


if __name__ == "__main__":
    result: int = day_2_1(input_path)
    print(result)
