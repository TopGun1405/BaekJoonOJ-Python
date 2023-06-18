def main():
    N = int(input())
    member = []

    for _ in range(N):
        age, name = input().split()
        member.append([int(age), name])

    # 파이썬 정렬은 기본 stable sort
    member.sort(key=lambda k: k[0], reverse=False)

    for i in range(N):
        print(member[i][0], member[i][1])


if __name__ == "__main__":
    main()
