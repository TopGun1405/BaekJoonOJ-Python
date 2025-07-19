def main():
    T = int(input())
    for _ in range(T):
        N, M, L = map(int, input().split())
        S = list(map(int, input().split()))

        P = sorted(filter(lambda e: e != -1, S))

        X = M - P[0] if P and M - P[0] > L else L
        txt = "minutes" if X != 1 else "minute"

        print(f"The scoreboard has been frozen with {X} {txt} remaining.")


if __name__ == "__main__":
    main()
