def main():
    w, h = map(int, input().split())
    cut = int(input())
    ver, hor = [0, w], [0, h]
    for i in range(cut):
        d, p = map(int, input().split())
        if d == 0:
            hor.append(p)
        elif d == 1:
            ver.append(p)
    ver.sort()
    hor.sort()
    ar = []
    for i in range(len(ver) - 1):
        for j in range(len(hor) - 1):
            ar.append((ver[i + 1] - ver[i]) * (hor[j + 1] - hor[j]))
    print(max(ar))


if __name__ == "__main__":
    main()
