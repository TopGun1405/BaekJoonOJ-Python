def main():
    S = input()

    subs = []
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            subs.append(S[i:j])
    subs = sorted(set(subs), reverse=True)

    print(subs)
    print(subs[0])


if __name__ == "__main__":
    main()
