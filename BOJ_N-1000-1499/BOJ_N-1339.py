def main():
    N = int(input())
    words = [input() for _ in range(N)]
    alp = {chr(n): 0 for n in range(65, 91)}

    for word in words:
        for i, c in enumerate(word):
            alp[c] += 10 ** (len(word) - i - 1)

    tot = 0
    nums = sorted(filter(lambda n: n > 0, alp.values()), reverse=True)
    for i, num in enumerate(nums):
        tot += num * (9 - i)

    print(tot)


if __name__ == "__main__":
    main()
