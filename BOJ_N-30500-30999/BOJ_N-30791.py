def main():
    votes = list(map(int, input().split()))
    cnt = 0
    for vi in votes[1:]:
        if votes[0] - vi <= 1000:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
