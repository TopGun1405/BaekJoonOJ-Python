def main():
    N = int(input())
    move = input()
    pos = [0, 0]
    for w in move:
        if w == 'E':
            pos[0] += 1
        elif w == 'W':
            pos[0] -= 1
        elif w == 'N':
            pos[1] += 1
        else:
            pos[1] -= 1
    print(abs(pos[0]) + abs(pos[1]))


if __name__ == "__main__":
    main()
