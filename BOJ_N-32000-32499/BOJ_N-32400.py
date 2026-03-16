def main():
    score = list(map(int, input().split()))

    i = score.index(20)
    Alice = (score[i-1] + score[i] + score[(i + 1) % 20]) / 3
    Bob = sum(score) / 20

    if Alice > Bob:
        print("Alice")
    elif Bob > Alice:
        print("Bob")
    else:
        print("Tie")


if __name__ == "__main__":
    main()
