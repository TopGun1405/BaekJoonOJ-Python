def main():
    N, K = map(int, input().split())

    cnt = 0
    for h in range(N + 1):
        for m in range(60):
            for s in range(60):
                t = ""
                if h < 10:
                    t += "0" + str(h)
                else:
                    t += str(h)

                if m < 10:
                    t += "0" + str(m)
                else:
                    t += str(m)

                if s < 10:
                    t += "0" + str(s)
                else:
                    t += str(s)

                if str(K) in t:
                    cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
