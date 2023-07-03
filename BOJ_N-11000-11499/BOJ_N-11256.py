def main():
    T = int(input())
    for _ in range(T):
        J, N = map(int, input().split())

        box = []
        for _ in range(N):
            R, C = map(int, input().split())
            box.append(R * C)
        box.sort(reverse=True)

        boxNum = 0
        for i in range(N):
            J, boxNum = J - box[i], boxNum + 1
            if J <= 0:
                break
        print(boxNum)


if __name__ == "__main__":
    main()
