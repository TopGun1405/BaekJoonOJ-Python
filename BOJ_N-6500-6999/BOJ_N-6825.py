def main():
    weight, height = float(input()), float(input())
    BMI = weight / height ** 2
    print("Overweight" if BMI > 25
          else ("Normal weight" if 18.5 <= BMI <= 25
                else "Underweight"))


if __name__ == "__main__":
    main()