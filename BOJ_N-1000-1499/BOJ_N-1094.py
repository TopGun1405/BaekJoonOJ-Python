def main():
    X = int(input())
    stick = [64]

    while True:
        if sum(stick) <= X:
            break
        stick[-1] = stick[-1] // 2
        stick.append(stick[-1])
        if sum(stick[:-1]) >= X:
            del stick[-1]
    print(len(stick))


if __name__ == "__main__":
    main()
