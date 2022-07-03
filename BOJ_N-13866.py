def main():
    skill = list(map(int, input().split()))
    diff = set()
    tot = sum(skill)
    for i in range(len(skill)):
        for j in range(i + 1, len(skill)):
            diff.add(abs(tot - (skill[i] + skill[j]) * 2))
    print(min(diff))


if __name__ == "__main__":
    main()
