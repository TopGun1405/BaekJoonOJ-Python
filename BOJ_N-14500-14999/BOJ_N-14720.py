def main():
    N = int(input())
    store = list(map(int, input().split()))
    milk = []
    s = 0
    for i in range(len(store)):
        if store[i] == 0:
            s = i
            milk.append(store[i])
            break
    else:
        s = len(store)

    for i in range(s, len(store)):
        if milk[-1] == 0 and store[i] == 1:
            milk.append(store[i])
        elif milk[-1] == 1 and store[i] == 2:
            milk.append(store[i])
        elif milk[-1] == 2 and store[i] == 0:
            milk.append(store[i])
    print(len(milk))


if __name__ == "__main__":
    main()
