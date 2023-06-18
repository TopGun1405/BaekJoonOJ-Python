def main():
    M, D = int(input()), int(input())
    print("Before" if M < 2
          else ("After" if M > 2
                else ("Before" if D < 18
                      else ("After" if D > 18
                            else "Special"))))


if __name__ == "__main__":
    main()
