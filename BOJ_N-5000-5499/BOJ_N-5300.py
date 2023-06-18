def main():
    N = int(input())
    go = []
    for i in range(N):
        go.append(i + 1)
        if (i + 1) % 6 == 0:
            go.append("Go!")
    if go[-1] != "Go!":
        go.append("Go!")
    print(*go)


if __name__ == "__main__":
    main()
