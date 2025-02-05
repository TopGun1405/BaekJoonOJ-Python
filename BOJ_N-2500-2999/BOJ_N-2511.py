def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    winner = ""
    score_A, score_B = 0, 0
    for A_i, B_i in zip(A, B):
        if A_i > B_i:
            score_A += 3
            winner = "A"
        elif A_i < B_i:
            score_B += 3
            winner = "B"
        else:
            score_A += 1
            score_B += 1

    print(score_A, score_B)
    if score_A > score_B:
        print("A")
    elif score_A < score_B:
        print("B")
    else:
        if winner == "A":
            print("A")
        elif winner == "B":
            print("B")
        else:
            print("D")


if __name__ == "__main__":
    main()
