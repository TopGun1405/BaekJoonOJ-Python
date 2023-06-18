def main():
    N = int(input())
    isPrime = [False, False] + [True] * (N - 1)
    for i in range(2, int(N ** 0.5) + 1):
        if isPrime[i]:
            for j in range(2 * i, N + 1, i):
                isPrime[j] = False

    primeNums = [0]
    for num, val in enumerate(isPrime):
        if val:
            primeNums.append(primeNums[-1] + num)

    low, high = 0, 1
    case = 0
    while high < len(primeNums):
        primeSum = primeNums[high] - primeNums[low]
        if primeSum < N:
            high += 1
        elif primeSum > N:
            low += 1
        else:
            low, case = low + 1, case + 1
    print(case)


if __name__ == "__main__":
    main()
