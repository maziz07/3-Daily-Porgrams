class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append({"description": description, "amount": amount})

    def get_total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

# Example usage
tracker = ExpenseTracker()
tracker.add_expense("Groceries", 50)
tracker.add_expense("Internet", 30)
print("Total Expenses:", tracker.get_total_expenses())
