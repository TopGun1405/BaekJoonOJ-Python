def main():
    N, M = map(int, input().split())
    linkPW = dict()
    for _ in range(N):
        url, pw = input().split()
        linkPW.update({url: pw})
    for _ in range(M):
        url = input()
        print(linkPW[url])


if __name__ == "__main__":
    main()
