def main():
    minC, minT = '', 201
    while True:
        name, temperature = input().split()
        if name == "Waterloo":
            break
        temperature = int(temperature)
        if temperature < minT:
            minC, minT = name, temperature
    print(minC)


if __name__ == "__main__":
    main()
