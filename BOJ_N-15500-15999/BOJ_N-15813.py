def main():
    N = int(input())
    name = input()
    score = sum(map(ord, name)) - 64 * N
    print(score)


if __name__ == "__main__":
    main()
