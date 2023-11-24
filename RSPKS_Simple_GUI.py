from tkinter import *
from datetime import datetime
import csv
import os
import pandas as pd

date_format = "%d/%m/%Y"

root = Tk()
root.title('RSPK Jewellers Business Dashboard')
root.geometry('300x300')

def exit_main():
    print("Exiting the program. Goodbye!")
    root.quit()

# Define an empty list to store transactions
transactions = []

#Function to open Gold Transaction Window
def toplevel_gold():
    top_gold = Toplevel()

    top_gold.title('Add Gold Transaction')

    #Create Labels for each information
    gold_label = Label(top_gold, text = 'Welcome to Gold Sale Transaction Window')
    gold_label.grid(row=0, column=0, padx=10, pady=12, sticky='w')

    date_label = Label(top_gold, text="Today's Date:")
    date_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

    name_label = Label(top_gold, text="Customer's Name:")
    name_label.grid(row=2, column=0, padx=10, pady=12, sticky='w')

    phone_label = Label(top_gold, text = "Customer's Phone Number:")
    phone_label.grid(row=3, column=0, padx=10, pady=12, sticky='w')

    description_label = Label(top_gold, text="Transaction Description (Gold Jewellery):")
    description_label.grid(row=4, column=0, padx=10, pady=12, sticky='w')

    type_label = Label(top_gold, text="Transaction Type (Sale):")
    type_label.grid(row=5, column=0, padx=10, pady=12, sticky='w')

    gold_rate_label = Label(top_gold, text="Today's Gold Rate per gram:")
    gold_rate_label.grid(row=6, column=0, padx=10, pady=12, sticky='w')

    gold_wt_label = Label(top_gold, text = "Weight of Jewellery (in gms): ")
    gold_wt_label.grid(row=7, column=0, padx=10, pady=12, sticky='w')

    gold_amount_label = Label(top_gold, text="Total Amount (Inclusive GST): ")
    gold_amount_label.grid(row=8, column=0, padx=10, pady=12, sticky='w')

    # Create entry box for filling or typing the information.
    date_field = Entry(top_gold)
    date_field.grid(row=1, column=1, pady=12, sticky='w')

    name_field = Entry(top_gold)
    name_field.grid(row=2, column=1, pady=12, sticky='w')

    phone_field = Entry(top_gold)
    phone_field.grid(row=3, column=1, pady=12, sticky='w')
    
    description_field = Entry(top_gold)
    description_field.grid(row=4, column=1, pady=12, sticky='w')

    type_field = Entry(top_gold)
    type_field.grid(row=5, column=1, pady=12, sticky='w')

    gold_rate_field = Entry(top_gold)
    gold_rate_field.grid(row=6, column=1, pady=12, sticky='w')  
    
    gold_weight_field = Entry(top_gold)
    gold_weight_field.grid(row=7, column=1, pady=12, sticky='w')

    gold_amount_field = Entry(top_gold)
    gold_amount_field.grid(row=8, column=1, pady=12, sticky='w')

    # Make a function for exit button
    def exit_top_gold():
        top_gold.destroy()
        top_gold.update()

    #Function for clearing the contents of all entry boxes   
    def clear_all() :
    # whole content of entry boxes is deleted
        gold_rate_field.delete(0, END)
        gold_weight_field.delete(0, END)
        gold_amount_field.delete(0, END)
        date_field.delete(0, END)
        name_field.delete(0, END)
        phone_field.delete(0, END)
        description_field.delete(0, END)
        type_field.delete(0, END)

        # set focus on the principal_field entry box  
        gold_amount_field.focus_set() 

    def add_gold_transaction():
        date = date_field.get()
        name = name_field.get()
        phone = phone_field.get()
        description = description_field.get()
        type = type_field.get()
        gold_rate = float(gold_rate_field.get())
        wt = float(gold_weight_field.get())
        making = 0.18 * wt
        price = (gold_rate * wt) + making
        #GST on price
        tax = 0.03 * price
        #Final price
        amount = price + tax

        #Calculated cost will be inserted into the Amount Entry box
        gold_amount_field.insert(2, amount)

        transactions.append({'Date': date, 'Name': name, 'Phone': phone, 'Description': description, 'Type': type, 'Amount': amount})

        with open("TransactionReport.csv", "w") as csvfile:
            fields = ['Date', 'Name', 'Phone', 'Description', 'Type', 'Amount']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
            csvwriter.writeheader()
            csvwriter.writerows(transactions)
        
        print("Transaction added successfully!")

    # Create a Button to calculate cost and add transaction using gold_sale function
    button1 = Button(top_gold, text = "Calculate Cost & Add Transaction", command=add_gold_transaction)
    button1.grid(row=10, column=0, padx=10, pady=12, sticky='w')

    # Create a Clear Button to clear the entered values  
    button2 = Button(top_gold, text = "Clear", command=clear_all)
    button2.grid(row=10, column=1, padx=10, pady=12, sticky='w')

    #Create an Exit Button to exit the application
    button3 = Button(top_gold, text = "Close Application", command=exit_top_gold)
    button3.grid(row=10, column=2, pady=12, sticky='w')

