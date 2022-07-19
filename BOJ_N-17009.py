def main():
    a3, a2, a1 = int(input()), int(input()), int(input())
    b3, b2, b1 = int(input()), int(input()), int(input())
    a_tot = a3 * 3 + a2 * 2 + a1
    b_tot = b3 * 3 + b2 * 2 + b1
    print("A" if a_tot > b_tot else ("B" if a_tot < b_tot else "T"))


if __name__ == "__main__":
    main()
