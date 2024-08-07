def main():
    n, m = map(int, input().split())
    pref = [
        {'kor': set(), 'eng': set(), 'math': set(), '-': set(range(n))},
        {'apple': set(), 'pear': set(), 'orange': set(), '-': set(range(n))},
        {'red': set(), 'blue': set(), 'green': set(), '-': set(range(n))}
    ]
    for i in range(n):
        subject, fruit, color = input().split()
        pref[0][subject].add(i)
        pref[1][fruit].add(i)
        pref[2][color].add(i)

    for _ in range(m):
        Q_s, Q_f, Q_c = input().split()
        print(len(pref[0][Q_s] & pref[1][Q_f] & pref[2][Q_c]))


if __name__ == "__main__":
    main()
