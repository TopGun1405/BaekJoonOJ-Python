def main():
    T = int(input())
    alp = {}
    for _ in range(T):
        c, n = input().split()
        alp[n] = c
    N = input()

    text = ""
    for i in range(0, len(N), 4):
        try:
            text += alp[N[i:i+4]]
        except KeyError:
            text += "?"

    print(text)


if __name__ == "__main__":
    main()
