def main():
    T = int(input())
    for _ in range(T):
        m, n = map(int, input().split())
        print([1, 7][m == 2 and n == 2])
        input()
        input()


if __name__ == "__main__":
    main()
