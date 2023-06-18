def main():
    N = int(input())
    left = 0
    for _ in range(N):
        student, apple = map(int, input().split())
        left += apple % student
    print(left)


if __name__ == "__main__":
    main()
