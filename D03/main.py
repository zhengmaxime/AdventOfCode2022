INPUT_FILE = 'input'

def get_score(c):
    shift = ord('A') - 26 if c.isupper() else ord('a')
    val = ord(c) - shift + 1
    return val

def read_line(s):
    m = len(s) // 2
    for c in s[m:]:
        if c in s[:m]:
            return get_score(c)
    return 0

def read_file():
    with open(INPUT_FILE, 'r') as f:
        return sum(map(read_line, f))

def main():
    return read_file()

if __name__ == "__main__":
    res = main()
    print(res)
