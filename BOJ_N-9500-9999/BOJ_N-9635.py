def main():
    T = int(input())
    for _ in range(T):
        N, X, Y = map(int, input().split())
        colors = list(map(int, input().split()))
        print("BOTH" if X == colors[0] and Y == colors[-1]
              else ("EASY" if X == colors[0]
                    else ("HARD" if Y == colors[-1]
                          else "OKAY")))


if __name__ == "__main__":
    main()
