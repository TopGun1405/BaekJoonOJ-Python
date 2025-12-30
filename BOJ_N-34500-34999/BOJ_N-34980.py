def main():
    N = int(input())
    m = list(input())
    d = list(input())

    b_m, b_d = m.count("w"), d.count("w")
    if m == d:
        print("Good")
    elif b_m == b_d:
        print("Its fine")
    elif b_m > b_d:
        print("Oryang")
    elif b_m < b_d:
        print("Manners maketh man")


if __name__ == "__main__":
    main()
