def main():
    form = input()
    
    if form[0] == 'c':
        num = 26
    else:
        num = 10

    for i in range(1, len(form)):
        if form[i] == 'c':
            num = num * (25 if form[i-1] == 'c' else 26)
        else:
            num = num * (9 if form[i-1] == 'd' else 10)

    print(num)


if __name__ == "__main__":
    main()
