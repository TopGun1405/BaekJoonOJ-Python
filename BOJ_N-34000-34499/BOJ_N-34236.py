def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(A[-1] + (A[-1] - A[-2]))


if __name__ == "__main__":
    main()
