def main():
    n = int(input())
    scores = []
    for _ in range(n):
        bi, pi, qi, ri = map(int, input().split())
        scores.append([bi, pi * qi * ri, pi + qi + ri])
    scores.sort(key=lambda k: (k[1], k[2], k[0]))
    print(scores[0][0], scores[1][0], scores[2][0])


if __name__ == "__main__":
    main()
