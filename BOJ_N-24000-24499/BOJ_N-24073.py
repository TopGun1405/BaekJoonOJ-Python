def main():
    N = int(input())
    S = input()

    IOI, i = "IOI", 0
    for c in S:
        if i > 2:
            print("Yes")
            break
        if c == IOI[i]:
            i += 1
    else:
        print("Yes" if i > 2 else "No")


if __name__ == "__main__":
    main()
