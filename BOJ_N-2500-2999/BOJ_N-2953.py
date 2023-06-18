def main():
    score = [[i + 1, sum(map(int, input().split()))] for i in range(5)]
    score.sort(key=lambda k: k[1], reverse=True)
    print(score[0][0], score[0][1])


if __name__ == "__main__":
    main()
