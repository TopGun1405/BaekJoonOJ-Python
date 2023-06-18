def main():
    while True:
        l, w, a = map(int, input().split())
        if l == w == a == 0:
            break
        l = a // w if l == 0 else l
        w = a // l if w == 0 else w
        a = l * w if a == 0 else a
        print(l, w, a)


if __name__ == "__main__":
    main()
