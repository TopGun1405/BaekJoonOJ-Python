def main():
    S = input()

    cnt = 0
    for c1, c2 in zip(S, "SciComLove"):
        if c1 != c2:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
