def main():
    N = int(input())
    ans = input()

    sub = {'B': 0, 'S': 0, 'A': 0}
    for s in ans:
        sub[s] += 1
    interest = list(filter(lambda n: sub[n] == max(sub.values()), sub))

    print("SCU" if len(interest) == 3 else "".join(interest))


if __name__ == "__main__":
    main()
