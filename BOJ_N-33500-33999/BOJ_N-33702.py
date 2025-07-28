def main():

    def dfs(k):
        if len(pw) == 9:
            cnt['PW'] += 1
            return

        for n in numPad[k]:
            if not visited[n]:
                visited[n] = True
                pw.append(n)
                dfs(n)
                pw.pop()
                visited[n] = False

    numPad = {
        1: [2, 4],
        2: [1, 3, 5],
        3: [2, 6],
        4: [1, 5, 7],
        5: [2, 4, 6, 8],
        6: [3, 5, 9],
        7: [4, 8],
        8: [5, 7, 9],
        9: [6, 8]
    }
    visited = [False for _ in range(10)]

    K = int(input())

    visited[K] = True
    pw, cnt = [K], {'PW': 0}

    dfs(K)

    print(cnt['PW'])


if __name__ == "__main__":
    main()
