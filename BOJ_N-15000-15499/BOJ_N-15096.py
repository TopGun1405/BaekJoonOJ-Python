def main():
    n = int(input())
    bats = list(map(int, input().split()))
    res = list(filter(lambda x: x != -1, bats))
    print(sum(res) / len(res))


if __name__ == "__main__":
    main()
