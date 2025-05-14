def main():
    N = int(input())
    S = input()
    T = input()

    A, B = 0, 0
    for s, t in zip(S, T):
        if (s == "R" and t == "S") or (s == "S" and t == "P") or (s == "P" and t == "R"):
            A += 1
        elif (t == "R" and s == "S") or (t == "S" and s == "P") or (t == "P" and s == "R"):
            B += 1

    print(A, B)


if __name__ == "__main__":
    main()
