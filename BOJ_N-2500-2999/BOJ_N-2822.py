def main():
    score = {int(input()): i for i in range(1, 9)}
    s = sorted(score.keys())
    p = [score[n] for n in s[-5:]]
    print(sum(s[-5:]))
    print(*sorted(p), sep=' ')


if __name__ == "__main__":
    main()
