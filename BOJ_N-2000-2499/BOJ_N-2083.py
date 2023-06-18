def main():
    while True:
        name, age, weight = input().split()
        age, weight = int(age), int(weight)
        if name == '#' and age == weight == 0:
            break
        if age > 17 or weight >= 80:
            print(name, 'Senior')
        else:
            print(name, 'Junior')


if __name__ == "__main__":
    main()
