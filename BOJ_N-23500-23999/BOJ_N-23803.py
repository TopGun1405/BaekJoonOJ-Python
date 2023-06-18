def main():
    N = int(input())
    for _ in range(N * 4):
        print('@' * N)
    for _ in range(N):
        print('@' * N * 5)


if __name__ == "__main__":
    main()
