def main():
    W = input()
    S = input()

    w = ""
    for c in W:
        if c in w:
            continue
        w += c
    W = list(w)

    C = sorted(set(chr(n) for n in range(65, 91)) - set(W))
    enc = {chr(n): c for n, c in zip(range(65, 91), W+C)}

    E = []
    for c in S:
        E.append(enc[c])

    print("".join(E))


if __name__ == "__main__":
    main()
