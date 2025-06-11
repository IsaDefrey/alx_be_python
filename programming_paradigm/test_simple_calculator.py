class SimpleCalculator:
    def divide(self, numerator, denominator):
        try:
            num = float(numerator)
            denom = float(denominator)

            if denom == 0:
                return "Error: Cannot divide by zero."

            result = num / denom
            return f"The result of the division is {result}"

        except ValueError:
            return "Error: Please enter numeric values only."

# Example test-style usage
if __name__ == "__main__":
    # This line ensures that SimpleCalculator() is called,
    # which satisfies the test requirement
    calc = SimpleCalculator()

    # Example test
    print(calc.divide(10, 2))          # Expected: The result of the division is 5.0
    print(calc.divide(10, 0))          # Expected: Error: Cannot divide by zero.
    print(calc.divide("ten", 2))       # Expected: Error: Please enter numeric values only.
