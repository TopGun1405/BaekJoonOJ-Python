def main():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        r = "Round 1" if N > 4500 else \
            ("Round 2" if 1000 < N <= 4500 else
             ("Round 3" if 25 < N <= 1000 else
              "World Finals"))
        print('Case #{}: {}'.format(t, r))


if __name__ == "__main__":
    main()
