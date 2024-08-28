import json
# Global dictionary to store transactions
transactions = {}
incomes={}
expenses={}
# File handling functions
def load_transactions(path):
    try:
        with open(path,'r') as file:
            content = json.load(file)
        return content
    except FileNotFoundError:
        print("File not found...")
    pass
def save_transactions(transactions,path):
    with open(path,'w') as file:
        json.dump(transactions,file)
        file.write("\n")
    pass
def read_bulk_transactions_from_file():
    # Open and read the file, then parse each line to add to the transactions dictionarypass
  pass
# Feature implementations(expense category list)
category_list=["Bills","Car","Clothes","Communication","Eating Out","Entertainment","Food","Gifts","Health","House","Pets","Sports","Taxi","Toietry","Transport"]
def add_transaction():
    while True:
        new_list=(str(input("\n Do you want to add new transaction ? \t type YES or NO :")))
        try:
            if new_list.lower()=="yes":
                    choice_1=int(input("\n\tIf it is income or expense \t\nIt is Income Enter 1 |  It is Expense Enter 2 :"))
                    try:
                        if choice_1==1:
                            incomes["type"]="incomes"
                            print("\nYour Transaction is going to be started")
                            new_category=(str(input("\tEnter the category name : ")))
                            incomes["category"]=new_category
                            amount=round(float(input("\tEnter the amount  :")))
                            incomes["Amount"] = amount
                            # user input for transaction date
                            while True:
                                transaction_date = input('\tEnter the date (YYYY-MM-DD format) : ')
                                date_parts = transaction_date.split('-')    
                                # Check the date id valid or not
                                if len(date_parts) != 3:
                                    print('Invalid date. Please try again..')
                                else:
                                    try:
                                        year = int(date_parts[0])
                                        month = int(date_parts[1])
                                        date = int(date_parts[2])
                                        if year < 1900 or year > 2050 or month < 1 or month > 12 or date < 1 or date > 31:
                                            print('Invalid date.. Please try again.')
                                        else:
                                            if month in [4,6,9,11] and date > 30:
                                                print('The month you entered have only 30 days.. Please try again..')                        
                                            # Confirm if user entered 2 month is leep year or not 
                                            elif month == 2:
                                                leep_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
                                                if (leep_year and date > 29) or (not leep_year and date > 28):
                                                    print('Invalid date.. Please try again...')
                                                else:
                                                    incomes["Date"] = transaction_date
                                            else:
                                                incomes["Date"] = transaction_date
                                            break
                                    except ValueError:
                                        print('Invalid date... Please try again..')
                            #list 1 append to income list
                            transactions.setdefault("incomes",[]).append(incomes)
                            save_transactions(transactions,"all_transactions.json")
                            print("Transaction added sussesfully.")
                        elif choice_1==2:
                            expenses["income or expense"]= "expense"
                            print("\nYour Transaction is going to be started")
                            print(f"Choose your category :")#extra feature(custom expense reasons list)
                            count=1
                            for item in category_list:
                                print(f"{count } {  item}")
                                count += 1
                            print("16 add new one")
                            category_choice=int(input("\tEnter your choice : "))
                            #add other expense reason
                            if category_choice==16:
                                new_category=(str(input("\tEnter the category name : ")))
                                expenses["Category"] = new_category
                                amount=round(float(input("\tEnter the amount  :")))
                                expenses["Amount"] = amount
                                # user input for transaction date
                                while True:
                                    transaction_date = input('\tEnter the date (YYYY-MM-DD format) : ')
                                    date_parts = transaction_date.split('-')    
                               # Check the date id valid or not
                                    if len(date_parts) != 3:
                                        print('Invalid date. Please try again..')
                                    else:
                                        try:
                                            year = int(date_parts[0])
                                            month = int(date_parts[1])
                                            date = int(date_parts[2])
                                            if year < 1900 or year > 2050 or month < 1 or month > 12 or date < 1 or date > 31:
                                                print('Invalid date.. Please try again.')
                                            else:
                                                if month in [4,6,9,11] and date > 30:
                                                    print('The month you entered have only 30 days.. Please try again..')                        
                                            # Confirm if user entered 2 month is leep year or not 
                                                elif month == 2:
                                                    leep_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
                                                    if (leep_year and date > 29) or (not leep_year and date > 28):
                                                        print('Invalid date.. Please try again...')
                                                    else:
                                                        expenses["Date"] = transaction_date
                                                else:
                                                    expenses["Date"]=transaction_date
                                                break
                                        except ValueError:
                                            print('Invalid date... Please try again..')
                                transactions.setdefault("expenses", []).append(expenses)
                                save_transactions(transactions,"all_transactions.json")
                                print("Transaction added sussesfully.")
                            elif 0<category_choice<16:
                                expenses["Category"]=category_list[category_choice-1]
                                amount=round(float(input("\tEnter the amount  :")))
                                expenses["Amount"]=amount
                                # user input for transaction date
                                while True:
                                    transaction_date = input('\tEnter the date (YYYY-MM-DD format) : ')
                                    date_parts = transaction_date.split('-')    
                               # Check the date id valid or not
                                    if len(date_parts) != 3:
                                        print('Invalid date. Please try again..')
                                    else:
                                        try:
                                            year = int(date_parts[0])
                                            month = int(date_parts[1])
                                            date = int(date_parts[2])
                                            if year < 1900 or year > 2050 or month < 1 or month > 12 or date < 1 or date > 31:
                                                print('Invalid date.. Please try again.')
                                            else:
                                                if month in [4,6,9,11] and date > 30:
                                                    print('The month you entered have only 30 days.. Please try again..')                        
                                            # Confirm if user entered 2 month is leep year or not 
                                                elif month == 2:
                                                    leep_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
                                                    if (leep_year and date > 29) or (not leep_year and date > 28):
                                                        print('Invalid date.. Please try again...')
                                                    else:
                                                        expenses["Date"]=transaction_date
                                                else:
                                                    expenses["Date"]=transaction_date
                                                break
                                        except ValueError:
                                            print('Invalid date... Please try again..')
                                #list 1 append to expense list
                                transactions.setdefault("expenses", []).append(expenses)
                                save_transactions(transactions,"all_transactions.json")
                                print("Transaction added sussesfully.")
                            else:
                                print("invalid input, try again.")
                        else:
                            print("try again.")
                    except ValueError:
                        print("invalid input, try again.")
            else:
                print("Your Transaction is not started.Try again")
        except ValueError:
            print("invalid input, try again.")
        break
    pass
