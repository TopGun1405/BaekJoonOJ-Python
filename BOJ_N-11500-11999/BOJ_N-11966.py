def main():
    N = int(input())
    while N % 2 == 0:
        N //= 2
    print(1 if N == 1 else 0)


if __name__ == "__main__":
    main()
