def main():
    N = int(input())
    bread = []
    for _ in range(N):
        A, B = map(int, input().split())
        if A <= B:
            bread.append(B)
    print(min(bread) if len(bread) > 0 else -1)


if __name__ == "__main__":
    main()
