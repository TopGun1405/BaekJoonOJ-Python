def main():
    q = int(input())
    quotes = {n + 1: input() for n in range(q)}
    r = int(input())
    rules = [int(input()) for _ in range(r)]
    for rule in rules:
        print(f"Rule {rule}: ", end='')
        try:
            print(quotes[rule])
        except KeyError:
            print("No such rule")


if __name__ == "__main__":
    main()
