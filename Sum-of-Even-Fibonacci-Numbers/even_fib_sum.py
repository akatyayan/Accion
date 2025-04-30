class EvenFibonacciSum:
    def __init__(self, count: int):
        self.count = count
        self.even_fibs = []
        self.total = 0

    def generate_even_fibonacci(self):
        a, b = 0, 1
        while len(self.even_fibs) < self.count:
            a, b = b, a + b
            if a % 2 == 0:
                self.even_fibs.append(a)
                self.total += a

    def get_sum(self) -> int:
        return self.total

    def get_series(self):
        return self.even_fibs


if __name__ == "__main__":
    fib_counter = EvenFibonacciSum(100)
    fib_counter.generate_even_fibonacci()
    print("Sum of first 100 even-valued Fibonacci numbers:", fib_counter.get_sum())
    print("Even Fibonacci Numbers:", fib_counter.get_series())
