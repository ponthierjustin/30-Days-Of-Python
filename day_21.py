# 5/13/24 
# Justin
from collections import Counter
import math

class Statistics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        freq = Counter(self.data)
        modes = freq.most_common()
        max_freq = modes[0][1]
        return [mode[0] for mode in modes if mode[1] == max_freq]

    def range(self):
        return max(self.data) - min(self.data)

    def variance(self):
        mean_val = self.mean()
        return sum((x - mean_val) ** 2 for x in self.data) / len(self.data)

    def standard_deviation(self):
        return math.sqrt(self.variance())

    def minimum(self):
        return min(self.data)

    def maximum(self):
        return max(self.data)

    def count(self):
        return len(self.data)

    def percentile(self, q):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        index = (q / 100) * (n - 1)
        if index.is_integer():
            return sorted_data[int(index)]
        else:
            lower = math.floor(index)
            upper = math.ceil(index)
            return (sorted_data[lower] + sorted_data[upper]) / 2

    def frequency_distribution(self):
        freq = Counter(self.data)
        return freq

data = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10]
stats = Statistics(data)
print("Mean:", stats.mean())
print("Median:", stats.median())
print("Mode:", stats.mode())
print("Range:", stats.range())
print("Variance:", stats.variance())
print("Standard Deviation:", stats.standard_deviation())
print("Minimum:", stats.minimum())
print("Maximum:", stats.maximum())
print("Count:", stats.count())
print("Percentile (50th):", stats.percentile(50))
print("Frequency Distribution:", stats.frequency_distribution())



class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def total_income(self):
        return sum(amount for amount, _ in self.incomes.values())

    def total_expense(self):
        return sum(amount for amount, _ in self.expenses.values())

    def account_info(self):
        return f"{self.firstname} {self.lastname}'s Account\n" \
               f"Total Income: {self.total_income()}\n" \
               f"Total Expense: {self.total_expense()}\n" \
               f"Account Balance: {self.account_balance()}"

    def add_income(self, amount, description):
        if amount > 0:
            self.incomes[len(self.incomes) + 1] = (amount, description)
        else:
            raise ValueError("Income amount must be positive.")

    def add_expense(self, amount, description):
        if amount > 0:
            self.expenses[len(self.expenses) + 1] = (amount, description)
        else:
            raise ValueError("Expense amount must be positive.")

    def account_balance(self):
        return self.total_income() - self.total_expense()

account = PersonAccount("John", "Doe")
account.add_income(500, "Freelance Work")
account.add_income(1000, "Salary")
account.add_expense(200, "Groceries")
account.add_expense(50, "Dinner")
print(account.account_info())
