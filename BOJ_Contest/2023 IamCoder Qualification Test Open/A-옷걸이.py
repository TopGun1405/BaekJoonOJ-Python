def main():

    def dfs(clothes, i):
        if len(clothes) == N:
            print("YES")
            print(''.join(clothes))
            exit(0)
        for a in A[i:]:
            if a == 1 and cnt['U'] > 0:
                clothes.append('U')
                cnt['U'] -= 1
                dfs(clothes, i + 1)
            elif a == 2 and cnt['D'] > 0:
                clothes.append('D')
                cnt['D'] -= 1
                dfs(clothes, i + 1)
            elif a == 3:
                if cnt['U'] > 0:
                    clothes.append('U')
                    cnt['U'] -= 1
                    dfs(clothes, i + 1)
                    cnt['U'] += 1
                    clothes.pop()
                elif cnt['D'] > 0:
                    clothes.append('D')
                    cnt['D'] -= 1
                    dfs(clothes, i + 1)
                    cnt['D'] += 1
                    clothes.pop()
        else:
            print("NO")
            exit(0)

    N = int(input())
    # 1: U, 2: D, 3: UD
    A = list(map(int, input().split()))
    U, D = map(int, input().split())
    cnt = {'U': U, 'D': D}
    dfs('', 0)


if __name__ == "__main__":
    main()
