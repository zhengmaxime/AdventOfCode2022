from collections import defaultdict


def main():
    filepath = []
    fqdn = defaultdict(int)

    f = open('input', 'r')
    for line in f:
        if line.startswith('$ ls'):
            continue
        elif line.startswith('$ cd'):
            dir = line[5:].strip()
            if dir == "..":
                filepath.pop()
            else:
                filepath.append(dir + '/')
        else:
            if line.startswith('dir'):
                continue
            else:
                size = int(line.split()[0])
                for i in range(1, 1 + len(filepath)):
                    fqdn["".join(filepath[:i])] += size

    f.close()
    return sum([size for size in fqdn.values() if size <= 100_000]), \
            min([size for size in fqdn.values() if size > 30_000_000 - (70_000_000 - fqdn['//'])])

