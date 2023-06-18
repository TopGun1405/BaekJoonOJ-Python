def main():
    K = int(input())
    for i in range(K):
        score = list(map(int, input().split()))
        del score[0]
        score.sort(reverse=True)
        gap = [score[i] - score[i + 1] for i in range(len(score) - 1)]
        print("Class {}".format(i + 1))
        print("Max {}, Min {}, Largest gap {}".format(score[0], score[-1], max(gap)))


if __name__ == "__main__":
    main()
