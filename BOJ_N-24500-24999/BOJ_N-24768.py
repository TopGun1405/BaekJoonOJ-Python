def main():
    while True:
        x, y = map(int, input().split())
        if x == y == 0:
            break
        print("Never speak again." if x + y == 13
              else ("Left beehind." if x < y
                    else ("Undecided." if x == y
                          else "To the convention.")))


if __name__ == "__main__":
    main()
