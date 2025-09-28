def main():
    D = int(input())
    E = int(input())
    for _ in range(E):
        op = input()
        Q = int(input())

        if op == "+":
            D += Q
        elif op == "-":
            D -= Q

    print(D)


if __name__ == "__main__":
    main()
