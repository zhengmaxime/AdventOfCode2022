INPUT_FILE = 'input'

# Rock: A X
# Paper: B Y
# Scissors C Z

LOSE, DRAW, WIN = 0, 3, 6

def get_result_1(opponent, myplay):
    if myplay == (opponent + 1) % 3:
        return WIN
    elif myplay == opponent:
        return DRAW
    else:
        return LOSE

def get_score_1(line):
    opponent, myplay = ord(line[0]) - ord('A'), ord(line[2]) - ord('X')
    return 1 + myplay + get_result_1(opponent, myplay)


# Part 2
ROUND_RESULT_VALUES = {
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN
}

def get_score_2(line):
    round_result = ROUND_RESULT_VALUES[line[2]]
    opponent = ord(line[0]) - ord('A')
    selected_shape = 1

    if round_result == WIN:
        selected_shape += (opponent + 1) % 3
    elif round_result == DRAW:
        selected_shape += opponent
    else:
        selected_shape += (opponent - 1) % 3

    return selected_shape + round_result

def main():
    with open(INPUT_FILE, 'r') as f:
        return sum([get_score_2(line) for line in f])

if __name__ == "__main__":
    res = main()
    print(res)