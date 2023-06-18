def main():
    R, C = map(int, input().split())
    pLot = [list(input()) for _ in range(R)]
    able = {n: 0 for n in range(5)}
    for r in range(R):
        for c in range(C):
            if r == R - 1 or c == C - 1:
                break

            p1, p2 = pLot[r][c:c+2]
            p3, p4 = pLot[r+1][c:c+2]
            p = p1 + p2 + p3 + p4
            
            if '#' in p:
                continue
            able[p.count('X')] += 1
    print(*able.values(), sep='\n')


if __name__ == "__main__":
    main()
