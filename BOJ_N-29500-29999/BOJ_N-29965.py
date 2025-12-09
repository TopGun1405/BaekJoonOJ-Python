def main():
    N = int(input())
    score = {'M': [0, 0], 'J': [0, 0]}
    for _ in range(N):
        S, P = map(lambda e: int(e) if e.isdigit() else e, input().split())

        score[S][0] += P
        score[S][1] += 1

    avg = {
        'M': (score['M'][0] / score['M'][1]) if score['M'][1] else 0,
        'J': (score['J'][0] / score['J'][1]) if score['J'][1] else 0
    }

    print("M" if avg['M'] > avg['J'] else ("J" if avg['M'] < avg['J'] else "V"))


if __name__ == "__main__":
    main()
