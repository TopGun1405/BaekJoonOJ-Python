def main():
    games = [input() for _ in range(6)]
    print(1 if games.count('W') >= 5
          else (2 if games.count('W') >= 3
                else (3 if games.count('W') >= 1 else -1)))


if __name__ == "__main__":
    main()
