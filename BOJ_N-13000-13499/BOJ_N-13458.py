def main():
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    ans = N
    for t in A:
        t -= B
        if t > 0:
            ans = ans + (t // C) + (1 if t % C else 0)
    print(ans)


if __name__ == "__main__":
    main()
