def main():
    equation = input().split()
    print("YES" if int(equation[0]) + int(equation[2]) == int(equation[4])
          else "NO")


if __name__ == "__main__":
    main()
