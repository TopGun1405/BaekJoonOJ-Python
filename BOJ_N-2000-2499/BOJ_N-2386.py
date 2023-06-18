def main():
    while True:
        n = input()
        if n == '#':
            break
        val, data = n[0], n[2::]
        res = data.count(val) + data.count(val.upper())
        print(val, res)


if __name__ == "__main__":
    main()
