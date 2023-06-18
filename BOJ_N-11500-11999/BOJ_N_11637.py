def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        cand = {i + 1: int(input()) for i in range(n)}
        sorting = sorted([[key, val] for key, val in cand.items()], key=lambda k: k[1], reverse=True)
        if sorting[0][1] == sorting[1][1]:
            print("no winner")
        elif sorting[0][1] > sum(cand.values()) // 2:
            print("majority winner {}".format(sorting[0][0]))
        else:
            print("minority winner {}".format(sorting[0][0]))


if __name__ == "__main__":
    main()
