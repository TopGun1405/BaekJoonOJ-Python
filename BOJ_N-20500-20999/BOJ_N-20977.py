def main():
    N = int(input())
    S = input()

    J = S.count("J")
    O = S.count("O")

    print("J"*J + "O"*O + "I"*(N-J-O))


if __name__ == "__main__":
    main()
