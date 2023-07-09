def main():
    team1, team2 = [], []
    for _ in range(3):
        P, Y, S = input().split()
        team1.append(int(Y))
        team2.append([int(P), S])

    team1.sort()
    team2.sort(reverse=True)

    print(''.join(map(lambda n: str(n % 100), team1)))
    print(''.join(map(lambda c: c[1][0], team2)))


if __name__ == "__main__":
    main()
