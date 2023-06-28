def main():
    N = int(input())
    mentor_mentee = [input().split() for _ in range(N)]
    mentor_mentee.sort()

    names = {}
    for mentor, mentee in mentor_mentee:
        if mentor in names:
            names[mentor].append(mentee)
        else:
            names[mentor] = [mentee]

    for mentor in names:
        names[mentor].sort(reverse=True)

    for mentor, mentees in names.items():
        for mentee in mentees:
            print(mentor, mentee)


if __name__ == "__main__":
    main()
