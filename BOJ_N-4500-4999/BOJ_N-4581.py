def main():
    while True:
        vote = input()
        if vote == '#':
            break
        votes = {'Y': 0, 'N': 0, 'P': 0, 'A': 0}
        for v in vote:
            votes[v] += 1
        print("need quorum" if votes['A'] >= len(vote) / 2
              else ("yes" if votes['Y'] > votes['N']
                    else ("no" if votes['N'] > votes['Y']
                          else "tie")))


if __name__ == "__main__":
    main()
