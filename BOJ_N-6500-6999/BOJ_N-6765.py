def main():
    k = int(input())
    icon = [
        ''.join(map(lambda c: c * k, "*x*")),
        ''.join(map(lambda c: c * k, " xx")),
        ''.join(map(lambda c: c * k, "* *"))
    ]
    icon = [
        '*'*k + 'x'*k + '*'*k,
        ' '*k + 'x'*k + 'x'*k,
        '*'*k + ' '*k + '*'*k
    ]
    for i in icon:
        for _ in range(k):
            print(i)


if __name__ == "__main__":
    main()
