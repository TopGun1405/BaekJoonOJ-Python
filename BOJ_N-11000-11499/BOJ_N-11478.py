def main():
    S = list(input())
    o_s = ''.join(S)

    r = len(S)
    for i in range(r):
        for j in range(i + 1, r):
            S.append(o_s[i:j + 1])

    print(len(set(S)))


if __name__ == "__main__":
    main()
