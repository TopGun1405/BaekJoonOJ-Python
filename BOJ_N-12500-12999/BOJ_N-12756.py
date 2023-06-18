def main():
    Aa, Ah = map(int, input().split())
    Ba, Bh = map(int, input().split())
    A = Ah // Ba + (1 if Ah % Ba else 0)
    B = Bh // Aa + (1 if Bh % Aa else 0)
    print("PLAYER A" if A > B
          else ("PLAYER B" if A < B
                else "DRAW"))


if __name__ == "__main__":
    main()
