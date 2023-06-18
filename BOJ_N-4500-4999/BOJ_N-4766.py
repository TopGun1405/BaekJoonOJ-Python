def main():
    d = float(input())
    while True:
        temp = d
        d = float(input())
        if d == 999:
            break
        print("{:0.2f}".format(d - temp))


if __name__ == "__main__":
    main()
