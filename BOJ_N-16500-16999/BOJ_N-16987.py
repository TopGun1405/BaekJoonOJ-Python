def main():
    # incomplete

    def cntEgg():
        cnt = 0
        for egg in eggs:
            if egg[0] <= 0:
                cnt += 1

        return cnt

    def hit(depth):
        if depth == N:
            res['BREAK'] = max(res['BREAK'], cntEgg())
            return

        if eggs[depth][0] <= 0:
            hit(depth+1)
        else:
            isBroken = True
            for i in range(N):
                if depth < i and eggs[i][0] > 0:
                    isBroken = False
                    eggs[depth][0] -= eggs[i][1]
                    eggs[i][0] -= eggs[depth][1]

                    hit(depth+1)

                    eggs[depth][0] += eggs[i][1]
                    eggs[i][0] += eggs[depth][1]
                    
            if isBroken:
                hit(N)

    N = int(input())
    eggs = []
    for _ in range(N):
        S_i, W_i = map(int, input().split())
        eggs.append([S_i, W_i])

    res = {'BREAK': 0}


if __name__ == "__main__":
    main()
