def main():
    N, M = map(int, input().split())
    J = int(input())
    dis = 0
    left, right = 0, M - 1
    for _ in range(J):
        apple = int(input()) - 1
        if apple > right:
            dis += apple - right
            left, right = apple - M + 1, apple
        elif apple < left:
            dis += left - apple
            left, right = apple, apple + M - 1
    print(dis)


if __name__ == "__main__":
    main()
