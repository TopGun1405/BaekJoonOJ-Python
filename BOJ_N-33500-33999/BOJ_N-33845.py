def main():
    S = list(input())
    T = list(input())

    T_ = []
    for i in range(len(T)):
        if T[i] in S:
            continue
        T_.append(T[i])

    print("".join(T_))


if __name__ == "__main__":
    main()
