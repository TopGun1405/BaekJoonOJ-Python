def main():
    n = int(input())
    s = sorted(map(int, input().split()))
    si = []
    for sa, sb in zip(s, s[::-1]):
        si.append(sa + sb)
    print(min(si))


if __name__ == "__main__":
    main()
