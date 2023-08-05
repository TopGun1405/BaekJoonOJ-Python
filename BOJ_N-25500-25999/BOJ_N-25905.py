def main():
    p = [float(input()) for _ in range(10)]

    maxP = 1
    for pi in p:
        maxP *= pi
    maxP /= min(p)
    print(round(maxP * 10**9 / 362880, 7))


if __name__ == "__main__":
    main()
