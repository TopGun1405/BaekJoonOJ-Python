def main():
    while True:
        n = int(input())
        if n == 0:
            break
        v = list(map(int, input().split()))

        peaks = 0
        for i in range(1, n - 1):
            if v[i - 1] < v[i] and v[i] > v[i + 1]:
                peaks += 1
        print(peaks)


if __name__ == "__main__":
    main()
