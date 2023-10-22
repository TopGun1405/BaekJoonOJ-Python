def main():
    # def create_Pi_table(pattern: str) -> list:
    #     Pi = [0 for _ in range(len(pattern))]
    #     i = 0
    #     for j in range(1, len(pattern)):
    #         while i > 0 and pattern[i] != pattern[j]:
    #             i = Pi[i - 1]
    #         if pattern[i] == pattern[j]:
    #             i += 1
    #             Pi[j] = i
    #
    #     return Pi
    #
    # def kmp(text: str, pattern: str) -> list:
    #     Pi = create_Pi_table(pattern)
    #     result, i = [], 0
    #     for j in range(len(text)):
    #         while i > 0 and pattern[i] != text[j]:
    #             i = Pi[i - 1]
    #         if pattern[i] == text[j]:
    #             i += 1
    #             if i == len(pattern):
    #                 result.append(j - i + 2)
    #                 i = Pi[i - 1]
    #
    #     return result

    def kmp(text: str, pattern: str) -> list:
        Pi = [0 for _ in range(len(pattern))]
        i = 0
        for j in range(1, len(pattern)):
            while i > 0 and pattern[i] != pattern[j]:
                i = Pi[i-1]
            if pattern[i] == pattern[j]:
                i += 1
                Pi[j] = i

        result, i = [], 0
        for j in range(len(text)):
            while i > 0 and pattern[i] != text[j]:
                i = Pi[i-1]
            if pattern[i] == text[j]:
                i += 1
                if i == len(pattern):
                    result.append(j-i+2)
                    i = Pi[i-1]

        return result

    T = input()
    P = input()
    res = kmp(T, P)
    print(len(res))
    print(*res)


if __name__ == "__main__":
    main()
