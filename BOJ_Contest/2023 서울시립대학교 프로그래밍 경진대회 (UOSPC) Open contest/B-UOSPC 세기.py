def main():
    n = int(input())
    S = input()
    UOSPC = {'u': 0, 'o': 0, 's': 0, 'p': 0, 'c': 0}
    for s in S:
        try:
            UOSPC[s] += 1
        except KeyError:
            continue
    print(min(UOSPC.values()))


if __name__ == "__main__":
    main()
