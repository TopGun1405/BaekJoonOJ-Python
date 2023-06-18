def main():
    p1, q1, p2, q2 = map(int, input().split())
    r = p1 / q1 * p2 / q2 / 2
    if int(r) == r:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
