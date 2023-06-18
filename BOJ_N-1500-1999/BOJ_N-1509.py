def main():
    S = input()
    lenS = len(S)

    dp = [2501 for _ in range(lenS)] + [0]
    isPalindrome = [[0 for _ in range(lenS)] for _ in range(lenS)]

    for i in range(lenS):
        isPalindrome[i][i] = 1

    for i in range(1, lenS):
        if S[i-1] == S[i]:
            isPalindrome[i-1][i] = 1

    for i in range(3, lenS+1):
        for start in range(lenS-i+1):
            end = start+i-1
            if S[start] == S[end] and isPalindrome[start+1][end-1]:
                isPalindrome[start][end] = 1

    for end in range(lenS):
        for start in range(end+1):
            if isPalindrome[start][end]:
                dp[end] = min(dp[end], dp[start-1] + 1)
            else:
                dp[end] = min(dp[end], dp[end-1] + 1)

    print(dp[lenS-1])


if __name__ == "__main__":
    main()
