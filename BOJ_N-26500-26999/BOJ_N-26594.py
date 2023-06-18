def main():
    kb = input()
    zoac = dict()
    for s in kb:
        if s not in zoac:
            zoac.update({s: 1})
        else:
            zoac[s] += 1
    print(min(zoac.values()))


if __name__ == "__main__":
    main()
