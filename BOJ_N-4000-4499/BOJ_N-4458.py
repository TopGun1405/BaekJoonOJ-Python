def main():
    N = int(input())
    for _ in range(N):
        line = input().split()
        line[0] = line[0].title()
        print(' '.join(line))


if __name__ == "__main__":
    main()
