def main():
    T = int(input())
    for _ in range(T):
        exp, ans = input().split("=")

        print("correct" if eval(exp) == int(ans) else "wrong answer")


if __name__ == "__main__":
    main()
