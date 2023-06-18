def main():

    def roundK(num, digits=0):
        return round(num + 10 ** (-len(str(num)) - 1), digits)

    n = int(input())
    if n == 0:
        print(0)
        exit(0)
    else:
        opinions = sorted([int(input()) for _ in range(n)])
        i = int(roundK(n * 0.15))
        print(int(roundK(sum(opinions[i:(n if i == 0 else -i)]) / (n - 2*i))))


if __name__ == "__main__":
    main()
