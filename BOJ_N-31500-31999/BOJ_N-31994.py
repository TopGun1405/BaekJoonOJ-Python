def main():
    data = []
    for _ in range(7):
        name, num = input().split()
        data.append([name, int(num)])

    data.sort(key=lambda k: k[1])
    print(data[-1][0])


if __name__ == "__main__":
    main()
