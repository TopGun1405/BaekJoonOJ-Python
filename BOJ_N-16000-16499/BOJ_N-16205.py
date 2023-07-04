def main():
    n, name = input().split()
    if n == '1':
        snake = ['_' + c.lower() if c.isupper() else c for c in name]
        print(name)
        print(''.join(snake))
        print(name[0].upper() + name[1:])
    elif n == '2':
        camel = name.split('_')
        for i in range(len(camel[1:])):
            camel[i+1] = camel[i+1][0].upper() + camel[i+1][1:]
        camel = ''.join(camel)
        print(camel)
        print(name)
        print(camel[0].upper() + camel[1:])
    else:
        snake = [name[0].lower()] + ['_' + c.lower() if c.isupper() else c for c in name[1:]]
        print(name[0].lower() + name[1:])
        print(''.join(snake))
        print(name)


if __name__ == "__main__":
    main()
