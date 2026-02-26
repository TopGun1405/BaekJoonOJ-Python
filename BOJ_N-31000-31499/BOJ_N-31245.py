def main():
    cena1, cena2, cena3 = input().split()

    if cena1[-1] == cena2[0]:
        cena2 = "'" + cena2[1:]
    if cena2[-1] == cena3[0]:
        cena3 = "'" + cena3[1:]

    print(cena1 + cena2 + cena3)


if __name__ == "__main__":
    main()
