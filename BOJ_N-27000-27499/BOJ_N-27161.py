def main():
    N = int(input())

    time, T = 1, 1
    for _ in range(N):
        S, X = map(lambda e: int(e) if e.isdigit() else e, input().split())

        act = "NO"
        if (S == "HOURGLASS") & (time == X):
            act = "NO"
        elif S == "HOURGLASS":
            T *= -1
        else:
            if time == X:
                act = "YES"

        print(time, act)
        time = (time + T) % 12
        time += 12 if time == 0 else 0


if __name__ == "__main__":
    main()
