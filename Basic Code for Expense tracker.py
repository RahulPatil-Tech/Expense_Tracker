class ExpenseTraker:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self,description,amount):
        expense ={'description':description,'amount':amount}
        self.expenses.append(expense)
        print("Expense added successfully")
    
    def total_expenses(self):
        total = 0
        for expense in self.expenses:
            total += expense['amount']
        return total

    def print_expenses(self):
        if not self.expenses:
            print("No expenses")
        else:
            for expense in self.expenses:
                print(f"{expense['description']} - {expense['amount']}")
#Expample Usage
tracker = ExpenseTraker()
tracker.add_expense("Coffee", 2.50)
tracker.add_expense("Tea", 1.50)
tracker.add_expense("Cake", 4.50)
tracker.add_expense("Sandwich", 3.50)
tracker.add_expense("Burger", 5.50)

print("Total Expenses:",tracker.total_expenses())
tracker.print_expenses()