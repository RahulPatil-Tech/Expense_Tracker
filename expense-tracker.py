import tkinter as tk
import xlsxwriter

def save_expense():
    expense_data = {
        'Date': date_entry.get(),
        'Category': category_entry.get(),
        'Amount': amount_entry.get()
    }
    expenses.append(expense_data)
    clear_entries()
    update_excel()
    update_total()

def clear_entries():
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def update_excel():
    workbook = xlsxwriter.Workbook('expenses.xlsx')
    worksheet = workbook.add_worksheet()

    # Write headers
    headers = ['Date', 'Category', 'Amount']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Write expense data
    for row, expense in enumerate(expenses, start=1):
        worksheet.write(row, 0, expense['Date'])
        worksheet.write(row, 1, expense['Category'])
        worksheet.write(row, 2, expense['Amount'])

    workbook.close()

def update_total():
    total = sum(float(expense['Amount']) for expense in expenses)
    total_label.config(text=f'Total Expenses: Rs {total:.2f}')

# Create GUI
root = tk.Tk()
root.title('Expense Tracker')

date_label = tk.Label(root, text='Date:')
date_label.grid(row=0, column=0, padx=10, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1)

category_label = tk.Label(root, text='Category:')
category_label.grid(row=1, column=0, padx=10, pady=5)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

amount_label = tk.Label(root, text='Amount:')
amount_label.grid(row=2, column=0, padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1)

save_button = tk.Button(root, text='Save', command=save_expense)
save_button.grid(row=3, column=0, columnspan=2, pady=10)

total_label = tk.Label(root, text='Total Expenses: Rs 0.00')
total_label.grid(row=4, column=0, columnspan=2, pady=5)

# Track expenses
expenses = []

root.mainloop()