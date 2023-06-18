def main():
    N = int(input())
    S = input()
    box, pos = [0, 0, 0], 0
    for s in S:
        if s == 'L':
            pos = pos - (1 if pos > 0 else 0)
            box[pos] += 1
        else:
            pos = pos + (1 if pos < 2 else 0)
            box[pos] += 1
    print(box[2])


if __name__ == "__main__":
    main()
