def main():
    l, r = map(int, input().split())
    print("Not a moose" if l == 0 and r == 0
          else ("Even {}".format(l + r) if l == r
                else "Odd {}".format(max(l, r) * 2)))


if __name__ == "__main__":
    main()
