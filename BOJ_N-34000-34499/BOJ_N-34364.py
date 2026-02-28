def main():
    N, S = map(lambda e: int(e) if e.isdigit() else list(e), input().split())

    shift = 1
    for i in range(N):
        n = ord(S[i]) - ord("A")
        S[i] = chr((n + shift) % 26 + ord("A"))
        shift *= 2

    print("".join(S))


if __name__ == "__main__":
    main()
