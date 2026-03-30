def main():
    T = int(input())
    for _ in range(T):
        nums = list(map(int, input().split()))

        date = [(1, 31), (2, 29), (3, 31), (4, 30), (5, 31), (6, 30),
                (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
        cnt = 0
        for MM, DD in date:
            for m in map(int, list(str(MM))):
                if nums[m]:
                    break
            else:
                for dd in range(1, DD+1):
                    for d in map(int, list(str(dd))):
                        if nums[d]:
                            break
                    else:
                        cnt += 1

        print(cnt)


if __name__ == "__main__":
    main()
