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


def day_2_2(input_path: str) -> int:
    games: list[tuple[int, list[list[int]]]] = []
    powers: list[int] = []

    with open(input_path, 'r') as input:
        lines: list[str] = input.readlines()

    for line in lines:
        id, game = line.split(': ')

        id = int(id[5:])
        subgames: list[str] = game.split('; ')

        rgb_subgames: list[list[int]] = [rgb(subgame) for subgame in subgames]

        games.append((id, rgb_subgames))

    for id, game in games:
        max_red: int = 0
        max_green: int = 0
        max_blue: int = 0

        for subgame in game:
            if subgame[0] > max_red:
                max_red = subgame[0]
            if subgame[1] > max_green:
                max_green = subgame[1]
            if subgame[2] > max_blue:
                max_blue = subgame[2]

        power: int = max_red * max_green * max_blue
        powers.append(power)
    
    return sum(powers)

if __name__ == "__main__":
    result: int = day_2_2(input_path)
    print(result)
