class DecimalDigitTransformation:
    def __init__(self, digit: int):
        if not isinstance(digit, int):
            raise ValueError("Input must be an integer.")
        if digit < 0 or digit > 9:
            raise ValueError("Input must be a single digit (0-9).")
        self.digit = digit

    def calculate_transformation(self) -> int:
        x = str(self.digit)
        result = int(x) + int(x*2) + int(x*3) + int(x*4)
        return result


if __name__ == "__main__":
    try:
        digit = int(input("Enter a decimal digit (0-9): "))
        transformation = DecimalDigitTransformation(digit)
        result = transformation.calculate_transformation()
        print(f"The result of the transformation for {digit} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
