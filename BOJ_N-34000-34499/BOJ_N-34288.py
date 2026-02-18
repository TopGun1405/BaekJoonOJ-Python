def main():
    l, a = map(int, input().split())
    h = list(map(int, input().split()))
    for i in range(l):
        if h[i+1] - h[i] > a:
            print("BUG REPORT")
            break
    else:
        print("POSSIBLE")


if __name__ == "__main__":
    main()
