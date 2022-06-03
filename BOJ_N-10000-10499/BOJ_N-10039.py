def main():
    # w, se, sa, su, ga = int(input()), int(input()), int(input()), int(input()), int(input())
    # if w < 40:
    #     w = 40
    # if se < 40:
    #     se = 40
    # if sa < 40:
    #     sa = 40
    # if su < 40:
    #     su = 40
    # if ga < 40:
    #     ga = 40
    # print((w + se + sa + su + ga) // 5)

    s = 0
    for _ in range(5):
        score = int(input())

        if score < 40:
            score = 40

        s = s + score
    print(s // 5)


if __name__ == "__main__":
    main()
