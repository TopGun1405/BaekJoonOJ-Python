def main():

    def bigAndSmall():
        if len(num) == len(X):
            if int("".join(num)) > int(X):
                res.append(int("".join(num)))
            return

        for i, x in enumerate(X):
            if not visited[i]:
                visited[i] = True
                num.append(x)
                bigAndSmall()
                num.pop()
                visited[i] = False

    X = input()

    num, res = [], []
    visited = [False] * len(X)
    bigAndSmall()

    print(sorted(res)[0] if res else 0)


if __name__ == "__main__":
    main()
