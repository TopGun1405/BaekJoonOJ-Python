def main():
    N, P, S = map(int, input().split())
    cards = set(range(1, N + 1))
    for _ in range(S):
        m = set(list(map(int, input().split()))[1:])
        if P in m:
            print("KEEP")
            cards = m
        else:
            print("REMOVE")
            cards -= m


if __name__ == "__main__":
    main()
