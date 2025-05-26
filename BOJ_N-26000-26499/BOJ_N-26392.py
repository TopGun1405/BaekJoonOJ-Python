def main():

    def check(i):
        for j in range(s):
            if mat[i][j] == "#":
                return True
        return False

    n, r, s = map(int, input().split())
    for _ in range(n):
        mat = [list(input()) for _ in range(r)]

        a = 0
        while a < r and not check(a):
            a += 1

        b = r-1
        while b >= 0 and not check(b):
            b -= 1

        print(b - a)


if __name__ == "__main__":
    main()
