def main():
    n = int(input())
    tot = 0
    for _ in range(n):
        tot += int(input())
    print(tot)
    # print(sum(int(input()) for _ in range(int(input()))))


if __name__ == "__main__":
    main()
