def main():
    t = int(input())
    for _ in range(t):
        input()
        r, c = map(int, input().split())
        box = [list(input()) for _ in range(r)]

        candy = 0
        for i in range(r):
            for j in range(c):
                if box[i][j] != "o":
                    continue

                if 0 < i < r-1 and box[i-1][j] == "v" and box[i+1][j] == "^":
                    candy += 1
                if 0 < j < c-1 and box[i][j-1] == ">" and box[i][j+1] == "<":
                    candy += 1

        print(candy)


if __name__ == "__main__":
    main()
