from typing import Tuple


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        print(*isPalindrome(S))


def recursion(s: chr, l: int, r: int, rec: int) -> Tuple[int, int]:
    rec += 1
    if l >= r:
        return 1, rec
    elif s[l] != s[r]:
        return 0, rec
    else:
        return recursion(s, l + 1, r - 1, rec)


def isPalindrome(s: chr) -> Tuple[int, int]:
    return recursion(s, 0, len(s) - 1, 0)


if __name__ == "__main__":
    main()
