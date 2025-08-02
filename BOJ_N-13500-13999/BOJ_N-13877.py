def main():
    T = int(input())
    for _ in range(T):
        K, S = input().split()
        O = int(S, 8) if max(list(S)) < "8" else 0

        print(int(K), O, int(S), int(S, 16))


if __name__ == "__main__":
    main()