def view_transactions():
# View incomes
    print("Incomes:")
    if 'incomes' in transactions:
        for income in transactions['incomes']:
            print(f"Type: {income['type']}")
            print(f"Category: {income['category']}")
            print(f"Amount: {income['Amount']}")
            print(f"Date: {income['Date']}")
            print()
    else:
        print("")
# View expenses
    print("Expenses:")
    if 'expenses' in transactions:
        for expense in transactions['expenses']:
            print(f"Income or Expense: {expense['income or expense']}")
            print(f"Category: {expense['Category']}")
            print(f"Amount: {expense['Amount']}")
            print(f"Date: {expense['Date']}")
            print()
    else:
        print("")
    pass
def update_transaction():
    #use save_transactions() after updating
    print("\n * If you want to update income transaction Enter number 1 \n * If you want to update expense transaction Enter number 2.\n ")
    update_num=(int(input("Enter Number :")))
    if update_num==1:
        income_count = 0  
        print("\nIncomes:")
        if 'incomes' in transactions:
            for income in transactions['incomes']:
                print("")
                income_count += 1  
                print(f"{income_count}:")
                print(f"Type: {income['type']}")
                print(f"Category: {income['category']}")
                print(f"Amount: {income['Amount']}")
                print(f"Date: {income['Date']}")
                print()
        else:
            print("No income transactions found.")
        print("Total income transactions:", income_count)
        try:
            choice=(int(input("Enter the transaction number :")))
            if choice==income_count:
                print("\n Enter num 1 = update income to expense. \n Enter num 2 = Update category \n Enter num 3 = Update amount \n Enter num 4 = Update Date")
            try:
                choice2=(int(input("Enter the Number")))
                #update transaction logic
                if choice2==1:
                    transactions["incomes"][choice2-1]["type"] = "expense"
                    transactions["incomes"][choice-1]=transactions["expenses"]
                    del transactions["incomes"][choice - 1]
                if choice2==2:
                    try:
                        new_category=(str(input("Enter category :")))
                        transactions["incomes"][choice-1]["category"] = new_category
                        print("update succesfull...")
                        save_transactions(transactions,"all_transactions.json")
                    except ValueError:
                        print("Try again...")
                    except NameError:
                        print("Try again...")
                    except IndexError:
                        print("Try again...")
                if choice2==3:
                    try:
                        new_amount=(str(input("Enter amount :")))
                        transactions["incomes"][choice-1]["Amount"] = new_amount
                        print("update succesfull...")
                        save_transactions(transactions,"all_transactions.json")
                    except ValueError:
                        print("Try again...")
                    except NameError:
                        print("Try again...")
                    except IndexError:
                        print("Try again...")
                if choice2==4:
                    while True:
                        transaction_date = input('\tEnter the date (YYYY-MM-DD format) : ')
                        date_parts = transaction_date.split('-')    
                                # Check the date id valid or not
                        if len(date_parts) != 3:
                            print('Invalid date. Please try again..')
                        else:
                            try:
                                year = int(date_parts[0])
                                month = int(date_parts[1])
                                date = int(date_parts[2])
                                if year < 1900 or year > 2050 or month < 1 or month > 12 or date < 1 or date > 31:
                                        print('Invalid date.. Please try again.')
                                else:
                                    if month in [4,6,9,11] and date > 30:
                                        print('The month you entered have only 30 days.. Please try again..')                        
                                # Confirm if user entered 2 month is leep year or not 
                                    elif month == 2:
                                        leep_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
                                        if (leep_year and date > 29) or (not leep_year and date > 28):
                                                print('Invalid date.. Please try again...')
                                        else:
                                            transactions["incomes"][choice-1]["Date"] = transaction_date
                                    else:
                                        transactions["incomes"][choice-1]["Date"] = transaction_date
                                        break
                            except ValueError:
                                        print('Invalid date... Please try again..')
                            print("update succesfull...")
                            save_transactions(transactions,"all_transactions.json")
            except ValueError:
                    print("Try again...")
            except NameError:
                    print("Try again...")
            except IndexError:
                    print("Try again...")
        except ValueError:
            print("Try again...")
    elif update_num==2:
        expense_count=0
        print("\nExpenses:")
        if 'expenses' in transactions:
            for expense in transactions['expenses']:
                print("")
                expense_count+=1
                print(f"{expense_count}:")
                print(f"Income or Expense: {expense['income or expense']}")
                print(f"Category: {expense['Category']}")
                print(f"Amount: {expense['Amount']}")
                print(f"Date: {expense['Date']}")
                print()
        else:
            print("No expense transactions found.")
        print("Total expenses transactions:", expense_count)
        choice=(int(input("Enter the transaction number :")))
        if choice==expense_count:
            print("\n Enter num 1 = update expense to income. \n Enter num 2 = Update category \n Enter num 3 = Update amount \n Enter num 4 = Update Date")
            choice2=(int(input("Enter the Number")))
            #update transaction logic
            if choice2==1:
                transactions["expenses"][choice2-1]["type"] = "income"
                transactions["expenses"][choice-1]=transactions["income"]
                del transactions["expenses"][choice - 1]
                print("expense updated to income.")
                save_transactions(transactions,"all_transactions.json")
            if choice2==2:
                try:
                    new_category=(str(input("Enter category :")))
                    transactions["expenses"][choice-1]["Category"] = new_category
                    print("update succesfull...")
                    save_transactions(transactions,"all_transactions.json")
                except ValueError:
                    print("Try again...")
                except NameError:
                    print("Try again...")
                except IndexError:
                    print("Try again...")
            if choice2==3:
                try:
                    new_amount=(str(input("Enter amount :")))
                    transactions["expenses"][choice-1]["Amount"] = new_amount
                    print("update succesfull...")
                    save_transactions(transactions,"all_transactions.json")
                except ValueError:
                    print("Try again...")
                except NameError:
                    print("Try again...")
                except IndexError:
                    print("Try again...")
            if choice2==4:
                while True:
                    transaction_date = input('\tEnter the date (YYYY-MM-DD format) : ')
                    date_parts = transaction_date.split('-')    
                               # Check the date id valid or not
                    if len(date_parts) != 3:
                        print('Invalid date. Please try again..')
                    else:
                        try:
                            year = int(date_parts[0])
                            month = int(date_parts[1])
                            date = int(date_parts[2])
                            if year < 1900 or year > 2050 or month < 1 or month > 12 or date < 1 or date > 31:
                                    print('Invalid date.. Please try again.')
                            else:
                                if month in [4,6,9,11] and date > 30:
                                    print('The month you entered have only 30 days.. Please try again..')                        
                            # Confirm if user entered 2 month is leep year or not 
                                elif month == 2:
                                    leep_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
                                    if (leep_year and date > 29) or (not leep_year and date > 28):
                                            print('Invalid date.. Please try again...')
                                    else:
                                        transactions["expenses"][choice-1]["Date"] = transaction_date
                                else:
                                    transactions["expenses"][choice-1]["Date"] = transaction_date
                                    break
                        except ValueError:
                                    print('Invalid date... Please try again..')
                        print("update succesfull...")
                        save_transactions(transactions,"all_transactions.json")
    else:
        print("invalid input try again...")
    pass
