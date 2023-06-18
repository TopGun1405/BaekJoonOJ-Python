def main():
    N = int(input())
    n = [int(input()) for _ in range(N)]
    print('NS'[max(n) == n[0]])


if __name__ == "__main__":
    main()
