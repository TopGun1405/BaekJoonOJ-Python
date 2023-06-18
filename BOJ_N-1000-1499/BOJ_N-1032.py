def main():
    N = int(input())
    pattern = list(input())
    for _ in range(N - 1):
        name = input()
        for i in range(len(pattern)):
            if pattern[i] != name[i]:
                pattern[i] = '?'
    print(''.join(pattern))


if __name__ == "__main__":
    main()
