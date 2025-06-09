def main():
    C = int(input())

    sbecs, maxSbecs = 100, 100
    for _ in range(C):
        V = int(input())

        sbecs += V
        if maxSbecs < sbecs:
            maxSbecs = sbecs

    print(maxSbecs)


if __name__ == "__main__":
    main()
