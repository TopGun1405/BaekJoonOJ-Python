def main():
    h = ['N', 'E', 'S', 'W']
    i = 0
    ti = {1: 1, 2: 2, 3: -1}
    for _ in range(10):
        t = int(input())
        i = (i + ti[t]) % 4
    print(h[i])


if __name__ == "__main__":
    main()
