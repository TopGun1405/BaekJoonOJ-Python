def main():
    N, K = map(int, input().split())
    # human = [i for i in range(1, N + 1)]
    human = list(range(1, N + 1))

    i, p = 0, []
    # while True:
    #     temp.append(human[i % len(human)])
    #     d = human.index(human[i % len(human)])
    #     del human[i % len(human)]
    #     if len(human) == 0:
    #         break
    #     i = d + K - 1
    # print("<{}".format(temp[0]), end="")
    # for n in range(1, N):
    #     print(", {}".format(temp[n]), end="")
    # print(">")
    while human:
        i = (i + K - 1) % len(human)
        p.append(str(human.pop(i)))
    print("<" + ", ".join(p) + ">")


if __name__ == "__main__":
    main()
