def main():
    while True:
        n = float(input())
        if n == 0:
            break
        print("{:0.2f}".format(1 + n + n**2 + n**3 + n**4))


if __name__ == "__main__":
    main()
