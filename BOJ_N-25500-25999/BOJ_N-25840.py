def main():
    n = int(input())
    births = {input() for _ in range(n)}
    print(len(births))


if __name__ == "__main__":
    main()
