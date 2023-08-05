def main():
    while True:
        P1, P2 = input(), input()
        if P1 == P2 == 'E':
            break
        S1, S2 = 0, 0
        for G1, G2 in zip(P1, P2):
            if G1 == 'R' and G2 == 'S':
                S1 += 1
            elif G1 == 'P' and G2 == 'R':
                S1 += 1
            elif G1 == 'S' and G2 == 'P':
                S1 += 1

            elif G2 == 'R' and G1 == 'S':
                S2 += 1
            elif G2 == 'P' and G1 == 'R':
                S2 += 1
            elif G2 == 'S' and G1 == 'P':
                S2 += 1
        print("P1:", S1)
        print("P2:", S2)


if __name__ == "__main__":
    main()
