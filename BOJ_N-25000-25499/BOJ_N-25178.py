def main():
    N = int(input())
    W1 = input()
    W2 = input()

    w1, w2 = {}, {}
    s1, s2 = [], []
    for c1, c2 in zip(W1, W2):
        if c1 not in ['a', 'e', 'i', 'o', 'u']:
            s1.append(c1)
        if w1.get(c1, 0):
            w1[c1] += 1
        else:
            w1.update({c1: 1})

        if c2 not in ['a', 'e', 'i', 'o', 'u']:
            s2.append(c2)
        if w2.get(c2, 0):
            w2[c2] += 1
        else:
            w2.update({c2: 1})

    s1 = ''.join(s1)
    s2 = ''.join(s2)
    # print("YES" if w1 == w2 and W1[0] == W2[0] and W1[-1] == W2[-1] and s1 == s2 else "NO")
    if w1 == w2 and W1[0] == W2[0] and W1[-1] == W2[-1] and s1 == s2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
