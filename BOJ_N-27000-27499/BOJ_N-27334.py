def main():
    N = int(input())
    A = list(map(int, input().split()))
    ranking = {}
    for idx, val in enumerate(sorted(A)):
        try:
            ranking[val] = min(ranking[val], idx + 1)
        except KeyError:
            ranking[val] = idx + 1
    print(ranking)
    for Ai in A:
        print(ranking[Ai])


if __name__ == "__main__":
    main()
