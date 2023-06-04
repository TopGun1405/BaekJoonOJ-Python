def main():
    N = int(input())
    for i in range(5 * N):
        if i < N:
            print('@' * 5 * N)
        else:
            print('@' * N)


if __name__ == "__main__":
    main()
