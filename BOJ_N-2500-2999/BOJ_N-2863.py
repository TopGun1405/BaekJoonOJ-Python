def main():
    ab = list(map(int, input().split()))
    dc = list(map(int, input().split()))
    num = ab + dc
    f = []
    for i in range(4):
        f.append(num[0] / num[2] + num[1] / num[3])
        t = num.pop()
        num.append(num.pop(0))
        num.append(t)
        num.append(num.pop(0))
    print(f.index(max(f)) if f.count(max(f)) == 1 else min(f))


if __name__ == "__main__":
    main()
