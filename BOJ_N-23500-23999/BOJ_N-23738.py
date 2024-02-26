def main():
    S = input()

    p = {'B': "v", 'E': "ye", 'H': "n", 'P': "r", 'C': "s", 'Y': "u", 'X': "h"}
    for k in p:
        S = S.replace(k, p[k])

    print(S.lower())


if __name__ == "__main__":
    main()
