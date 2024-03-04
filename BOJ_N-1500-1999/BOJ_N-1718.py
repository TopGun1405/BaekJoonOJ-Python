def main():
    P = input()
    K = input()

    C = ""
    for i in range(len(P)):
        if P[i] == " ":
            C += " "
        else:
            C += chr((ord(P[i]) - ord(K[i % len(K)]) - 1) % 26 + ord("a"))

    print(C)


if __name__ == "__main__":
    main()
