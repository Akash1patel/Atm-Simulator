import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Invalid withdrawal amount."

def check_balance():
    balance = atm.check_balance()
    messagebox.showinfo("Balance", f"Your balance is ${balance}")

def deposit():
    amount = float(deposit_entry.get())
    result = atm.deposit(amount)
    messagebox.showinfo("Deposit", result)
    deposit_entry.delete(0, 'end')
    check_balance()

def withdraw():
    amount = float(withdraw_entry.get())
    result = atm.withdraw(amount)
    messagebox.showinfo("Withdraw", result)
    withdraw_entry.delete(0, 'end')
    check_balance()

atm = ATM(50000)  # Initial balance

# Create a GUI window
window = tk.Tk()
window.title("ATM Simulator")

# Labels
balance_label = tk.Label(window, text=f"Balance: INR {atm.check_balance()}", font=("Arial", 16))
balance_label.pack()

deposit_label = tk.Label(window, text="Deposit:", font=("Arial", 14))
deposit_label.pack()
deposit_entry = tk.Entry(window, font=("Arial", 14))
deposit_entry.pack()
deposit_button = tk.Button(window, text="Deposit", font=("Arial", 14), command=deposit)
deposit_button.pack()

withdraw_label = tk.Label(window, text="Withdraw:", font=("Arial", 14))
withdraw_label.pack()
withdraw_entry = tk.Entry(window, font=("Arial", 14))
withdraw_entry.pack()
withdraw_button = tk.Button(window, text="Withdraw", font=("Arial", 14), command=withdraw)
withdraw_button.pack()

check_balance_button = tk.Button(window, text="Check Balance", font=("Arial", 14), command=check_balance)
check_balance_button.pack()

window.geometry("400x300")
window.mainloop()
