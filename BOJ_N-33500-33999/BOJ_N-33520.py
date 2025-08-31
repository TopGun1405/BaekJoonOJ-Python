def main():
    N = int(input())
    a, b = 0, 0
    for _ in range(N):
        a_i, b_i = map(int, input().split())

        a_i, b_i = min(a_i, b_i), max(a_i, b_i)
        a, b = max(a, a_i), max(b, b_i)

    print(a * b)


if __name__ == "__main__":
    main()