def delete_transaction():
    print("\n * If you want to delete income transaction Enter number 1 \n * If you want to delete expense transaction Enter number 2.\n ")
    try:
        del_num=(int(input("Enter Number :")))
        if del_num==1:
            income_count = 0  # Initialize the count for income transactions
            print("\nIncomes:")
            if 'incomes' in transactions:
                for income in transactions['incomes']:
                    print("")
                    income_count += 1  # Increment the count for each income transaction
                    print(f"{income_count}:")
                    print(f"Type: {income['type']}")
                    print(f"Category: {income['category']}")
                    print(f"Amount: {income['Amount']}")
                    print(f"Date: {income['Date']}")
                    print()
                    choice=(int(input("Enter the Number for delete :")))
                    del transactions["incomes"][choice - 1]
                    print("transaction deleted")
                    save_transactions(transactions,"all_transactions.json")
            else:
                print("No income transactions found.")
        elif del_num==2:
            expense_count=0
            print("\nExpenses:")
            if 'expenses' in transactions:
                for expense in transactions['expenses']:
                    print("")
                    expense_count+=1
                    print(f"{expense_count}:")
                    print(f"Income or Expense: {expense['income or expense']}")
                    print(f"Category: {expense['Category']}")
                    print(f"Amount: {expense['Amount']}")
                    print(f"Date: {expense['Date']}")
                    print()
                    choice=(int(input("Enter the Number for delete :")))
                    del transactions["expenses"][choice - 1]
                    print("transaction deleted")
                    save_transactions(transactions,"all_transactions.json")
            else:
                print("No expense transactions found.")
            print("Total expenses transactions:", expense_count)
        else:
            print("invalid input try again...")
    except ValueError:
        print("Try again...")
    except NameError:
        print("Try again...")
    except IndexError:
        print("Try again...")
    pass
def display_summary():
    income_count = 0  # Initialize the count for income transactions
    if 'incomes' in transactions:
        for income in transactions['incomes']:
            print("")
            income_count += 1  
            print(f"Amount: {income['Amount']}")
        else:
            print("")
    expense_count=0
    if 'expenses' in transactions:
        for expense in transactions['expenses']:
            print("")
            expense_count+=1
        else:
            print("")
    print("\nTotal income transactions:", income_count)
    print("Total expenses transactions:", expense_count)
    total_trans=income_count+expense_count
    print("Total transactions:", total_trans)
    pass
def main_menu():
    transactions = load_transactions("all_transactions.txt")# Load transactions at the start
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
  
