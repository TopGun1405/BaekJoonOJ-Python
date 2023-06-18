def main():
    dish = list(input())
    length = 0
    for i in range(len(dish)):
        # length = length + 5 if i !=  0 and dish[i] == dish[i - 1] else length + 10
        if i != 0 and dish[i] == dish[i - 1]:
            length += 5
        else:
            length += 10
    print(length)


if __name__ == "__main__":
    main()
