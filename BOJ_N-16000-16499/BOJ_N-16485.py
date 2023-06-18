def main():
    a, b = map(int, input().split())
    print(a // b if a % b == 0 else "{:0.10f}".format(a / b))


if __name__ == "__main__":
    main()
