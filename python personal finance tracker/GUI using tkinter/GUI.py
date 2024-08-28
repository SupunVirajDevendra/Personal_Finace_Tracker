import tkinter as tk
from tkinter import ttk
import json

# Global dictionary to store transactions
transactions = {}
incomes={}
expenses={}
# File handling functions
class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")
        self.root.geometry('1200x800+150+15')
        self.transactions = self.load_transactions("all_transactions.json")
        self.create_widgets(root)
        self.root.configure(background='#6CB4EE')
        self.category_list = [
            "Bills", "Car", "Clothes", "Communication", "Eating Out",
            "Entertainment", "Food", "Gifts", "Health", "House", "Pets",
            "Sports", "Taxi", "Toiletry", "Transport"
        ]

    def create_widgets(self, app):
        tk.Label(app, text="Personal Finance Tracker !", font=("Impact", 50), bg='#6CB4EE', fg='black').pack(pady=5)
        tk.Button(app, text='1.  Add Transaction', font=("Helvetica", 20), bd='5', command=self.add_transaction, bg='#5adbb5', fg='black').pack(pady=10)
        tk.Button(app, text='2.  View Transactions', font=("Helvetica", 20), bd='5', command=self.view_transactions, bg='#5adbb5', fg='black').pack(pady=10)
        tk.Button(app, text='3.  Update Transactions', font=("Helvetica", 20), bd='5', command=self.update_transaction, bg='#5adbb5', fg='black').pack(pady=10)
        tk.Button(app, text='4.  Delete Transactions', font=("Helvetica", 20), bd='5', command=self.delete_transaction, bg='#5adbb5', fg='black').pack(pady=10)
        tk.Button(app, text='5.  Summary', font=("Helvetica", 20), bd='5', command=self.display_summary, bg='#5adbb5', fg='black').pack(pady=10)
        tk.Button(app, text='6.  Exit !', font=("Helvetica", 20), bd='5', command=app.destroy, bg='#5adbb5', fg='black').pack(pady=10)
        
    def load_transactions(self, filename):
        try:
            with open(filename, 'r') as file:
                content = json.load(file)
            return content
        except FileNotFoundError:
            print("File not found...")
            return {}
        
    def save_transactions(self, transactions, filename):
        with open(filename, 'w') as file:
            json.dump(transactions, file, indent=4)

    def validate_date(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False
        
    def add_transaction(self):
        incomes = {}
        expenses = {}
        new_window = tk.Toplevel(self.root)
        new_window.title("Add Transaction")
        new_window.geometry("400x300")
        tk.Label(new_window, text="Add Transaction", font=("Helvetica", 20)).pack(pady=10)

        choice_var = tk.IntVar()
        tk.Radiobutton(new_window, text="Income", variable=choice_var, value=1).pack()
        tk.Radiobutton(new_window, text="Expense", variable=choice_var, value=2).pack()

        category_var = tk.StringVar()
        tk.Label(new_window, text="Category:").pack()
        category_entry = tk.Entry(new_window, textvariable=category_var)
        category_entry.pack()

        amount_var = tk.DoubleVar()
        tk.Label(new_window, text="Amount:").pack()
        amount_entry = tk.Entry(new_window, textvariable=amount_var)
        amount_entry.pack()

        date_var = tk.StringVar()
        tk.Label(new_window, text="Date (YYYY-MM-DD):").pack()
        date_entry = tk.Entry(new_window, textvariable=date_var)
        date_entry.pack()

        def submit_transaction():
            if choice_var.get() == 1:  # Income
                incomes["type"] = "incomes"
                incomes["category"] = category_var.get()
                incomes["Amount"] = round(amount_var.get(), 2)
                incomes["Date"] = date_var.get()
                self.transactions.setdefault("incomes", []).append(incomes)
                self.save_transactions(self.transactions, "all_transactions.json")
                print("Income added successfully.")
            elif choice_var.get() == 2:  # Expense
                expenses["type"] = "expense"
                expenses["Category"] = category_var.get()
                expenses["Amount"] = round(amount_var.get(), 2)
                expenses["Date"] = date_var.get()
                self.transactions.setdefault("expenses", []).append(expenses)
                self.save_transactions(self.transactions, "all_transactions.json")
                print("Expense added successfully.")
            else:
                print("Invalid choice.")
            new_window.destroy()

        tk.Button(new_window, text="Submit", command=submit_transaction).pack(pady=10)

    # Define other methods as needed...
    def view_transactions(self):
        viewWindow = tk.Toplevel(self.root)
        viewWindow.geometry('1000x800+150+15')

        # View incomes
        incomes_label = ttk.Label(viewWindow, text="Incomes:", font=("Impact", 20)).pack()
        if 'incomes' in self.transactions:
            for idx, income in enumerate(self.transactions['incomes'], start=1):
                income_info = f"ID: {idx}, Type: {income['type']}, Category: {income['category']}, Amount: {income['Amount']}, Date: {income['Date']}"
                ttk.Label(viewWindow, text=income_info).pack()
        else:
            ttk.Label(viewWindow, text="No income transactions").pack()

        # View expenses
        expenses_label = ttk.Label(viewWindow, text="Expenses:", font=("Impact", 20)).pack()
        if 'expenses' in self.transactions:
            for idx, expense in enumerate(self.transactions['expenses'], start=1):
                expense_info = f"ID: {idx}, Type: {expense['type']}, Category: {expense['Category']}, Amount: {expense['Amount']}, Date: {expense['Date']}"
                ttk.Label(viewWindow, text=expense_info).pack()
        else:
            ttk.Label(viewWindow, text="No expense transactions").pack()

        # Table title
        table_title = ttk.Label(viewWindow, text='Transactions Table', font=('Helvetica', 20)).pack()

        # Frame for table and scrollbar
        m_frame = ttk.Frame(viewWindow, borderwidth=2)
        m_frame.pack()

        # Treeview for displaying transactions
        table = ttk.Treeview(m_frame, columns=('id', 'type', 'amount', 'date'), show='headings')
        table.heading('id', text='ID')
        table.heading('type', text='Type')
        table.heading('amount', text='Amount')
        table.heading('date', text='Date')

        for idx, income in enumerate(self.transactions.get('incomes', []), start=1):
            table.insert('', 'end', values=(idx, income['type'], income['Amount'], income['Date']))

        for idx, expense in enumerate(self.transactions.get('expenses', []), start=1):
            table.insert('', 'end', values=(idx, expense['type'], expense['Amount'], expense['Date']))

        table.pack(side='left')

        # Scrollbar for the Treeview
        scrollbar = ttk.Scrollbar(m_frame, orient='vertical', command=table.yview)
        scrollbar.pack(side='right')
        table.configure(yscrollcommand=scrollbar.set)

    def update_transaction(self):
        updateWindow = tk.Toplevel(self.root)
        updateWindow.title("Update Transaction")
        updateWindow.geometry("400x300")

        tk.Label(updateWindow, text="Update Transaction", font=("Helvetica", 20)).pack(pady=10)

        tk.Label(updateWindow, text="Select transaction type:").pack()
        transaction_type_var = tk.StringVar()
        transaction_type_var.set("Income")
        transaction_type_var.set("Expense")
        tk.OptionMenu(updateWindow, transaction_type_var, "Income", "Expense").pack()

        tk.Label(updateWindow, text="Select transaction index:").pack()
        transaction_index_var = tk.IntVar()
        transaction_index_entry = tk.Entry(updateWindow, textvariable=transaction_index_var)
        transaction_index_entry.pack()

        def update():
            try:
                idx = transaction_index_var.get() - 1
                if transaction_type_var.get() == "Income":
                    transaction = self.transactions['incomes'][idx]
                else:
                    transaction = self.transactions['expenses'][idx]

                category = transaction['category']
                amount = transaction['Amount']
                date = transaction['Date']

                updateWindow.destroy()

                updateTransactionWindow = tk.Toplevel(self.root)
                updateTransactionWindow.title("Update Transaction")
                updateTransactionWindow.geometry("400x300")

                tk.Label(updateTransactionWindow, text="Category:").pack()
                category_var = tk.StringVar()
                category_var.set(category)
                category_entry = tk.Entry(updateTransactionWindow, textvariable=category_var)
                category_entry.pack()

                tk.Label(updateTransactionWindow, text="Amount:").pack()
                amount_var = tk.DoubleVar()
                amount_var.set(amount)
                amount_entry = tk.Entry(updateTransactionWindow, textvariable=amount_var)
                amount_entry.pack()

                tk.Label(updateTransactionWindow, text="Date (YYYY-MM-DD):").pack()
                date_var = tk.StringVar()
                date_var.set(date)
                date_entry = tk.Entry(updateTransactionWindow, textvariable=date_var)
                date_entry.pack()

                def save_update():
                    transaction['category'] = category_var.get()
                    transaction['Amount'] = amount_var.get()
                    transaction['Date'] = date_var.get()

                    self.save_transactions(self.transactions, "all_transactions.json")
                    updateTransactionWindow.destroy()
                    print("Transaction updated successfully.")

                tk.Button(updateTransactionWindow, text="Save", command=save_update).pack(pady=10)
            except IndexError:
                print("Invalid index.")

        tk.Button(updateWindow, text="Update", command=update).pack(pady=10)
    def delete_transaction(self):
        deleteWindow = tk.Toplevel(self.root)
        deleteWindow.title("Delete Transaction")
        deleteWindow.geometry("400x300")

        tk.Label(deleteWindow, text="Delete Transaction", font=("Helvetica", 20)).pack(pady=10)

        tk.Label(deleteWindow, text="Select transaction type:").pack()
        transaction_type_var = tk.StringVar()
        transaction_type_var.set("Income")
        tk.OptionMenu(deleteWindow, transaction_type_var, "Income", "Expense").pack()

        tk.Label(deleteWindow, text="Select transaction index:").pack()
        transaction_index_var = tk.IntVar()
        transaction_index_entry = tk.Entry(deleteWindow, textvariable=transaction_index_var)
        transaction_index_entry.pack()

        def delete():
            try:
                idx = transaction_index_var.get() - 1
                if transaction_type_var.get() == "Income":
                    del self.transactions['incomes'][idx]
                else:
                    del self.transactions['expenses'][idx]

                self.save_transactions(self.transactions, "all_transactions.json")
                deleteWindow.destroy()
                print("Transaction deleted successfully.")
            except IndexError:
                print("Invalid index.")

        tk.Button(deleteWindow, text="Delete", command=delete).pack(pady=10)

    def display_summary(self):
        summaryWindow = tk.Toplevel(self.root)
        summaryWindow.title("Summary")
        summaryWindow.geometry('600x400+150+15')

        # Create a Treeview widget for displaying the summary
        summary_tree = ttk.Treeview(summaryWindow)
        summary_tree['columns'] = ('Category', 'Amount')
        summary_tree.heading('#0', text='Type')
        summary_tree.column('#0', width=100, anchor='center')
        summary_tree.heading('Category', text='Category')
        summary_tree.column('Category', width=200, anchor='center')
        summary_tree.heading('Amount', text='Amount')
        summary_tree.column('Amount', width=200, anchor='center')

        # Add data to the Treeview
        if 'incomes' in self.transactions:
            total_income = sum(income['Amount'] for income in self.transactions['incomes'])
            summary_tree.insert('', 'end', text='Income', values=('Total', total_income))
        if 'expenses' in self.transactions:
            total_expense = sum(expense['Amount'] for expense in self.transactions['expenses'])
            summary_tree.insert('', 'end', text='Expense', values=('Total', total_expense))

        summary_tree.pack(expand=True, fill='both')
def main_menu():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    root.mainloop()
    transactions = load_transactions("all_transactions.json")# Load transactions at the start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("\tEnter your choice: ")
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()
# if you are paid to do this assignment please delete this line of comment
  
