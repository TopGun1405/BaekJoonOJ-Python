def main():
    T = int(input())
    for t in range(T):
        fName, lName = input(), input()
        print("Case {}: {}, {}".format(t + 1, lName, fName))


if __name__ == "__main__":
    main()
