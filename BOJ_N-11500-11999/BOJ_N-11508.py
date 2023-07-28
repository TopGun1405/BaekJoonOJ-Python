def main():
    N = int(input())
    C = sorted([int(input()) for _ in range(N)], reverse=True)
    print(sum(C) - sum(C[2::3]))


if __name__ == "__main__":
    main()
