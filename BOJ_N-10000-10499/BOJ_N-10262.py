def main():
    a1, b1, a2, b2 = map(int, input().split())
    a3, b3, a4, b4 = map(int, input().split())

    G1, G2 = a1+a2, b1+b2
    E1, E2 = a3+a4, b3+b4

    if G1-E1 + G2-E2 > 0:
        print("Gunnar")
    elif G1-E1 + G2-E2 < 0:
        print("Emma")
    else:
        print("Tie")


if __name__ == "__main__":
    main()
