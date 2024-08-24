def main():
    N = int(input())
    couples = {}
    for _ in range(N):
        p_i, s_i = input().split()
        if s_i == "-":
            continue
        try:
            couples[s_i].append(p_i)
        except KeyError:
            couples[s_i] = [p_i]

    couples = list(filter(lambda e: len(e) == 2, couples.values()))
    print(len(couples))
    for couple in couples:
        print(*couple)


if __name__ == "__main__":
    main()
