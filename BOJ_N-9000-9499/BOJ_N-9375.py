def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        cloth = {}
        for _ in range(n):
            c, t = input().split()
            if t in cloth:
                cloth[t].append(c)
            else:
                cloth.update({t: [c]})

        # + 1 -> 안 입는 경우
        # - 1 -> 모두 안 입는 경우
        count = 1
        for key in cloth.keys():
            count = count * (len(cloth[key]) + 1)
        print(count - 1)


if __name__ == "__main__":
    main()
