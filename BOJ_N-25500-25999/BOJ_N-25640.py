def main():
    mbti = input()
    N = int(input())
    same = 0
    for _ in range(N):
        F_mbti = input()
        if mbti == F_mbti:
            same += 1
    print(same)


if __name__ == "__main__":
    main()