#Function to open Silver Transaction Window
def toplevel_silver():
    top_silver = Toplevel()

    top_silver.title('Add Silver Transaction')

    #Create Labels for each information
    silver_label = Label(top_silver, text = 'Welcome to Silver Sale Transaction Window')
    silver_label.grid(row=0, column=0, padx=10, pady=12, sticky='w')

    date_label = Label(top_silver, text="Today's Date:")
    date_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

    name_label = Label(top_silver, text="Customer's Name:")
    name_label.grid(row=2, column=0, padx=10, pady=12, sticky='w')

    phone_label = Label(top_silver, text = "Customer's Phone Number:")
    phone_label.grid(row=3, column=0, padx=10, pady=12, sticky='w')

    description_label = Label(top_silver, text="Transaction Description (Silver Jewellery):")
    description_label.grid(row=4, column=0, padx=10, pady=12, sticky='w')

    type_label = Label(top_silver, text="Transaction Type (Sale):")
    type_label.grid(row=5, column=0, padx=10, pady=12, sticky='w')

    silver_rate_label = Label(top_silver, text="Today's Silver Rate per gram:")
    silver_rate_label.grid(row=6, column=0, padx=10, pady=12, sticky='w')

    silver_wt_label = Label(top_silver, text = "Weight of Jewellery (in gms): ")
    silver_wt_label.grid(row=7, column=0, padx=10, pady=12, sticky='w')

    silver_amount_label = Label(top_silver, text="Total Amount (Inclusive GST): ")
    silver_amount_label.grid(row=8, column=0, padx=10, pady=12, sticky='w')

    # Create entry box for filling or typing the information.
    date_field = Entry(top_silver)
    date_field.grid(row=1, column=1, pady=12, sticky='w')

    name_field = Entry(top_silver)
    name_field.grid(row=2, column=1, pady=12, sticky='w')

    phone_field = Entry(top_silver)
    phone_field.grid(row=3, column=1, pady=12, sticky='w')
    
    description_field = Entry(top_silver)
    description_field.grid(row=4, column=1, pady=12, sticky='w')

    type_field = Entry(top_silver)
    type_field.grid(row=5, column=1, pady=12, sticky='w')

    silver_rate_field = Entry(top_silver)
    silver_rate_field.grid(row=6, column=1, pady=12, sticky='w')  
    
    silver_weight_field = Entry(top_silver)
    silver_weight_field.grid(row=7, column=1, pady=12, sticky='w')

    silver_amount_field = Entry(top_silver)
    silver_amount_field.grid(row=8, column=1, pady=12, sticky='w')

    # Make a function for exit button
    def exit_top_silver():
        top_silver.destroy()
        top_silver.update()

    #Function for clearing the contents of all entry boxes   
    def clear_all() :
    # whole content of entry boxes is deleted
        silver_rate_field.delete(0, END)
        silver_weight_field.delete(0, END)
        silver_amount_field.delete(0, END)
        date_field.delete(0, END)
        name_field.delete(0, END)
        phone_field.delete(0, END)
        description_field.delete(0, END)
        type_field.delete(0, END)

        # set focus on the principal_field entry box  
        silver_amount_field.focus_set() 

    # Function to add silver transaction to the list
    def add_silver_transaction():
        date = date_field.get()
        name = name_field.get()
        phone = phone_field.get()
        description = description_field.get()
        type = type_field.get()
        silver_rate = float(silver_rate_field.get())
        wt = float(silver_weight_field.get())
        making = 0.18 * wt
        price = (silver_rate * wt) + making
        #GST on price
        tax = 0.03 * price
        #Final price
        amount = price + tax

        #Calculated cost will be inserted into the Amount Entry box
        silver_amount_field.insert(2, amount)
    
        transactions.append({'Date': date, 'Name': name, 'Phone': phone, 'Description': description, 'Type': type, 'Amount': amount})

        with open("TransactionReport.csv", "w") as csvfile:
            fields = ['Date', 'Name', 'Phone', 'Description', 'Type', 'Amount']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
            csvwriter.writeheader()
            csvwriter.writerows(transactions)
        
        print("Transaction added successfully!")


    # Create a Button to calculate cost and add transaction using gold_sale function
    button1 = Button(top_silver, text = "Calculate Cost & Add Transaction", command=add_silver_transaction)
    button1.grid(row=10, column=0, padx=10, pady=12, sticky='w')

    # Create a Clear Button to clear the entered values  
    button2 = Button(top_silver, text = "Clear", command=clear_all)
    button2.grid(row=10, column=1, padx=10, pady=12, sticky='w')

    #Create an Exit Button to exit the application
    button3 = Button(top_silver, text = "Close Application", command=exit_top_silver)
    button3.grid(row=10, column=2, pady=12, sticky='w')

