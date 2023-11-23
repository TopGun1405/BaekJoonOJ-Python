def main():
    k = int(input())
    myAns = input()
    friends = input()

    comp = {'same': 0, 'diff': 0}
    for ans1, ans2 in zip(myAns, friends):
        if ans1 == ans2:
            comp['same'] += 1
        else:
            comp['diff'] += 1

    maxCorrect = k if comp['same'] >= k else comp['same']
    k -= comp['same']
    maxCorrect += comp['diff'] - (k if k > 0 else 0)

    print(maxCorrect)


if __name__ == "__main__":
    main()
