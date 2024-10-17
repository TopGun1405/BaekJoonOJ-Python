def main():
    N = int(input())
    S = set(list(input()))

    low = {"r", "o", "y", "g", "b", "i", "v"}
    up = {"R", "O", "Y", "G", "B", "I", "V"}

    if low & S == low and up & S == up:
        print("YeS")
    elif low & S == low:
        print("yes")
    elif up & S == up:
        print("YES")
    else:
        print("NO!")


if __name__ == "__main__":
    main()
