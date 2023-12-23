INPUT_FILE = 'input'

def get_score(c):
    shift = ord('A') - 26 if c.isupper() else ord('a')
    val = ord(c) - shift + 1
    return val

def read_lines(s1, s2, s3):
    for c in s1:
        if c in s2:
            if c in s3:
                return get_score(c)
    return 0

def read_file():
    score = 0

    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            score += read_lines(lines[i], lines[i+1], lines[i+2])
            i += 3
    return score

def main():
    return read_file()

if __name__ == "__main__":
    res = main()
    print(res)

