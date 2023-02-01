def main():
    T = int(input())
    for _ in range(T):
        c1, c2 = input().split()
        dis = ''
        for i in range(len(c1)):
            x, y = ord(c1[i]) - 64, ord(c2[i]) - 64
            d = y - x if y >= x else y + 26 - x
            dis += ' {}'.format(d)
        print("Distances:" + dis)


if __name__ == "__main__":
    main()
