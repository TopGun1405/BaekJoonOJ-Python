def main():
    N = int(input())
    nums = [1, 2] + [n for n in range(3, N)] + [997]
    print(N)
    print(*nums)


if __name__ == "__main__":
    main()
