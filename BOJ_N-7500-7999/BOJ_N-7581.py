def main():
    while True:
        l, w, h, v = map(int, input().split())
        if l == w == h == v == 0:
            break
        l = l if l else v // w // h
        w = w if w else v // l // h
        h = h if h else v // l // w
        v = v if v else l * w * h
        print(l, w, h, v)


if __name__ == "__main__":
    main()
