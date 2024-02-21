def main():
    N = int(input())
    for _ in range(N):
        s1, s2 = map(sorted, input().split())
        print("Possible" if s1 == s2 else "Impossible")


if __name__ == "__main__":
    main()
