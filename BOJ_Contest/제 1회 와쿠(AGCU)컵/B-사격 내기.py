def main():
    SA, SB = map(int, input().split())
    score = [2 ** i for i in range(10)]
    able = [set()]
    t = {1}
    t.add(2)
    print(1, t)
    for s in score:
        size = len(able)
        for e in range(size):
            print(able[e])
            print(able)
            t = able[e].union(s)
            able.append(t)
    print(score)
    print(able)


if __name__ == "__main__":
    main()