#Function to open Loan Transaction Window
def toplevel_loan():
    top_loan = Toplevel()

    top_loan.title('Add Loan Transaction')

    #Create Labels for each information
    loan_label = Label(top_loan, text='Welcome to Loan Transaction Window')
    loan_label.grid(row=0, column=0, padx=10, pady=12, sticky='w')

    date_label = Label(top_loan, text="Today's Date: ")
    date_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

    name_label = Label(top_loan, text="Customer's Name: ")
    name_label.grid(row=2, column=0, padx=10, pady=12, sticky='w')

    phone_label = Label(top_loan, text = "Customer's Phone Number: ")
    phone_label.grid(row=3, column=0, padx=10, pady=12, sticky='w')

    description_label = Label(top_loan, text="Transaction Description: ")
    description_label.grid(row=4, column=0, padx=10, pady=12, sticky='w')

    type_label = Label(top_loan, text="Transaction Type (Loan): ")
    type_label.grid(row=5, column=0, padx=10, pady=12, sticky='w')

    principal_label = Label(top_loan, text="Principal Amount: ")
    principal_label.grid(row=6, column=0, padx=10, pady=12, sticky='w')

    date1_label = Label(top_loan, text = "Start Date of Tenure: ")
    date1_label.grid(row=7, column=0, padx=10, pady=12, sticky='w')

    date2_label = Label(top_loan, text="End Date of Tenure: ")
    date2_label.grid(row=8, column=0, padx=10, pady=12, sticky='w')

    time_label = Label(top_loan, text="Time (in days): ")
    time_label.grid(row=9, column=0, padx=10, pady=12, sticky='w')

    amount_interest_label = Label(top_loan, text="Total amount owed (Inclusive Interest): ")
    amount_interest_label.grid(row=10, column=0, padx=10, pady=12, sticky='w')

    # Create entry box for filling or typing the information.
    date_field = Entry(top_loan)
    date_field.grid(row=1, column=1, pady=12, sticky='w')

    name_field = Entry(top_loan)
    name_field.grid(row=2, column=1, pady=12, sticky='w')

    phone_field = Entry(top_loan)
    phone_field.grid(row=3, column=1, pady=12, sticky='w')
    
    description_field = Entry(top_loan)
    description_field.grid(row=4, column=1, pady=12, sticky='w')

    type_field = Entry(top_loan)
    type_field.grid(row=5, column=1, pady=12, sticky='w')

    principal_field = Entry(top_loan)
    principal_field.grid(row=6, column=1, pady=12, sticky='w')
    
    date1_field = Entry(top_loan)
    date1_field.grid(row=7, column=1, pady=12, sticky='w')
    
    date2_field = Entry(top_loan)
    date2_field.grid(row=8, column=1, pady=12, sticky='w')
    
    time_field = Entry(top_loan)
    time_field.grid(row=9, column=1, pady=12, sticky='w')
    
    amount_field = Entry(top_loan)
    amount_field.grid(row=10, column=1, pady=12, sticky='w')

    # Make a function for exit button
    def exit_top_loan():
        top_loan.destroy()
        top_loan.update()

    #Function for clearing the contents of all entry boxes   
    def clear_all() :
        
        # whole content of entry boxes is deleted
        date_field.delete(0, END)
        name_field.delete(0, END)
        phone_field.delete(0, END)
        description_field.delete(0, END)
        type_field.delete(0, END)
        principal_field.delete(0, END)
        date1_field.delete(0, END)
        date2_field.delete(0, END)
        time_field.delete(0, END)
        amount_field.delete(0, END)
   
        # set focus on the principal_field entry box  
        amount_field.focus_set() 

    #Function to calculate the cost of loan amount (inclusive interest)
    def add_loan_transaction():
        date = date_field.get()
        name = name_field.get()
        phone = phone_field.get()
        description = description_field.get()
        type = type_field.get()
        principal = float(principal_field.get())
        a = datetime.strptime(date1_field.get(), date_format)
        b = datetime.strptime(date2_field.get(), date_format)
        time_elapsed = (b - a)
        time = (time_elapsed.days)

        time_field.insert(0, time)

        roi = 0.066
        interest = (principal * roi * time) / 100
        #Final price
        amount = principal + interest

        #Calculated cost will be inserted into the Amount Entry box
        amount_field.insert(2, amount)
    
        transactions.append({'Date': date, 'Name': name, 'Phone': phone, 'Description': description, 'Type': type, 'Amount': amount})

        with open("TransactionReport.csv", "w") as csvfile:
            fields = ['Date', 'Name', 'Phone', 'Description', 'Type', 'Amount']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
            csvwriter.writeheader()
            csvwriter.writerows(transactions)
        
        print("Transaction added successfully!")


    # Create a Button to calculate cost and add transaction using gold_sale function
    button1 = Button(top_loan, text = "Calculate Cost & Add Transaction", command=add_loan_transaction)
    button1.grid(row=11, column=0, padx=10, pady=12, sticky='w')

    # Create a Clear Button to clear the entered values  
    button2 = Button(top_loan, text = "Clear", command=clear_all)
    button2.grid(row=11, column=1, padx=10, pady=12, sticky='w')

    #Create an Exit Button to exit the application
    button3 = Button(top_loan, text = "Close Application", command=exit_top_loan)
    button3.grid(row=11, column=2, pady=12, sticky='w')

#Function to display Transaction Report
def display_transactions():
    path = os.getcwd()
    df = pd.read_csv(path+"\\TransactionReport.csv")
    df.to_excel("TransactionReport.xlsx", sheet_name="Transaction Report", index=False)
    os.startfile(path+"\\TransactionReport.xlsx")

#Start-up Window
label = Label(root, text="Welcome to RSPK Jewellers")
label.grid(row=0, column=0, padx=10, pady=12, sticky='w')

button1 = Button(root, text="Add Gold Transaction", command=toplevel_gold)
button1.grid(row=1, column=0, padx=10, pady=12, sticky='w')

button2 = Button(root, text="Add Silver Transaction", command=toplevel_silver)
button2.grid(row=2, column=0, padx=10, pady=12, sticky='w')

button3 = Button(root, text="Add Loan Transaction", command=toplevel_loan)
button3.grid(row=3, column=0, padx=10, pady=12, sticky='w')

button4 = Button(root, text="View Transaction Report", command=display_transactions)
button4.grid(row=4, column=0, padx=10, pady=12, sticky='w')

button5 = Button(root, text='Exit Main window', command=exit_main)
button5.grid(row=5, column=0, padx=10, pady=12, sticky='w')

root.mainloop()
