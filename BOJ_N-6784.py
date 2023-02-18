def main():
    N = int(input())
    ans = [input() for _ in range(N)]
    C = 0
    for i in range(N):
        C = C + (1 if input() == ans[i] else 0)
    print(C)


if __name__ == "__main__":
    main()
