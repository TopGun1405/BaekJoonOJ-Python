def main():
    ISBN = list(map(lambda e: int(e) if e.isdigit() else e, list(input())))

    k, s = 0, 0
    for i in range(13):
        if ISBN[i] == "*":
            s = 1 if i % 2 == 0 else 3
            continue
        k += (1 if i % 2 == 0 else 3) * ISBN[i]

    for i in range(10):
        if (k + s * i) % 10 == 0:
            print(i)
            break


if __name__ == "__main__":
    main()
