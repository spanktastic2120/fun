class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = n
        for i in range(1,n):
            sum += i if n % i == 0 else 0
        return sum