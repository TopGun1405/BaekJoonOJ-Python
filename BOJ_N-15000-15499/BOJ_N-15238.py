def main():
    size = int(input())
    word = input()
    cnt = dict()
    for c in word:
        if c not in cnt:
            cnt.update({c: 1})
        else:
            cnt[c] += 1
    cntRev = {val: key for key, val in cnt.items()}
    print(cntRev[max(cnt.values())], max(cnt.values()))


if __name__ == "__main__":
    main()
