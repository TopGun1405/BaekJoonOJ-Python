def main():
    N = int(input())
    names = dict()
    for _ in range(N):
        n = input()
        if n[0] in names:
            names[n[0]] += 1
        else:
            names.update({n[0]: 1})
    afn = ''
    for n in sorted(names.keys()):
        if names[n] >= 5:
            afn += n
    print(afn if afn else "PREDAJA")


if __name__ == "__main__":
    main()
