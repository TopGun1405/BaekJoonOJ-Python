def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(*sorted(set(A)), sep="\n")


if __name__ == "__main__":
    main()
