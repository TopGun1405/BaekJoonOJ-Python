def main():
    t = int(input())
    for _ in range(t):
        c, v = map(int, input().split())
        print("You get {} piece(s) and your dad gets {} piece(s).".format(c // v, c % v))


if __name__ == "__main__":
    main()
