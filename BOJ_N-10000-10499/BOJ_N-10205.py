def main():
    K = int(input())
    for n in range(K):
        h = int(input())
        actions = input()
        for a in actions:
            if a == 'c':
                h += 1
            else:
                h -= 1
            if h == 0:
                break
        print("Data Set {}:".format(n + 1))
        print(h)
        print()


if __name__ == "__main__":
    main()
