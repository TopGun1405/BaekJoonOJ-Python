def main():
    N, M = map(int, input().split())

    names, groups = {}, {}
    for _ in range(N):
        groupName = input()
        nums = int(input())
        groups[groupName] = []
        for _ in range(nums):
            name = input()
            names[name] = groupName
            groups[groupName].append(name)

    for group in groups:
        groups[group].sort()

    for _ in range(M):
        name = input()
        qType = int(input())
        if qType == 0:
            print(*groups[name], sep="\n")
        else:
            print(names[name])


if __name__ == "__main__":
    main()
