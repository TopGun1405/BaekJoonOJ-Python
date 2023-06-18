def main():
    S, A, B = int(input()), int(input()), int(input())
    print(250 if S <= A
          else (250 + ((S - A) // B) * 100 if (S - A) // B == (S - A) / B
                else 250 + ((S - A) // B + 1) * 100))


if __name__ == "__main__":
    main()
