from collections import Counter


def main():
    n = int(input())
    for _ in range(n):
        s = input()

        cnt = 0
        for c in Counter(s):
            if c.lower() == "g":
                cnt += Counter(s)[c]
            elif c.lower() == "b":
                cnt -= Counter(s)[c]

        print(s + (" is GOOD" if cnt > 0 else (" is A BADDY" if cnt < 0 else " is NEUTRAL")))


if __name__ == "__main__":
    main()
