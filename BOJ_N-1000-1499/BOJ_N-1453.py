def main():
    N = int(input())
    computers = [0] * 101
    customers = list(map(int, input().split()))
    rejected = 0
    for c in customers:
        if computers[c]:
            rejected += 1
        else:
            computers[c] = 1
    print(rejected)


if __name__ == "__main__":
    main()
