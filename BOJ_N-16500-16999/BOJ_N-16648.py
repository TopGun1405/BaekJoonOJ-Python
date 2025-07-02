def main():
    t, p = map(int, input().split())

    if p > 20:
        v = t / (100 - p)

        print((p - 20 + 40) * v)
    else:
        v = t / ((20 - p) * 2 + 80)

        print(p * 2 * v)


if __name__ == "__main__":
    main()
