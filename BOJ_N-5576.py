def main():
    W = sorted(int(input()) for _ in range(10))
    K = sorted(int(input()) for _ in range(10))
    print(sum(W[-3:]), sum(K[-3:]))


if __name__ == "__main__":
    main()
