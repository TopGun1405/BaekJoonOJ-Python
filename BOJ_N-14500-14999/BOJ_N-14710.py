def main():
    t1, t2 = map(int, input().split())
    if t1 % 30 * 12 != t2:
        print("X")
    else:
        print("O")


if __name__ == "__main__":
    main()
