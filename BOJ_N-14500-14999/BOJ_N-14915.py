def main():
    m, n = map(int, input().split())

    num = ""
    while m > 0:
        m, mod = divmod(m, n)
        num += str(mod) if mod < 10 else chr(mod + 55)

    print(num[::-1] if num else 0)


if __name__ == "__main__":
    main()
