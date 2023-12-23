INPUT_FILE = 'input'

N = 3 # Part 1
N = 14 # Part 2

def is_marker(s):
    set_ = set(s)
    return len(set_) == len(s)

def read_file():
    f = open(INPUT_FILE, 'r')
    s = f.read()
    f.close()

    for i in range(len(s) - N + 1):
        if is_marker(s[i : i+N]):
            return i + N
    return -1

def main():
    return read_file()


if __name__ == "__main__":
    res = main()
    print(res)
