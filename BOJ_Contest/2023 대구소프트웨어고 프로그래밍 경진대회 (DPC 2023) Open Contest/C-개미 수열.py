def main():
    N = int(input())
    ant = [1]
    for i in range(1, 101):
        cnt = 0
        curr, nextAnt = str(ant[i-1])[0], str(ant[i-1])[0]
        print(curr, nextAnt)
        for s in str(ant[i-1]):
            if curr != s:
                print(cnt)
                curr = s
                nextAnt += str(cnt)
            else:
                cnt += 1
        nextAnt += str(cnt)
        ant.append(int(nextAnt))
    print(ant)


if __name__ == "__main__":
    main()
