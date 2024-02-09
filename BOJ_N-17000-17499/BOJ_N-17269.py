def main():
    alp = {
        'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1,
        'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 2,
        'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1,
        'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1
    }
    N, M = map(int, input().split())
    A, B = input().split()

    comp = []
    for a, b in zip(A, B):
        comp.append(alp[a])
        comp.append(alp[b])

    if len(A) < len(B):
        comp += list(map(lambda c: alp[c], B[N:]))
    else:
        comp += list(map(lambda c: alp[c], A[M:]))

    while len(comp) > 2:
        comp = [(n1 + n2) % 10 for n1, n2 in zip(comp[:-1], comp[1:])]

    print("{}%".format(int("".join(map(str, comp)))))


if __name__ == "__main__":
    main()
