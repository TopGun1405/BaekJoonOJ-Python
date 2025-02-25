def main():
    N, H = map(int, input().split())
    d = list(map(int, input().split()))

    card = 0
    for d_i in d:
        if H <= 0:
            break
        card += 1
        H -= d_i

    print(card if H <= 0 else -1)


if __name__ == "__main__":
    main()
