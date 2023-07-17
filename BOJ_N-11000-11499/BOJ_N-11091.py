def main():
    alp = {chr(n) for n in range(97, 123)}
    N = int(input())
    for _ in range(N):
        text = set(list(map(lambda c: c.lower(), filter(lambda c: c.isalpha(), input()))))
        if len(text) == 26:
            print("pangram")
        else:
            print(f"missing {''.join(sorted(alp - text))}")


if __name__ == "__main__":
    main()
