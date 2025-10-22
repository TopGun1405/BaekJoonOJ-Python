def main():
    G, S, C = map(int, input().split())

    BP = 3*G + 2*S + C
    if BP >= 8:
        V = "Province"
    elif BP >= 5:
        V = "Duchy"
    elif BP >= 2:
        V = "Estate"
    else:
        V = ""

    if BP >= 6:
        T = "Gold"
    elif BP >= 3:
        T = "Silver"
    else:
        T = "Copper"

    if V:
        print(f"{V} or {T}")
    else:
        print(f"{T}")


if __name__ == "__main__":
    main()
