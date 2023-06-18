def main():
    T = int(input())
    alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for _ in range(T):
        S = input()
        tot = 0
        for a in alp:
            if a not in S:
                tot += ord(a)
        print(tot)


if __name__ == "__main__":
    main()
