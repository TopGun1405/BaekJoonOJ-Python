def main():
    N, R, C = map(int, input().split())

    for i in range(N):
        if i % 2 == (0 if (R + C) % 2 == 0 else 1):
            print("v." * (N // 2) + 'v' * (N % 2))
        else:
            print(".v" * (N // 2) + '.' * (N % 2))


if __name__ == "__main__":
    main()
