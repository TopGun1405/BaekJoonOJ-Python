def main():
    N = int(input())
    S = list(map(int, input().split()))

    maxFruits = 0
    left, right = 0, 0
    fruits = [0] * 10
    while right < N:
        fruits[S[right]] += 1
        while len([n for n in fruits if n > 0]) > 2:
            fruits[S[left]] -= 1
            left += 1
        maxFruits = max(maxFruits, right - left + 1)
        right += 1

    print(maxFruits)


if __name__ == "__main__":
    main()
