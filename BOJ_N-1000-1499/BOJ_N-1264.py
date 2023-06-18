def main():
    while True:
        line = input()
        c = 0
        if line == '#':
            break
        for w in 'aeiou':
            c = c + line.count(w) + line.count(w.upper())
        print(c)


if __name__ == "__main__":
    main()
