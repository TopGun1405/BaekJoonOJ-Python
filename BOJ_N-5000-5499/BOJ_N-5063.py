def main():
    N = int(input())
    for _ in range(N):
        r, e, c = map(int, input().split())
        print("advertise" if r < e - c
              else ("does not matter" if r == e - c
                    else "do not advertise"))


if __name__ == "__main__":
    main()
