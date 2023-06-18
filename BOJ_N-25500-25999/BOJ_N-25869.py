def main():
    w, h, d = map(int, input().split())
    print([0, (w - 2*d) * (h - 2*d)][w > 2*d and h > 2*d])


if __name__ == "__main__":
    main()
