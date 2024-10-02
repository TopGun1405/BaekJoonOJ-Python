def main():
    alp = {chr(n): 0 for n in range(65, 91)}

    S = input()
    for c in S:
        try:
            alp[c.upper()] += 1
        except KeyError:
            continue

    for key, val in alp.items():
        print(f"{key} | {'*' * val}")


if __name__ == "__main__":
    main()
