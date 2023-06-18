def main():
    n = int(input())
    for i in range(1, n + 1):
        data = input()
        result = ''
        for j in range(len(data)):
            value = ord(data[j]) + 1
            if value > 90:
                value = 65
            result += chr(value)
        # print('String #%d' % i)
        print('String #{}'.format(i))
        print(result)
        print()


if __name__ == "__main__":
    main()
