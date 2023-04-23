def main():
    N = int(input())
    words = []
    for _ in range(N):
        w = input()
        words.append([w, len(w)])

    words.sort(key=lambda k: (k[1], k[0]))
    print(words[0][0])
    for i in range(1, N):
        if words[i][0] == words[i - 1][0]:
            continue
        print(words[i][0])

    ###################################################
    # readline()은 개행 문자도 입력 받음 -> rstrip() 활용 #
    ###################################################

    # N = int(sys.stdin.readline())
    # words = [sys.stdin.readline().rstrip() for _ in range(N)]
    # words = list(set(words))
    #
    # for i in range(len(words)):
    #     words[i] = [words[i], len(words[i])]
    #
    # words.sort(key=lambda k: (k[1], k[0]))
    # for i in range(len(words)):
    #     print(words[i][0])


if __name__ == "__main__":
    main()
