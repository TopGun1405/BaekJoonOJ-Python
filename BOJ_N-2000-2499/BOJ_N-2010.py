def main():
    N = int(input())
    p = int(input())
    for _ in range(N - 1):
        temp = int(input())
        p = p - 1 + temp
    print(p)


if __name__ == "__main__":
    main()
