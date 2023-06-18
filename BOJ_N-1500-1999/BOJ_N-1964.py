def main():
    N = int(input())
    dot, n = 5, 7
    for i in range(1, N):
        dot, n = dot + n, n + 3
    print(dot % 45678)


if __name__ == "__main__":
    main()
