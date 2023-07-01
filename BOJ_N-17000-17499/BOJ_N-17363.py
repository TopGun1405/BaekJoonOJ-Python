def main():
    c = {'.': 46, 'O': 79, '-': 124, '|': 45, '/': 92,
         '\\': 47, '^': 60, '<': 118, 'v': 62, '>': 94}

    N, M = map(int, input().split())
    pic = [input() for _ in range(N)]

    for i in range(M-1, -1, -1):
        print(''.join(map(chr, [c[pic[j][i]] for j in range(N)])))


if __name__ == "__main__":
    main()
