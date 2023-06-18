def main():
    ACM = []
    ansCnt, penalty = 0, 0
    while True:
        log = input().split()
        if log[0] == '-1':
            break
        if log[2] == "right":
            penalty += ACM.count(log[1]) * 20 + int(log[0])
            ansCnt += 1
        ACM.append(log[1])
    print(ansCnt, penalty)


if __name__ == "__main__":
    main()
