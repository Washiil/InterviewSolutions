def addDigits(self, num: int) -> int:
    while True:
        total = 0
        while num > 0:
            d = num % 10  # Get the last digit of the number
            total += d   # Add to sum
            num //= 10   # Remove the digit

        if total < 10:   # Simple single digit check
            return total
        else:
            num = total  # Reset for next loop
