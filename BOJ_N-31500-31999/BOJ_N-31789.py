def main():
    N = int(input())
    X, S = map(int, input().split())
    weapons = [list(map(int, input().split())) for _ in range(N)]

    for c, p in weapons:
        if c <= X and p > S:
            print("YES")
            break
    else:
        print("NO")


if __name__ == "__main__":
    main()
