class ArmstrongChecker:
    def __init__(self, number):
        """Initialize with the given number"""
        self.number = number

    def is_armstrong(self):
        """Check if the number is an Armstrong number"""
        digits = [int(d) for d in str(self.number)]
        power = len(digits)
        total = sum(d ** power for d in digits)
        return total == self.number

    def show_result(self):
        """Display result"""
        if self.is_armstrong():
            print(f"✅ {self.number} is an Armstrong Number!")
        else:
            print(f"❌ {self.number} is NOT an Armstrong Number.")


