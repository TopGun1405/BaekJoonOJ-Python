def main():
    T = int(input())
    for _ in range(T):
        a, b, c = map(int, input().split())
        # brute force
        # ans = []
        # for x in range(1, a + 1):
        #     for y in range(1, b + 1):
        #         for z in range(1, c + 1):
        #             if x % y == y % z == z % x:
        #                 ans.append((x, y, z))
        # print(len(ans))
        print(min(a, b, c))


if __name__ == "__main__":
    main()
