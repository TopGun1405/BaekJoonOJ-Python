def main():
    rev_W = {'L': "RIGHT", 'R': "LEFT"}
    way, loc = [], ["HOME"]
    while True:
        W, L = input(), input()
        way.append(W)
        if L == "SCHOOL":
            break
        loc.append(L)

    for w, l in zip(way[::-1], loc[::-1]):
        if l == "HOME":
            print(f"Turn {rev_W[w]} into your {l}.")
        else:
            print(f"Turn {rev_W[w]} onto {l} street.")


if __name__ == "__main__":
    main()
