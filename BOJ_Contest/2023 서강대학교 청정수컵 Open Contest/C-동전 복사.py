def main():
    N = int(input())
    x, y = map(int, input().split())
    if N == 1:
        print(0)
    elif (x == 1 or x == N) and (y == 1 or y == N):
        print(2)
    elif (x == 1 or x == N) or (y == 1 or y == N):
        print(3)
    else:
        print(4)


if __name__ == "__main__":
    main()
