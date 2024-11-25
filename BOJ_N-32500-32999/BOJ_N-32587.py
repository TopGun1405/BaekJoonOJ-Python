def main():
    n = int(input())
    a, b = input(), input()

    A, B = 0, 0
    for a_i, b_i in zip(a, b):
        if a_i == "R" and b_i == "S":
            A += 1
        elif a_i == "S" and b_i == "P":
            A += 1
        elif a_i == "P" and b_i == "R":
            A += 1
        elif b_i == "R" and a_i == "S":
            B += 1
        elif b_i == "S" and a_i == "P":
            B += 1
        elif b_i == "P" and a_i == "R":
            B += 1

    print("victory" if A > B else "defeat")


if __name__ == "__main__":
    main()
