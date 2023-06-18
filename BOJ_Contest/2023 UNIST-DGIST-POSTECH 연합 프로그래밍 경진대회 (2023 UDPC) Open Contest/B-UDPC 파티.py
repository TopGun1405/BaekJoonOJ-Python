def main():
    votes = input()
    total = {'U': 0, 'D': 0, 'P': 0, 'C': 0}
    for v in votes:
        total[v] += 1
    ans = ''
    UC, DP = total['U'] + total['C'], total['D'] + total['P']
    if UC > (DP + 1) / 2:
        ans += 'U'
    if DP > 0:
        ans += 'DP'
    print(ans)


if __name__ == "__main__":
    main()
