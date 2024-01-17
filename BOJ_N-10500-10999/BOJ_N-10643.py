def main():
    pizza = [int(input()) for _ in range(8)]
    pizza += pizza
    maxMush = 0
    for i in range(8):
        maxMush = max(maxMush, sum(pizza[i:i+4]))
    print(maxMush)


if __name__ == "__main__":
    main()
